import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = "http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
with uReq(my_url) as uClient:
    page_html = uClient.read()

# html parsing
page_soup = soup(page_html, "html.parser")


with open("product.csv", "w") as f:
    headers = "brand, product_name, shipping\n"
    f.write(headers)

    #
    containers = page_soup.findAll("div", {"class": "item-container"})

    for container in containers:
        brand = container.div.div.a.img["title"]

        title_container = container.findAll("a", {"class": "item-title"})
        product_name = title_container[0].text

        shipping_container = container.findAll("li", {"class": "price-ship"})
        shipping = shipping_container[0].text.strip()

        print("brand: " + brand)
        print("product_name: " + product_name)
        print("shipping: " + shipping)
        print("--------------------")
        f.write(
            ",".join([brand, product_name.replace(",", " "), shipping]) + "\n")
