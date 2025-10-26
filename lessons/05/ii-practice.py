# 🧩 დავალება №5 — საკუთარი 20x20 დაფა

import random

# 20x20 დაფა
board = []
for row in range(20):
    board.append(["~"] * 20)

# სამი ნავი
for i in range(3):
    x = random.randint(0, 19)
    y = random.randint(0, 19)
    board[y][x] = "🚢"

print("📋 შენი 20x20 თამაშის დაფა:")
for row in board:
    print(" ".join(row))

# დავალება:
# 1) დაამატე 'shots' სია სროლების შესანახად.
# 2) სროლისას შეცვალე უჯრა:
#    🚢 → 💥 (Treffer), "~" → "o" (Miss)
# 3) ყოველი სროლის შემდეგ დაბეჭდე განახლებული დაფა.
# 4) გააგრძელე სანამ ყველა ნავი განადგურდება.
