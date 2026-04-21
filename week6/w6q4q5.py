days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month_no = int(input("Enter month number (1-12): "))
year_no = int(input("Enter year: "))

month_no -= 1

if month_no < 0 and month_no > 11:
    print("Invalid month")
else:
    if month_no == 1:
        if (year_no % 4 == 0 and year_no % 100 != 0) or (year_no % 400 == 0):
            print(days[month_no] + 1)
        else:
            print(days[month_no])
    else:
        print(days[month_no])
