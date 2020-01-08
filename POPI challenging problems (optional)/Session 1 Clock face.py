"""
Hour hand turned by A degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour. Input and output in this problems are floating-point numbers. 

For example, on input
190
output must be
120
"""

hourHandDegrees = float(input())

hourHandDegreesMins = hourHandDegrees % 30
minutes = hourHandDegreesMins * 2
minuteHandDegrees = int(minutes * 6)
print(minuteHandDegrees)