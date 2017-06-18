# class Solution(object):
#     def findWords(self, words):
"""
:type words: List[str]
:rtype: List[str]
"""
words=["Hello","Alaska","Dad","Peace"]
final = []
r1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
r2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
r3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
# p=re.compile('([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$',re.IGNORECASE)
# print (len(words))
for word in words:
    if (word[0].lower() in r1):
        for i in range(1, len(word)):
            if word[i] in r1:
                continue
            else:
                break
        if (i == len(word) - 1):
            final.append(word)
    elif (word[0].lower() in r2):
        for i in range(1, len(word)):
            if word[i] in r2:
                continue
            else:
                break
        if (i == len(word) - 1):
            final.append(word)
    elif (word[0].lower() in r3):
        for i in range(1, len(word)):
            if word[i] in r3:
                continue
            else:
                break
        if (i == len(word) - 1):
            final.append(word)


            # if(words[i] in r1 or words[i] in r2 or words[i] in r3)
            #     #word=words[i]
            #     #final=p.match(word)
            #     final.append(words[i])
            # print final
# re.match(r'[qwertyuiop]|[asdfghjkl]|[zxcvbnm]',words,re.I)
print (final)