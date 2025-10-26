# 🎯 თემა: სიები (lists) და თამაშის დაფა
# 🧠 მიზანი: 20x20 დაფის შექმნა და მანიპულაცია.

print("ნავების ომი — გაკვეთილი №5")

# სიების ძირითადი იდეა:
numbers = [10, 20, 30]
print("პირველი ელემენტი:", numbers[0])
print("მესამე ელემენტი:", numbers[2])

# 20x20 დაფა (~ წყალი)
board = []
for row in range(20):
    board.append(["~"] * 20)

# ბეჭდვა
for row in board:
    print(" ".join(row))

# ერთი ნავის მოთავსება შემთხვევით
import random
ship_x = random.randint(0, 19)
ship_y = random.randint(0, 19)
board[ship_y][ship_x] = "🚢"

print("\nნავი მოთავსებულია დაფაზე (საიდუმლოდ). მაგალითი:")
for row in board:
    print(" ".join(row))

# board[y][x] — კონკრეტული უჯრა
