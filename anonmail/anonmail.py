import urllib.request
import re
import string
import requests

URL="https://generator.email"
def get_available_domain():
	dat=urllib.request.urlopen(URL).read().decode("utf8")
	udom=re.findall(r">[a-z0-9]+\.[a-z]{0,4}<",dat)
	avail_doms=[ dom[1:-1] for dom in udom ]
	return avail_doms
def get_name():
	req=urllib.request.Request("https://fauxid.com",headers={ 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)' })
	response=urllib.request.urlopen(req).read().decode("utf-8")
	pos1=response.find('<span class="id_name can-copy">',response.find('Fake Name:'))+31
	pos2=response.find('</span>',pos1)
	name=response[pos1:pos2].strip()
	return name
def get_username(name=get_name()):
	global username
	name=get_name().replace(".","").replace(" ",".").lower()
	whitelist = string.ascii_letters + string.digits + '.'
	user = ''.join(char for char in name if char in whitelist)
	return user
def get_email(user="",domain=""):
	user= get_username() if user=="" else user
	domain=get_available_domain()[0] if domain=="" else domain
	return (user+"@"+domain)
def fetch_emails(mail):
	#page=urllib.request.urlopen(URL+"/"+mail).read().decode("utf8")
	username,domain=mail.split('@')
	head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'DNT': '1', 'Connection': 'close', 'Upgrade-Insecure-Requests': '1', 'Cookie': 'surl='+domain+'%2F'+username+'; io=Xok_Idw8mxyoJx9WAA2; embx=%5B%22'+username+'%40'+domain+'%22%5D'}
	page=requests.get("https://generator.email:443/inbox/", headers=head).text
	mails=[]
	mailtemplate={"id":"",
				  "receiver":mail,
				  "sender":"",
				  "subject":"",
				  "time":""}
	elements=['e7m from_div_45g45gg','e7m subj_div_45g45gg','e7m time_div_45g45gg','e7m mess_bodiyy plain']
	senders=re.findall(r"(?<="+elements[0]+"\">).*?(?=<\/div>)",page)
	subjects=re.findall(r"(?<="+elements[1]+"\">).*?(?=<\/div>)",page)
	times=re.findall(r"(?<="+elements[2]+"\">).*?(?=<\/div>)",page)
	if not elements[3] in page:
		ids=re.findall(r"(?<=\/"+domain.replace(".","\.")+"\/"+username.replace(".","\.")+"\/)[a-z0-9]{32}",page)
	else:
		ids=re.findall(r'(?<=\".smurl.\"/)[a-z0-9]{32}(?=\".?\")',page)
	for i in range(len(senders)):
		mailtemplate={"id":ids[i],
					  "receiver":mail,
					  "sender":senders[i],
					  "subject":subjects[i],
					  "time":times[i]}
		mails.append(mailtemplate)
	return mails
def fetch_content(mail,id):
	username,domain=mail.split('@')
	url="https://generator.email:443/"+domain+"/"+username+"/"+id
	head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'DNT': '1', 'Connection': 'close', 'Upgrade-Insecure-Requests': '1', 'Cookie': 'surl='+domain+'%2F'+username+'; io=Xok_Idw8mxyoJx9WAA2; embx=%5B%22'+username+'%40'+domain+'%22%5D'}
	page=requests.get(url, headers=head,timeout=10).text
	content=re.findall(r"(?<=\"e7m mess_bodiyy plain\"><p>)[\s\S]+(?=<\/p>)",page)[0]
	return content