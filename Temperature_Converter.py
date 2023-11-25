def con():
    conti=input("press y to continue: ").lower()
    if (conti=="y"):
        choice()






def tem_in_kelvin(k):
    celsius=k-273.15
    farenheit=9/5*(k-273.15)+32
    print("The given kelvin value is ",round(k,2)," K","\nThe kelvin to celsius value is ",round(celsius,2),"℃","\nThe kelvin to farenheit value is ",round(farenheit,2),"°F")
    con()

def tem_in_farenheit(f):
    celsius=(f-32)*5/9
    kelvin=5/9*(f-32)+273.15
    print("The given  farenheit value is ",round(f,2),"°F","\nThe farenheit to  celsius value is ",round(celsius,2),"℃","\nThe   farenheit to kelvin value is ",round(kelvin,2),"k")
    con()

def tem_in_celsius(c):
    farenheit=c*9/5+32
    kelvin=c+273.15
    print("The given  celsius value is ",round(c,2),"℃","\nThe celsius to farenheit  value is ",round(farenheit,2),"℃","\nThe celsius to kelvin value is ",round(kelvin,2),"k")
    con()

def choice():
    print("Select the choice to enter the input value ")
    print("For Kelvin press K,\nFor Celsius press C, \nFor Farenheit press F")

    choice =input ("Enter the choice :").upper()
    if choice =="K":
        value = float (input ("Enter the Kelvin value:"))
        tem_in_kelvin(value)
    elif choice =="F":
        value = float (input ("Enter the Farenheit value:"))
        tem_in_farenheit(value)
    elif choice =="C":
        value = float (input ("Enter the Celsius value:"))
        tem_in_celsius(value)

    else :
        print("please enter the valid input ")
    
if __name__ == "__main__":
    choice()