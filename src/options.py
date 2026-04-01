from utils import get_account_type, get_fee_status_icon
from constants import table_headers


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


def get_accounts_info(ids, paids, days, statuses):
    print(
        f"{table_headers[0]:<10} {table_headers[1]:<15}{table_headers[2]:<20}{table_headers[3]}")
    print("-" * 56)

    for gamer_id, paid, day, status in zip(ids, paids, days, statuses):
        if day <= 90:
            print(
                f"{gamer_id:<15}{get_account_type(gamer_id):<15}{get_fee_status_icon(paid):<15}{status}")
        else:
            print(
                f"{gamer_id:<15}{get_account_type(gamer_id):<15}{get_fee_status_icon(paid):<15}{status} 🚨")


def delete_record(ids, paids, days, statuses):
    id_to_find = input("Enter the gamer id you want to delete: ").upper()
    if id_to_find not in ids:
        return print(f"{id_to_find} is not in the records.")
    index = ids.index(id_to_find)
    ids.pop(index)
    paids.pop(index)
    days.pop(index)
    statuses.pop(index)
    print(f"{id_to_find} is now deleted")


def add_new_record(ids, paids, days, statuses):
    id_to_add = input("Enter the gamer id you want to add: ").upper()
    if id_to_add in ids:
        return print(f"{id_to_add} is already in the records.")
    ids.append(id_to_add)
    paids.append('No')
    days.append(0)
    statuses.append('Active')
