from locators.oprytech.login_locator import LoginLocators

class LoginPage:
    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        self.page.get_by_placeholder(
            LoginLocators.USERNAME_PLACEHOLDER
        ).fill(username)

    def enter_password(self, password):
        self.page.get_by_placeholder(
            LoginLocators.PASSWORD_PLACEHOLDER
        ).fill(password)

    def click_signin(self):
        self.page.get_by_role(
            "button",
            name=LoginLocators.SIGNIN_BUTTON_NAME
        ).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_signin()

    def click_jobs_menu(self):
        self.page.get_by_role("link", name=LoginLocators.JOBS_BUTTON_NAME).click()

    def click_create_job(self):
        self.page.get_by_role("button", name=LoginLocators.CREATE_JOB_BUTTON_NAME).click()
