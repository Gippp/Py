student1=[1,'Sidorov',20]
student2=[1,'Panin',19]
student3=[2,'Petrov',20]
student4=[2,'Ivanov',21]
stud=[student1,student2,student3,student4]

age_avg_course={1:[0,0,'First course'],
                2:[0,0,'Second course'],
                3:[0,0,'Third course']}

for student in stud:
    course=student[0]
    if course not in age_avg_course:
        print("Ошибка: Студента {} не существует".format(student))
    else:
        age_avg_course[course][0]+=student[2]
        age_avg_course[course][1]+=1
for i in age_avg_course:
    avg=age_avg_course[i]
    print("{}:".format(avg[2]),end='')
    if avg[1]!=0:
        print(avg[0]/avg[1])
    else:
        print('-')
    
    
