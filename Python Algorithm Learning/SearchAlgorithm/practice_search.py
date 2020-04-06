
def main():


    data = list(range(1001))
    search = input("1부터 1,000중 찾을 값을 입력하세요 :")
    search = int(search)
    N = len(data)
    flag = False; index = -1;
    low = 0; high = N - 1;

    while low <= high :
        mid = int((low + high) / 2)
        if search == data[mid] :
            flag = True; index = mid; result = index + 1; break;
        if search > data[mid] :
            low = mid + 1
        else :
            high = mid - 1

    if flag :
        print(f"{search}는 {index}번째 숫자입니다.")
    else :
        print("찾을 수 없습니다.")

if __name__ == "__main__" :
    main()