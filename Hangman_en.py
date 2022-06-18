def draw_table(table):
    for i in range(7):
        for j in range(7):
            print(table[i][j], end= "")
        print()
table = [[" "] * 7 for i in range(7)]
count = 0
pos = ["|","|","o","/|/","//"," "]
for i in range(7):
    table[0][i] = "_"
    table[i][0] = "|"
a = input("Make word:").strip().lower()
word = ["_" for l in range(len(a))]
win_flag = True
while "_" in word:
    if count==6:
        win_flag = False
        break
    for sigment in word:
        print(sigment, end =" ")
    print()
    draw_table(table)
    letter = input("Enter the letter:").strip()
    flag = True
    for step in range(len(a)):
        if letter == a[step]:
            word[step] = letter
            flag = False
    if flag:
        count+=1
        table[count][4] = pos[count-1]
print("You win") if win_flag else print("You lose(")
print("Word was a:", a)
print("Your position")
draw_table(table)
