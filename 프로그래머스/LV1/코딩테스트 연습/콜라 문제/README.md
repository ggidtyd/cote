콜라는 처음에 n개로 시작한다  

x번째 콜라 교환을 수행한 후의 콜라 개수를 a<sub>x</sub>라고 하면  
a<sub>x</sub> = n - (a-b)*x 와 같이 초항 == n, 등차 d == (a-b)인 등차수열로 나타낼 수 있다  

문제에서 요구하는 것은 받은 콜라 개수다  
이것을 위해서 x (교환 횟수)를 알아야 한다  

n,a,b는 주어지므로 교환을 최대로 한 마지막항 a<sub>x</sub>의 값을 알면 x를 구할 수 있다    

말항 a<sub>x</sub>는 n - (a-b)*x가 < a가 되는 순간이다  
n - a < (a-b) * x  
(n-a) // (a-b) < x 이고  

이로부터  
x의 값이 (n-a) // (a-b) + 1 이라는 것을 알 수 있다  
여기에 b를 곱하면 받은 콜라의 개수다  

(n-a) // (a-b) + 1을 정리하면 (n-b) // (a-b) 가 된다


따라서  
```python
def solution(a, b, n):
    return ((n-a) // (a-b) + 1) * b
```
또는  
```python
def solution(a, b, n):
    return (n-b) // (a-b) * b
``` 




