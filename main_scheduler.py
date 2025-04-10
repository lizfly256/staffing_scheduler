class Staff:
    '''Create staff and their scheduling related info'''
    _registry = [] # Creates a list of the staff to allow iterating through them
    def __init__(self, name, pref, avail, hours_min, hours_max):
        self._registry.append(self)
        self.name = name
        self.pref = pref
        self.avail = avail
        self.hours_min = hours_min
        self.hours_max = hours_max


hazel = Staff('Hazel', ['wed', 'thurs'], ['mon', 'tues', 'wed', 'thurs'], 20, 30)
willa = Staff('Willa', ['sat', 'sun'], ['fri', 'sat', 'sun'], 10, 20)
homer = Staff('Homer', ['mon', 'wed', 'fri'], ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat'], 10, 30)
#ollie = Staff('Ollie', ['mon', 'tues', 'wed', 'thurs'], ['mon', 'tues', 'wed', 'thurs', 'fri'], 25, 35)
#juliet = Staff('Juliet', ['sat', 'sun'],['sat', 'mon', 'fri', 'sun'], 20, 30)
#ruby = Staff('Ruby', ['tues', 'thurs'], ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat'], 10, 30)
#maya = Staff('Maya', ['thurs', 'fri'], ['wed', 'thurs', 'fri', 'sat'], 10, 35)
#teddy = Staff('Teddy', ['wed', 'thurs'],['tues', 'wed', 'thurs'], 10, 30)
#bear = Staff('Bear', ['sat', 'sun'], ['sat', 'wed', 'sun'], 10, 20)
#bob = Staff('Bob', ['mon'], ['mon', 'tues'], 25, 35)
#kima = Staff('Kima', ['tues'], ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat'], 15, 25)
#billie = Staff('Billie', [],['mon'], 0, 10)


def who_prefers_low(new_shift, hours_scheduled):
    '''Retun a dict with prefers to work this day and how many hours they are already scheduled'''
    prefers_shift = dict()
    for s in Staff._registry :
        if new_shift in s.pref :
            if s.name.lower() in hours_scheduled:
                current_hours = hours_scheduled[s.name.lower()]
            else : current_hours = 0
            if current_hours > s.hours_min : continue
            prefers_shift[s.name] = prefers_shift.get(s.name, current_hours)
    return prefers_shift

def who_avail_low(new_shift, hours_scheduled): 
    '''Return a dict of who is available and the hours they already are scheduled'''
    available = dict()
    for s in Staff._registry :
        if new_shift in s.avail : 
            if s.name.lower() in hours_scheduled :
                current_hours = hours_scheduled[s.name.lower()]
            else : current_hours = 0
            if current_hours > s.hours_min : continue
            available[s.name] = available.get(s.name, current_hours)
    return available

def who_prefers_high(new_shift, hours_scheduled):
    '''Return a dict of who prefers this day, under max hours, w/ the hours they're scheduled'''
    pref = dict()
    for s in Staff._registry:
        if s.name.lower() in hours_scheduled :
            current_hours = hours_scheduled[s.name.lower()]
        else : current_hours = 0
        if current_hours + 8 > s.hours_max : continue #assume shift lenght is 8hr
        pref[s.name] = pref.get(s.name, current_hours)
    return pref

def who_avail_high(new_shift, hours_scheduled) :
    '''Return s dict of who is available, under max hours, w/ the hours they're scheduled'''
    available = dict()
    for s in Staff._registry :
        if s.name.lower() in hours_scheduled :
            current_hours = hours_scheduled[s.name.lower()]
        else: current_hours = 0
        if current_hours + 8 > s.hours_max : continue # Assume shift lenght is 8hr.
        available[s.name] = pref.get(s.name, current_hours)
    return available

schedule = dict()
new_shift = None
hours_scheduled = dict()
while new_shift != 'done':
    new_shift = input("\nDay: ")
    best_options = dict()
    if new_shift == 'done': break

    if len(best_options) == 0 : best_options = who_prefers_low(new_shift, hours_scheduled)
    if len(best_options) == 0 : best_options = who_avail_low(new_shift, hours_scheduled)
    if len(best_options) == 0 : best_options = who_prefers_high(new_shift, hours_scheduled)
    if len(best_options) == 0 : best_options = who_avail_high(new_shift, hours_scheduled)
    
    
    
    print('\nBest')
    if not best_options : print('no one available')
    else: print(best_options)
    assigned_staffer = input("Select staffer for " + str(new_shift)).lower()
    schedule[new_shift] = assigned_staffer  #dictionary[key] = value
    #dict[key] = dict.get(key, default_value) + value_addition 
    hours_scheduled[assigned_staffer] = hours_scheduled.get(assigned_staffer, 0) + 8 #assume shift lenght is 8hr
    

print(hours_scheduled)
print(schedule)




