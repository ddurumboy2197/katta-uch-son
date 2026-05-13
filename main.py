def eng_katta_son(a, b, c):
    return max(a, b, c)

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

print("Eng katta son:", eng_katta_son(a, b, c))
```

```python
def eng_katta_son(*sonlar):
    return max(sonlar)

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

print("Eng katta son:", eng_katta_son(a, b, c))
