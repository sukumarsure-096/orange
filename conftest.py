from playwright.sync_api import Playwright
import pytest

@pytest.fixture(scope='session')
def browser_content(playwright:Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    yield context

    context.close()
    browser.close()

@pytest.fixture(scope='session')
def page(browser_content):
    page = browser_content.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    yield page
    page.close()

