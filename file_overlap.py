with open('primenumbers.txt', 'r') as open_file:
    prime = open_file.read()
with open('happynumbers.txt', 'r') as open_file:
    happy = open_file.read()
for i in set(prime.split()) & set(happy.split()):
    print(i)