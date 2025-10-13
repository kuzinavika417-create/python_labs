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
### max_min
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

### unique_sorted
```
nums = [[3, 1, 2, 1, 3],[],[-1, -1, 0, 2, 2],[1.0, 1, 2.5, 2.5, 0]]
def unique_sorted(nums):
    if not nums:
        return []
    return sorted(set(nums))
for num in nums:
    print(f'{num} -> {unique_sorted(num)}')
```
![alt text](images/lab02/ex02.png)
### flatten
```
nums = [[[1, 2], [3, 4]],([1, 2], (3, 4, 5)),[[1], [], [2, 3]],[[1, 2], "ab"]]
def flatten(nums):
    exit_material = []
    for i  in nums:
        if type(i) != str:
            for j in i :
                exit_material.append(j)
        else:
            return 'TypeError'
    return exit_material
for i in nums:
     print(f'{i} -> {flatten(i)}')
```
![alt text](images/lab02/ex03.png)

## Задание В
```
def transpose(mat: list[list[float | int]]) -> list[list] :
    if not mat:
        return []
    for i in mat :
        if len(i) != len(mat[0]) :
            return 'ValueError'
    str = []
    for i in range(len(mat[0])) :
        A = []
        for j in range(len(mat)):
            A.append(mat[j][i])
        str.append(A)
    return str
print(f'{[1, 2, 3]} -> {transpose([[1, 2, 3]])}') 
print(f'{[1], [2], [3]} -> {transpose([[1], [2], [3]])}')  
print(f'{[[1, 2], [3, 4]]} -> {transpose([[1, 2], [3, 4]])}')  
print(f'{[]} -> {transpose([])}')  
print(f'{[[1, 2], [3]]} -> {transpose([[1, 2], [3]])}') 
```
![alt text](images/lab02/ex04.png)