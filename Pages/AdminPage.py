from playwright.sync_api import Page

class AdminPage:

    def __init__(self, page:Page):
        self.page = page
        self.admin = self.page.locator("//span[text()='Admin']")
        self.username = self.page.locator("input.oxd-input").nth(1)
        self.userrole = self.page.get_by_text('-- Select --').nth(0)
        self.employeename = self.page.get_by_placeholder('Type for hints...')
        self.status = self.page.get_by_text('-- Select --')
        self.search = self.page.locator("//button[text()=' Search ']")


    def admin_page(self):
        try:
            self.admin.click()
        except Exception as e:
            print(f'exception while enter the user name as {e}')
            raise

    def enter_user_name(self, user):
        try:
            self.username.fill(user)
        except Exception as e:
            print(f'exception while enter the user name as {e}')
            raise

    def select_user_role(self, userrole_type):
        try:
            self.userrole.click()
            self.userrole.focus()
            if userrole_type == 'Admin': 
                self.page.keyboard.press('ArrowDown')
                self.page.keyboard.press('Enter')
            else :
                self.page.keyboard.press('ArrowDown')
                self.page.keyboard.press('ArrowDown')
                self.page.keyboard.press('Enter')
            self.page.wait_for_timeout(5000)
        except Exception as e:
            print(f'exception while enter the user name as {e}')
            raise

    def enter_employee_name(self, emp_name):
        try:
            self.employeename.type(emp_name, delay=100)
            self.page.keyboard.press('ArrowDown')
            self.page.keyboard.press('Enter')
        except Exception as e:
            print(f'exception while entering as {e}')
            raise

    def select_status(self, status):
        try:
            self.status.click()
            self.status.focus()
            if status == 'Enabled':
                self.page.keyboard.press('ArrowDown')
                self.page.keyboard.press('Enter')
            else :
                self.page.keyboard.press('ArrowDown')
                self.page.keyboard.press('ArrowDown')
                self.page.keyboard.press('Enter')
        except Exception as e:
            print(f'exception while enter the user name as {e}')
            raise

    def click_search(self):
        try:
            self.search.click()
        except Exception as e:
            print(f'exception while enter the user name as {e}')
            raise

    def enter_details(self, user, userrole_type, emp_name, status):
        self.enter_user_name(user)
        self.select_user_role(userrole_type)
        self.enter_employee_name(emp_name)
        self.select_status(status)

    
    