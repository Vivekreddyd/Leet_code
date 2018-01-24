
def shoppingOffers(price, special, needs):
    """
    :type price: List[int]
    :type special: List[List[int]]
    :type needs: List[int]
    :rtype: int
    """
    tval=[]

    for sp in special:
        flag = False
        val=sp.pop(-1)
        n1=[a_i - b_i for a_i, b_i in zip(sp, needs)]
        #print(n1)
        for ind, pr in enumerate(n1):
            #print (pr)
            if(pr<0):
                val+=abs(pr)*price[ind]
            elif(pr>0):
                flag=True
                continue
        if(flag==False):
            tval.append(val)
    return (min(tval))
print(shoppingOffers([0,0,0],[[1,1,0,4],[2,2,1,9]],[1,1,1]))