num_list = [-1,2,-3,4,5,6,-87,8,9-99]
print(num_list)
newlist=[x for x in num_list if x>0]
print("the positive numbers are",newlist)


n=int(input("enter the number of elements:"))
num_list=[]
for i in range(n):
    a=int(input("enter the number: "))
    num_list.append(a)
print("entered list:",num_list)
sqr_lst=[x**2 for x in num_list]
print(sqr_lst)


word=input("enter the word: ")
vowels=[x for x in word if x in "aeiou"]
print("vowels:",vowels)



w=input("enter the word: ")
ord=[ord(x) for x in w]
print("the ordinal value is:",ord)

