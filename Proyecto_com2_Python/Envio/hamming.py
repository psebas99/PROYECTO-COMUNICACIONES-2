def hamming(archivo):
    import math 
    from operator import xor 
    d1=int
    d2=int
    d3=int
    d4=int
    p1=int
    p2=int
    p3=int
    
    for i in archivo :
        
        if archivo == "1":
            archivo = "1000"
        if archivo == "0":
            archivo = "0000"

        
        if archivo == "11":
            archivo = "1100"
        if archivo == "00":
            archivo = "0000"
        if archivo == "10":
            archivo = "1000"
        if archivo == "01":
            archivo = "0100"

        
        if archivo == "111":
            archivo = "1110"
        if archivo == "110":
            archivo = "1100"
        if archivo == "101":
            archivo = "1010"
        if archivo == "100":
            archivo = "1000"
        if archivo == "011":
            archivo = "0110"
        if archivo == "010":
            archivo = "0100"
        if archivo == "001":
            archivo = "0000"
        if archivo == "000":
            archivo = "0000"
        

        d1=archivo[0]
        d2=archivo[1]
        d3=archivo[2]
        d4=archivo[3]

        
        p1=xor(int(d1),int(d2))
        p1=xor(p1,int(d4))
        p2=xor(int(d1),int(d3))
        p2=xor(p2,int(d4))
        p3=xor(int(d2),int(d3))
        p3=xor(p3,int(d4))

        mensaje_final=str(p1)+str(p2)+str(d1)+str(p3)+str(d2)+str(d3)+str(d4)
        return mensaje_final



        

        
        
    

   
   
   