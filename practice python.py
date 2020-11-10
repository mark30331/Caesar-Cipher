"""
A rotation cipher is one of the simplest, plain-text ciphers, known 
since at least the time of Julius Caesar. It takes in a plain-text 
string, and translates it into a new string based on a rotation of the 
alphabet being used. The basis is a “rotation”, a re-sequencing of an alphabet. 

Plain Alphabet	ABCDEFGHIJKLMNOPQRSTUVWXYZ
Caesar Alphabet (+3)DEFGHIJKLMNOPQRSTUVWXYZABC

Crypt DCODEX with a rotation of 3.
To encrypt D, take the alphabet and look 3 letters after: G. So D is encrypted with G.
To encrypt X, loop the alphabet: after X : Y, after Y : Z, after Z : A. So X is coded A.
DCODEX is coded GFRGHA

Another way to crypt, more mathematical, note A=0, B=1, ..., Z=25, and add a constant 
(the shift), then the result modulo 26 (alphabet length) is the coded text.

"""
#This is string containing all alphabets from a-z
a_to_z="abcdefghijklmnopqrstuvwxyz"
options = input("Please enter e to encode, d to decode, q to quit: ")
while (options != "q"):
    """
    If the command is encode, then the program prompts for a string
    to encode and a rotation integer in the range of 1-25. 
    """
    if options == "e":
        string_from_user = input("Enter a string to be encoded: ")
        string_from_user = string_from_user.lower()
        rotation = int(input("Enter a rotation to be applied to the string: "))
       
        #This basis is a “rotation”, a re-sequencing of an alphabet.
        new_a_to_z = a_to_z[rotation:] + a_to_z[:rotation]
        #print(new_a_to_z)
        encoded_string =""
        for x in string_from_user:
            if x in a_to_z:
                new_index = a_to_z.index(x)
                encoded_string += new_a_to_z[new_index]
            else:
                encoded_string += x
        print(encoded_string)

    elif (options =="d"):        
        """
        If the command is decode, then the program should prompt
        for a string to decode and a plain-text word that appears in 
        the text (decoded string). The output should be the rotation 
        needed to decode the string and the decoded string (text
        """
        #prompts the user for a string to decode
        input_to_decode = input("Give the string to decode: ")
        input_to_decode = input_to_decode.lower()#return lower case version of the string
        rotation = int(input("What was the rotation: "))
        key_word = input("Give a word in the string: ")
        key_word = key_word.lower() # returns lower case of the key_word
        
        new_a_to_z = a_to_z[rotation:] + a_to_z[:rotation]
        #print(new_a_to_z)
        decoded_string =""
        for x in input_to_decode:
            if x in new_a_to_z:
                new_index = new_a_to_z.index(x)
                decoded_string += a_to_z[new_index]
            else:
                decoded_string += x

        if key_word not in decoded_string:
            print("couldnt find a decoding.")
        else:
            print(decoded_string)  

    
    else:
        print("invalid command: Try again")
    options = input("Please enter e to encode, d to decode, q to quit: ")

#If the command is quit, then the program ends and prints goodbye message
print("good bye")

