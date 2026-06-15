if __name__ == '__main__':
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append([name, score])
sorted_scores = sorted(scores, key=lambda x: x[1])
print(sorted_scores)


#вариант 1 - удаляем сначала минимальный элемент, затем удаляем максимальные до тех пор, пока min не станет равен max