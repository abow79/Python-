from bs4 import BeautifulSoup
import requests
import codecs
import prettytable
h={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
	"Cookie":"TS010c55bd=0107dddfeffb659d45455d7bd9fbe111f9ac39ace6a96771169e2ee140c8a405a716fc7ea27274066d14d7e7744623a545c845842d; TS558d33eb027=08dc4bbcbbab200066d07c77d6262e98eb702e621b999a95f96f1b00b3358bce38234efddd7183710856f1bcd4113000e88490a895fd7d345857bc1f9e310a9fc1a4853b1685a85ce18ca142afb033653e0cb945e4047c58ed92a3b70634e102; _ga=GA1.3.1015935367.1606293678; _gid=GA1.3.239161874.1606293678",
	"ID":"Wed%20Nov%2025%202020%2016:44:46%20GMT+0800%20(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)"
}
r1=requests.get("https://www.cwb.gov.tw/V8/C/W/TemperatureTop/County_TMax_T.html",
		headers=h
	)
b=BeautifulSoup(r1.text, "html.parser")
p=prettytable.PrettyTable(["地區","氣溫"], encoding="utf8")
p.align["地區"]="l"  #靠左對齊
p.align["氣溫"]="c"	 #置中對齊
data=b.find_all("tr")
for x in data:
	data2=x.find("th")
	data3=x.find("span",class_="tem-C is-active")
	p.add_row([data2.text,data3.text])
print(p)