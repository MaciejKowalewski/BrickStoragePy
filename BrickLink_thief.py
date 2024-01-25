from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class thief:
    def __init__(self, url: str):
        PATH = 'C:\chromedriver\chromedriver.exe'
        s = Service(PATH)
        self._driver = webdriver.Chrome(service=s)
        self._url = url
        self._driver.get(self._url)

    def get_name(self):
        name = self._driver.find_element(By.ID, 'item-name-title').text
        return name

    def get_id(self):
        part_id = self._driver.find_elements(By.TAG_NAME, 'td')[1].text.split(':')
        return part_id[len(part_id) - 1][1:]

    def get_price(self):
        price = self._driver.find_elements(By.CLASS_NAME, 'pciItemRowEven')[0].find_elements(By.TAG_NAME, 'td')[4].text
        price = price[4:8]
        return price

    def get_img(self):
        img = self._driver.find_element(By.ID, '_idImageMain').get_attribute("src")
        return img

    def get_type(self):
        brick_type = self._driver.find_elements(By.TAG_NAME, 'td')[1].text.split(':')
        return brick_type[len(brick_type) - 2][1:]

d = thief('https://www.bricklink.com/v2/catalog/catalogitem.page?P=26047#T=S&C=85&O={"color":"85","ss":"PL","loc":"PL","rpp":"500","iconly":0}')

print(d.get_type())
