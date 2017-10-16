from urllib.request import *
import sys
import time

from bs4 import BeautifulSoup
import matplotlib.pyplot as p

class inpu :
    def __init__(self):
        print("input 실행!")
        print("\n")
    def inputf(self, n) :
        default = "http://finance.naver.com/sise/"
        if n==1 :
            abc = "sise_rise.nhn"
        elif n==2 :
            abc = "sise_steady.nhn"
        elif n == 3 :
            abc = "sise_fall.nhn"
        fullsite = default + str(abc)
        return fullsite
    
class outpu :
    def __init__(self):
        print("output 실행!")
        print("\n")
    def outputf(self, List) :
        for i in range(100) :
            name = List[i].text
            print(name)

class process :
    def information(self) :
        start = inpu()
        n = int(input("어떤 주식을 원하시나요? 1:상승 2:보합 3:하락"))
        url = start.inputf(n)
        data = urlopen(url)
        soup = BeautifulSoup(data)
        trList = soup.findAll('a', attrs={'class':'tltle'})
        end = outpu()
        end.outputf(trList)

middle = process()
middle.information()
