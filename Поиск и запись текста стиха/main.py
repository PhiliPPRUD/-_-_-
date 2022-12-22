import requests
from bs4 import BeautifulSoup

def get_links(adr):
    resp_co = requests.get(adr)
    all_text_co = resp_co.text
    soup = BeautifulSoup(all_text_co, "html.parser")
    resp = soup.find_all("a")
    return resp

new_file = 1

f = open("output" + str(new_file) + ".txt", "w")

mas_links_a_dirt = get_links("https://stihibase.ru/author/")

mas_links_a = []


kol_links_a = 0
kol_links_s = 0

for links_a1 in mas_links_a_dirt:
    links_a = links_a1.get("href")
    if "/author/" in links_a and links_a.count("/") == 4 and links_a not in mas_links_a:
        kol_links_a += 1
        mas_links_a.append(links_a)

        mas_links_s_dirt = get_links("https://stihibase.ru" + links_a)

        for links_s1 in mas_links_s_dirt:
            links_s = links_s1.get("href")
            if links_s.count("/") == 5:
                kol_links_s += 1
                if kol_links_s % 3000 == 0:
                    new_file += 1
                    f.close()
                    f = open("output" + str(new_file) + ".txt", "w")
                f.write("https://stihibase.ru" + links_s + "\n")
f.close()
                    
