from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

def make_driver(url):
    """

    :param url: the url behind which our data lies
    :return: returns a webdriver
    """
    driver = None
    try:
        driver = webdriver.Chrome()
        driver.get(url)
        driver.implicitly_wait(0.8)
        yield driver
    except (TimeoutException, NoSuchWindowException) as e:
        print(f"an error occurred: {e}")
    finally:
        if driver:
            driver.quit()


def get_data(url):
    """

    :param url: the url behind which our data lies
    :return:
    """
    with make_driver(url) as driver:
        try:
            item_name = driver.find_element(by=By.CLASS_NAME, value="sc-pc-title-full-desktop")
            current_price = driver.find_element(by=By.CLASS_NAME, value="Price-group")
            inline_price = driver.find_element(by=By.CLASS_NAME, value="sc-pc-single-price-inline-price")
            return item_name, per_lb_price, total_price
        except NoSuchElementException as e:
            print(f"element not found {e}")
            return None

