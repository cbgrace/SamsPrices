from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()

    driver.get("https://www.samsclub.com/p/case-sale-90-percent-lean-ground-beef-chubs/prod17160007?xid=plp_product_3")

    title = driver.title  # what is this doing?

    driver.implicitly_wait(0.8)  # it said this is not the best way to do this, so what is?

    item_name = driver.find_element(by=By.CLASS_NAME, value="sc-pc-title-full-desktop")
    per_lb_price = driver.find_element(by=By.CLASS_NAME, value="Price-group")
    total_price = driver.find_element(by=By.CLASS_NAME, value="sc-pc-single-price-inline-price")

    print(item_name.text)
    print(per_lb_price.text)
    print(total_price.text)

    driver.quit()


if __name__ == "__main__":
    main()
