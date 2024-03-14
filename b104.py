first = input().split()
count = int(first[0]) #回答者の数
questions = int(first[1]) #設問数

def craft_list_in_lists(want_lists_count):
    list = []
    for i in range(want_lists_count):
        list.append([])
    return list


list_in_lists = craft_list_in_lists(questions)

for i in range(count):
    answer = input().split()
    for j in range(questions):
        try:
            int_answer = int(answer[j])
            if 0 <= int_answer and int_answer <= 100:
                list_in_lists[j].append(int_answer)
            else:
                pass
        except ValueError:
            pass

for list in list_in_lists:
    if len(list) == 0:
        print(0)
    else:    
        print(int(sum(list)/len(list)))