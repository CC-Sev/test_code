names = ('Mark', 'Mark', 'Patrick',' Richard', 'Aya', 'Kay', 'Q',
         'Q', 'Aya', 'Paul', 'Paul', 'Mark', 'Kay', 'Ryan', 'Aya', 'Q', 'Richard',
         'Roz', 'Aya', 'Ellie', 'Q', 'Ray', 'Q'
         )

record_names = dict()

def count_names(list_names):
    for i in range(len(list_names)):
        name = list_names[i]
        if name not in record_names:
            record_names[name] = 1
        else:
            record_names[name] += 1
    return record_names
count_names(names)
#print(record_names)

record_names2 = dict()
def length_names(list_names):
    global record_names2
    record_names2 = {name: len(name) for name in list_names}
    return record_names2
length_names(names)
print(record_names2)