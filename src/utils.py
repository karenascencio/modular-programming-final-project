def get_account_type(gamer_id):
    preffix = gamer_id[0:3]
    if preffix == 'CAS':
        return 'Casual'
    else:
        return 'Pro'


def get_fee_status_icon(is_fee_paid):
    if is_fee_paid == 'Yes':
        return '✅'
    else:
        return '❎'
