from requests import post
from Config.Config import OAUTH

print("Running Config block")
print("Running config block")

res=post(OAUTH.END_POINT,params={"client_id":OAUTH.CLIENT_ID,"client_secret":OAUTH.CLIENT_SECRET,"refresh_token":OAUTH.REFRESH_TOKEN},headers={"Content-type":"application/x-www-form-urlencoded"})
OAUTH.TOKEN=res.json()["access_token"]
print(OAUTH.TOKEN)