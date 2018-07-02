# 1. 编程思想  

1. 使用循环，代替重复语句。  
2. 使用函数，使之可重复利用。  
3. 使用参数，代替固定值，使之可以应用于更广泛的场景。  
4. 使用用户输入，使参数调用更灵活，增加用户参与感。  

## 1.1 封装
使用函数，这个点是**封装**的想法。  
> 把一段代码用函数包裹起来，称为封装（encapsulation）。封装的好处是：它给这段代码一个有意义的名称，增加了可读性。重复使用这段代码时，调用一次函数比复制粘贴代码要简易得多。

从polygon转circle的过程中，使用了封装：  

我的程序：  

```
def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        rt(t, 360 / n)  # 右转非90度。


def circle(t, r):
    n = 60
    for i in range(n):
        fd(t, 2 * pi * r / n)
        lt(t, 360 / n)
```
书上的程序：  


```
def polygon(t, length, n):
    for i in range(n):
        fd(t, length)
        lt(t, 360 / n)


def circle(t, r):
    n = 60
    circum = 2 * pi * r
    length = circum / n
    polygon(t, n, length)
```

## 1.2 泛化  
使用参数，这个点是**泛化**的想法。  
> 给函数添加参数的过程，称为泛化（generalization），因为它会让函数变得更通用。  

## 1.3 接口设计  

> 在circle函数中，r属于函数的接口，因为它指定了所画圆的基本属性。

## 1.4 重构

> 重新组织程序，以改善函数的接口，提高代码复用——被称为重构（refactoring）

