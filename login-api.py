import requests
import json

url = "https://grizzlysms.com/api/users/login"

payload = json.dumps({
  "username": "example@gmail.com",
  "password": "password",
  "token": ""
})

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
  'Accept': "application/json, text/plain, */*",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/json",
  'x-forwarded-host': "grizzlysms.com",
  'sec-ch-ua-platform': "\"Android\"",
  'sec-ch-ua': "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
  'sec-ch-ua-mobile': "?0",
  'x-session-token': "frntwyjvgcyx9",
  'x-user-locale': "en",
  'origin': "https://grizzlysms.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'referer': "https://grizzlysms.com/authorization",
  'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
  'priority': "u=1, i",
  'Cookie': "sessionToken=frntwyjvgcyx9; payment-test=true; show-rent=; currency=usd; _ym_uid=1731253121690152584; _ym_d=1731253121; _ym_isad=2; _ym_visorc=w; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-11-10%2018%3A38%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrizzlysms.com%2Fauthorization%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2024-11-10%2018%3A38%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fgrizzlysms.com%2Fauthorization%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F130.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fgrizzlysms.com%2Fauthorization; fp=0346b541a17c51ed5ee4eef986adecfd"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)
