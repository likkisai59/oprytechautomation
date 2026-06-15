import pytest
from pytest_bdd import given, when, then
from playwright.sync_api import Page
from pageobject.login_page import LoginPage
from utils.config import load_config

"""
Shared fixtures and configuration for pytest execution.
"""

@pytest.fixture
def config_data():
    return load_config()

@given('the user is on the login page')
def user_on_login_page(page: Page, config_data):
    page.goto(config_data['login_url'])

@when('the user enters valid username and password')
def user_enters_credentials(page: Page, config_data):
    login_page = LoginPage(page)
    login_page.login(config_data['username'], config_data['password'])

@when('clicks on the Sign In button')
def click_sign_in(page: Page):
    # The LoginPage.login method already performs enter_username, enter_password, and click_signin.
    # Therefore, this step can be a no-op / pass.
    pass

@then('the user should be redirected to the dashboard page')
def verify_dashboard(page: Page, config_data):
    page.wait_for_url(config_data['dashboard_url'])
    assert page.url == config_data['dashboard_url']
    page.wait_for_timeout(10000)

