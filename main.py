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






def main():
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
                 encoder(int(password))
             else:
                 print('Sorry, password must be an 8-digit integer number.')
         elif choice == 3:
             quit()










if __name__ == '__main__':
    main()