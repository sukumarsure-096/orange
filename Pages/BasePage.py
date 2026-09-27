from playwright.sync_api import Page

class BasePage:

    def __init__(self, page:Page):
        self.page = page

    def click(self, element):
        self.page.click()
        self.page.locator("//span[text()='Admin']")
        