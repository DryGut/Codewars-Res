def get_drink_by_profession(param):
  menu = {
    'Jabroni': 'Patron Tequila',
    'School Counselor': 'Anything with Alcohol',
    'Programmer': 'Hipster Craft Beer',
    'Bike Gang Member': 'Moonshine',
    'Politian': 'Your tax dollars',
    'Rapper': 'Cristal'
  }
  for k, v in menu.items():
    if param.lower() == k.lower():
      print(v)

  print('Beer')

get_drink_by_profession('jabroni')