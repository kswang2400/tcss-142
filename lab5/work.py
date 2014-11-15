
x = 3
y = 18
finished = False
while x <= y and not finished:
    subtotal = 0
    for z in range(x):
        subtotal += x
    if y // x <= 2:
        finished = True
    else:
        x += 2

print(x, y, subtotal, finished)