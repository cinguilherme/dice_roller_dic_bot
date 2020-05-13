
def roll_damage(dice_pars, roll_functions):
    
    number_dices, type_dice, dificulty = roll_functions.interpret_inp(
        dice_pars).values()
    all_dices, success, crit_success, crit_failures = roll_functions.build_results(
        number_dices, type_dice, dificulty).values()
    
    message = build_messages_of_damage_as_string(all_dices, success, crit_success, dificulty)
    message_object = build_messages_of_damage(all_dices, success, crit_success, dificulty)
    
    return message_object

def roll_dices(dices, roll_functions):

    number_dices, type_dice, dificulty = roll_functions.interpret_inp(
        dices).values()
    
    all_dices, success, crit_success, crit_failures = roll_functions.build_results(
        number_dices, type_dice, dificulty).values()
    
    success_calc = roll_functions.critical_balance(
        success, crit_success, crit_failures)
    
    message = build_messages_of_atack_as_string(all_dices, success, crit_success, crit_failures, success_calc, dificulty)
    messages_object = build_messages_of_atack(all_dices, success, crit_success, crit_failures, success_calc, dificulty)

    return messages_object

def build_messages_of_damage(all_dices, success, crit_success, dificulty):

    messages = {
        'general': f'all dices {all_dices}',
        'success': f'results of success is {len(success)}',
        'crits': f'results of successwith expecialization {len(success)+len(crit_success)}',
        'dificulty': f'{dificulty}'
    }

    return messages

def build_messages_of_damage_as_string(all_dices, success, crit_success, dificulty):

    message_list = build_messages_init(all_dices, dificulty, success)
    message_list.append(f'  results of success is {len(success)}')
    message_list.append(f'+ results of successwith expecialization {len(success)+len(crit_success)} ')
    return "\n".join(message_list)

def build_messages_of_atack(all_dices, success, crit_success, crit_failures, success_calc, dificulty):
    
    messages = {
        'general': f'all dices {all_dices}',
        'success': f'results of success is {len(success)}',
        'crits': f'results of successwith expecialization {crit_success}',
        'fails': f'you had {len(crit_failures)} critical failures - {crit_failures}',
        'balance': f'results of successwith expecialization {success_calc}',
        'dificulty': f'{dificulty}'
    }

    return messages

def build_messages_of_atack_as_string(all_dices, success, crit_success, crit_failures, success_calc, dificulty):

    message_list = build_messages_init(all_dices, dificulty, success)
    message_list.append(f'- you had {len(crit_failures)} critical failures - {crit_failures}')
    message_list.append(f'+ you had {len(crit_success)} critical success {crit_success}')
    message_list.append(f'  results of success is {len(success) - len(crit_failures)}')
    message_list.append(f'+ results of successwith expecialization {success_calc}')
    return "\n".join(message_list)

def build_messages_init_object(all_dices):
    return {
        'general': f'all dices {all_dices}'
    }

def build_messages_init(all_dices, dificulty, success):
    message_list = []
    message_list.append(f'ok, rolling your dices!')
    message_list.append(f"all dices {all_dices}")
    return message_list
