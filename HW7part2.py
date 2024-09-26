# start

good_jumps: float = 0
highest: float = 0
winner: str = None
all_result = 0.0
for i in range(7):
    jump: float = float(input('enter the result: '))
    if jump >= 5.80:
        good_jumps += 1
        all_result += jump
    if jump > highest:
        highest = jump
    if jump > 6.23:
        winner: str = str(input('the name is : '))
    else:
        continue
print(f'the number of good jumps is {good_jumps}')
print(f'the highest jump is {highest}')
print(f'the new world record is {highest} and the name of the winner is {winner}')
avg: float = all_result / good_jumps
print(f'the average of the good jumps is {avg}')
