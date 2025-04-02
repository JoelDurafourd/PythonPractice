def long_word(word):
    return 7 >= len(word)
    
    
print(long_word('cantelope'))
print(long_word("Python"))
print(long_word("magnificent"))
print(long_word("Haruka"))
print(long_word("Pythagoras"))

print("Break this up") 

def first_longer_than_second(a, b): 
    return len(a) >= len(b)

print(first_longer_than_second("Python", "Ruby"))
print(first_longer_than_second("cat", "mouse"))
