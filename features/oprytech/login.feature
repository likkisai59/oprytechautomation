Feature: Oprytech Application Login

  As an administrator
  I want to login to the Oprytech system
  So that I can access the dashboard

  Scenario: Successful login with valid administrator credentials
    Given the user is on the login page
    When the user enters valid username and password
    And clicks on the Sign In button
    Then the user should be redirected to the dashboard page
