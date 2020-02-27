import webbrowser

url = 'https://intranet.seidor.es/sap/bc/ui5_ui5/ui2/ushell/shells/abap/Fiorilaunchpad.html'

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)

import requests
from bs4 import BeautifulSoup

user = 'cgarcia'
password = 'Codigo20!'
with Session() as s:
    site = s.get("http://quotes.toscrape.com/login")
    print(site.content)