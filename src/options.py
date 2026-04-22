from utils import get_account_type, get_fee_status_icon
from constants import HEADERS


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
        f"{HEADERS[0]:<10} {HEADERS[1]:<15}{HEADERS[2]:<20}{HEADERS[3]}")
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
    print(f"{id_to_add} has been added successfully")


def update_record(ids, statuses):
    id_to_find = input("Enter the gamer id you want to update: ").upper()
    if id_to_find not in ids:
        return print(f"{id_to_find} is not in the records.")
    index = ids.index(id_to_find)
    new_status = input(
        f"The current status for {id_to_find} is {statuses[index]}, please enter the new status: ").capitalize()
    statuses[index] = new_status
    print(f"{id_to_find} status is now {statuses[index]}")


def save_records(ids, paids, days, statuses):
    with open('gamers.txt', "w") as new_books_file:
        for gamer_id, paid, day, status in zip(ids, paids, days, statuses):
            new_books_file.write(f"{gamer_id}, {paid}, {day}, {status} \n")
    print("Data has been saved succesfully! :D")


def get_gamer_type_percentage(ids):
    pro_gamers = [id for id in ids if id[:3] == 'PRO']
    casual_gamers = [id for id in ids if id[:3] == 'CAS']

    percentage_pro = len(pro_gamers) * 100 / len(ids)
    percentage_casual = len(casual_gamers) * 100 / len(ids)

    print(
        f"The percentage of casual gamers is {percentage_casual}% and the pro gamers is {percentage_pro}%.")


def export_ids_by_status(ids, statuses):
    active = [ids[index]
              for index, status in enumerate(statuses) if status == 'Active']
    disabled = [ids[index]
                for index, status in enumerate(statuses) if status == 'Disabled']
    locked = [ids[index]
              for index, status in enumerate(statuses) if status == 'Locked']

    export_to_file('active.txt', active)
    export_to_file('disabled.txt', disabled)
    export_to_file('locked.txt', locked)


def export_to_file(file_name, data_array):
    with open(file_name, "w") as new_file:
        for data in data_array:
            new_file.write(f"{data} \n")
    print(f"{file_name} written succesfully! <3")
