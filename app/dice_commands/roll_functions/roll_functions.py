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

    all_dices = roll_n_dices(number_dices, type_dice)
    successes = success_checks(all_dices, dificulty)
    crit_fails = crit_failures(all_dices)
    crits = crit_success(all_dices, type_dice)

    results = {
        'all_dices': all_dices,
        'success': successes,
        'crit_success': crits,
        'crit_failures': crit_fails}

    return results


def crit_failures(arr):
    return list(filter(lambda x: x == 1, arr))


def crit_success(arr, type_dice):
    return list(filter(lambda x: x == type_dice, arr))


def success_checks(results, difficulty_check, abouveOnly=True):
    if abouveOnly:
        return list(filter(lambda x: x > difficulty_check, results))
    return list(filter(lambda x: x >= difficulty_check, results))


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
    if inp.find('d') != -1:
        fgroup = inp.split('d')
        try:
            return int(fgroup[1][0:2])
        except:
            return int(fgroup[1][0:1])
    return 0


def get_fix(inp):
    try:
        return int((inp.split('+'))[1].strip())
    except:
        return 0


def get_difficulty(inp):
    try:
        rest = inp.split('>')[1].strip()
        x = 0
        for c in rest:
            if c.isnumeric():
                x += 1
            else:
                break

        return int(rest[:x])
    except:
        return 0
