
def roll_damage(dice_pars, roll_functions):
    
    number_dices, type_dice, dificulty = roll_functions.interpret_inp(
        dice_pars).values()
    all_dices, success, crit_success, crit_failures = roll_functions.build_results(
        number_dices, type_dice, dificulty).values()
    
    message_object = build_messages_of_damage(all_dices, success, crit_success, dificulty)
    
    return message_object

def build_messages_of_damage(all_dices, success, crit_success, dificulty):

    messages = {
        'general': f'all dices {all_dices}',
        'success': f'results {len(success)} of success is {success}',
        'crits': f'results {len(success)+len(crit_success)} of successwith expecialization',
        'dificulty': f'{dificulty}'
    }

    return messages


def roll_dices(dices, roll_functions):

    number_dices, type_dice, dificulty = roll_functions.interpret_inp(
        dices).values()
    
    all_dices, success, crit_success, crit_failures = roll_functions.build_results(
        number_dices, type_dice, dificulty).values()
    
    success_calc = roll_functions.critical_balance(success, crit_success, crit_failures)
    
    messages_object = build_messages_of_atack(all_dices, success, crit_success, crit_failures, success_calc, dificulty)

    return messages_object

def build_messages_of_atack(all_dices, success, crit_success, crit_failures, success_calc, dificulty):
    
    messages = {
        'general': f'all dices {all_dices}',
        'success': f'results {len(success) - len(crit_failures)} of success {success}',
        'crits': f'results {len(success)} of successwith expecialization {crit_success}',
        'fails': f'you had {len(crit_failures)} critical failures - {crit_failures}',
        'balance': f'results {success_calc} of success with expecialization',
        'dificulty': f'{dificulty}'
    }

    return messages
