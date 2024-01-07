A Harsh Reality of Passwords
=

Recently, Iris's company had a breach. Her password's hash has been exposed. This challenge is focused on understanding Iris as a person.

Hash: `$2b$04$DkQOnBXHNLw2cnsmSEdM0uyN3NHLUb9I5IIUF3akpLwoy7dlhgyEC`

The flag format is `irisctf{plaintextPassword}`

## Note: 

```
Hi everyone, here are hints for the last osint challenge with the password hash.

- Focus on Iris and what she finds important!
- There are three words (not letters, but words), and a certain amount of numbers following it
- There's no leet words, proper capitalization nothing like (ExAmPLE), no special characters as well like -,! etc.
 
If you find a specific date, do not include the month'a name into your word list. Just use the numbers!!
```

Hint - Please, don't spend time looking for database breaches.

By - Lychi

Solution
=

By looking at the hash, I figured it was a bcrypt hash and couldn't be decoded unless we actually knew the plaintext. This wasn't the case so I focused at the hint and figured I had to make a wordlist of what Iris found important.

I went to [Iris's instagram page](https://www.instagram.com/irisstein_station) and looked at each of her posts and asking myself `what does Iris find important`.

After several rounds of this, I got my wordlist:

```
"Tiramisu",
"Starbucks",
"Cocoa",
"Mimosas",
"Portofino",
"Berlin",
"Netherland",
"Italy"
```

Then I again looked at the question and found out that the plaintext password was in the format `Word1Word2Word3Numbers`.

By this, I guessed that the numbers could only be Elaina's (Iris's mother) DOB (since mom's are the most important :)). I got Elaina's DOB through her [Facebook page](https://www.facebook.com/profile.php?id=61555040318052), April 8, 1965. I then formatted `April 8, 1965` to 4 combinations. `0841965`, `8041965`, `0481965` and `4081965`. 2 American formatted and 2 Indian formatted.

I was now ready for the final part, the coding.

Using my wordlist and my suffixes, I made a simple python program to generate all possible cases in the `Word1Word2Word3Numbers` format.

```
from itertools import permutations

wordlist = ["Tiramisu", "Starbucks", "Cocoa", "Mimosas", "Portofino", "Berlin", "Netherland", "Italy"]

combinations = [''.join(p) for p in permutations(wordlist, 3)]

for combination in combinations:
    print(combination)
```