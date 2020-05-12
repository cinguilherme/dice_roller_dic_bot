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
        'crit_failures': crit_failure_arr }
    return results

def crit_failures(arr):
    return list(filter(lambda x: x == 1, arr))

def crit_success(arr, type_dice):
    return list(filter(lambda x: x == type_dice, arr))

def success_arr(results, diff):
    return list(filter(lambda x: x >= diff,results))

def roll_n_dices(number_dices, type_dice):
    mylist = []
    for i in range(0,number_dices):
        x = random.randint(1,type_dice)
        mylist.append(x)
    return mylist

def interpret_inp(inp):
    fgroup = inp.split('d')
    num_dices = int(fgroup[0].strip())
    type_dif = fgroup[1].split('>')
    dif = int(type_dif[1].strip())
    type_dice = int(type_dif[0].strip())
    return {'num_dices' : num_dices, 'type_dice': type_dice, 'dif': dif}