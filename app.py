
# Imports 
import bs4, requests , os
import pandas as pd
import csv  
#1 : asking user for the product's url , for developing purpose using pre-defined  url 



#product_url = """https://www.flipkart.com/tizum-aluminium-portable-stand-convenient-charging-port-design-all-smartphone-mobile-holder/p/itmf6mdmkzf2rdaf?pid=MOHF6M6ZRZAWBT3D&lid=LSTMOHF6M6ZRZAWBT3DXNE8PI"""

product_url =  """
https://www.flipkart.com/book-simple-living/p/
itm0138d585a262a?pid=9788193071007&lid=LSTBOK97881930710070XE163&
marketplace=FLIPKART&spotlightTagId=BestvalueId_bks&srno=s_1_1&
otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1
=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&fm=
SEARCH&iid=f2fb9007-4759-4e04-a5c7-077cbb5d6717.9788193071007
.SEARCH&ppt=sp&ppn=sp&ssid=4r12vxx88w0000001614007592753&qH=bff6669a85bb615d """ 

#2: getting url using requests

url = requests.get(product_url)


#3: checking if the link is succesfully established or not if it is 200 then return true,else false

if url.status_code != 200:
	print('False')


#4: creating a soup object to scrape data

soup = bs4.BeautifulSoup(url.text,'html.parser')

# 5: getting price title and price
## 5.1 : getting title

product_title = []

product_title.append((soup.find('h1').text) )

## 5.2 getting price of the product

product_price = []

product_price.append((soup.find('div', class_ = '_30jeq3 _16Jk6d').text) )#<div class="_30jeq3 _16Jk6d">₹267</div>

# 6 getting data in a pandas dataframe and saving it as an .csv file.
# check if products.csv exists if not create one, else open that file and insert the data
df = pd.DataFrame({'Product title':product_title,'Price':product_price})
df.to_csv('products.csv', index=False, encoding='utf-8')

