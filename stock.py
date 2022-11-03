import requests
from bs4 import BeautifulSoup
import time
HOME_URL = "https://www.stock.com.py/default.aspx"

NoneType = type(None)   
def parsing(HOME_URL):
    try:   
            response = requests.get(HOME_URL)
            if response.status_code == 200:
                html = response.content
                soup_main = BeautifulSoup(html,"html.parser")
                ul_to_section = soup_main.find("ul",class_="wsmenu-submenu-sub wstitemright clearfix")
                link_to_section = ul_to_section.find_all("a",class_ = "collapsed")
                i = 0
                print(len(link_to_section))
                for link in link_to_section:
                    link = link.get("href")
                    if type(link) != NoneType:    
                        print(f"{link} ESTE ES EL LINK DE LA SECCION" )
                        i = i + 1
                        print(i)
                        if "https://www.stock.com.py/" in link:
                            hyperlink = link
                            r = requests.get(hyperlink)
                            html_ = r.content
                            soup = BeautifulSoup(html_,"html.parser")   
                            find_img = soup.find("div",class_="picture")
                            condition = not type(find_img) == NoneType
                            if condition:
                                product_img = find_img.find("img")
                                product_img = product_img.get("src")          
                                img = requests.get(product_img)
                                find_name = soup.find("h2",class_="product-title")
                                name = find_name.find("a")
                                name_file = name.text.replace("/","")
                                find_price = soup.find("span",class_="price-label")
                                price = find_price.text
                                with open(f"./stock/product_name/{i}{name_file}.txt",'w') as f:
                                    f.write(name_file)
                                    f.write("\n\n")
                                    f.write(price)
                                with open(f"./stock/productos/{name_file}{i}.jpg",'wb') as picture:
                                    picture.write(img.content)
                            else:
                                print("It's a none")
                                continue
                        else: 
                            print("Not a link.")
                            continue
                    else:
                        print(link)
                        continue

            else:
                raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
            print(ve)


parsing(HOME_URL)