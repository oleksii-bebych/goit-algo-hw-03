# Модуль 3. Робота з датою, часом та розширена робота з рядками

## Перше завдання
Створіть функцію `get_days_from_today(date)`, яка розраховує кількість днів між заданою датою і поточною датою.

### Вимоги до завдання:
1. Функція приймає один параметр: `date` — рядок, що представляє дату у форматі `'РРРР-ММ-ДД'` (наприклад, `'2020-10-09'`).
2. Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
3. У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
4. Для роботи з датами слід використовувати модуль `datetime` Python.

### Рекомендації для виконання:
1. Імпортуйте модуль `datetime`.
2. Перетворіть рядок дати у форматі `'РРРР-ММ-ДД'` у об'єкт `datetime`.
3. Отримайте поточну дату, використовуючи `datetime.today()`.
4. Розрахуйте різницю між поточною датою та заданою датою.
5. Поверніть різницю у днях як ціле число.

### Критерії оцінювання:
1. Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
2. Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
3. Читабельність коду: код повинен бути чистим і добре документованим.

### Приклад:
Якщо сьогодні 5 травня 2021 року, виклик `get_days_from_today("2021-10-09")` повинен повернути `157`, оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року.

## Друге завдання
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.
Вам необхідно написати функцію `get_numbers_ticket(min, max, quantity)`, яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.
Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.

### Вимоги до завдання:
1. Параметри функції:
* `min` - мінімальне можливе число у наборі (не менше 1).
* `max` - максимальне можливе число у наборі (не більше 1000).
* `quantity` - кількість чисел, які потрібно вибрати (значення між min і max).
2. Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
3. Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.


### Рекомендації для виконання:
1. Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
2. Використовуйте модуль random для генерації випадкових чисел.
3. Використовуйте множину або інший механізм для забезпечення унікальності чисел.
4. Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.


### Критерії оцінювання:
1. Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
2. Унікальність результату: усі числа у видачі повинні бути унікальними.
3. Відповідність вимогам: результат має бути у вигляді відсортованого списку.
4. Читабельність коду: код має бути чистим і добре документованим.


### Приклад: 
Припустимо, вам потрібно вибрати `6` унікальних чисел для лотерейного квитка, де числа повинні бути у діапазоні від `1` до `49`. Ви можете використати вашу функцію так:

```python
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
```

Цей код викликає функцію get_numbers_ticket з параметрами min=1, max=49 та quantity=6. В результаті ви отримаєте список з 6 випадковими, унікальними та відсортованими числами, наприклад, [4, 15, 23, 28, 37, 45]. Кожен раз при виклику функції ви отримуватимете різний набір чисел.

## Третє завдання (не обов'язкове)
У вашій компанії ведеться активна маркетингова кампанія за допомогою SMS-розсилок. Для цього ви збираєте телефонні номери клієнтів із бази даних, але часто стикаєтеся з тим, що номери записані у різних форматах. Наприклад:

```
"    +38(050)123-32-34"
"     0503451234"
"(050)8889900"
"38050-111-22-22"
"38050 111 22 11   "
```

Ваш сервіс розсилок може ефективно відправляти повідомлення лише тоді, коли номери телефонів представлені у коректному форматі. Тому вам необхідна функція, яка автоматично нормалізує номери телефонів до потрібного формату, видаляючи всі зайві символи та додаючи міжнародний код країни, якщо потрібно.
Розробіть функцію `normalize_phone(phone_number)`, що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ `'+'` на початку. Функція приймає один аргумент - рядок з телефонним номером у будь-якому форматі та перетворює його на стандартний формат, залишаючи тільки цифри та символ `'+'`. Якщо номер не містить міжнародного коду, функція автоматично додає код `'+38'` (для України). Це гарантує, що всі номери будуть придатними для відправлення SMS.

### Вимоги до завдання:
1. Параметр функції `phone_number` - це рядок з телефонним номером у різноманітних форматах.
2. Функція видаляє всі символи, крім цифр та символу `'+'`.
3. Якщо міжнародний код відсутній, функція додає код `'+38'`. Це враховує випадки, коли номер починається з `'380'` (додається лише `'+'`) та коли номер починається без коду (додається `'+38'`).
4. Функція повертає нормалізований телефонний номер у вигляді рядка.

### Рекомендації для виконання:
1. Використовуйте модуль re для регулярних виразів для видалення непотрібних символів.
2. Перевірте, чи номер починається з `'+'`, і виправте префікс згідно з вказівками.
3. Видаліть всі символи, крім цифр та `'+'`, з номера телефону.
4. На забувайте повертати нормалізований номер телефону з функції.

### Критерії оцінювання:
1. Коректність роботи функції: функція має правильно обробляти різні формати номерів, враховуючи наявність або відсутність міжнародного коду.
2. Читабельність коду: код має бути чистим, добре організованим і добре документованим.
3. Правильне використання регулярних виразів для видалення зайвих символів та форматування номера.

###  Приклад використання:

```python
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
```

У результаті ви повинні отримати список номерів у стандартному форматі, готових до використання у SMS-розсилці.

```
Нормалізовані номери телефонів для SMS-розсилки: ['+380671234567', '+380952345678', '+380441234567', '+380501234567', '+380501233234', '+380503451234', '+380508889900', '+380501112222', '+380501112211']
```
