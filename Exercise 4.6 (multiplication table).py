dimension = int(input("Please input the dimension of the multiplication table:"))

max_digits = len(str(dimension**2)) #finder antallet af cifre i det største tal i gangetabellen, bruges senere til formattering

row = "*  ".rjust(max_digits + 1) #skriver "*" det rette sted
for i in range(1,dimension + 1): #producerer tallene i øverste række
    row += (str(i)).rjust(max_digits + 1)
print(row) #printer første række

print("-" * len(row)) #printer listen med "-----" i den rette længde ved at printe samme antal tegn som linjen over

for i in range(1,dimension + 1): #i er rækkenummer, j er cellenummer
    row = (str(i) + ": ").rjust(max_digits + 1) #genererer starten af rækken, dvs. "1:   " i første række
    for j in range(1,dimension + 1):
        row += ((str(i*j)).rjust(max_digits + 1))   #Genererer resten af række. Vi kører med +1 så vi får et mellemrum mellem ALLE tal.
    print(row) #printer rækken inden vi fortsætter til næste række