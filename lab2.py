# a1=[5,10,15,20,25]
# newlist1=[]
# newlist1.append(a1[0])
# newlist1.append(a1[4])
# print(newlist1)


# for i in range(len(a1)):
# 	if (a1[i]>5):
# 		print(a1[i])












# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# newlist=[]
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             numberExists=False
#             for num in newlist:
#                 if a[i]==num:
#                     numberExists=True
#             if numberExists==False:
#                 newlist.append(a[i])
        
# print(newlist)

c=0
input1 = input("prime?")
for i in range(input1):
	if (input1%(i+1)==0):
		c=c+1
if (c==2):
	print("is prime number")
else:
	print("not prime number")








   
