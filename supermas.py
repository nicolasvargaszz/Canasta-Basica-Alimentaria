from logging import warning
import requests
from bs4 import BeautifulSoup
import time
HOME_URL = "https://www.supermas.com.py/"

NoneType = type(None)   
def parsing(HOME_URL):
    try:   
            response = requests.get(HOME_URL)
            if response.status_code == 200:
                html = response.content
                soup = BeautifulSoup(html,"html.parser")
                ul_to_section = soup.find("ul",class_="dropdown-menu yamm departments-menu-dropdown")
                i = 0
                link_to_section = ul_to_section.find_all("a")
                print(len(link_to_section))
                for link in link_to_section:
                    link = link.get("href")
                    if not type(link) == NoneType:
                        i = i + 1    
                        print(f"{link} ESTE ES EL LINK DE LA SECCION" )
                        print(i)
                        link = f"{HOME_URL}{link}"
                        if "https://www.supermas.com.py/" in link:
                            hyperlink = link
                            print(hyperlink)
                            r = requests.get(hyperlink)
                            html_ = r.content
                            soup = BeautifulSoup(html_,"html.parser")  
                            find_div_with_img = soup.find("div",class_="product-list-image") 
                            condition = not type(find_div_with_img) == NoneType
                            if condition:
                                find_img = find_div_with_img.find("img")
                                product_img = find_img.get("data-src")          
                                img = requests.get(product_img)
                                find_name = soup.find("h2",class_="woocommerce-loop-product__title")
                                name_for_a_file = find_name.text.replace("/","") #if the article have a / in the name it wont work
                                find_price = soup.find("span",class_="price")
                                price = find_price.text
                                with open(f"./supermas/product_name/{i}{name_for_a_file}.txt",'w') as f:
                                    f.write(name_for_a_file)
                                    f.write("\n\n")
                                    f.write(price)
                                with open(f"./supermas/productos/{name_for_a_file}{i}.png",'wb') as picture:
                                    picture.write(img.content)
                            else:
                                print("It's a none")
                                continue
                        else: 
                            print("Not a link.")
                            continue
                    else:
                        print("error with the a etiquet")
                        continue

            else:
                raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
            print(ve)


parsing(HOME_URL)