## Условен израз

Условният израз (conditional expression) е съкратена форма за изчисляване на стойност под условие.

```
а = x if C else y
```

Горният блок е еквивалентен на:
```
if C:
    a = x
else:
    a = y
```

## Примери
```
value = 'вярно' if True else 'грешно'
let_in = True if age>18 else False
abs_value = x if x>0 else -x
name = text.upper() if text else None
item = items[0] if len(items)>0 else None
```