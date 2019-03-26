from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import requests
import os
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException

options = Options()
options.add_argument("--headless")

class InstaDownloader:
        def __init__(self, username):
               self.username = username
        
        def instaParser(self):
                url = 'http://instagram.com/'+self.username
                self.driver = webdriver.Firefox(firefox_options=options)
                try:
                        self.driver.get(url)
                except WebDriverException as ex:
                        print("Cannot fetch the insta site")
                        print(ex)
                        exit()

                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                self.images = soup.find_all(class_="FFVAD")
        
        def picsDownloader(self):
                if os.path.isdir(self.username) is False:
                        os.mkdir(self.username)
                for imagesrc in self.images:
                        image_url = imagesrc["src"]
                        try:
                                resp = requests.get(image_url)
                        except Exception as ex:
                                print("Network error")
                                print(ex)
                                exit()
                        if resp.status_code is not 200:
                                print("error fetching response")
                                exit()
                        print("Downloading", image_url)
                        image_data = resp.content
                        with open(self.username+"/"+str(self.images.index(imagesrc))+".jpg", "wb") as f:
                                f.write(image_data)
                print("Files are downloaded")
                self.driver.quit()

insta = InstaDownloader("pyasiarun")
insta.instaParser()
insta.picsDownloader()




#openarungeek@gmail.com