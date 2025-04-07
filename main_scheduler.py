from staff_info import staff_list

def start_week(staff_list):
    """Returns a dict with which to keep track of how many hours each staffer has been scheduled."""
    hours_total = dict()
    for staff in staff_list:
        staff_name = staff["name"]
        hours_total[staff_name] = 0
    print(hours_total)
    return hours_total

def get_options(new_shift, hours_total):
    """Returns best selection of staffers to fill shift"""
    best_options = dict()
    for staff in staff_list:
        if new_shift in staff['pref day'] and under_min_hour(staff) is True:
            print('ACCESSED') #add them to best_options
    
    # preffers day and hasn't met minimum
    # available and hasn't met minimum
    # prefers day and isn't over max
    # available and isn't over max
        # add shift to schedule with selected staffer, update staffs running total
    
hours_total = start_week(staff_list)
new_shift = input('Shift day: ')
get_options(new_shift, hours_total)






