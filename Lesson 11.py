import requests

responce = requests.get("https://coinmarketcap.com/")

# coin_list = []
# responce_text = responce.text.split("<span>")
# for elem in responce_text:
#     if elem.startswith("$"):
#         for elem2 in elem.split("</span>"):
#             if elem2.startswith("$"):
#                 coin_list.append(float(elem2.replace("$", "").replace(",", "")))
#
# print("BTC -", coin_list[0])



from bs4 import BeautifulSoup
soup = BeautifulSoup(responce.text, features="html.parser")
soup_list = soup.find("div", {"class", "sc-b3fc6b7-0"}).next_element.text
# soup_list = soup.find_all("sc-b3fc6b7-0 dzgUIj rise")
print(soup_list)