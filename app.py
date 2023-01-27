def paralell (list):
    y = 0
    for x in list:
        y = y + 1/x
   
    y = 1/y
    print(y ,"ohms")
    return y




def potential_divider(volt , list):
    #return volt(list[1]/(list[0]+list[1]))
    y = 0
    for x in list:
        y = y + x
    
    i = volt / y

    for x in list:
        z = x * i
        print(z,"v") 



paralell([332,1000,2200])



potential_divider(9,[3000,1000])