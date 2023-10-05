domain = input()
    
dot1 = domain.find('.')
first_part = domain[:dot1]

dot2 = domain.find('.', dot1+1)
second_part = domain[dot1+1:dot2]
third_part = domain[dot2+1:]

print(third_part, second_part, first_part, sep='\n')