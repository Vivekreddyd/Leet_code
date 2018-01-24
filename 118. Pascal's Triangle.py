# def tri(val1,val2):
#     return [x+y for x,y in zip(val1,val2)]
def generate(numRows):
    res = [[1]]
    for i in range(1, numRows):
        temp1=res[-1]+[0]
        temp2=[0]+res[-1]
        res.append(list(map(lambda x,y:x+y, res[-1]+[0],[0]+res[-1])))
        # temp= map(tri(temp1,temp2),temp1,temp2)
        # res += temp
    return res[:numRows]
    # res = [[1]]
    # for i in range(1, numRows):
    #     temp1 = res[-1] + [0]
    #     temp2 = [0] + res[-1]
    #     res.append([temp1[i] + temp2[i] for i in range(len(temp1))])
    # return res[:numRows]

for i in range(5):
    print(generate(i))