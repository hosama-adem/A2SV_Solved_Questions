if __name__ == '__main__':
    students_point={}
    points=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_point[name]=score
        points.append(score)
    new=sorted(set(points))
    second_lp=new[1]
    for name in sorted(students_point):
        if students_point[name]==second_lp:
            print(name)
