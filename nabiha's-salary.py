import pprint
def calculaions(salary,savings,rent,electricity):
        print(f"month:{choosen_month}")
        total = savings + rent + electricity
        print(f"The amount allocated to savings is: {savings}")
        print(f"The amount allocated to rent is: {rent}")
        print(f"The amount allocated to electricity is: {electricity}")
        print(f"The total amount spend on savings, rent, and electricity is: {total}")
        print(f"The remainder of nabiha's salary is: {salary-total}")
        print(f"Estimated yearly rent and electicity: {(rent*12)+(electricity*12)}")
        print(f"Nabiha's salary squared:{salary**2}")

        
month = None ; salary = 0 ; savings = 0 ; rent = 0 ; electricity = 0 ; d = {}
while month != "exit":
        month = str(input("Please enter the name of the month (type exit to quit):"))
        if month != "exit" : 
            if month in d:
                print(f"{month} is entered twice addional income will be added to savings")
                aditional_income = int(input("additonal income:"))
                d[month]['savings'] += aditional_income 
            else:
                while True:
                    salary = int(input("Please enter your salary for this month:"))
                    savings = int(input("Please enter savings percentage:"))
                    rent = int(input("Please input Rent percentage:"))
                    electricity = int(input("Please input electricity percentage:"))
                    total = savings + rent + electricity
                    if total > 100:
                        print("The combined percentage exceeds 100%. Please enter the values again.")
                        continue
                    else:
                        break
                savings = salary*(savings/100) ; rent = salary*(rent/100) ; electricity = salary*(electricity/100)
                d[month] = {"salary":salary,"savings":savings,"rent":rent,"electricity":electricity}
pprint.pprint(d,sort_dicts=False,compact=True)
choosen_month = str(input("Please choose a month:"))
print(d[choosen_month])
calculaions(d[choosen_month]["salary"],d[choosen_month]["savings"],d[choosen_month]["rent"],d[choosen_month]["electricity"])