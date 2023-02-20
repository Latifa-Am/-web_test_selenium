import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC 

url = "https://www.mozilla.org"
title  = "Internet for people"

@pytest.fixture
def webFix():
    driver = webdriver.Firefox()
    driver.get(url)
    try:
        element = wait(driver, 10).until(EC.title_contains(title))
    except Exception as ex:
        print(ex)
    yield driver

    driver.quit()

def test_web_link(webFix):
    webFix.find_element(By.LINK_TEXT, "Learn more about us").click()
    title = webFix.title
    assert 'About' in title

def test_web_links(webFix):
    links = webFix.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute("href")
        assert 'mozilla' in href or 'mastodon' in href or 'spotify' in href\
        or 'twitter' in href or 'instagram' in href or 'youtube' in href
        
"""def test_add():
    assert 4 + 2 == 6"""