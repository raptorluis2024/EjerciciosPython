l1 = [1,2,3,4]
l2 = ["a","b","c","a"]

dic = {k:v for k,v in zip(l1,l2)}
print(dic)
dic2 = {k:v for k,v in dic.items() if v =="a"}
print(dic2)
print(dic.items())

