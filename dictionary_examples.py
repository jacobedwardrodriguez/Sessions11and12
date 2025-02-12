d = {} # empty dictionary
eng_to_spa = {"one":"uno", "two":"dos", "three":"tres"}
print(eng_to_spa)

eng_to_spa["i"] = "yo"
eng_to_spa["am"] = "soy"
eng_to_spa["spanish"] = "espanol"
print(eng_to_spa)

sentence = "i am spanish"
words = sentence.split()
for word in words:
    print(eng_to_spa[word])

eng_to_spa.update({"yes":"si", "no":"no"})
print(eng_to_spa)

del eng_to_spa["no"] # this i show you remove an key/value from dict
print(eng_to_spa)

# print(eng_to_spa.popitem()) # not very useful since it is hard to know which is the last
print(eng_to_spa.pop("two")) # much better to pop a value by specifying the key

if "tree" in eng_to_spa:
    print(eng_to_spa["tree"])
else:
    print("i dont know that word")

print(eng_to_spa.get("tree", "unknown word"))

for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")


