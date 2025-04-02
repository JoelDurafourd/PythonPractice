mad_libs = "{noun} punched {second_noun} in the {body_part}"

print("Let's play MadLibs")
noun = (input("Enter a noun "))
second_noun = (input("Enter a second noun "))
body_part = (input("Enter a body part "))


print(mad_libs.format(noun = noun, second_noun = second_noun, body_part = body_part))
print("Thanks for playing!")