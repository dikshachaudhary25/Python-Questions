#Create a dictionary to represent key-value pairs and perform operations like adding,
#updating, and accessing values.

mydict = {
    "name":"DIKSHA",
    "age":"21",
    "city":"PATNA"
}
mydict.update({"roll_no":"2105962"})
print("updated dict:",mydict)
mydict.update({"name":"ANANY"})
print("updated dict:",mydict)
print("accessing value :",mydict["city"])
