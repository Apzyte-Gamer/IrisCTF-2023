import bcrypt
from itertools import permutations

# suffix of 8041965, 0841965, 4081965, 0481965

bcrypt_hash = "$2b$04$DkQOnBXHNLw2cnsmSEdM0uyN3NHLUb9I5IIUF3akpLwoy7dlhgyEC"


wordlist = ["Tiramisu", "Starbucks", "Cocoa", "Mimosas", "Portofino", "Berlin", "Netherland", "Italy"]
suffix = "0481965" # random choice

combinations = [''.join(p) + suffix for p in permutations(wordlist, 3)]

combinations_array = list(combinations)

# Check each combination against the bcrypt hash
for combination in combinations_array:
    combination_bytes = combination.encode('utf-8')
    if bcrypt.checkpw(combination_bytes, bcrypt_hash.encode('utf-8')):
        print(f"The combination '{combination}' matches the provided bcrypt hash.")
