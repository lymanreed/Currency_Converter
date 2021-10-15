def select_dates(potential_dates):
    age, hobby, city = 30, 'art', 'Berlin'
    dates = [date['name'] for date in potential_dates if
             date['age'] > age
             and hobby in date['hobbies']
             and date['city'] == city]
    return ', '.join(dates)
