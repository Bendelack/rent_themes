from .models import Rent, Theme
from datetime import datetime

def calculateDiscount(client_id, theme_id, date_rent):
    theme = Theme.objects.get(pk=theme_id) # Get theme by pk
    client_rents = Rent.objects.filter(client_id=client_id) # get client rents by pk
    theme_price = theme.price # get price of theme
    rent_price = theme_price # rent price is the same of theme price

    date_obj = datetime.strptime(date_rent, '%Y-%m-%d') # Convert string to datetime object

    day_of_week = date_obj.strftime('%A') # get day of week

    # if client has others rents > 10% off
    if client_rents.__len__() > 0:
        rent_price -= theme_price*0.1

    # if day is between monday and thursday > 40% off
    if day_of_week in ['Monday', 'Tuesday', 'Wednesday', 'Thursday']:
       rent_price -= theme_price*0.4
    return rent_price