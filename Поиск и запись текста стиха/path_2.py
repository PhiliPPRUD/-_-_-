import library

import requests
from bs4 import BeautifulSoup

f = open("output2.txt", "r")
mas_links_s = f.read().split("\n")

indf = 2998

for links_s in mas_links_s:
    #print(links_s)
    if links_s != "":
        indf += 1
        library.library_poema(links_s, indf)
f.close()
