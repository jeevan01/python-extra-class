from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import requests
import os
username = "jeevanpandey01"
url = 'http://instagram.com/' +username
driver = webdriver.chrome(executable_path="/home/jeevan/Downloads/chromedriver")

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'html.parser')
images = soup.find_all(class_="FFVAD")
os.mkdir(username)
for imagesrc in images:
    image_url = imgsrc["src"]
    resp = requests.get(image_url)
    print("Downloading", image_url)
    image_data = resp.content
    with open(username+"/"+str(images.index(imagesrc))+".jpg","wb") as f:
        f.write(image_data)

print("Files are downloaded")