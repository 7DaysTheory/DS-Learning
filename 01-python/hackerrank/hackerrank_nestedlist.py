"""Given the names and grades for each student in a class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
Input Format:
The first line contains an integer, N, the number of students.
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.
"""

if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])

#получаем список уникальных оценок
grade_list = []
for i in scores:
    if i[1] in grade_list:
        continue
    else:
        grade_list.append(i[1])
        
#сортируем список уникальных оценок
grade_list = sorted(grade_list)

#получаем второй элемент списка (вторую худшую)
second_best = grade_list[1]

#выбираем тех, у которых оценка == второй худшей
name_list = []
for k in scores:
    if k[1] == second_best:
        name_list.append(k[0])

#печатаем сортированный список
for j in sorted(name_list):
    print(j)