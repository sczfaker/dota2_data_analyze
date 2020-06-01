from os import chdir,listdir,rename
from re import findall,compile
from bs4 import BeautifulSoup
from random import randint
from time import sleep
from json import dump
from requests import get
import requests
import random
chdir("dota")
links=[]
for i in listdir():
	if i[:5]=="hero_":
		with open(i,"r+",encoding="utf-8") as f:
			need_to_clean=f.read()
			bs4_=BeautifulSoup(need_to_clean,"html.parser")
	if i[:5]=="hero_":
		z=bs4_.find(class_="hero-secondary-ability-icons r-none-mobile")
		ppp=z.find_all("img",alt=True)
		ability=[i.attrs["alt"] for i in ppp]
		link=z.find("a",href=True)["href"]
		links.append(link)
assert len(links)==117
with open("abi_links.txt","w+") as f:
	f.writelines([i+"\n" for i in links])















