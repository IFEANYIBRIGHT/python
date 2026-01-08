for day in range(1, 13):

    match day:
        case 1:
            print("on First day of christmas")
        case 2:
            print("on SecOnd day of christmas")
        case 3:
            print("On Third day of christmas")
        case 4:
            print("On Fourth day of christmas")
        case 5:
            print("On Fifth day of christmas")
        case 6:
            print("On Sixth day of christmas")
        case 7:
            print("On Seventh day of christmas")
        case 8:
            print("On Eighth day of christmas")
        case 9:
            print("On Ninth day of christmas")
        case 10:
            print("On Tenth day of christmas")
        case 11:
            print("On Eleventh day of christmas")
        case 12:
            print("On Twelfth day of christmas")

    
    print("Oo My true love sent to me : ")

    
    for gifts in range(day, 0, -1):
        match gifts:
            case 12:
                print("Twelve drummers' drumming")
            case 11:
                print("Eleven pipers piping")
            case 10:
                print("Ten lords a-leaping")
            case 9:
                print("Nine ladies dancing")
            case 8:
                print("Eight maids a-milking")
            case 7:
                print("Seven swans a-swimming")
            case 6:
                print("Six geese a-laying")
            case 5:
                print("Five golden rings")
            case 4:
                print("Four calling birds")
            case 3:
                print("Three French hens")
            case 2:
                print("Two turtle doves")
            case 1:
                print("A partridge in a pear tree")

    print()   

