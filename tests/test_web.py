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

def test_account_form(webFix):
    webFix.find_element(By.LINK_TEXT, "Explore Firefox").click()
    try:
        element = wait(webFix, 3).until(EC.presence_of_element_located(By.CLASS_NAME, "fxa-email-field-container"))
    except Exception as ex:
        print(ex)
    text_input = webFix.find_element(By.ID, "fxa-email-field")
    text_input.send_keys("example@gmail.com")
    webFix.find_element(By.ID, "fxa-email-form-submit").click()
    prefillEmail = "none"
    try:
        prefillEmail = wait(webFix, 3).until(EC.presence_of_element_located((By.ID, "prefillEmail"))).text
    except Exception as ex:
        print(ex)
    assert "example@gmail.com" in prefillEmail

"""def test_add():
    assert 4 + 2 == 6"""