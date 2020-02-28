#ok so I haven't been commenting on the other programs this week,
#I'm gonna go back an finish it, but with this program I don't know what to do,
#I've checked the solution and changed a few things on my code, but I can't get this to run
#I'm gonna continue work on this next week, and hopefully have a working solution then
def Uno_Reverse(uno):
    sentence = raw_input("Say something: ")
    sentence = uno.split()
    return " ".join(reversed((sentence)))
    print(Uno_Reverse(sentence))