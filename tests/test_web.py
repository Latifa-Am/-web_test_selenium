import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait

url = "https://www.mozilla.org"
title  = "Internet for people"

@pytest.fixture
def webFix():
    driver = webdriver.Firefox()
    driver.get(url)
    
def test_add():
    assert 4 + 2 == 6