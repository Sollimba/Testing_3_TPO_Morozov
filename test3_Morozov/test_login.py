import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options as EdgeOptions

baseURL = "https://practicetestautomation.com/practice-test-login/"
okUser = "student"
okPass = "Password123"
incorrectUser = "incorrectUser"
incorrectPass = "incorrectPassword"

def make_driver():
    driver = webdriver.Edge()
    return driver

@pytest.fixture
def driver():
    d = make_driver()
    yield d
    d.quit()

def _login(d, user, pwd):
    d.get(baseURL)
    d.find_element(By.ID, "username").send_keys(user)
    d.find_element(By.ID, "password").send_keys(pwd)
    d.find_element(By.ID, "submit").click()
    time.sleep(1)

def test_success_login(driver):
    _login(driver, okUser, okPass)
    msg = driver.find_element(By.TAG_NAME, "h1").text
    assert "Logged In Successfully" in msg

def test_wrong_password(driver):
    _login(driver, okUser, incorrectPass)
    error = driver.find_element(By.ID, "error").text
    assert "Your password is invalid" in error

def test_wrong_username(driver):
    _login(driver, incorrectUser, okPass)
    error = driver.find_element(By.ID, "error").text
    assert "Your username is invalid" in error
