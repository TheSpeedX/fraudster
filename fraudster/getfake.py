import requests

url = 'https://fauxid.com'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

r = requests.get(url,headers=headers)

def getprofile():
	profile = {'name':'','phone':'','dob':''}
	p = iter(str(r.content.decode()).split('\n'))
	for i in p:
		if i == '<h5 class="not-bottom-spaced not-top-spaced">Fake Name:</h5>':
			profile['name'] = next(p,None).strip('<br><span class="id_name can-copy"></span>')
		elif i == '<h5><i class="fas fa-phone small"></i> Phone:</h5>':
			profile['phone'] = next(p,None).strip('<br><span class="can-copy left-spaced"></span>')
		elif i == '<h5><i class="fas fa-calendar-alt"></i> Date of Birth:</h5>':
			profile['dob'] = next(p,None).strip('<br><span class="can-copy left-spaced"></span>')
	return profile

def getbank():
	bank = {'card_number':'','exp_date':'','cvv':'','bank_name':'','bank_account_number':'','routing_number':'','iban':''}
	p = iter(str(r.content.decode()).split('\n'))
	for i in p:
		if i == '<h5>Credit Card Number:</h5>':
			bank['card_number'] = next(p,None).strip('<br><span class="can-copy left-spaced"><code></code></span>')
		elif i == '<h5>Exp Date:</h5>':
			bank['exp_date'] = next(p,None).strip('<span class="can-copy"></span>')
		elif i == '<h5 class="left-spaced">CVV:</h5>':
			bank['cvv'] = next(p,None).strip('<span class="can-copy"></span>')
		elif i == '<h5><i class="fas fa-university"></i> Bank:</h5>':
			bank['bank_name'] = next(p,None).strip('<span class="can-copy"></span>')
		elif i == '<h5>Bank Account Number:</h5>':
			bank['bank_account_number'] = next(p,None).strip('<span class="can-copy"><code></code></span>')
		elif i == '<h5>Routing Number:</h5>':
			bank['routing_number'] = next(p,None).strip('<span class="can-copy"><code></code></span>')
		elif i == '<h5>IBAN:</h5>':
			bank['iban'] = next(p,None).strip('<span class="can-copy"><code></code></span>')
		else:
			pass
	return bank

def getcrypto():
	crypto = {'bitcoin':'','ethereum':'','monero':'','ripple':''}
	p = iter(str(r.content.decode()).split('\n'))
	for i in p:
		if i == '<br><img src="/img/bitcoin.svg" class="icon" title="Bitcoin" />':
			crypto['bitcoin'] = next(p,None).strip('<span class="can-copy left-spaced"><code></code></span>')
		elif i == '<br><img src="/img/ethereum.svg" class="icon" title="Ethereum" />':
			crypto['ethereum'] = next(p,None).strip('<span class="can-copy left-spaced"><code></code></span>')
		elif i == '<br><img src="/img/ripple.svg" class="icon" title="Ripple" />':
			crypto['ripple'] = next(p,None).strip('<span class="can-copy left-spaced"><code></code></span>')
		elif i == '<br><img src="/img/monero.svg" class="icon" title="Monero" />':
			crypto['monero'] = next(p,None).strip('<span class="can-copy left-spaced small"><code></code></span>')
		else:
			pass
	return crypto

def getinternet():
	internet = {'ipv4':'','ipv6':'','mac':'','iplocal':'','user-agent':''}
	p = iter(str(r.content.decode()).split('\n'))
	for i in p:
		if i == '<h5>IP Address (IPv4):</h5>':
			internet['ipv4'] = next(p,None).strip('<span class="can-copy"><code></code></span>')
		elif i == '<h5>IP Address (Local):</h5>':
			internet['iplocal'] = next(p,None).strip('<span class="can-copy"><code></code></span>')
		elif i == '<h5>MAC Address:</h5>':
			internet['mac'] = next(p,None).strip('<span class="can-copy"><code></code></span>')
		elif i == '<h5>IP Address (IPv6):</h5>':
			internet['ipv6'] = next(p,None).strip('<br><span class="can-copy left-spaced"><code></code></span>')
		elif i == '<h5>User Agent:</h5>':
			internet['user-agent'] = next(p,None).strip('<br><span class="can-copy left-spaced"><code></code></span>')
		else:
			pass
	return internet