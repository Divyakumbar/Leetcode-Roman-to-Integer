roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def roman_to_num(roman,n):
    result=0
    for i in range(len(n)):
        print(roman[n[i]])
        if i+1<len(n) and roman[n[i]]<roman[n[i+1]]:
            result-=roman[n[i]]
        else:
            result+=roman[n[i]]
    return result
n=input("Enter a roman value: ")
print(roman_to_num(roman,n.upper()))


