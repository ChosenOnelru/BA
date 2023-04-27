import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope='session') # задаем уровень использования фикстуры уровень функции/сессии/тд. по умолчанию - уровень функции
def driver():
    print('start browser')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
