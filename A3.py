units= int(input("please enter a number of units you comsumed: "))
if(units<=50):
    amount= units*2.60
    surcharge= 25
elif(units<=100):
    amount= 130+((units-50)*3.25)
    supercharge= 35
elif (units<=200):
    amount= 130+162.50+526+((units-100)*8.45)
    supercharge=45
else:
    amount= 130+162.50+526+((units-200)*8.45)
    supercharge=75
    print("\nElectricity bill=%.2f "%total)