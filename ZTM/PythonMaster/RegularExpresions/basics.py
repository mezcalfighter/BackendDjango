import re # Module for regular expresions

string = "search inside of this text please!"
print(re.search("this",string))

# Collecting emails example
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = "b@b.com"
a = pattern.search(string)
print(a)