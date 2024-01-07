from itertools import permutations

# suffix of 8041965, 0841965, 4081965, 0481965

wordlist = ["Tiramisu", "Starbucks", "Cocoa", "Mimosas", "Portofino", "Berlin", "Netherland", "Italy"]
suffix = "0481965" # random choice

combinations = [''.join(p) + suffix for p in permutations(wordlist, 3)]

combinations_array = list(combinations)
