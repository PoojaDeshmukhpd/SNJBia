import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
page=requests.get("http://www.snjb.org/engineering/Placement/engineering_mba_placement_profile")
souped=BeautifulSoup(page.content,"html.parser")
imgs=souped.find_all("img")
link=""
for img in tqdm(imgs):
    imglink=img.attrs.get("src")
    image=requests.get(imglink).content
    for i in imglink:
        if i.__contains__("pacement") or i.__contains__("offer") or i.__contains__("placements") or i.__contains__("Offers"):
            link=link+i
    filename=r"cards"+link[link.rfind("/"):]
    with open(filename,"wb") as file:
        file.write(image)