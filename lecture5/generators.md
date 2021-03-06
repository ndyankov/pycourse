## Генератори
Генераторите в Питон служат за динамично генериране на поредица от стойности.

### Генератори-изрази
Синтактично, генераторите-изрази много наподобяват list comprehensions. При замяна на квадратните скоби ```[]``` с кръгли ```()``` в кой-да е list comprehension (само от тип list!) получаваме обект 
от тип генератор-израз.

```
# list comprehension
>>> items = [x for x in range(2)]
>>> items
[0, 1]
>>> type(items)
<type 'list'>


# generator expression
>>> gitems = (x for x in range(2))
>>> gitems
<generator object <genexpr> at 0x7f9f48097640>
>>> type(gitems)
<type 'generator'>
```

За разлика от list comprehension, които веднага връщат резултат, стойностите от генератора се получават само динамично "при поискване" посредством итератор-протокола:
```
>>> next(gitems)
0
>>> next(gitems)
1
>>> next(gitems)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Вградената функция ```next``` позволява извличането на стойности от генератора до достигане на края му, 
след което се хвърля изключение/грешка от тип ```StopIteration``` 
(същият ефект се постига и чрез директно извикване на метода върху обекта ```next/__next__``` съответно във версия 2 или 3).

Итератор-протокола обикновено остава скрит и не се ползва експлицитно в кода. Това позволява замяната на всеки един
list comprehension със съответния му генератор.
```
>>> items = [x for x in range(2)]
>>> gitems = (x for x in range(2))
>>> for x in items: print(x)
... 
0
1
>>> for x in gitems: print(x)
... 
0
1
```

Това, обаче, води и до някои разлики. Ако един списък може да се обходи колкото пъти искаме, то 
генераторът може да се обходи само веднъж. В това има логика, щом като стойностите се генерират динамично 
и не се запазват никъде автоматично.
```
>>> for x in items: print(x)
... 
0
1
>>> for x in gitems: print(x)
... 
>>> 
```

Поради същата причина, той няма отнапред зададена дължина:
```
>>> len([x for x in range(2)])
2
>>> len((x for x in range(2)))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'generator' has no len()
```

Поради динамичната природа на генераторите, те се държат по-скоро като функции по отношение на 
(глобалните) променливи, които реферират. Това понякога може да води до изненади.
```
>>> alist = [1, 2]
>>> glist = (x for x in alist)
>>> alist.append(3)
>>> for x in glist: print(x)
... 
1
2
3
```

### Генератори-функции
В случай че е нужна по-сложна логика, отколкото може да се изрази посредством генератор-израз, може да се използва
генератор-функция. Разликата с обикновените функции е единствено по наличието на ключовата дума ```yield``` (една или повече), 
която се използва за връщане на изчислените стойности. 

Ето един безкраен генератор на поредицата от естествени числа:
```
def integers():
    x = 0
    while True:
        x = x + 1
        yield x
```

Той би се използвал посредством фунцкията ```next``` или например така:
```
for x in integers():
    print(x)
    if x>100:
        break
```

### Генератори-класове
За пълнота, ето как се имплементира генератор директно посредством итератор-протокола:
```
class integers(object):

    def __init__(self):
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.x += 1
        return self.x

    def next(self):
        return self.__next__()
```


### Ресурси
https://www.python.org/dev/peps/pep-3114/

http://anandology.com/python-practice-book/iterators.html#generators
