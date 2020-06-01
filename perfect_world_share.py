import requests
import time
url = "https://act.dota2.com.cn/heavenandhell"
body={
	"task":"share_like",
	"user_id":""
}

for i in range(50):
	r=requests.post(url,data=body)
	print (r.text)
	time.sleep(0.5)
#16769223