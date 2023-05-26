# dictionaries are values defined using key : value pairs. you access values using a key instead of an index. this makes sense you have a lot of data.
person = {"name": "Letina", "age":24, "location": "Narok", "email" :"letinaroderick.com"}
print(person["location"])
# key cannot be repeated in a dictionary...for example when you define the word name .when you try to create anotther the previous value will be replaced.
# keys are case sensitive i.e. "Name" is different from "name"
# you can get a list of all keys by usng person.keys(). This can help you create a boolean to check if a key exists. when you enter a key that doesn't exist, you get a key error so instead create a boolean to check if a key exist by use of in conditional operators

b1 = "age" in person.keys()
print(b1)

b2 = "Location" in person.keys()
print(b2)

# a value in a dictionary can be of any datatype, but a key must only be a string

#  create  a dictionary replica IEBC voters with their personal info
# voterlist = {"name1" : "Alex", "idno1" : "3747474", "age1" : "20", "name2": "John", "idno2" : "6454663", "age2": "22"}
# print(voterlist["idno2"])

voterlist = {
    "1": {
        "age": 30,
        "name": "Brian",
        "city": "Kisumu",
        "id" : 98273763
    },
    "2": {
        "age": 28,
        "name": "Scovia",
        "city": "Narok",
        "id" : 7843892
    },
    "3": {
        "age": 35,
        "name": "Peter",
        "city": "nairobi",
        "id" : 123455
    }
}

print(voterlist["3"])
print(voterlist["1"]["city"])

