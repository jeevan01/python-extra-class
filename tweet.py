from  bs4 import BeautifulSoup
import requests

try:
	page = requests.get("https://twitter.com/adhikaritaiwan")
	soup = BeautifulSoup(page.content, 'html.parser')
	all_items = soup.find_all(class_="content")

	for content in all_items:
		tweet_text = content.find(class_="js-tweet-text-container").get_text()
		print(tweet_text)
except Exception as ex :
	print("Couldn't connect to Twitter")