def check_isvowel(lst, letter):
    for i in lst:
        if i == letter:
            return True
    return False


vowel_list = ["A", "E", "I", "O", "U"]

print(check_isvowel(vowel_list, "A"))
print(check_isvowel(vowel_list, "B"))
