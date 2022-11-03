import requests
from bs4 import BeautifulSoup
import time
HOME_URL = "https://grutteronline.casagrutter.com.py/"


def parsing(HOME_URL):
    try:   
            response = requests.get(HOME_URL)
            if response.status_code == 200:
                html = response.content
                soup_main = BeautifulSoup(html,"html.parser")
                ul_to_section = soup_main.find("ul",class_="mega-menu")
                link_to_section = ul_to_section.find_all("a")
                i = 0
                print(len(link_to_section))
                for link in link_to_section:
                    print(link)
                    i = i + 1
                    print(i)
                    hyperlink = link.get("href")
                    r = requests.get(hyperlink)
                    html_ = r.content
                    soup = BeautifulSoup(html_,"html.parser")   
                    find_img = soup.find("img",class_="lazy img-responsive replace-2x")
                    NoneType = type(None)
                    condition = not type(find_img) == NoneType
                    if condition:
                        product_img = find_img.get("data-original")          
                        img = requests.get(product_img)
                        find_name = soup.find("div",class_="caption")
                        name = find_name.find("h2")
                        name_file = name.text.replace("/","")
                        find_praise = soup.find("div",class_="button-wrapper")
                        praise = find_praise.text.replace("Añadir al carrito Añadir a la lista de deseos Quick View","")
                        with open(f"./casa_grutter/product_name/{name_file}{i}.txt",'w') as f:
                            f.write(praise)
                        with open(f"./casa_grutter/productos/{i}.jpg",'wb') as picture:
                            picture.write(img.content)
                    else:
                        print("It's a none")
                        continue
            else:
                raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
            print(ve)


parsing(HOME_URL)
