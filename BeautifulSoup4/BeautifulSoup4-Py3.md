
	>>> import json
	>>> import requests
	>>> from bs4 import BeautifulSoup
	>>>
	>>> html_text = """<html>
	... <head></head>
	... <body>
	... <pre style="word-wrap: break-word; white-space: pre-wrap;">
	... "{"Title":"One Indian Girl","Year":"2016","Author":"Chetan Bhagat"}"
	... </pre>
	... </body>
	... </html>"""
	>>>
	>>> soup = BeautifulSoup(html_text, "html.parser")
	>>> print(soup.prettify())
	<html>
	 <head>
	 </head>
	 <body>
	  <pre style="word-wrap: break-word; white-space: pre-wrap;">
	"{"Title":"One Indian Girl","Year":"2016","Author":"Chetan Bhagat"}"
	</pre>
	 </body>
	</html>
	>>>
	>>> print(soup.find("pre"))
	<pre style="word-wrap: break-word; white-space: pre-wrap;">
	"{"Title":"One Indian Girl","Year":"2016","Author":"Chetan Bhagat"}"
	</pre>
	>>>
	>>> print(soup.find("pre").string)

	"{"Title":"One Indian Girl","Year":"2016","Author":"Chetan Bhagat"}"

	>>> print(soup.find("pre").string[2:-2])
	{"Title":"One Indian Girl","Year":"2016","Author":"Chetan Bhagat"}
	>>>
	>>> d = json.loads(soup.find("pre").string[2:-2])
	>>> type(d)
	<type 'dict'>
	>>>
	>>> d
	{u'Author': u'Chetan Bhagat', u'Year': u'2016', u'Title': u'One Indian Girl'}
	>>>
	>>> d["Author"]
	u'Chetan Bhagat'
	>>>
	>>> d["Year"]
	u'2016'
	>>>
	>>> d["Title"]
	u'One Indian Girl'
	>>>