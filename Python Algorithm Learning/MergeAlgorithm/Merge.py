
first = [ 1, 3, 5, 300, 500 ]
second = [ 2, 4, 200, 400 ]
merge = first + second

A = len (first)
B = len (second)
C = A + B

for i in range (C) :
    for j in range (C) :
        if merge[i] < merge[j] :
            temp = merge[i]; merge[i] = merge[j]; merge[j] = temp;

print (merge)