import random


def critical_balance(success, crit_success, crit_failures):
    sucess_without_crit = len(success) - len(crit_success)
    crits_balance = len(crit_success) - len(crit_failures)
    if crits_balance > 0:
        final = crits_balance * 2
    else:
        final = crits_balance
    return sucess_without_crit + final


def build_results(number_dices, type_dice, dificulty):
    arr_of_dices = roll_n_dices(number_dices, type_dice)
    suc_arr = success_arr(arr_of_dices, dificulty)
    crit_failure_arr = crit_failures(arr_of_dices)
    crit_suc = crit_success(arr_of_dices, type_dice)
    results = {
        'all_dices': arr_of_dices,
        'success': suc_arr,
        'crit_success': crit_suc,
        'crit_failures': crit_failure_arr}
    return results


def crit_failures(arr):
    return list(filter(lambda x: x == 1, arr))


def crit_success(arr, type_dice):
    return list(filter(lambda x: x == type_dice, arr))


def success_arr(results, diff):
    return list(filter(lambda x: x >= diff, results))


def roll_n_dices(number_dices, type_dice):
    mylist = []
    for i in range(0, number_dices):
        x = random.randint(1, type_dice)
        mylist.append(x)
    return mylist


def interpret_inp(inp):
    num_dices = get_num_dices(inp)
    dif = get_difficulty(inp)
    type_dice = get_type_dices(inp)

    return {'num_dices': num_dices, 'type_dice': type_dice, 'dif': dif}


def interpre_plus_fix(inp):
    num_dices = get_num_dices(inp)
    type_dice = get_type_dices(inp)
    fix = get_fix(inp)
    return {'num_dices': num_dices, 'type_dice': type_dice, 'fix': fix}


def get_num_dices(inp):
    fgroup = inp.split('d')
    return int(fgroup[0].strip())


def get_type_dices(inp):
    fgroup = inp.split('d')
    try:
        return int(fgroup[1][0:2])
    except:
        return int(fgroup[1][0:1])


def get_fix(inp):
    try:
        return int((inp.split('+'))[1].strip())
    except:
        return 0


def get_difficulty(inp):
    try:
        print('dif')
        rest = inp.split('>')[1].strip()
        x = 0
        for c in rest:
            if c.isnumeric():
                print(c)
                x += 1
            else:
                break

        return int(rest[:x])
    except:
        return 0