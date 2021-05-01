def reverse(n):
    result=0
    n_str=str(n)
    size=len(n_str)
    temp=n
    while True:
        remainder=temp%10
        result=result+remainder*(10**(size-1))
        size=size-1
        temp=temp//10
        
        if temp==0:
            break

    return result
