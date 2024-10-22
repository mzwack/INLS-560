MIN_EXP_HOCKEY = 2
MIN_SHOOTING_PRACTICE_YEARS = 1

hockey_exp = int(input('How long have you been playing hockey?: '))
shooting_years = int(input('How long have you been practicing shooting goals?: '))

if hockey_exp >= MIN_EXP_HOCKEY and shooting_years >= MIN_SHOOTING_PRACTICE_YEARS:
    print("Please submit your application to join the hockey team; let's talk!")
else:
    print(f'''
        We are looking for someone with at least:
        * {MIN_EXP_HOCKEY} years of hockey experience
        * {MIN_SHOOTING_PRACTICE_YEARS} year of shooting goals experience

        Checkout our website at https://hockeytryouts.com/teams
        for other opportunties on different teams!
        ''')
    