from playwright.sync_api import Playwright, Page

class Directory:

    def __init__(self, page:Page):
        self.page = page
        self.directory_link = self.page.locator("//span[text()='Directory']")
        self.emp_name = self.page.get_by_placeholder('Type for hints...')
        self.job_title = self.page.locator("div.oxd-select-text-input").nth(0)
        self.location = self.page.locator("div.oxd-select-text-input").nth(1)
        self.search = self.page.locator("//button[text()=' Search ']")

    def click_directory_link(self):
        try:
            self.directory_link.click()
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while clicking on link as {e}")
            raise

    def enter_employee_name(self, empname):
        try:
            self.emp_name.fill(empname)
        except Exception as e:
            print(f"exception while clicking on link as {e}")
            raise

    def select_jobtitle(self):
        try:
            self.job_title.click()
            self.job_title.focus()
            self.page.keyboard.press('ArrowDown')
            self.page.keyboard.press('ArrowDown')
            self.page.keyboard.press('ArrowDown')
            self.page.keyboard.press('Enter')
            self.page.wait_for_timeout(10000)
        except Exception as e:
            print(f"exception while clicking on link as {e}")
            raise

    
    def select_location(self):
        try:
            self.location.click()
            self.location.focus()
            self.page.keyboard.press('ArrowDown')
            self.page.keyboard.press('ArrowDown')
            self.page.keyboard.press('ArrowDown')
            self.page.keyboard.press('Enter')
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f"exception while clicking on link as {e}")
            raise

    def click_search_button(self):
        self.search.click()
        self.page.wait_for_timeout(10000)
    


        