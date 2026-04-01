#solution for #https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
n=24
if n % 2 == 0:
    if n in range(2,6):
        print ("Not Weird")
    if n in range(5,21):
        print ("Weird")
    if n>20:
        print ("Not Weird")
else:
    print("Weird")