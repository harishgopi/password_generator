import string
import random

#one time global initialisation of sample list of all alphabets, special characters and numbers
global alphabets, numbers, spl_characters

alpha = string.ascii_lowercase + string.ascii_uppercase 
alphabets = [ random.choice(alpha) for i in range(2100)]

numbers = [str(random.randrange(1, 9, 1)) for i in range(2100)]

spl = ["@","#","$","%","^","&","*","(",")","_","-","+","=","?","<",">","~","]","["]
spl_characters = [ random.choice(spl) for i in range(2100)]