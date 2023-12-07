import requests  
  
appid = 'wx3818d86371bb39e2'  
appsecret = 'c8a94eba14b51141c681785b07e20ea2'  
  
response = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + appsecret)  
  
print(response.json())