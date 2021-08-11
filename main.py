from bs4 import BeautifulSoup
import requests
import pandas as pd


class pirce_track:

    def __init__(self) -> None:
       
        content=requests.get('https://www.flipkart.com/ambrane-10000-mah-power-bank-20-w-delivery-2-0-quick-charge-3-0/p/itm1274cc9e51c94?pid=PWBFZ9AWGHMNRGFQ&otracker=wishlist&lid=LSTPWBFZ9AWGHMNRGFQNNEIM9&fm=organic&iid=79d94e21-436b-429a-ab18-155020e3fdb7.PWBFZ9AWGHMNRGFQ.PRODUCTSUMMARY&ppt=hp&ppn=homepage&ssid=x8bpw1jonk0000001628662589741').text
        self.soup=BeautifulSoup(content,'lxml')
    def get_name(self):
        self.names=self.soup.find_all('h1',class_='yhB1nd')
        

        for name in self.names:
            self.product_name=name.text
        return self.product_name

    def get_price(self):   
        self.prices=self.soup.find_all('div',class_='_30jeq3 _16Jk6d')

        for price in self.prices:
            self.product_pirce=price.text
        return self.product_pirce

        

    # product_dict={
    #     'product_name':product_name,
    #     'product_price':product_pirce[1:]
    # }


    # df=pd.DataFrame(product_dict,index=[0])

    # df.to_csv('price.csv')

