## Comprehensions

*list/set/dict comprehensions* са изрази, които, след изчисление, имат за резултат обект от съответния тип - 
списък (```list```), множество (```set```) или речник (```dict```). Те преобразуват един (или повече) входящи изрази в друг - изходящ, като дават
възможност за филтриране по зададено условие (едно или повече).

### Пример
Следният израз намира всички нетривиални Питагорови тройки числа (в зададения интервал):
```
>>> [(x, y, z) for x in range(6) for y in range(6) for z in range(6) if x**2 + y**2 == z**2 if x*y*z>0]
[(3, 4, 5), (4, 3, 5)]
```

Най-просто изразите имат следната структура:
```
[<expr<var>> for <var> in <iterable> if <condition>]
```

Ето някои примери:

### List comprehensions
```
# квадрати на числа в интервал
squares = [x*x for x in range(5)]
print(squares)
[0, 1, 4, 9, 16]

# четни числа в интервал
even = [x for x in range(10) if x%2==0]
print(even)
[0, 2, 4, 6, 8]

# намира главни букви в низ
caps = [x for x in 'GiveMeCapsOnly' if x.upper()==x]
print(caps)
['G', 'M', 'C', 'O']
```

### Set comprehensions
Преобразуването на list в set comprehensions става чрез простата замяна на типа скоби: ```[]``` в ```{}```.

```
unique = {letter for letter in "abracadabra"}
print(unique)
set(['a', 'r', 'b', 'c', 'd'])

ints = {x for x in (1, 3, "hello", 5) if isinstance(x, int)}
print(ints)
set([1, 3, 5])
```

### Dict comprehensions
Comprehensions от тип речник използват същите скоби като тези за множество, но добавят ```:``` като разделител за ключ/стойност.
```
squares = {x: x**2 for x in range(5)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

inverted = {v:k for (k, v) in {2:3, 4:5}.items()}
{3: 2, 5: 4}
```

### Генератори
При замяна на квадратните скоби ```[]``` с кръгли ```()``` в кой-да е list comprehension (само от тип list!) получаваме обект 
от тип генератор.
