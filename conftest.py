import base64
from playwright.sync_api import Playwright
import pytest

@pytest.fixture(scope='session')
def browser_content(playwright:Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(viewport={"width": 1280 , "height": 720})
    yield context
    context.close()
    browser.close()

@pytest.fixture(scope='session')
def page(browser_content):
    page = browser_content.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    yield page
    page.close()

# --- ADD THIS HOOK FOR CI/CD HTML SCREENSHOTS ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Captures a screenshot on failure from the session page fixture 
    and embeds it directly inside the pytest-html report.
    """
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    # Capture screenshots only during execution ("call") on test failure
    if report.when == "call" and report.failed:
        # Check if our session "page" fixture is available in this test item
        if "page" in item.funcargs:
            page = item.funcargs["page"]

            if page and not page.is_closed():
                try:
                    page.wait_for_timeout(1000)
                    # 1. Take a screenshot in memory (returns bytes)
                    screenshot_bytes = page.screenshot(full_page=False, timeout = 500)
                    
                    # 2. Encode to Base64 safe string format
                    base64_string = base64.b64encode(screenshot_bytes).decode("utf-8")
                    
                    # 3. Create inline HTML element
                    html_image = (
                        f'<div><img src="data:image/png;base64,{base64_string}" '
                        f'alt="screenshot" style="width:600px; max-height:400px; margin-bottom:10px;" '
                        f'onclick="window.open(this.src)"/></div>'
                    )
                    
                    # 4. Append directly into pytest-html extra data block
                    pytest_html = item.config.pluginmanager.getplugin("html")
                    if pytest_html:
                        extra.append(pytest_html.extras.html(html_image))
                        report.extra = extra
                except Exception as e:
                    print(f"Failed to capture Playwright failure screenshot: {e}")
