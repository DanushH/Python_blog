alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_tuple = tuple(alphabet)
print(alphabet_tuple)
sentence = input("Enter a sentence:\n")
sentence = set(sentence.lower())
print(sentence)
pangram = True
for letter in alphabet_tuple:
    if letter not in sentence:
        pangram = False

if pangram:
    print("Your sentence is a pangram")
else:
    print("Your sentence is not a pangram")
