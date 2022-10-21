import pandas as pd
import requests
import CardFinder
class Process:

    cardFinder = CardFinder.Finder()

    def __init__(self, magic_file):
        self.magic_df = pd.read_excel(magic_file, index_col=None)


    def get_cart(self, index=None, add=None, number=None):

        self.add = self.magic_df.iloc[index]['add']
        self.number = self.magic_df.iloc[index]['number']
        self.cardFinder.open_card_link(add=self.add, number=self.number)
        return self.add, self.number


    def add_card_name(self, index=None):
        add, number = self.get_cart(index)
        self.name = self.cardFinder.get_card_name(add=add, number=number)
        if self.name:
            self.magic_df.iloc[index, self.magic_df.columns.get_loc('name')] = self.name
            print(f"---> {self.name}")
            return True
        else:
            print(f"---> Card Not Found")
            return False


    def add_card_price(self, index=None):
        price = self.cardFinder.get_card_price()
        self.magic_df.iloc[index, self.magic_df.columns.get_loc('price')] = price
        print(f"---> {price}")

    def download_image(self):
        image = self.cardFinder.get_card_image()
        pull_image = requests.get(image, verify=False)

        with open(f"Images\{self.number}_{self.name}.jpg", "wb+") as myfile:
            myfile.write(pull_image.content)

    def generate_allegro_link(self, index):
        link = f"https://allegro.pl/listing?string={self.name}"
        self.magic_df.iloc[index, self.magic_df.columns.get_loc('link')] = link
        print(f"---> {link}")

