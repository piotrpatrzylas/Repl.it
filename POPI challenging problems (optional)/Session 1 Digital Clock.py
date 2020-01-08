"""
Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?

The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).

For example, on input 
150
output must be
2 30
"""

clock = int(input())


hours = clock // 60

minutes = clock % 60

print(hours, " ", minutes)