def sum(x,y):
    return x+y
    
def mul(x,y):
    return x*y


    l1 = {2,3,4,5,6}
    l2 = {3,4,1,4,5}
    
    for a in l2:
            print(sum(l1[l2.index(a)],a)