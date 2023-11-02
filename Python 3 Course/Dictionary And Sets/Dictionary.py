mydict = { 
    "name":"harsh",
    "age":20,
    "work":"React and Python developer",
    "remote":"Full-time and remote",
    "type":{
        "work_day":"Mon to Fri",
        "salary":120000,
        "Holiday":"Sat and Sun"
    }
}

updatelist = {
    "Gender":"Male",
    "Phone":"01010101"
}

print(mydict)
# print(mydict['name'])
# print(mydict['type'])
# print(mydict['type']['Holiday'])
# print(mydict.keys()); print(mydict.values())

# Dictionary Methods
mydict.update(updatelist)
print(mydict)

# Suppose we have a key that not present in our dictionary.
print(mydict.get("Religion")) # Print None
print(mydict["Religion"]) # Throw an error
