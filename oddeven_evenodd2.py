import random

def get_rand_num():
    return random.randint(1,100)


def lists():
    a = []

    for i in range(10):
        status = True
        if len(a) != 0:
            if a[i-1] % 2 == 0:
                while status == True:
                    val = get_rand_num()
                    if val % 2 != 0:
                        a.append(val)
                        status = False
            else:
                while status == True:
                    val = get_rand_num()
                    if val % 2 == 0:
                        a.append(val)
                        status = False
        else:
            a.append(get_rand_num())
    return a


print(lists())
