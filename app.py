def paralell (list):
    y = 0
    for x in list:
        y = y + 1/x
   
    y = 1/y
    print(y ,"ohms")
    return y




def potential_divider(volt , list):
    y = 0
    for x in list:
        y = y + x
    
    i = volt / y

    for x in list:
        z = x * i
        print(z,"v") 


def temperature_check(temp,unit):
    if unit == "F" or unit == "f":
        unit = "C"
        temp = (temp - 32)*5/9
    
    if unit == "C" or unit == "c":
        if temp <= 30:
            print("The patient is hypothermic")
        elif temp >= 40:
            print("the patient is hyperthermis")
        elif temp > 30 and temp < 40:
            print("The patient is normal")
        else:
            print("Enter a usable number")
    else:
        print("Enter usable unit ")









paralell([332,1000,2200])

potential_divider(9,[3000,1000])

temperature_check(15,"f")