# this script demonstrates how to identify an object's type
myString = "this is a string."
myList = ["This","is","a","list"];
print  "I will print the value of my variables."

print myString
print myList
print "now I will print the types:"
print type(myString)
print type(myList)
print "now I will type true false statements based on types"
print type(myList) is list
if type(myString) is str:
	print "This is a string"
else:
	print "this is a list"
