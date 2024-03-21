def match_case():
    value = int(input("Enter a value: "))
    match value:
        case 1 if value > 0:
            print("Value is a positive 1")
        case 2 if value % 2 == 0:
            print("Value is an even 2")
        case 3 if value < 10:
            print("Value is less than 10 and is 3")
        case _:
            print("Value does not match any specific case")

match_case()