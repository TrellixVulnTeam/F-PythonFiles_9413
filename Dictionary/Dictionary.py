thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# ORIGINAL
print(thisdict)

# ADD
thisdict["addedItem"] = "best car ever"
print(thisdict)

# REMOVE
thisdict.pop("year")
# del thisdict["model"] #OTHER OPTION
print(thisdict)

# GET ELEMENT
x = thisdict["model"]
thisdict["model"] = "GT"

# CHECK IF KEY EXISTS
print("Does \"model\" exist in the dictionary? " + str("model" in thisdict))
print("Does \"year\" exist in the dictionary? " + str("year" in thisdict))

# COPY DICTIONARY
copiedDictionary = thisdict

# CLEAR DICTIONARY
thisdict.clear()
if len(thisdict) == 0: print("Empty dictionary")
print(thisdict)

for i in copiedDictionary:
    print(copiedDictionary[i])
