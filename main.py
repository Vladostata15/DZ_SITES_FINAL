import requests
import lxml
import fake_useragent
from bs4 import BeautifulSoup


url = 'https://kups.club/'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')



products = soup.find_all('div', class_='col-lg-4 col-md-4 col-sm-6 portfolio-item')




for product in products:
        title_product = product.find('h3', class_='card-title')
        price_product = product.find('p', class_='card-text')
        shop_product = product.find('a', class_='text-black link-default')
        product_product = product.find('a').get('href')
        product_img = product.find('img').get('src')

        if shop_product.text == '':
                s = str(product.find('img', class_='mr-2'))
                c = s.rfind('"')
                n = s.rfind('=') + 2



                print(title_product.text, price_product.text, shop_product.text, s[n:c])
                print(f'Фото: {product_img}')
                print(f'Товар: {product_product}')
        else:
                print(title_product.text, price_product.text, shop_product.text)
                print(f'Фото: {product_img}')
                print(f'Товар: {product_product}')







incomeBig = 0
gamesBig = 0
foodBig = 0
expBig = 0
income = 1
while True:
    income = int(input("Enter your mont icome: "))
    if income == 0:
        break
    incomeBig += income
    games = int(input("Enter your expenses for games: "))
    gamesBig += games
    food = int(input("Enter your expenses for food: "))
    foodBig+=food
    expenses = games+food
    expBig+=expenses
    print("--------")



gamesPer = (gamesBig/expBig)*100
foodPer = (foodBig/expBig)*100
print("\n\nEXPENSES SUMMARY\n-----------------------")
print(f"Games expenses: {gamesBig} \nMonth percent: {round(gamesPer, 2)}%\n")
print(f"Food expenses: {foodBig} \nMonth percent: {round(foodPer, 2)}%")
res = abs(incomeBig-(gamesBig+foodBig))
if (gamesBig+foodBig) > incomeBig:
    print(f"\nYou owe: {res}")
else:
    print(f"\nMoney left: {res}")


