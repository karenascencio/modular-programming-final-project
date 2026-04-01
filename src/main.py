from options import get_accounts_info, get_gamers_info, delete_record


if __name__ == "__main__":
    gamer_ids, paid_fee, days_since_reset, statuses = get_gamers_info()
    get_accounts_info(gamer_ids, paid_fee, days_since_reset, statuses)
    delete_record(gamer_ids, paid_fee, days_since_reset, statuses)
