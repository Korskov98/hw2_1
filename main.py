import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("http://149.255.118.78:7080")
    yield driver
    driver.close()


"""Успешная авторизация"""


def test_auth(driver):
    login = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")
    password = driver.find_element(by=By.XPATH, value="//input[@type='password']")
    password.send_keys("test")
    enter = driver.find_element(by=By.CSS_SELECTOR, value=".uk-button")
    enter.click()
    main_title = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, "h3")))
    assert main_title.is_displayed()
    assert main_title.text == "Добро пожаловать!"


"""Авторизация с пустым адресом"""


def test_auth(driver):
    enter = driver.find_element(by=By.CSS_SELECTOR, value=".uk-button")
    enter.click()
    error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "emailFormatError")))
    assert error_message.is_displayed()
    assert error_message.text == "Неверный формат E-Mail"


"""Авторизация с пустым паролем"""


def test_auth(driver):
    login = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")
    enter = driver.find_element(by=By.CSS_SELECTOR, value=".uk-button")
    enter.click()
    error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "KEKEKEKEKEKKEKE")))
    assert error_message.is_displayed()
    assert error_message.text == "Неверный E-Mail или пароль"


"""Авторизация с неверным адресом"""


def test_auth(driver):
    login = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("ыфвпвыпа@sdgf")
    password = driver.find_element(by=By.XPATH, value="//input[@type='password']")
    password.send_keys("test")
    enter = driver.find_element(by=By.CSS_SELECTOR, value=".uk-button")
    enter.click()
    error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "KEKEKEKEKEKKEKE")))
    assert error_message.is_displayed()
    assert error_message.text == "Неверный E-Mail или пароль"


"""Авторизация с неверным паролем"""


def test_auth(driver):
    login = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "loginEmail")))
    login.send_keys("test@protei.ru")
    password = driver.find_element(by=By.XPATH, value="//input[@type='password']")
    password.send_keys("teапst")
    enter = driver.find_element(by=By.CSS_SELECTOR, value=".uk-button")
    enter.click()
    error_message = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "KEKEKEKEKEKKEKE")))
    assert error_message.is_displayed()
    assert error_message.text == "Неверный E-Mail или пароль"
