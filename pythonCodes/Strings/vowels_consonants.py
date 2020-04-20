# A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.
# Find the count of number of vowels and consonants
def count_vowels_alphabets(str_var):
    vowels = 0
    consonants = 0

    vowel_obj = set('aeiouAEIOU')

    for i in str_var:
        if i in vowel_obj:
            vowels+=1
        else:
            consonants+=1

    print("Total number of vowels: "+str(vowels))
    print("Total number of consonants: "+str(consonants))

count_vowels_alphabets("Geeks for Geeks")
