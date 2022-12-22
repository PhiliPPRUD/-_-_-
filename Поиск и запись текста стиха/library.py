import requests
from bs4 import BeautifulSoup


def library_poema(links_p, indf, encoding = "utf-8"):
    

    resp_p = requests.get(links_p)
    all_text_p = resp_p.text
            
    soup = BeautifulSoup(all_text_p, "html.parser")
        
    fo = open("stih0000" + str(indf) + ".txt", "w", encoding = "utf-8")
        
    if "block-poema" in all_text_p:

        text_stih = soup.find("article", class_ = "block-poema")
        content = text_stih.find_all("p")
                
        for line in content:

            #print(line.text)
            fo.write((line.text) + "\n")
    fo.close()
            
