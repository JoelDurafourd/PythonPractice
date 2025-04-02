def same_first_and_last_letter(word):
    return word[0] == word[-1]

print(same_first_and_last_letter("runner"))
print(same_first_and_last_letter("Runner")) 
print(same_first_and_last_letter("clock"))    
print(same_first_and_last_letter("q"))       

print("Breakup this line please \n")

def three_number_sum(string1):
    return int(string1[0]) + int(string1[1]) + int(string1[2])

print(three_number_sum("123"))
print(three_number_sum("567"))
print("\n")
print(three_number_sum("444"))
print(three_number_sum("000"))
