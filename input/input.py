def inputsite(a) :
    vat = ""
    if a == 1 :
        vat += str('sise_rise.nhn')
        fullsite = "http://finance.naver.com/sise/"+str("sise_rise.nhn")
    elif a ==2 :
        vat = 'sise_steady.nhn'
        fullsite ="http://finance.naver.com/sise/" +str('sise_steady.nhn')
    elif a==3 :
        vat = 'sise_fall.nhn'
        fullsite ="http://finance.naver.com/sise/"+ str('sise_fall.nhn')
    print(vat)
    fullsite = "http://finance.naver.com/sise/"+vat
    print(fullsite)

    return fullsite
