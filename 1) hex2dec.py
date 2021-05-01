print("16진수를 10진수로 바꾸는 프로그램입니다. 알파벳 입력시에는 소문자로 입력하고, 따옴표를 해주세요. 예:hex2dec('a1')")
def hex2dec(hex_number):
    hex_str=str(hex_number)
    size=len(hex_str)
    sum=0
    i=0
    while size>0:
        if(hex_str[i]=='1'):
            sum=sum+pow(16, size-1)
        if(hex_str[i]=='2'):
            sum=sum+2*pow(16, size-1)
        if(hex_str[i]=='3'):
            sum=sum+3*pow(16, size-1)
        if(hex_str[i]=='4'):
            sum=sum+4*pow(16, size-1)
        if(hex_str[i]=='5'):
            sum=sum+5*pow(16, size-1)
        if(hex_str[i]=='6'):
            sum=sum+6*pow(16, size-1)
        if(hex_str[i]=='7'):
            sum=sum+7*pow(16, size-1)
        if(hex_str[i]=='8'):
            sum=sum+8*pow(16, size-1)
        if(hex_str[i]=='9'):
            sum=sum+9*pow(16, size-1)
        if(hex_str[i]=='a'):
            sum=sum+10*pow(16, size-1)
        if(hex_str[i]=='b'):
            sum=sum+11*pow(16, size-1)
        if(hex_str[i]=='c'):
            sum=sum+12*pow(16, size-1)
        if(hex_str[i]=='d'):
            sum=sum+13*pow(16, size-1)
        if(hex_str[i]=='e'):
            sum=sum+14*pow(16, size-1)
        if(hex_str[i]=='f'):
            sum=sum+15*pow(16, size-1)
        i=i+1
        size=size-1
            
    return sum
            
        
