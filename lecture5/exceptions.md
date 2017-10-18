## Изключения (грешки)

Изключения в езика Питон са обекти със специално предназначение, които се хвърлят при наличие на условие за грешка.

### Примери

Деление на нула:

```>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
```

Опит за достъп до елемент извън списъка
```
>>> a = []; a[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

Опит за конверсия към число при невалидна стойност:
```
>>> int('foo')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'foo'
```

Събиране на низ с число
```
>>> 2 + '2'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### Йерархия
Грешките обикновено наследяват `Exception`, така че не е нужно да се помнят имената на всяка една грешка при обработката им.
```
>>> isinstance(ValueError(), Exception)
True
>>> isinstance(TypeError(), Exception)
True
>>> isinstance(IndexError(), Exception)
True
```

### Прихващане (обработка) на грешки
Прихващането на грешки става с употребата на try/except/finally блок.
```
try:
    1/0
except:
    print("Деление на нула!")
```

Същият резултат може да се получи и с прибавяне на типа на прихващаната грешка:
```
try:
    1/0
except Exception:
    print("Деление на нула!")
```

Ако е нужна референция към грешката, то тя може да се вземе като се даде име на променливата(e, error) по следния начин:
```
try:
    1/0
except Exception as e:
    print(e)
```

Няколко типа грешки се обработват при посочване на всеки от типовете - заедно или поотделно
```
try:
    1/0
except ValueError as e:
    print(e)
except (IndexError, TypeError) as e:
    print(e)
except Exception as e:
    pass
```

При изреждането на повече от една except клаузи е важно те да бъдат подредени според специфичността на грешката -
от най-конкретни към общи.

### try/except/finally
Блокът finally е опционален и в него се слага код, който трябва да се изпълни *винаги*, независимо дали е възникнала грешка или не.
Възможна употреба би била за затваряне на отделени по-рано ресурси (отворени файлове, връзка към бази от данни...)
```
try:
    do_something()
except:
    pass
finally:
    pass
```

### Хвърляне на грешки
Хвърлянето на грешки от потребителя става с ключовата дума `raise`.
```
try:
    raise ValueError("this is an error!")
except Exception as e:
    print(e)
```

Употребата на `raise` самостоятелно ще хвърли отново вече обработена грешка.
```
try:
    raise ValueError("two times an error!")
except Exception as e:
    print(e)
    raise
```

## Връзки
https://docs.python.org/3/library/exceptions.html

https://docs.python.org/3/tutorial/errors.html