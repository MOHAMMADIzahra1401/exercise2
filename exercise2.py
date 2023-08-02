import math
op= input("Enter a alamat riazi(+,-,*,/,sin,cos,tan,cot,factorial,radical)")
if op=="+" or op=="-" or op=="*" or op=="/":
    num1=int(input("Enter number 1:"))
    num2=int(input("Enter number 2:"))
    if op=="+":
        print(num1+num2)
    if op=="-":
        print(num1-num2)
    if op=="*":
        print(num1*num2)

    if op=="/":
        if num2==0:
            print("it is taarif nashode")
        else:
            print(num1/num2)
elif op=="sin" or op=="cos" or op=="tan" or op=="cot":
    darage=int(input("Enter a darage:"))
    if op=="sin":
        print(math.sin(math.degrees(darage)))
    if op=="cos":
        print(math.cos(math.degrees(darage)))
    if op=="tan":
        print(math.tan(math.degrees(darage)))
    if op=="cot":
        kasr=math.tan(math.degrees(darage))
        print(1/kasr)
elif op=="factorial":
    adad=int(input("Enter a number:"))
    if adad==0:
        
        print("0!=1")
    else:
        print(math.factorial(adad))
elif op=="radical":
    adad2=int(input("Enter a number:"))
    print(math.sqrt(adad2))


else:
    print("pleas entekhab kon ieki as alamat haie gofteshode ra")

        