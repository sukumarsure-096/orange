import base64
from playwright.sync_api import Playwright, Page, BrowserType
import pytest
import os

AUTH_FILE = "auth.json"
BASE_URL = "https://opensource-demo.orangehrmlive.com"

# 1. Suite start avvagane okasari Login ayyi 'auth.json' create chesthundi
@pytest.fixture(scope="session", autouse=True)
def generate_auth_state(playwright: Playwright, browser_type :BrowserType):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    # Note: OrangeHRM lo CSRF token untundi kabatti, UI nundi okasari login ayyi state save cheyadam best
    page.goto(f"{BASE_URL}/web/index.php/auth/login")
    page.fill("input[name='username']", "Admin")
    page.fill("input[name='password']", "admin123")
    page.click("button[type='submit']")
    page.wait_for_url("**/dashboard/index")
    
    # Session cookies ni auth.json lo save chesthunnam
    context.storage_state(path=AUTH_FILE)
    browser.close()
    
    yield
    # Suite ayipoyaka auth.json delete cheyali ante ee line unchandi:
    if os.path.exists(AUTH_FILE):
        os.remove(AUTH_FILE)


@pytest.fixture(scope='session')
def page(playwright:Playwright,browser_type : BrowserType):
    browser = browser_type.launch(headless=True)
    # auth.json load cheyadam valla direct ga logged-in state osthundi
    context = browser.new_context(storage_state=AUTH_FILE)
    page = context.new_page()
    page.goto(f"{BASE_URL}/web/index.php/dashboard/index")
    yield page
    context.close()
    browser.close()

# 3. Login Tests Kosam Separate Fixture (Logged-out Page)
@pytest.fixture(scope='session')
def login_page(playwright:Playwright, browser_type : BrowserType):
    browser = browser_type.launch(headless=True)
    # Ikkada storage_state ivvatledu, kabatti fresh login page open avthundi
    context = browser.new_context()
    page = context.new_page()
    page.goto(f"{BASE_URL}/web/index.php/auth/login")
    yield page
    context.close()
    browser.close()



# --- MEE EXISTING SCREENSHOT HOOK (Updated to support both 'page' and 'login_page') ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call" and report.failed:
        # 'page' leda 'login_page' edaina sare screenshot teeskuntundi
        active_page = item.funcargs.get("page") or item.funcargs.get("login_page")

        if active_page and not active_page.is_closed():
            try:
                active_page.wait_for_timeout(1000)
                screenshot_bytes = active_page.screenshot(full_page=False, timeout=2000)
                base64_string = base64.b64encode(screenshot_bytes).decode("utf-8")
                
                html_image = (
                    f'<div><img src="data:image/png;base64,{base64_string}" '
                    f'alt="screenshot" style="width:600px; max-height:400px; margin-bottom:10px;" '
                    f'onclick="window.open(this.src)"/></div>'
                )
                
                pytest_html = item.config.pluginmanager.getplugin("html")
                if pytest_html:
                    extra.append(pytest_html.extras.html(html_image))
                    report.extra = extra
            except Exception as e:
                print(f"Failed to capture Playwright failure screenshot: {e}")


'''
import base64
from playwright.sync_api import Playwright, Page, BrowserType
import pytest
import os
# @pytest.fixture(scope='session')
# def browser_content(playwright:Playwright, browser_channel):
#     if browser_channel == 'chromium':
#         browser = playwright.chromium.launch(headless=False)
#     else :
#         browser = playwright.firefox.launch(headless=False)
#     context = browser.new_context()
#     yield context
#     context.close()
#     browser.close()

@pytest.fixture(scope='session')
def browser_content(playwright:Playwright,browser_type : BrowserType):
    browser = browser_type.launch(headless=True)
    context = browser.new_context()
    yield context
    context.storage_state()
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

'''