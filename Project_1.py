'''
author = Radim Jedlicka
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

users = ("bob", "ann", "mike", "liz", "Radim")
passwords = ("123", "pass123", "password123", "pass123", "666")
separator = "-" * 50
stars = "*"

list = dict(zip(users, passwords))
# print(list)

user = input("Hello there, what is your user name? ")
if user not in users:
    print(f"I am sorry, access denied!", "Program terminated!!! :-(",
          separator, sep="\n")
    quit()
else:
    password = input("Enter your password, please: ")
    if password == list[user]:
        print(separator,
              f"Welcome, {user}, you may continue, enjoy :-)",
              f"We have {len(TEXTS)} texts to be ananyzed.",
              separator, sep="\n")
    else:
        print("!!! Wrong password !!!", separator, sep="\n")
        quit()

# print(len(TEXTS))

textnr = input(
               f"Choose number of the text from 1 to {len(TEXTS)}: ")
textlength = range(1, len(TEXTS) + 1)
# print(textlength)

# if textnr.isdigit() and int(textnr) >= 1 and int(textnr) <= len(TEXTS):   # jiny zapis
if textnr.isdigit() and int(textnr) in textlength:
    pass
else:
    print("!!! Sorry, input must be digit and in range !!!")
    quit()
print(separator)

# - počet slov,
split = TEXTS[int(textnr)-1].split()
# print(split)
print(f"There are {len(split)} words in the selected text.")

# - počet slov začínajících velkým písmenem,
title = []
for slovo in split:
    if slovo.istitle():
        title.append(slovo.strip(".:;,!?"))
# print(title)
print(f"There are {len(title)} titlecase words.")

# - počet slov psaných velkými písmeny,
upper = []
for slovo in split:
    if slovo.isupper() and slovo.isalpha():
        upper.append(slovo.strip(".:;,!?"))
# print(upper)
print(f"There are {len(upper)} uppercase words.")

# - počet slov psaných malými písmeny,
lower = []
for slovo in split:
    if slovo.islower():
        lower.append(slovo.strip(".:;,!?"))
# print(lower)
print(f"There are {len(lower)} lowercase words.")

# - počet čísel (ne cifer),
numeric = []
for slovo in split:
    if slovo.isnumeric():
        numeric.append(slovo.strip(".:;,!?"))
# print(numeric)
print(f"There are {len(numeric)} numeric strings.")

# - sumu všech čísel (ne cifer) v textu.
numbers = []
for num in numeric:
    numbers.append(int(num))
print(f"The sum of all the numbers {sum(numbers)}")
print(separator)

# 6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu.
occurence = []
for word in split:
    occurence.append(len(word.strip(".:;,?!")))
# print(occurence)

graph = {}
for pocet in occurence:
    if pocet not in graph:
        graph.setdefault(pocet, 1)
    else:
        graph[pocet] += 1
# print("Graph:", graph)

result = (sorted(zip(graph.keys(), graph.values())))
# print(result)

print("LEN|    OCCURENCES    |NR.", (separator), sep="\n")
for a,b in result:
    print(

        f"{a:>3}|{(stars * b):<18}|{b:<3}",
        sep="\n")

# just testing:
# for index, dvojice in enumerate(vysledky,1):
#     print(
#         ODDELOVAC,
#         f"|{index}.| {dvojice[0]:^10} |{dvojice[1]}x|",
#         ODDELOVAC, sep="\n")
























































