conta = 1 // 3 * 3 ** 0
conta2 = 1 ** 2 - 4 // 3
conta3 = 4 / 2 + 2 ** 1
conta4 = 4 - 3 // 2 + 1

print(conta, conta2, conta3, conta4)

print('='*20)

torque = 0
while torque != 0:
    torque //= 2
    print("*", end="")
else:
    print("*")

print('='*20)

planets = 1 + 2 * 3 // 4
if planets < 0:
    print("#")
elif planets > 2:
    print("##")
else:
    print("###")

print('='*20)

others = 1
for i in range(2, 4):
    for j in range(-1, 2):
        if i == j:
            others += 1
        else:
            break
print(others)

print('='*20)

power = 2
while power < 5:
    power += 1
    if power == 3:
        continue
    print("@", end="")
else:
    print("@")

print('='*20)

angle = -1
for i in range(-1, 1):
    if 2 * i < 4:
        angle += 1
else:
    angle +=2
print(angle)

print('='*20)

list_one = [1,2]
list_two = list_one[:]
list_two.append(3)
print(list_one[-1] + list_two[-1])

print('='*20)

answers = (False, True, True)
selection = answers[:]
points = 0
for answer in selection[1:]:
    if answer:
        points +=1
print(points)

print('='*20)

#def process(data):
#    data = 2
 #   return data


#measurements = [0 for i in range(3)]
#result = process(measurements)
#print(result[-2])
#code problematic

print('='*20)

def walk(top):
    if top == 0:
        return 0
    else:
        return top * walk(top-1)

print(walk(2))