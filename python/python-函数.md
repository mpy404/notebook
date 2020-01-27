#### 将列表返回

```py
names = ["a", "b", "c", "d", "e"]


def print_list(names):
    for inx, name in enumerate(names):
        print(inx)
        print(name)


print_list(names)
```

#### 将字典返回

```py

age = {"a": "a", "b": "b", "c": "c"}

def print_dict(age):

    for key, value in age.items():
        print("Key:" + key)
        print("Value:" + value + "\n")


print_dict(age)


def print_dicts(first, last, **people):
    a = {}
    a["firstname"] = first
    a["lastname"] = last
    for key, value in people.items():
        a[key] = value
    return a


b = print_dicts("mpy", "abc", a="a", b="b")
print(b)

```
#### 将元组返回

```py

def print_tuple(size, *names):
    print(size)
    for name in names:
        print(name)


print_tuple(12, "a", "b")

```

