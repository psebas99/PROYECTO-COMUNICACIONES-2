
def hammingdeco(palabra):
    from operator import xor
    aux = int
    d1 = int
    d2 = int
    d3 = int
    d4 = int
    #PARIEDAD DE TRANSMISION
    p1 = int
    p2 = int
    p3 = int
    #PARIEDAD DE RECEPCION
    p11 = int
    p12 = int
    p13 = int

    e1 = int
    e2 = int
    e3 = int

    er = int

    correlativo = int
    correlativo1 = int

    mensaje = str('')
    mensaje1 = str('')

    texto = []
    tren= ""
    
    for j in palabra:

        #print(j[0]+j[1]+j[2]+j[3]+j[4]+j[5]+j[6])
        word = ''
        p1 = j[0]
        p2 = j[1]  
        d1 = j[2] 
        p3 = j[3]  
        d2 = j[4]
        d3 = j[5]
        d4 = j[6]

        #print(p1+p2+d1+p3+d2+d3+d4)

        p11=xor(int(d1),int(d2))
        p11=xor(p11,int(d4))
        p22=xor(int(d1),int(d3))
        p22=xor(p22,int(d4))
        p33=xor(int(d2),int(d3))
        p33=xor(p33,int(d4))

        e1=xor(int(p1),p11)
        e2=xor(int(p2),p22)
        e3=xor(int(p3),p33)
        er=(4*e3)+(2*e2)+(1*e1)
        #print(er)



        #if er==3:
           # if d1==1:d1=0
           # else: d1=1

        #if er==5:
            #if d2==1:d2=0
            #else: d2=1

        #if er==6:
         #   if d3==1:d3=0
          #  else: d3=1

        #if er==7:
         #   if d4==1:d4=0
          #  else: d4=1   
    
        #print(p1+p2+d1+p3+d2+d3+d4)
    
        word = d1+d2+d3+d4
        #print(word)
        #print(word)

        texto.append(word)
        tren = str(tren) + str(word)

    print(tren)
    return tren
