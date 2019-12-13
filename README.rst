# Fraudster
Fraudster Provides You Temporary And Disosable Mails To Use

## How To Install
This Code is hosted on PyPI so you can install by;
```
pip install fraudster
```

## Requirements 
-> requests 
<br>```pip install requests```

### How To USE
To Get Available Domain For Fraudster

```
>>> import fraudster
>>> domain=fraudster.get_available_domain()
```

To Get A Random Person Name

```
>>> from fraudster import *
>>> name=get_name()
```

To Get A Random Disposable E-Mail

```
>>> from fraudster import *
>>> email=get_email()
```

To Get A Custom UserName E-Mail

```
>>> from fraudster import *
>>> email=get_email("speedx",get_available_domains()[0])
```

To Get A List of All Received Mails

```
>>> from fraudster import *
>>> mails=fetch_emails()
```

To Get Body Of Any Mail

```
>>> from fraudster import *
>>> body=fetch_content(<Your_Mail_ID>,<Your_Message_ID>)
```

### TODO
-> Add Command Line Usage

-> Add More Features

-> Remove requests Dependencies


## Note 

Its Heavily  Under Work.... Report Any Bugs 

Made With ♥ By SpeedX


