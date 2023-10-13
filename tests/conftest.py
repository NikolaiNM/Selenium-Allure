"""
Configuration test
"""
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def browser():
  """
  Main fixture
  """
  chrome_options = Options()
  chrome_options.add_argument("--no-sandbox") #Отключить все песочницы
  chrome_options.add_argument("start-maximized") # открываем на полный экран
  chrome_options.add_argument("--disable-infobars") # отключаем инфо сообщения
  chrome_options.add_argument("--disable-extensions") # отключаем расширения
  chrome_options.add_argument("--disable-gpu") # отлючаем GPU
  chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless") # спец. режим "без браузера"

	# устанавливаем webdriver в соответствии с версией используемого браузера
  service = Service()
  # запускаем браузер с указанными выше настройками
  driver = webdriver.Chrome(service=service, options=chrome_options)
  yield driver
  driver.quit()