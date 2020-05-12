
def roll_damage(dice_pars, roll_functions):
    
    number_dices, type_dice, dificulty = roll_functions.interpret_inp(
        dice_pars).values()
    all_dices, success, crit_success, crit_failures = roll_functions.build_results(
        number_dices, type_dice, dificulty).values()
    message = build_messages_of_atack(all_dices, success, crit_success, dificulty)
    return message

def roll_dices(dices, roll_functions):

    number_dices, type_dice, dificulty = roll_functions.interpret_inp(
        dices).values()
    all_dices, success, crit_success, crit_failures = roll_functions.build_results(
        number_dices, type_dice, dificulty).values()
    success_calc = roll_functions.critical_balance(
        success, crit_success, crit_failures)
    message = build_messages_str(all_dices, success, crit_success, crit_failures, success_calc, dificulty)
    return message


def build_messages_of_atack(all_dices, success, crit_success, dificulty):

    message_list = build_messages_init(all_dices, dificulty, success)
    message_list.append(f'  results of success is {len(success)}')
    message_list.append(f'+ results of successwith expecialization {len(success)+len(crit_success)} ')
    return "\n".join(message_list)


def build_messages_str(all_dices, success, crit_success, crit_failures, success_calc, dificulty):

    message_list = build_messages_init(all_dices, dificulty, success)
    message_list.append(f'- you had {len(crit_failures)} critical failures - {crit_failures}')
    message_list.append(f'+ you had {len(crit_success)} critical success {crit_success}')
    message_list.append(f'  results of success is {len(success) + len(crit_failures)}')
    message_list.append(f'+ results of successwith expecialization {success_calc}')
    return "\n".join(message_list)


def build_messages_init(all_dices, dificulty, success):
    message_list = []
    message_list.append(f'ok, rolling your dices!')
    message_list.append(f"dices roll results! {all_dices}")
    message_list.append(f'dificulty of {dificulty}, you had {len(success)} success + {success}')
    return message_list
