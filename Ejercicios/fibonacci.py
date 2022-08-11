def fibonacci(n):
    if n==0: 
        return 0
    if n==1:
        return 1
    resultado = 1
    while n >= 2 :
        resultado += (n-1)
        
        print (resultado)
        n -= 1

print(fibonacci(4))    