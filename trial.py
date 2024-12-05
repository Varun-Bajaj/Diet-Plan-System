import pickle
def trying(filename):
    f1=open(filename,'rb')
    c=0
    while f1:
        try:
            v=pickle.load(f1)
            c=c+1
        except:
            break

    return c
        
    
