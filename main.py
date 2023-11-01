def encoder(old):
    new = ""
    old = str(old)
    for item in old:

        item = int(item)
        if item <= 6:
            item += 3
            new += str(item)
        elif item > 6:
            if item == 7:
                new += '0'
            elif item ==8:
                new += '1'
            elif item ==9:
                new += '2'
    print('Your password has been encoded and stored!')
    print('')
    return new

def decoder(password):
    final = ""
    for i in password:
        i = int(i)
        if i >= 3:
            i = i - 3
            final = final + str(i)
        elif i < 3:
            if i == 2:
                final = final + '9'
            elif i == 1:
                final = final + '8'
            elif i == 0:
                final = final + '7'
    return final




def main():
    ps = 0
    while True:
         print('Menu')
         print('-------------')
         print('1. Encode')
         print('2. Decode')
         print('3. Quit')
         choice = int(input('Please enter an option: '))


         if choice ==1:
             password = (input('Please enter your password to encode: '))
             if len(password) == 8:
                 password = encoder(int(password))
                 ps = ps + 1
             else:
                 print('Sorry, password must be an 8-digit integer number.')
         if choice ==2:
             if ps >= 1:
                 decoded = decoder(password)
                 print("The encoded password is " + password + ", and the original password is " + decoded + ".")

             else:
                 print('Sorry, no password stored')
         elif choice == 3:
             quit()










if __name__ == '__main__':
    main()