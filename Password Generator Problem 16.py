# generates a password with length "password_Limiter" with no duplicate characters in the password from the defined list of "everything"
def PasswordGen(): 
    import random

    everything = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password_limiter = 13
    foolproofpassword =  "".join(random.sample(everything,password_limiter ))
    print (foolproofpassword)
PasswordGen()