import requests as req

uname = input("Enter your name : ")
pname = input("enter partner's name : ")

msg = input(uname+":")
url = "https://api.affiliateplus.xyz/api/chatbot?message="+msg+"&name="+pname+"&user=1"
while msg is not None:
  reply = req.get(url).json()
  print (pname+" : "+reply['message'])
  msg = input(uname+":")