# Caesar Cipher 1
# Description
# Demo
# https://appbrewery.github.io/python-day8-demo/
# TODO-1:
# Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.
# TODO-2:
# Inside the 'encrypt' function, shift each letter of the original_text forwards in the alphabet by the shift_amount and print the encrypted text.
# You can use the built-in Python index() function to find out the position of an item in a list. e.g.
# fruits = [Apple, "Pear", "Orange
# fruits.index(P)
# e.g. If we have following values:
# plain_text = "hello"
# shift_amount = 1
# The final encrypted output should be:
# Here is the encoded result: ifmmp
#  Where each of the fetters of 'hello' is shifted up by 1.
# Call the encrypt() function and pass in the user inputs. You should be able to test the code and encrypt a message.




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Inside the 'encrypt' function, shift each letter of the original_text forwards in
# the alphabet by the shift_amount and print the encrypted text.
def encrypt(original_text , shift_amount):
    cipher_text = ""

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
# Call the encrypt() function and pass in the user inputs. You should be able to test the code and encrypt a message.
        shifted_position %= len(alphabet)
        cipher_text = alphabet(shifted_position)
    print(f"here is the encoded result : {cipher_text}")
