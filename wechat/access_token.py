import requests  
  
appid = 'wx8284fb03f1ecf547'  
appsecret = 'f2694165b521023d7b207b6efe2a265d'  
  
response = requests.get('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=' + appid + '&secret=' + appsecret)  
  
print(response.json())