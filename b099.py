NM = input().split()
move_route = []
result = []
for i in range(int(NM[0])):
    move_route.append([])
for i in range(int(NM[0])):
    route = input().split()
    for j in range(len(route)):
        move_route[j].append(int(route[j]))
for index, route in enumerate(move_route):
    mu_san = True
    for value in route:
        if value >= int(NM[1]):
            mu_san = False
    if mu_san:
        result.append(str(index + 1))
if len(result) >= 1:
    print(' '.join(result))
else:
    print('wait')