from os import chdir,listdir,rename
from time import sleep
import random
from random import randint
from json import dump
import requests
from requests import get
from bs4 import BeautifulSoup
from re import findall,compile
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















