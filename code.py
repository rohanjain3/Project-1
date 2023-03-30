print(' 🌟  ⚜ UNIT CALCULATOR ⚜  🌟')
print('         ✡. cm  ➺  m')
print('         ✡. mm  ➺  cm')
print('         ✡. m  ➺  cm')
print('         ✡. cm  ➺  mm')
print('         ✡. m  ➺  mm')
print('         ✡. mm  ➺  m')
print('         ✡. km  ➺  m')
print('         ✡. m  ➺  km')
print('         ✡. mm  ➺  km')
print('         ✡. km  ➺  mm')
print('         ✡. cm  ➺  km')
print('         ✡. km  ➺  cm')
print('         ✡. ft  ➺  inch')
print('         ✡. inch  ➺  ft')
print('         ✡. inch  ➺  cm')
print('         ✡. inch  ➺  mm')
print('         ✡. km  ➺  miles')
print('         ✡. miles  ➺  km')
print('         ✡. kelvin  ➺  celsius')
print('         ✡. celsius  ➺  kelvin')
#first value
num1=input('|Enter the first value:')
unit1 = input(' ☸ which unit do you want it to convert from ➺')
unit2 = input(' ☸ which unit do you want it to convert to ➺') 
if (unit1 =='cm'and unit2 =='m'):
    ans1 = float(num1)/100
elif (unit1 =='mm' and unit2 =='cm'):
    ans1 = float(num1)/10
elif (unit1 =='m' and unit2 =='cm'):
    ans1 = float(num1)*100
elif (unit1 =='cm' and unit2 =='mm'):
    ans1 = float(num1)*10
elif ( unit1 =='m' and unit2 =='mm'):
    ans1 = float(num1)*1000
elif ( unit1 =='mm' and unit2 =='m'):
    ans1 = float(num1)/1000
elif ( unit1 =='km' and unit2 =='m'):
    ans1 = float(num1)*1000
elif ( unit1 =='m' and unit2 =='km'):
    ans1 = float(num1)/1000
elif ( unit1 =='mm' and unit2 =='km'):
    ans1 = float(num1)/1000000
elif (unit1=='km' and unit2=='mm'):
    ans1 = float(num1)*1000000
elif (unit1 =='cm' and unit2 =='km'):
    ans1 = float(num1)/100000
elif (unit1 =='km' and unit2 =='cm'):
    ans1 = float(num1)*100000
elif (unit1 =='ft' and unit2 =='inch'):
    ans1 = float(num1)*12
elif ( unit1 =='inch' and unit2 =='ft'):
    ans1 = float(num1)/12
elif (unit1 =='inch' and unit2 =='cm'):
    ans1 = float(num1)*2.54
elif ( unit1 =='inch' and unit2 =='mm'):
    ans1 = float(num1)*25.4
elif (unit1 =='km' and unit2 =='miles'):
    ans1 = float(num1)*0.6214
elif (unit1 =='miles' and unit2=='km'): 
    ans1 = float(num1)/0.6214
elif (unit1 =='kelvin' and unit2=='celsius'): 
    ans1 = float(num1)-273.15
elif (unit1 =='celsius' and unit2=='kelvin'): 
    ans1 = float(num1)+273.15
print(ans1,unit2)
#second value
num2 =input('|Enter the second value:')
unit3 = input(' ☸ which unit do you want it to convert from ➺')
unit4 = input(' ☸ which unit do you want it to convert to ➺') 
if (unit3 =='cm'and unit4 =='m'):
    ans2 = float(num2)/100
elif (unit3 =='mm' and unit4 =='cm'):
    ans2 = float(num2)/10
elif (unit3 =='m' and unit4 =='cm'):
    ans2 = float(num2)*100
elif (unit3 =='cm' and unit4 =='mm'):
    ans2 = float(num2)*10
elif ( unit3 =='m' and unit4 =='mm'):
    ans2 = float(num2)*1000
elif ( unit3 =='mm' and unit4 =='m'):
    ans2 = float(num2)/1000
elif ( unit3 =='km' and unit4 =='m'):
    ans2 = float(num2)*1000
elif ( unit3 =='m' and unit4 =='km'):
    ans2 = float(num2)/1000
elif ( unit3 =='mm' and unit4 =='km'):
    ans2 = float(num2)/1000000
elif (unit3=='km' and unit4=='mm'):
    ans2 = float(num2)*1000000
elif (unit3 =='cm' and unit4 =='km'):
    ans2 = float(num2)/100000
elif (unit3 =='km' and unit4 =='cm'):
    ans2 = float(num2)*100000
elif (unit3 =='ft' and unit4 =='inch'):
    ans2 = float(num2)*12
elif ( unit3 =='inch' and unit4 =='ft'):
    ans2 = float(num2)/12
elif (unit3 =='inch' and unit4 =='cm'):
    ans2 = float(num2)*2.54
elif ( unit3 =='inch' and unit4 =='mm'):
    ans = float(num2)*25.4
elif (unit3 =='km' and unit4 =='miles'):
    ans2 = float(num2)*0.6214
elif (unit3 =='miles' and unit4=='km'): 
    ans2 = float(num2)/0.6214
elif (unit3 =='kelvin' and unit4=='celsius'): 
    ans2 = float(num2)-273.15
elif (unit3 =='celsius' and unit4=='kelvin'): 
    ans2 = float(num2)+273.15
print(ans2,unit4)
#calculator
if unit2==unit4:    
    print("          Select operation.")
    print("          1.Add")
    print("          2.Subtract")
    print("          3.Multiply")
    print("          4.Divide")
    add=(ans1+ans2)
    subtract=(ans1-ans2)
    multiply=(ans1*ans2)
    divide=(ans1/ans2)
    while True:
        choice = input("Enter choice(1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            if choice == '1':
                print(ans1, "+", ans2, "=", add, unit4 ,'🎉')
            elif choice == '2':
                print(ans1, "-", ans2, "=", subtract, unit4 ,' 🎉')
            elif choice == '3':
                print(ans1, "*", ans2, "=", multiply, unit4 ,' 🎉')
            elif choice == '4':
                print(ans1, "/", ans2, "=", divide, unit4 ,' 🎉')
else:
    print("ERROR\n""For further calculations you have to take same unit for first and second value")
