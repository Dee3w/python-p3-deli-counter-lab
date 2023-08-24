katz_deli = []

def line(list):
    count = 1
    new_list = []
    if len(list) == 0:
        return print("The line is currently empty.")
    else:
        for i in list:
            new_list.append(str(count) + '. ' + str(i))
            count += 1
        return print("The line is currently: " +" ".join(new_list))
    
def take_a_number(list, name):
    list.append(name)
    num = len(list)
    return print(f'Welcome, {name}. You are number {num} in line.')

def now_serving(list):
    if len(list) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {list[0]}.")
        del list[0]
    return list