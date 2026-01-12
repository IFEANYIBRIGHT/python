def phone_book():
    print("""
Phone book:
1. Search
2. Service Nos
3. Add name
4. Erase
5. Edit
6. Assign tone
7. Send b'card
8. Options
9. Speed dials
10. Voice tags
""")
    choice = int(input("Choose an option: "))
    if choice == 1:
        print("Search for your option...")
    elif choice == 2:
        print("Service Nos")
    elif choice == 3:
        print("Add name")
    elif choice == 4:
        print("Erase")
    elif choice == 5:
        print("Edit")
    elif choice == 6:
        print("Assign tone")
    elif choice == 7:
        print("Send b'card")
    elif choice == 8:
        print("Options")
    elif choice == 9:
        print("Speed dials")
    elif choice == 10:
        print("Voice tags")
    else:
        print("Invalid button")

def messages():
    print("""
Messages:
1. Write messages
2. Inbox
3. Outbox
4. Picture messages
5. Templates
6. Smileys
7. Message settings
8. Info service
9. Voice mailbox number
10. Service command editor
""")
    choice = int(input("Choose an option: "))
    if choice == 1:
        print("Write message")
    elif choice == 2:
        print("Inbox")
    elif choice == 3:
        print("Outbox")
    elif choice == 4:
        print("Picture messages")
    elif choice == 5:
        print("Templates")
    elif choice == 6:
        print("Smiley")
    elif choice == 7:
        print("Message settings")
    elif choice == 8:
        print("Info service")
    elif choice == 9:
        print("Voice mailbox number")
    elif choice == 10:
        print("Service command editor")
    else:
        print("Invalid button")

def call_register():
    print("""
Call register:
1. Missed calls
2. Received calls
3. Dialled numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid
""")
    choice = int(input("Choose an option: "))
    if choice == 1:
        print("Missed calls")
    elif choice == 2:
        print("Received calls")
    elif choice == 3:
        print("Dialled numbers")
    elif choice == 4:
        print("Erase recent call lists")
    elif choice == 5:
        print("Show call duration")
    elif choice == 6:
        print("Show call costs")
    elif choice == 7:
        print("Call cost settings")
    elif choice == 8:
        print("Prepaid")
    else:
        print("Invalid button")

def tones():
    print("""
Tones:
1. Ringing tone
2. Ringing volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
""")
    choice = int(input("Choose an option: "))
    if choice == 1:
        print("Ringing tone")
    elif choice == 2:
        print("Ringing volume")
    elif choice == 3:
        print("Incoming call alert")
    elif choice == 4:
        print("Composer")
    elif choice == 5:
        print("Message alert tone")
    elif choice == 6:
        print("Keypad tones")
    elif choice == 7:
        print("Warning and game tones")
    elif choice == 8:
        print("Vibrating alert")
    elif choice == 9:
        print("Screen saver")
    else:
        print("Invalid button")

def main_menu():
    while True:
        print("""
Nokia Menu:
1. Phone book
2. Messages
3. Chat
4. Call register
5. Tones
6. Settings
7. Call divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. SIM services
0. Exit
""")
        option = int(input("Enter option: "))
        if option == 1:
            phone_book()
        elif option == 2:
            messages()
        elif option == 3:
            print("Chat selected")
        elif option == 4:
            call_register()
        elif option == 5:
            tones()
        elif option == 6:
            print("Settings selected")
        elif option == 7:
            print("Call divert selected")
        elif option == 8:
            print("Games selected")
        elif option == 9:
            print("Calculator selected")
        elif option == 10:
            print("Reminders selected")
        elif option == 11:
            print("Clock selected")
        elif option == 12:
            print("Profiles selected")
        elif option == 13:
            print("SIM services selected")
        elif option == 0:
            print("Exiting...")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main_menu()

