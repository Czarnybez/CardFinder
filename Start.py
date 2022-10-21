from CardProcess import *


cardProcess = Process("magic_final.xlsx")




for index in range(len(cardProcess.magic_df)):


   if cardProcess.add_card_name(index):
       cardProcess.add_card_price(index)
       cardProcess.generate_allegro_link(index)
       cardProcess.download_image()


cardProcess.magic_df.to_excel("magic_final.xlsx")