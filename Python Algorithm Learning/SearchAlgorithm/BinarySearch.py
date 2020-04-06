
def main():
    

    search = input("1~10 중 찾을 값을 입력하세요 : ")
    search = int(search)
    data = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    N = len (data)
    flag = False
    index = -1
    low = 0; high = N - 1;

    while low <= high :
        mid = int ((low + high) / 2)
        if data[mid] == search :
            flag = True; index = mid; break;
        if data[mid] > search :
            high = mid - 1
        else :
            low = mid + 1
    
    result = index + 1

    if flag :
        print(f"{search}는 {data}에서 {result}번째에 있습니다.")
    else :
        print("찾지 못했습니다.")

if __name__ == "__main__":
    main()