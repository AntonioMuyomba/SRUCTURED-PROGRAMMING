Menu=[]

while True:
    print("/n__Menu__")
    print("1.Add")
    print("2.View")
    print("3.exit")

    choice=(input("Enter Choice:"))
    match choice:
        case"1":
            print("Add selected")
        case"2":
            print("View selected")
        case"3":
            print("Goodbye!")
        case _:
                print("invalid choice")            
    

