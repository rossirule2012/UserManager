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


