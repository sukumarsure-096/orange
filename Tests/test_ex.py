from playwright.sync_api import Playwright, Page, expect
import pytest

@pytest.mark.skip
def test_sample(page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.wait_for_timeout(5000)
    page.get_by_text('Apple').click()
    page.wait_for_timeout(5000)


    
    