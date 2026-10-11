def hello():
    print("hello")
def ali():
    print("Ali")
def hamza():
    print("Hamza")
def hi():
    print("hi")
    
    
def filterMenu():
    
    while True:
        print("\nSelect Choice:")
        print("1:Print Hello")
        print("2:Print ali")
        print("3:Print hamza")
        print("4:Print hi")
        print("0:Exit")
        
        choice = int(input("Enter CHoice: "))
        
        if choice == 1:
            hello()
        elif choice == 2:
            ali()
        elif choice == 3:
            hamza()
        elif choice == 4:
            hi()
        elif choice == 0:
            break
        else:
            print("Invalid Choice")


        