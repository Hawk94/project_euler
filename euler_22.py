with open('p022_names.txt', 'r') as f:
    reader = f.read()
    name_list = reader.split(",")

alphabet = {'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7, 'H': 8,'I': 9,'J': 10,'K': 11,'L': 12,'M': 13,'N': 14,'O': 15,'P': 16,'Q': 17,'R': 18,'S': 19,'T': 20,'U': 21,'V': 22,'W': 23,'X': 24,'Y': 25,'Z': 26}

def euler():
    namescores = []
    for i in range(len(names)):
namesum = []
for letter in names[i]:
    namesum.append(alphabet[letter])
        namescore = sum(namesum) * (i+1)
        namescores.append(namescore)
    return namescores
