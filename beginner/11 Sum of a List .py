print("Sum-of-a-List Game\n")

while True:
    try:
        length = int(input("Enter the length of list\n>>"))
    except ValueError:
        print("ValueError!")
        length = 0

    listno = []

    while length > 0:
        try: 
            number = int(input("Enter number >>"))
            listno.append(number)
            length -= 1
        except ValueError:
            print("ValueError!")

    sumOfAList = sum(listno)
    print(f"The sum of the list is {sumOfAList}.\n")