temperatures=[73, 74, 75, 71, 69, 72, 76, 73]
final_arr=[]
for indx,i in enumerate(temperatures):
    for indx1,j in enumerate(temperatures[indx+1:]):
        if(j>i):
            final_arr.append(indx1+1)
            break
        if(len(temperatures[indx+1:])==indx1+1):
            final_arr.append(0)
final_arr.append(0)
print(final_arr)