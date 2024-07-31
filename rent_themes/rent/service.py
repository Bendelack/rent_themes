from .models import Rent, Theme

def calculateDiscount(client_id, theme_id, date):
    theme = Theme.objects.get(pk=theme_id) # Get theme by pk
    client_rents = Rent.objects.filter(client_id=client_id) # get client rents by pk
    theme_price = theme.price # theme price
    rent_price = theme_price # rent price is the same of theme price

    # if client has others rents > 10% off
    if client_rents.__len__() > 0:
        rent_price -= theme_price*0.1

    # if day is between monday and thursday> 40% off
    #if date(date).strftime('%A') == 'Monday' or date.strftime('%A') == 'Tuesday' or date.strftime('%A') == 'Wednesday' or date.strftime('%A') == 'Thursday':
    #    rent_price -= theme_price*0.4
    return rent_price