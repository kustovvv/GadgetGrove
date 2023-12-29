import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def chrome_browser_instance(request):
    options = Options()
    options.headless = False
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()