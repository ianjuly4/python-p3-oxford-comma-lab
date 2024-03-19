def oxford_comma(items):
    if len(items) == 1:
        one_person =  "".join(items)
        return one_person
   
    elif len(items) == 2:
        two_people = " and ".join(items)
        return two_people
    
    elif len(items) >= 3:
        three_people = ", ".join(items[:-1])
        return f'{three_people}, and {items[-1]}'