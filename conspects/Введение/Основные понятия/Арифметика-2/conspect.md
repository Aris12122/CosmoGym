## Арифметика - 2

### Быстрое возведение в степень

Ранее мы могли использовать следующую функцию для возведения числа в степень:

```cpp
int power(int a, int n){
    int ans = 1;
    for(int i = 0; i < n; i++){
        ans *= a;
    }
    return ans;
}
```

Для того, чтобы возвести число в степень $n$ нам необходимо было в точности $n$ операций, соответсвенно, асимптотика данного решения составляла $O(n)$.

Однако, существует способ, позволяющий возводить число в степень гораздо быстрее. Он базируется на следующих свойствах степеней:

1. $a^{2n} = (a^n)^2$
2. $a^{2n + 1} = (a^n)^2 \cdot a$

Проиллюстрировать это более наглядно можно так:

#TODO

### Операции по модулю

*Внимание! Данный раздел будет актуален только для языка с++*.

Часто в задачах вы будете встречаться с формулировкой, похожей на следующую:

> Так как ответ может получиться достаточно большим, выведите его по модулю $10^9 + 7$.

Она особенно характерна для комбинаторных задач, где величины растут очень быстро.

В прошлом разделе мы рассмотрели определение остатка от деления. 

> Выведите $n$-е ($1 \le n \le 10^4$) число Фибоначчи по модулю $10^6 + 3$

Первая мысль, которая может возникнуть &mdash; посчитать ответ как обычно и в конце один раз взять ответ по модулю, вот так:

```cpp
int f0 = 1
int f1 = 1
int mod = 1e6 + 3;
for(int i = 2; i <= n; i++){
    f = f0 + f1;
    f0 = f1;
    f1 = f;
}
cout << (f % mod);
```