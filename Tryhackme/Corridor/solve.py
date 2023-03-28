import hashlib
import requests

for i in range(0,100):
	hash = hashlib.md5(str(i).encode()).hexdigest()
	url = "http://10.10.211.175/" + hash
	res = requests.get(url)
	if res.status_code != 404:
		print(f"{i} - {hash} - {url}")


