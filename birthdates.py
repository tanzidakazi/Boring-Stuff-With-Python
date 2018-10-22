birthdates = {'Mahmuda': '25 Jan 1993',
              'Mazdia': '25 Jan 1993',
              'Sherin': '2 Oct 1994',
              'Shegufta': '19 Oct 1994',
              'Dad': '1 May 1960',
              'Mum': '23 Dec 1971',
              'Brother': '22 Sept 1988'}

while True:
    print('Enter a name: (blank to quit)')
    name =input()
    if name == '':
        break

    if name in birthdates:
        print(birthdates[name]+ ' is the birthdate' + name)
    else:
        print('No birthdate of ' + name)
        print('What is their birthdate')
        newdate = input()
        birthdates[name] = newdate
        print('Birthdate database updated.')
