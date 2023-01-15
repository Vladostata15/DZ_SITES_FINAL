import requests
import lxml
import fake_useragent
from bs4 import BeautifulSoup


url = f'https://kups.club/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')



try:
    products = soup.find_all('div', class_ ='col-lg-4 col-md-4 col-sm-6 portfolio-item')


    for product in products:
        title_product = product.find('h3', class_='card-title')
        price_product = product.find('p', class_='card-text')
        shop_product = product.find('a', class_='text-black link-default')
        product_product = product.find('a').get('href')
        product_img = product.find('img').get('src')



        if shop_product.text == str:
            print(title_product.text, price_product.text, shop_product.text)
            print(f'Фото: {product_img}')
            print(f'Товар: {product_product}')


except:
    pass


finally:
    logo_shop = soup.find_all('a', class_='text-black link-default')

    for lg_sh in logo_shop:
        logo_text = lg_sh.find('img').get('alt')

        if shop_product.text == None:
            print(title_product.text, price_product.text, shop_product.text)
            print(f'Фото: {product_img}')
            print(f'Товар: {product_product}')



