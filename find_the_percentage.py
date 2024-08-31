if __name__ == '__main__':
    n = int(input())                    #input
    student_marks={}
    for _ in range(n):
        name, *line=input().split()
        scores=list(map(float, line))
        student_marks[name]=scores
    query_name=input()
    if query_name in student_marks:          #calculate
        scores=student_marks[query_name]
        average=sum(scores)/len(scores)
        print(f"{average:.2f}")
    else:
        print("Student can't be found")
