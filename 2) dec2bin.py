print("10진수를 2진수로 바꾸는 프로그램입니다. 바뀐 2진수는 리스트의 형태로 출력됩니다. 예:dec2bin(26)->[1, 1, 0, 1, 0]")
def dec2bin(dec_number):
    list=[]
    
    while dec_number!=0:
        if (dec_number%2==0):
            list.append(dec_number%2)
            dec_number=dec_number//2
        else:
            list.append(dec_number%2)
            dec_number=dec_number//2


    list.reverse()
    return list       
