import requests
from bs4 import BeautifulSoup


HOME_URL = "https://www.casarica.com.py/"


def parsing(HOME_URL):
    try:   
            response = requests.get(HOME_URL)
            #Basic part
            if response.status_code == 200:
                html = response.content
                soup_main = BeautifulSoup(html,"html.parser")
            #Getting the link of all the section on the web page
                ul_to_section = soup_main.find("ul",class_="dropdown-menu yamm departments-menu-dropdown")
            #get the link
                link_to_section = ul_to_section.find_all("a")
                i = 0
                print(len(link_to_section))
                for link in link_to_section:
                    print(link)
                    i = i + 1
                    print(i)
                    #we get in all the links on the sections and we pass it to a bs4 object
                    hyperlink = link.get("href")
                    r = requests.get(f"https://www.casarica.com.py/{hyperlink}")
                    html_ = r.content
                    soup = BeautifulSoup(html_,"html.parser")   
                    #we get the img, but sometimes we recive a nonetype object and the script stop
                    #to prevent that, we use an if.
                    find_img = soup.find("div",class_="product-list-image")
                    print(find_img)
                    print("**********************")
                    #if we didn't find an img this is a NoneType
                    NoneType = type(None)
                    condition = not type(find_img) == NoneType
                    #if we have a none type the follow code won't execute.
                    if condition:
                        img = find_img.find("img")
                        product_img = img.get("data-src")          
                        final_img = requests.get(product_img)
                        #we get the name of the product
                        find_name = soup.find("h2",class_="ecommercepro-loop-product__title")
                        #in case that the name has a \ we'll delete it because it will make a problem
                        name = find_name.text.replace("/","")
                        find_praise = soup.find("span",class_="price")
                        praise = find_praise.text
                        #we save the praise, the img and the name in  two files.
                        with open(f"./casa_rica/productos/{i}.jpg",'wb') as picture:
                            picture.write(final_img.content)
                        with open(f"./casa_rica/name/{i}{name}.txt","w") as f:
                            f.write(name)
                            f.write("\n\n")
                            f.write(praise)
                   
                    else:
                        print("It's a none")
                        continue
            else:
                raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
            print(ve)


parsing(HOME_URL)