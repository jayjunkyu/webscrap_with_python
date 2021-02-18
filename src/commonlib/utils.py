def is_more_than_month_old(date):
    date_list = date.split()

    if 'month' in date_list:
        return False
    if 'months' in date_list:
        return False

    return True
