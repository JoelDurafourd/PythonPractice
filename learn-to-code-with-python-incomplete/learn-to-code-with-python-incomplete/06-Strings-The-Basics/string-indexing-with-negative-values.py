print("motorcycle"[2:6])
print("retrograde"[8:])
print("disco"[0:1]) 
print("santacon"[5:15])
print("hippocampus"[5:])
print("sanitarium"[-8:-5]) 
print("\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet[0:26:2])
print(alphabet[::-2])
print(alphabet[::-1])
print(len(alphabet))
print("mendacious"[:10:4])
print("hurricane"[::3]) 
def first_three_characters(word): 
    return word[0:3]
    
print(first_three_characters("dynasty"))
print("\n") 

def last_five_characters(word): 
    return word[-5:]

print(last_five_characters("dynasty"))
print("\n")  

def is_palindrome(word): 
    return word[::-1] == word

print(is_palindrome("racecar")) 
print(is_palindrome("yummy")) 