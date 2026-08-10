from playwright.sync_api import Page

class LoginPage:

    def __init__(self, page:Page):
        self.page = page
        self.username = self.page.get_by_placeholder('Username')
        self.password = self.page.get_by_placeholder('Password')
        self.login_button = self.page.locator("button[type='submit']")
        self.profile_icon = self.page.locator("div.oxd-topbar-header-userarea li")
        self.logout_button = self.page.locator("//a[text()='Logout']")
        self.dashboard = self.page.locator("//h6[text()='Dashboard']")
        self.invalid_credentials = self.page.get_by_text('Invalid credentials')

    def enter_username(self, user_name):
        try:
            self.username.fill(user_name)
        except Exception as e:
            print(f'while enter the username as {e}')
            raise

    def enter_password(self, pwd):
        try:
            self.password.fill(pwd)
        except Exception as e:
            print(f'while enter the password as {e}')
            raise

    def click_login_button(self):
        try:
            self.login_button.click()
        except Exception as e:
            print(f'while clicking the login button  as {e}')
            raise

    def click_profile_icon(self):
        try:
            self.profile_icon.click()
        except Exception as e:
            print(f'while clicking the profile icon  as {e}')
            raise

    def click_logout_button(self):
        try:
            self.logout_button.click()
        except Exception as e:
            print(f'while clicking the logout button  as {e}')
            raise

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    