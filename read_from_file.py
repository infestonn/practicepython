with open('names.txt', 'r') as open_file:
    l = (open_file.read().split())
    result = {a: 0 for a in l}
with open('names.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        if line.rstrip() in l:
            result[line.rstrip()] += 1
        line = open_file.readline()
for i,k in result.iteritems():
    print("%s: %d" % (i, k))
