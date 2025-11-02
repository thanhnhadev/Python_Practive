# i= input("nhap chieu cao tam giac:")
# n = int(i)
a= int(input("nhap chieu cao tam giac:"))
# print(f'tam giac vua nhap {i}')
# for i in range(n):
#     for j in range(1, n, i + 1):
#          print('*',end='')
#     print('')
# for i in range( 1, n+1):
#     print('*' * i,sep='')
# for i in range( 1, a+1):
#     print('' * (a-i), end='')
#     print('*' * i)
for i in range(1, a + 1):
    print(' '*(a-i),end='')
    print('*'*((i-1)*2+1))