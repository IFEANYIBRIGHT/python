def riders_pay_delivery():

    today_summary = """
        
    COLLECTION RATE   AMOUNT PER PERCEL    BASE PAY

    less than 50%                 160         5,000

    50 - 59%                      200         5,000

    60 - 69%                      250         5,000

    > = 70%                       500         5,000
     """


    print(today_summary)
    
    wage = 0
    successful_delivery = int(input("How many delivery did u make today ? :"))
    
    if(successful_delivery < 50):
        wages = successful_delivery * 160 + 5000
        print(wages,"wages was made today")

    elif(successful_delivery >= 60 and successful_delivery <= 69):
        wages = successful_delivery *200 + 5000
        print(wages,"wages was made today")

    elif(successful_delivery > 70 and successful_delivery >= 70):
        wages = successful_delivery * 250 + 5000
        print(wages,"wages was made today")

    elif(successful_delivery == 0):
        print("go and rest")
                     

riders_pay_delivery()
