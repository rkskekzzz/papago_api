from cmath import log
import os
import re
from xml.dom.minidom import Element
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs
from tqdm import tqdm

load_dotenv()
papago_id = os.getenv("S_PAPAGO_ID")
papago_secret = os.getenv("S_PAPAGO_SECRET")
papago_url = "https://openapi.naver.com/v1/papago/n2mt"
rfc_url = "https://datatracker.ietf.org/doc/html/rfc"

header = {
	"X-Naver-Client-Id":papago_id,
	"X-Naver-Client-Secret":papago_secret
	}

data = {
	'source' : 'en',
	'target': 'ko',
	'text': '',
	}


def _fetchRFCDocument(num):
	plainTextArray = []

	response = requests.get(rfc_url + num)
	soup = bs(response.text, "html.parser")

	elements = soup.select('.draftcontent > pre')
	for index, element in enumerate(elements):
		plainTextArray.append(re.sub('\s+', ' ', element.get_text()).strip())

	return plainTextArray


def translateProcess(num):
	translatedTextArray = []
	plainTextArray = _fetchRFCDocument(num)
	alllen = 0

	print(len(plainTextArray))
	data['text'] = plainTextArray[0]
	response = requests.post(papago_url, headers=header, data=data)
	print(response.json()['message']['result']['translatedText'])
	for element in tqdm(plainTextArray):
		alllen += len(element)
	# 	response = requests.post(papago_url, headers=header, data=data)
	# 	translatedTextArray.append(response.json()['message']['result']['translatedText'])

	print(alllen)
	# for result in translatedTextArray:
		# print(result)

