# Prompt: Write a function that returns the longest,
# contiguous increasing sequence(s) in a given list of numbers.
#
# f([1, 3, 4, 7, 0, 1, 2, 3]) = [[1, 3, 4, 7], [0, 1, 2, 3]]
# f([1, 5, 8, 0, 9]) = [[1, 5, 8]]

def longest_continuous (list_input):
    min_ind,max_ind=[],[] #store max indexes
    min_val=0
    max1 = 0
    for indx in range(len(list_input)-1):
        # if(list_input[indx]>list_input[indx+1]):
        #     min_val=indx
        if((list_input[indx]>list_input[indx+1]) or indx==len(list_input)-2):
            if(indx==len(list_input)-2):
                max_val=indx+1
            else:
                max_val=indx
            min_ind.append(min_val)
            max_ind.append(max_val+1)
            max1 = max(max1, max_val + 1 - min_val)
            min_val=indx+1
    #num = max([ind[0] - ind[1] for ind in zip(max_ind, min_ind)])
    # print(max1)
    for ind in zip(max_ind, min_ind):
        if (ind[0] - ind[1]) == max1:
            yield list_input[ind[1]: ind[0]]
input_val = [1, 3, 4, 7, 0, 1, 2, 3]
for l in longest_continuous(input_val):
    print(l)