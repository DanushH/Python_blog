# Example 1:
sentence = "Let's Learn Python "
word1 = sentence[6:11]
word2 = sentence[-7:]

repetition = (word2 * 3) # "Python Python Python "
print(repetition.rstrip()) # "Python Python Python"

concatenation = word1 + ' ' + word2 # "Learn Python "
print(concatenation.rstrip()) # "Learn Python"



# Example 2:
sentence = '''  the quick brown fox
    jumps over the lazy dog  '''

sentence = sentence.strip().capitalize()
print(sentence)
# "The quick brown fox
#     jumps over the lazy dog"

words = sentence.lower().split()
print(words)
# ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

pangram = " ".join(words)
print(pangram)
# "the quick brown fox jumps over the lazy dog"



# Example 3:
import re

def validate_mobile(mobile):
    pattern = r"^(\+\d{1,3}\s?)?(\d{9})$"
    match = re.search(pattern, mobile)

    return bool(match)


MOBILE = "+94 987654321"
is_valid = validate_mobile(MOBILE)

if is_valid:
    print(f"{MOBILE} is valid")
else:
    print(f"{MOBILE} is not valid")
# +94 987654321 is valid


