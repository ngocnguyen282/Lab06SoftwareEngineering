# Ngoc Nguyen

def encode(password_to_encode):
    encoded_password = [str(int(i) + 3) for i in password_to_encode]
    res = ''.join(encoded_password)

    return res


def decode(password_to_decode):
    decoded_password = [str(int(i) - 3) for i in password_to_decode]
    res = ''.join(decoded_password)

    return res


def display_menu():
    print()
    print('Menu')
    print('--------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def main():
    original_password = None

    while True:
        # display menu & prompt for user option
        display_menu()
        user_option = input('Please enter an option: ')
        if user_option == '3':
            break
        elif user_option == '1':
            original_password = input('Please enter your password to encode: ')
            encode(original_password)
            print('Your password has been encoded and stored!')
        elif user_option == '2':
            print(f'The encoded password is {encode(original_password)}, '
                  f'and the original password is {decode(encode(original_password))}.')


if __name__ == '__main__':
    main()