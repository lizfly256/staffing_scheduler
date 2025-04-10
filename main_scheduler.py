class Staff:
    '''This creates staff and their scheduling related info'''
    _registry = [] # Creates a list of the staff to allow iterating through them
    def __init__(self, name, pref, avail, hoursMin, hoursMax):
        self._registry.append(self)
        self.name = name
        self.pref = pref
        self.avail = avail
        self.hours_min = hoursMin
        self.hour_max = hoursMax


hazel = Staff('Hazel', ['wed', 'thurs'], ['mon', 'tues', 'wed', 'thurs'], 20, 30)
willa = Staff('Willa', ['sat', 'sun'], ['fri', 'sat', 'sun'], 10, 20)
homer = Staff('Homer', ['mon', 'wed', 'fri'], ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat'], 20, 30)
ollie = Staff('Ollie', ['mon', 'tues', 'wed', 'thurs'], ['mon', 'tues', 'wed', 'thurs', 'fri'], 25, 35)
juliet = Staff('Juliet', ['sat', 'sun'],['sat', 'mon', 'fri', 'sun'], 20, 30)
ruby = Staff('Ruby', ['tues', 'thurs'], ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat'], 10, 30)
maya = Staff('Maya', ['thurs', 'fri'], ['wed', 'thurs', 'fri', 'sat'], 10, 35)
teddy = Staff('Teddy', ['wed', 'thurs'],['tues', 'wed', 'thurs'], 10, 30)
bear = Staff('Bear', ['sat', 'sun'], ['sat', 'wed', 'sun'], 10, 20)
bob = Staff('Bob', ['mon'], ['mon', 'tues'], 25, 35)
kima = Staff('Kima', ['tues'], ['sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat'], 15, 25)
billie = Staff('Billie', [],['mon'], 0, 10)


#who prefers a day and needs more hour
schedule = dict()
new_shift = None
hours_scheduled = dict()
while new_shift != 'done':
    new_shift = input("day: ")
    if new_shift == 'done': break
    prefers_shift = list()
    for s in Staff._registry:
        if new_shift in s.pref:
            prefers_shift.append(s.name)
        
    print(prefers_shift)
    assigned_staffer = input("Select staffer for " + str(new_shift)).lower()
    schedule[new_shift] = assigned_staffer  #dictionary[key] = value
    #dict[key] = dict.get(key, default_value) + value_addition 
    hours_scheduled[assigned_staffer] = hours_scheduled.get(assigned_staffer, 0) + 8
    

print(hours_scheduled)
print(schedule)




