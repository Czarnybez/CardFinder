from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Finder:

    PATH = "c:\\dev\\chromedriver.exe"
    CARD_NAME = "card-text-card-name"
    PICTURE_BOX = 'span[class="price currency-usd"]'
    CARD_IMAGE = "div[class='card-image-front'] img"

    def __init__(self):
        self.driver_scryfall = webdriver.Chrome(Finder.PATH)

    def open_card_link(self, index=None,add=None,number=None):
        print('-'*30)
        print(f"Searching card {add}-{number}")

        #find card by addon and card number on scryfall
        self.driver_scryfall.get(f'https://scryfall.com/card/{add}/{number}')


    def get_card_name(self, index=None,add=None,number=None):

        try:
            return self.driver_scryfall.find_element(By.CLASS_NAME, Finder.CARD_NAME).text
        except:
            return False


    def get_card_price(self):
        return self.driver_scryfall.find_element(By.CSS_SELECTOR, Finder.PICTURE_BOX ).text


    def get_card_image(self):
        return self.driver_scryfall.find_element(By.CSS_SELECTOR, Finder.CARD_IMAGE ).get_attribute("src")
