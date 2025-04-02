def vowel_count(word):
    return word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")


print(vowel_count("estate"))
print(vowel_count("helicopter"))
print(vowel_count("ssh"))

print()

def find_my_letter(word, letter):
    return word.find(letter)

print(find_my_letter("dangerous", "a"))
print(find_my_letter("bazooka", "z"))
print(find_my_letter("lollipop", "z"))
