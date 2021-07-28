def int_to_Roman(inteiro):
    numero_romano = ''
    convertion = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                  'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    while inteiro > 0:
        for key, item in convertion.items():
            for vez in range(inteiro // item):
                numero_romano += key
                inteiro -= item

    print(numero_romano)
    
times = int(input())
numbers = []
for i in range(times):
	a = int(input())
	numbers.append(a)
 
for number in numbers:
    int_to_Roman(number)