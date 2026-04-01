from options import get_accounts_info, get_gamers_info, delete_record, add_new_record, update_record


if __name__ == "__main__":
    gamer_ids, paid_fee, days_since_reset, statuses = get_gamers_info()
    get_accounts_info(gamer_ids, paid_fee, days_since_reset, statuses)
    delete_record(gamer_ids, paid_fee, days_since_reset, statuses)
    add_new_record(gamer_ids, paid_fee, days_since_reset, statuses)
    print(gamer_ids, paid_fee, days_since_reset, statuses)
    get_accounts_info(gamer_ids, paid_fee, days_since_reset, statuses)
    update_record(gamer_ids, statuses)
    print(gamer_ids, paid_fee, days_since_reset, statuses)
