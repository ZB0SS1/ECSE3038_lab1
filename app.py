def paralell (list):
    y = 0
    for x in list:
        y = y + 1/x
   
    y = 1/y
    print(y ,"ohms")
    return y


paralell([332,1000,2200])
