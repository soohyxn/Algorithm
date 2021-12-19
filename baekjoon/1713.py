n = int(input())
m = int(input())
students = list(map(int, input().split()))
photo = []
count = []

for student in students:
    if student in photo:
        j = photo.index(student)
        count[j] += 1
    else:
        if len(photo) >= n:
            for i in range(n):
                if count[i] == min(count):
                    photo.pop(i)
                    count.pop(i)
                    break
        photo.append(student)
        count.append(1)

photo.sort()
print(*photo)