cj = input().split()
children_count = int(cj[0])
janken_count = int(cj[1])

train_list = []
train_list = [[] for _ in range(children_count)]

for i in range(children_count):
    train_list[i].append(i + 1)

for i in range(janken_count):
    xy = input().split()
    winner = int(xy[0])
    loser = int(xy[1])
    train_list[winner - 1].extend(train_list[loser - 1])
    train_list[loser - 1] = []

max_length = max(len(lst) for lst in train_list)
max_length_indexes = [i + 1 for i, lst in enumerate(train_list) if len(lst) == max_length]

for index in max_length_indexes:
    print(index)
