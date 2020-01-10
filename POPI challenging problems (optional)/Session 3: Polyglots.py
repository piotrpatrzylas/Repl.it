"""
Each student at a certain school speaks a number of languages. We need to determine which languages are spoken by all the students, which languages are spoken by at least one student.

Given, the number of students, and then for each student given the number of languages they speak followed by the name of each language spoken, find and print the number of languages spoken by all the students, followed by a list the languages by name, then print the number of languages spoken by at least one student, followed by the list of the languages by name. Print the languages in alphabetical order.
 
For example, on input:
3
3
Russian
English
Japanese
2
Russian
English
1
English
output must be:
1
English
3
English
Japanese
Russian
"""
numberOfStudents = int(input())
mlist = []

for i in range (0, numberOfStudents):
  numlang = int(input())
  llist = [numlang]
  for i in range(0, numlang):
    l = input()
    llist += [l]
  mlist += [llist]
  
minl = min(mlist)
minlSort = minl[1:]
minlSort.sort()
maxl = max(mlist)
maxlSort = maxl[1:]
maxlSort.sort()

print(minl[0])
for i in minlSort:
  print(i)
print(maxl[0])
for i in maxlSort:
  print(i)
