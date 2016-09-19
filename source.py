import pickle

tour = {
    "Firma1": "Italy Portugal Turkey",
    "Firma2": "Spain Egypt France",
    "Firma3": "Italy Russia",
    "Firma4": "Spain Canada",
    }
country = {
    "Italy": "Firma1 Firma3",
    "Portugal": "Firma1",
    "Spain": "Firma4",
}

search = raw_input('Choose your tour operator:')
if search in tour:
    print('They have tours to: ' + tour[search])

search2 = raw_input('Choose your country:')
if search2 in country:
    print('You can buy the tickets in these tour operators:' + country[search2])

search3 = raw_input('Select the tour operator: ')
if search3 in tour:
    print('Call to order: +18009768945 ')
