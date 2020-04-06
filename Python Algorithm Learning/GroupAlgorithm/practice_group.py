
class Subject() :
    def __init__(self, name, students):
        self.name = name # 상품명
        self.students = students # 수량

def main():
    # [1] Input
    subjects = [ Subject("Math", 28), Subject("Korean", 30), Subject("English", 33), Subject("Math", 12), Subject("Korean", 10), Subject("English", 7) ]
    group = [] # 출력 데이터
    N = len (subjects)
    # [2] Process
    ## [1] Sort
    for i in range (0, N - 1) :
        for j in range (i + 1, N) :
            if (subjects[i].name > subjects[j].name) :
                temp = subjects[i]; subjects[i] = subjects[j]; subjects[j] = temp;
    ## [2] Group
    subtotal = 0 # 소계가 담길 그릇
    for i in range (N) :
        subtotal = subtotal + subjects[i].students
        if ((i + 1) == N or subjects[i].name != subjects[i + 1].name) :
            group.append( Subject(subjects[i].name, subtotal))
            subtotal = 0
    # [3] Output
    print ("[1] 정렬된 원본 데이터:")
    for r in subjects:
        print(f"{r.name.rjust(7)} - {r.students}")
    print ("[2] 이름으로 그룹화된 데이터:")
    for g in group:
        print(f"{g.name.rjust(7)} - {g.students}")

if __name__ == "__main__" :
    main()