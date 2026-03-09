import math
def pizza_wahala():
 
        menu = """
       Pizza type      Number of Slices   Price per Box

        Sapa Size              4           2,000
        Small Money            6           2,400
        Big Boys               8           3,000
        Odogwu                12           4,200  
        """
        print(menu)
        recieve_order = input("What type of pizza do u want to buy ? ").lower()
        number_of_people = int(input("How many number of people ? "))
        
        match(recieve_order) :
        
            case "sapa size":
                pizza_slice = 4
                pizza_price = 2000 
            
            case "small money":
                pizza_slice = 6
                pizza_price = 2400 
            
            case "big boys":
                pizza_slice = 8
                pizza_price = 3000 

            
            case "odogwu":
                pizza_slice = 12
                pizza_price = 4200 
            
          
            case _:
                print("Invalid input")
                 
        
 
        print()
        number_of_boxes = math.ceil(number_of_people / pizza_slice)

        price_of_pizza = pizza_price * number_of_boxes

        remaining_pizza = number_of_boxes * pizza_slice - number_of_people

        slices_altogether = number_of_people * pizza_slice

        print(recieve_order, "size contains ",pizza_slice,"slices per box,",number_of_boxes,"box should be sufficient for",number_of_people,"people as it would contain",slices_altogether,"in all Which cost $",price_of_pizza, end=" ")
        print()
        print("Number of slices left after serving is",remaining_pizza,"slices")

        
pizza_wahala()       
         
            
