nums_list = input().split()

if len(nums_list) == len(set(nums_list)):
    print('Все числа разные')
elif len(set(nums_list)) == 1:
    print('Все числа равны')
else:
    print('Есть равные и неравные числа')
