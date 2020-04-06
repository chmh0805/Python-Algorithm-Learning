
def main():
    first = [ 3, 5, 1, 2, 9 ]
    second = [ 8, 4, 7, 0 ]
    M = len (first); N = len (second);
    merge = [0] * ( M + N )
    i = 0; j = 0; k = 0; l = 0; m = 0;
# Sort
    for i in range (0, M - 1):
        for j in range (i + 1, M):
            if first[i] > first[j]:
                temp_1 = first[i]; first[i] = first[j]; first[j] = temp_1;

    for k in range (0, N - 1):
        for l in range (k + 1, N):
            if second[k] > second[l]:
                temp_2 = second[k]; second[k] = second[l]; second[l] = temp_2;
# Intialize
    i = 0; k = 0; m = 0;
# Merge
    while i < M and k < N:
        if first[i] < second[k]:
            merge[m] = first[i]; i += 1; m += 1;
        else:
            merge[m] = second[k]; m += 1; k += 1;
    while i < M:
        merge[m] = first[i]; m += 1; i += 1;
    while k < N:
        merge[m] = second[k]; m += 1; k += 1;
#Print
    print (merge)

if __name__ == "__main__":
    main()