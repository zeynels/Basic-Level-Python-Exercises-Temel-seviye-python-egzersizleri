import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com.tr/gp/bestsellers/computers/12601898031'

html = requests.get(url).content
soup = BeautifulSoup(html, "lxml")

urunler = soup.find_all("div", attrs={"class":"a-column a-span12 a-text-center a-spacing-top-base s-position-relative"})
if not os.path.exists('images'):
    os.mkdir('images')
for urun in urunler:
    urunisim = urun.find("div", attrs={"class":"a-section a-spacing-none p13n-sc-truncate p13n-sc-line-clamp-3"})
    urunfiyat = urun.find("span", attrs={"class":"a-price-whole"})
    if urunisim is not None:
        urunisim = urunisim.text.strip()
        urunresim = urun.find("div", attrs={"class":"a-section a-spacing-mini _cDEzb_noop_3Xbw5"})
        urunresim = urunresim.find("img",{"class":"a-dynamic-image p13n-sc-dynamic-image p13n-product-image"})
        
        if urunisim is not None and urunresim is not None:
            urunisim = urunisim.text.strip()
            urunresim = urunresim['src']
            file.write(urunisim + '\n' + urunresim + '\n\n')
            
            # download the image and save to the 'images' folder
            response = requests.get(urunresim)
            with open(os.path.join('images', urunisim + '.jpg'), 'wb') as img_file:
                img_file.write(response.content)

print("Products saved to file: urunler.txt")
print("Images saved to folder: images")

