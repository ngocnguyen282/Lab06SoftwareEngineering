# repo link:
# https://github.com/ngocnguyen282/Lab06SoftwareEngineering

# Ngoc Nguyen
# Alissa Adams

# shift each digit up by 3 numbers
def encode(password_to_encode):
    encoded_password = [str(int(i) + 3) for i in password_to_encode]
    res = ''.join(encoded_password)

    return res


# shift each digit down by 3 numbers
def decode(encoded_password):
    result = ''
    for element in encoded_password:
        element = str(int(element) - 3)
        result += element

    return result


def display_menu():
    print()
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def main():
    encoded_password = None

    while True:
        # display menu & prompt for user option
        display_menu()
        user_option = input('Please enter an option: ')
        if user_option == '3':
            break
        elif user_option == '1':
            original_password = input('Please enter your password to encode: ')
            encoded_password = encode(original_password)
            print('Your password has been encoded and stored!')
        elif user_option == '2':
            print(f'The encoded password is {encoded_password}, and the '
                  f'original password is {decode(encoded_password)}.')


if __name__ == '__main__':
    main()