barcode = input()

even_count = 0
odd_count = 0

#    в задаче не совсем логичные условия
#    при написании программ, мы обычно используем порядок от 0 и далее,
#    но в данной ситуации, задача говорит о нумерации от 1:
#    (пример: "Например, вот кетчуп. Код у него – 4604075024433.
#    На нечетных местах: 4, 0, 0, 5, 2, 4, 3.
#    На четных: 6, 4, 7, 0, 4, 3.")
#    таким образом, возникает вопрос: "что на самом деле чётное???"
#    Поэтому, в решении данной задачи решила действовать так, чтобы выполнялись условия задачи,
#    даже если они и не очень логичны
#    Прошу принять, понять и простить грешника, но мой (i % 2 == 0) больше не означает четное....
    

for i in range(len(barcode)):
    if i % 2 == 0:
        odd_count += int(barcode[i])
    else:
        even_count += int(barcode[i])
        
summ = 3*even_count + odd_count
print(odd_count)
if summ % 10 == 0:
    print('yes')
else:
    print('no')