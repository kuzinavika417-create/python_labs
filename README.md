# python_labs
## Задание 1
```
name = input(f'Введите имя:')
age = int(input(f'Введите возраст:'))
print(f'Привет,{name}! Через год тебе будет {age + 1}' )
```

![alt text](images/ex01.png)

## Задание 2
```
a = input("a: ").replace(',','.')
b = input("b: ").replace(',','.')
a = float(a)
b = float(b)
summa = a + b
avg = summa/2
print(f"sum = {summa:.2f}; avg = {avg:.2f}")
```
![alt text](images/ex02.png)

## Задание 3
``` price = float (input("Цена:"))
discount = float (input("скидка %:"))
vat =float (input("НДС%:"))

base = price * (1 - (discount / 100))
vat_amount = base*(vat / 100)
total = base + vat_amount

print(f"База после скидки:{base}")
print(f"НДС:{vat_amount}")
print(f"Итого к оплате:{total}")
```
![alt text](images/ex03.png)
## Задание 4
```
m = int(input("Минуты :"))
day = m //(60*24)
daymin = m % (60*24)
hour = daymin // 60
minute = daymin % 60
if day > 0:
    print(f"{day}.{hour}.{minute:02d}")
else:
    print(f"{hour}.{minute:02d}")

```
![alt text](images/ex04.png)

## Задание 5
``` 
inicials = input("ФИО: ")
inicials_clear = " ".join(inicials.split())
words = inicials_clear.split()
iniciali = "".join([word[0].upper() for word in words]) + "."
print(f"ФИО: {inicials}")
print(f"Инициалы: {iniciali}")
print(f"Длина (символов) : {len(inicials_clear)}")

```
![alt text](images/ex05.png)

# Лабораторная работа 2
## Задание 1
```
nums = [[3, -1, 5, 5, 0],[42],[-5, -2, -9],[],[1.5, 2, 2.0, -3.1]]
def min_max(nums):
    if nums:
        return min(nums), max(nums)
    else:
        return ('ValueError')
for i in nums:
    print(f'{i} -> {min_max(i)}')
 ```
![alt text](images/lab02/ex01.png)