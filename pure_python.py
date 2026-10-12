f = open("scores.csv", "r",
         encoding="utf-8")
lines = f.readlines()
f.close()

print(len(lines))
print(lines[0])
print(lines[1])
