from . import alphabets, numbers, spl_characters
import random

def generator(min_length,spl_char_length,numbers_length,number_of_passwords):
    password = list()

    #calculating the number of alphabets in the password with consideration as minimum length is same as actual length
    alpha_len = min_length - spl_char_length - numbers_length

    #generating password
    for i in range(0,number_of_passwords):
        #generating random alphabets , numbers and special characters in a list format
        temp = random.sample(alphabets,alpha_len) + random.sample(numbers,numbers_length) + random.sample(spl_characters,spl_char_length)

        #shuffling the list randomly and forming a password in string format and adding to array
        temp = random.sample(temp,min_length)
        password.append("".join(temp))

    return password