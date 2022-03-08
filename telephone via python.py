string = input("Enter a 10-character phone Number as xxx-xxx-xxxx: ").upper()
codes = {"ABC": 2, "DEF": 3, "GHI": 4, "JKL": 5,
         "MNO": 6, "PQRS": 7, "TUV": 8, "WXYZ": 9, }
newString = ''

for i in string:
    if i.isalpha():
        for key in codes:
            if i in key:
                newString += str(codes[key])

    else:
        newString += i

print(newString)


# string = input("Enter the phone number as XXX-XXX-XXXX: ").upper()
#  letterNumber = {"ABC": 2, "DEF": 3, "GHI": 4, "JKL": 5, "MNO": 6, "PQRS": 7, "TUV": 8, "WXYZ": 9}
# num = ''

# if i.isalpha():
#       for string in letterNumber:
#           for digit in string:
#              if digit == 'A' or digit == 'B' or digit == 'C':
#                  num = '2'
#              elif digit == 'D' == digit == 'E' or digit == 'F':
#                num = '3'
#              elif digit == 'G' or digit == 'H' or digit == 'I':
#                num = '4'
#              elif digit == 'J' or digit == 'K' or digit == 'L':
#              num = '5'
#             elif digit == 'M' or digit == 'N' or digit == 'O':
#               num = '6'
#              elif digit == 'P' or digit == 'Q' or digit == 'R' or digit == 'S':
#                 num = '7'
#              elif digit in 'T' or digit in 'U' or digit in 'V':
#              num = '8'
#            elif digit == 'W' or digit == 'X' or digit == 'Y' or digit == 'Z':
#              num = '9'
#        else:
##            num += digit

# print(num)
