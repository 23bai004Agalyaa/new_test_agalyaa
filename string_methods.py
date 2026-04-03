#

# s="  Ppython is a Programming lang   "
# st="jhdhd"
# asci = "AB"

# print(s.capitalize())
# print(s.title())
# print(s.upper())
# print(s.lower())
# print(s.swapcase())
# print(s.count("p"))
# print(s.endswith("Ang"))
# print(s.startswith("P"))
# print(s.find("z")) #returns given value's index if it is not found retrns -1
# print(s.index("p")) #error raisng
# print(st.isalpha())
# print(st.isascii())
# print(s.replace("a","s"))
# print(s.split()) # convert into list
# print(s.strip())

# print(s.isdigit())

# s="STring"
# upper_count=0
# lower_count=0
# for str in s:
#     if str.isupper():
#         upper_count+=1
#     else :
#         lower_count+=1
# print("uppercase:  ",upper_count)
# print("lowercase:  ",lower_count)

# s="5766789878764432"
# if s.isdigit():
#     print("only digit")
# else:
#     print("not only digits")

# s="This is a Sentence"
# count=0
# for str in s:
#     count+=1
# print("letters:",count)
# words=s.split()
# count_words=len(words)
# print("words",count_words)

# s="STring"
# print(s.swapcase())

# s="@ strin_g"
# n=""
# for str in s:
#     if str ==" " or str =="@" or str =="#" or str =="%" or str =="*" or str =="&" or str =="_" or str =="!":
#         continue
#     else:
#         n=n+str
# print(n)

# s="A String"
# print(s.replace(" ","-"))

s="this is a digit @ 1234"
alphabets=0
digit=0
spe_char=0
for str in s:
    if str.isalpha():
        alphabets+=1
    elif str.isdigit():
        digit+=1
    elif str.isspace():
        continue
    else:
        spe_char+=1
print("alp:",alphabets)
print("digit:",digit)
print("special_characters:",spe_char)

s="character"
for str in s:
    if s.count(str)>1:
        print("more than 1",str)

s="53STring@"
if s.isdigit():
    print("only digit")
else:
    print("not only digits")
for str in s:
    if str.isalpha():
        alphabets+=1
    elif str.isdigit():
        digit+=1
    elif str.isspace():
        continue
    else:
        spe_char+=1
print("alp:",alphabets)
print("digit:",digit)
print("special_characters:",spe_char)



