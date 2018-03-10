import csv
whats = []
whens = []
wheres = []
whos = []
with open('RomanTerms.csv', 'rb') as Terms:
  reader = csv.reader(Terms)
  checkinput = raw_input("\nWhat are you searching for:   ")
  print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n[What,When,Where,Who]")
  for row in reader:
      for field in row:
          if field == checkinput:
              print(row)
      whats.append(row[0])
      whens.append(row[1])
      wheres.append(row[2])
      whos.append(row[3])
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
