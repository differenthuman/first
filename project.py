from urllib.request import *
import sys
import time

from bs4 import BeautifulSoup
import matplotlib.pyplot as p

def information() :
    pList = list()
    data = urlopen('http://finance.naver.com/sise/sise_rise.nhn')
    soup = BeautifulSoup(data)
    trList = soup.findAll('a', attrs={'class':'tltle'})
    for i in range(100):
        name = trList[i].text
        print(name)

information()
