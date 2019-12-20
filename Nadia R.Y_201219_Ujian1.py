# # 1. HASHTAG

# def Hashtag(string):
#     if len(string) == 0:
#         return False
#     else :
#         a = string.split(" ")
#         # print(a)
#         b= list(''.join(a)) 
#         # print(b)

#         hasil = ""
#         for i in b:
#             hasil+=i
#         c= hasil[0]
#         d = c.upper()
#         e = d + hasil[1:]
#         # return e

#         if len(e) > 140:
#             return False
#         else:
#             return "#" + e

#         # print("#" + d + hasil[1:])

# # kal = input("Masukkan kata : ")
# # print(Hashtag(kal))
# print(Hashtag("Hello there how are you doing"))

# 2. phone number

# def create_phone_number(number): 
#     if len(number) != 10:
#         return False
#     else:
#         awal = ""
#         for i in number[:3]:
#             # print(i)
#             awal+=str(i)
#         # print(awal)

#         tengah = ""
#         for j in number[3:6]:
#             tengah+=str(j)
#         # print(tengah)

#         akhir = ""
#         for k in number[6:]:
#             akhir+=str(k)
#         # print(akhir)

#         telpon = ("({}) {}-{}".format(awal,tengah,akhir))
#         return telpon
#         # print(telpon)

# print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))

# 3. sort odd even

# def sort_odd_even(num):

#     c = num[:]
#     genap = []
#     d = num[:]
#     ganjil = []

#     for i in range(len(d)):
#         if d[i] % 2 != 0:
#             ganjil.append(d[i])
#             # d[i] = ""
#     # print(ganjil)
    

#     for i in range(len(ganjil)):
#         for j in range(i+1, len(ganjil)):
#             if ganjil[i] > ganjil[j]:
#                 ganjil[i], ganjil[j] = ganjil[j], ganjil[i]
#     # print(ganjil)

#     for i in range(len(c)):
#         if c[i] % 2 == 0:
#             genap.append(c[i])
#     # print(genap)

#     for i in range(len(genap)):
#         for j in range(i+1, len(genap)):
#             if genap[i] < genap[j]:
#                 genap[i], genap[j] = genap[j], genap[i]
#     # print(genap)


#     e = ganjil+genap
#     return e

# print(sort_odd_even([5,3,2,8,1,4]))



# 4. Hollow Triangle

# def hollowTriangle(n):
#     plus = 4
#     for i in range(1,n+1):
#         for j in range(1,2*n):
#             if i+j == n+1 or j-i==n-1:
#                 print("*", end ="")
#             elif i==n and j!=plus:
#                 print("*",end="")
#                 plus = plus+2
#             else:
#                 print(end="-")
#         print()

# hollowTriangle(5)
