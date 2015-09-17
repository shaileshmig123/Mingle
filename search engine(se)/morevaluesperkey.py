l=[ [1, 'A'], [1, 'B','3'], [2, 'C'] ]
d={}
for key, val in l:
    d.setdefault(key, []).append(val)

print d
