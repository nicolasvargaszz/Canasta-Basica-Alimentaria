import requests
from bs4 import BeautifulSoup
import time
HOME_URL = "https://www.realonline.com.py/"


def parsing(HOME_URL):
    try:   
            response = requests.get(HOME_URL)
            if response.status_code == 200:
                html = response.content
                soup_main = BeautifulSoup(html,"html.parser")
                ul_to_section = soup_main.find("ul",class_="toggle-menu list-category-dropdown")
                print(len(ul_to_section))
                # print(ul_to_section)
                print("************************")
                link_to_section = ul_to_section.find_all("a")
                i = 0
                print(len(link_to_section))
                for link in link_to_section[8:]:
                    link = link.get("href")
                    print(f"{link} ESTE ES EL LINK DE LA SECCION" )
                    i = i + 1
                    print(i)
                    if "https://www.realonline.com.py" in link:
                        hyperlink = link
                        r = requests.get(hyperlink)
                        html_ = r.content
                        soup = BeautifulSoup(html_,"html.parser")   
                        find_img = soup.find("img",class_="product-image-photo")
                        NoneType = type(None)
                        condition = not type(find_img) == NoneType
                        if condition:
                            product_img = find_img.get("src")          
                            img = requests.get(product_img)
                            find_name = soup.find("div",class_="product details product-item-details")
                            name = find_name.find("a")
                            name_file = name.text.replace("/","")
                            find_praise = soup.find("span",class_="price")
                            praise = find_praise.text
                            with open(f"./real/product_name/{i}{name_file}.txt",'w') as f:
                                f.write(name_file)
                                f.write("\n\n")
                                f.write(praise)
                            with open(f"./real/productos/{name_file}{i}.jpg",'wb') as picture:
                                picture.write(img.content)
                        else:
                            print("It's a none")
                            continue
                    else: 
                        print("Not a link.")
                        pass

            else:
                raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
            print(ve)


parsing(HOME_URL)