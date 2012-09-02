f = open("statairfields.csv")

lines = []
for line_enc in f:
    line = line_enc.decode('iso-8859-8').strip()
    #items = line.split(',')
    lines.append(line)

item = lines[0]
print ''.join(list(reversed(item)))


