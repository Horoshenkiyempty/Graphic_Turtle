select = []
answer = input("Do you want change colors?  y - yes, n - no    ")

if answer == 'y':
    count = input("How manu colors?")
    answer = int(count)

    for i in range(answer):
         count = i
         color = input("Write a color " + str(count + 1) + " =")
         select.append(color)

print(select)