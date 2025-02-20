def calculaions():
    
    if total < 100 :
        savings = salary*(savings/100)
        rent = salary*(rent/100)
        electricity = salary*(electricity/100)
        total = savings + rent + electricity
        print(f"The amount allocated to savings is: {savings}")
        print(f"The amount allocated to rent is: {rent}")
        print(f"The amount allocated to electricity is: {electricity}")
        print(f"The total amount spend on savings, rent, and electricity is: {total}")
        print(f"The remainder of nabiha's salary is: {salary-total}")
        print(f"Estimated yearly rent and electicity: {(rent*12)+(electricity*12)}")
        print(f"Nabiha's salary squared:{salary**2}")
        save = int(input("The additional saving:"))
        print(f"Additional saving divided by total savings {save/savings}")

month = None ; salary = 0 ; savings = 0 ; rent = 0 ; electricity = 0 ; d = {}
while month != "exit":
    month = str(input("Please enter the name of the month (type exit to quit):"))
    if month != "exit" : 
        salary = int(input("Please enter your salary for this month:"))
        while True:
            savings = int(input("Please enter savings percentage:"))
            rent = int(input("Please input Rent percentage:"))
            electricity = int(input("Please input electricity percentage:"))
            total = savings + rent + electricity
            if total > 100:
                print("The combined percentage exceeds 100%. Please enter the values again.")
                continue
            else:
                break
        varibles = [salary,savings,rent,electricity] ; d[month] = varibles
print(d)
