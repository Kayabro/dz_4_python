
# list_1 = [int(input('добавьте число в список №1: ')) for i in range(int(input("Укажите длину первого списка №1: ")))]
# list_2 = [int(input('добавьте число в спискок:№2: ')) for i in range(int(input("Укажите длину второго списка №2 : ")))]
# list_result  = []
# for i in list_1:
#     if i in list_2 and i not in list_result:
#         list_result.append(i)
# print(*list_result)

# n = int(input('кол-во кустов: '))
# a = list(map(int, input('сколько ягод на каждом кусте: ').split()))
# berry = 0
# i = 1
# for i in range (1, n- 1):
#     if (a[i]+a[i+1]+a[i-1] > berry):
#         berry = a[i]+a[i+1]+a[i-1]
# print(berry)