
def roll_damage(dice_pars, roll_f, simple_output=False):

    number_dices, type_dice, dificulty = roll_f.interpret_inp(
        dice_pars).values()

    all_dices, success, crit_success, crit_failures = roll_f.build_results(
        number_dices, type_dice, dificulty).values()

    message_object = build_messages_of_damage(
        all_dices, success, crit_success, dificulty, True)

    return message_object


def build_messages_of_damage(all_dices, success, crit_success,
                             dificulty, simple_output=False):

    simple = len(success)
    crits = len(crit_success) + len(success)
    gen = f"all dices {all_dices} with difficulty of {dificulty}"

    if simple_output:
        messages = {
            'general': gen,
            'simple_output': (f"results {simple} with crits {crits} "),
        }
        return messages

    messages = {
        'general': f'all dices {all_dices}',
        'success': f'results {len(success)} of success is {success}',
        'crits': (f'results {crits} of with expecialization'),
        'dificulty': f'{dificulty}'
    }

    return messages


def roll_dices(dices, roll_functions, simple_output=False):

    number_dices, type_dice, dificulty = roll_functions.interpret_inp(
        dices).values()

    all_dices, success, crits, fails = roll_functions.build_results(
        number_dices, type_dice, dificulty).values()

    success_calc = roll_functions.critical_balance(
        success, crits, fails)

    messages_object = build_messages_of_atack(
        all_dices, success, crits, fails,
        success_calc, dificulty, simple_output)

    return messages_object


def build_messages_of_atack(all_dices, success, crits, fails,
                            success_calc, dificulty, simple_output=False):

    gen = f"all dices {all_dices} with difficulty of {dificulty}"
    bal = len(success) - len(fails)
    smp = f"results {bal}, with crits {success_calc} "
    if simple_output:
        messages = {
            'general': gen,
            'simple_output': smp,
        }
        return messages

    messages = {
        'general': f'all dices {all_dices}',
        'success': f'results {bal} of success {success}',
        'crits': f'results {len(success)} of with expecialization {crits}',
        'fails': f'you had {len(fails)} critical failures - {fails}',
        'balance': f'results {success_calc} of success with expecialization',
        'dificulty': f'{dificulty}'
    }

    return messages
