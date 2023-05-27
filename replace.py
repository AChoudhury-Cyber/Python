a_sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog!."
#a_sentence is my variable
print(a_sentence.replace("!"," "))
print(a_sentence.upper())
words = a_sentence.split("!")
words.reverse()
reversed_sentence = " ".join(words)
print(reversed_sentence)