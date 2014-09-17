def hash(to_hash):
    buffer=[]
    i=0
    s=''
    for char in to_hash:
        i-=1
        buffer+=[char,to_hash[i],to_hash[-(i+1)],char,to_hash[i]]
    for i in range(len(buffer)):
        s+=buffer[len(buffer)-1-i]
    return s

def dehash(to_dehash):
    temp=''
    dehashed=''
    buffer=[]
    for char in to_dehash:
        buffer+=char
    for i in range(len(buffer)):
       temp+=buffer[len(buffer)-1-i]
    for i in range(len(temp)):
        if i%5==0:
            dehashed+=(temp[i])
    return dehashed


