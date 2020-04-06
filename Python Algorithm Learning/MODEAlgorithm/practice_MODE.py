
# MODE = Data -> Count -> Max

def main():

    import sys

    scores = [ 100, 70, 75, 100, 95, 80 ]
    index = [0] * ( 100 + 1 )
    max = - sys.maxsize - 1
    mode = 0

    for i in range (0, len(scores)):
        index[scores[i]] = index[scores[i]] + 1
    for i in range (0, len(index)):
        if index[i] > max :
            max = index[i]; mode = i;

    print(f"최빈값은 {mode} 이며, {max}번 있습니다.")

if __name__ == "__main__":
    main()