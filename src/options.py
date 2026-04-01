def get_gamers_info():
    gamer_ids = []
    paid_fee = []
    days_since_reset = []
    statuses = []

    with open('gamers.txt', 'r') as data_source:
        for line in data_source:
            gamer_id, fee, days, status = line.split(',')
            gamer_ids.append(gamer_id.strip())
            paid_fee.append(fee.strip().capitalize())
            days_since_reset.append(int(days))
            statuses.append(status.strip().capitalize())

    return gamer_ids, paid_fee, days_since_reset, statuses


def get_accounts_info():
    gamer_ids, paid_fee, days_since_reset, statuses = get_gamers_info()
    print(gamer_ids, paid_fee, days_since_reset, statuses)
