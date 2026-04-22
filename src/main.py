from options import get_accounts_info, get_gamers_info, delete_record, add_new_record, update_record, save_records, get_gamer_type_percentage, export_ids_by_status

from constants import MENU


if __name__ == "__main__":
    gamer_ids, paid_fee, days_since_reset, statuses = get_gamers_info()

    choice = int(input(MENU))
    while choice != 8:
        if choice == 1:
            get_accounts_info(gamer_ids, paid_fee, days_since_reset, statuses)
        elif choice == 2:
            delete_record(gamer_ids, paid_fee, days_since_reset, statuses)
        elif choice == 3:
            add_new_record(gamer_ids, paid_fee, days_since_reset, statuses)
        elif choice == 4:
            update_record(gamer_ids, statuses)
        elif choice == 5:
            get_gamer_type_percentage(gamer_ids)
        elif choice == 6:
            export_ids_by_status(gamer_ids, statuses)
        choice = int(input(MENU))
    save_records(gamer_ids, paid_fee, days_since_reset, statuses)
