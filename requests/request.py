from __future__ import print_function

import requests

def getLocal():
	res = requests.get('http://localhost:5000/')
	print(res.status_code)
	print(res.headers['content-type'])
	print(res.text)
	#d = res.json()
	#print(d)
	#if d['status'] == 'ok':
	#	print("JSON was OK")

if __name__ == "__main__":

	getLocal()

