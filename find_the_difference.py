s="abcd"
t="abcde"



#def findTheDifference(self,s,t):
"""
:type s: str
:type t: str
:rtype: str
"""
val = 0
for i in t:
    # print(ord(i))
    val ^= ord(i)
for j in s:
    val ^= ord(j)
print (chr(val))
# print val
# findTheDifference(s,t)