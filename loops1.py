for s in range(1,5):
    print(s)

list1=[1,3,6,9,11,8,354,8976]
print(max(list1))
maximum=0
for n in list1:
    if n > maximum:
        maximum=n
print(maximum)

age=16
while age<18:
    age+=1
    print (f'A year has passed, now im {age}')

mylist2=[2,4,6,8,9,10,12]
for n in mylist2:
    print(n)
    if n%2 !=0:
        break
print('-----------')
for n in mylist2:
    print(n)
    if n%2 !=0:
        continue

#while True:
    #numri=input('please enter a positive number')
    #if numri.isnumeric():
        #if int(numri)>0:
            #print('Thank you')
           # break
num_list=[]
for n in range(0,100):
    if n%2==0:
        num_list.append(n)
    else:
        continue
print(num_list)



