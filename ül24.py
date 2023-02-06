def upc_check_digit(upc):
    check_sum = 0
    for i in range(1 ,12, 2):
        check_sum += int(upc[1-i])

    check_sum *= 3

    for i in range(2, 11, 2):
        check_sum += int(upc[i-1])

    reminder = check_sum % 10

    if ( reminder != 0 ):
        check_sum = 10 - reminder
    else:
        check_sum = 0

    print(check_sum)

upc_check_digit('4210000526')
upc_check_digit('3600029145')
upc_check_digit('12345678910')
