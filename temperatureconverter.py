
def CtoF(tempC):
    tempF = tempC*1.8 + 32
    print('It is',round(tempF,1),'degrees Farenheit outside.')
    remark(tempC)

def FtoC(tempF):
    tempC = (tempF - 32)/1.8
    print('It is',round(tempC,1),'degrees Celsius outside.')
    remark(tempC)

def remark(tempC):
    if tempC >= 38:
        print('It\'s dangerously hot outside.')
    elif tempC >= 35:
        print('Don\'t go out unless you have to.')
    elif tempC >= 30:
        print('Drink lots of water!')
    elif tempC >= 27:
        print('It\'s rather warm today.')
    elif tempC >= 21:
        print('The weather is just right! Fancy a stroll?')
    elif tempC>= 17:
        print('Take a light sweater with you just in case.')
    elif tempC >= 12:
        print('It\'s chilly.')
    elif tempC >= 8:
        print('It\'s cold.')
    elif tempC >= -5:
        print('It\'s freezing!')
    elif tempC >= -12:
        print('Are we in the Artic Circle?')
    else:
        print('Brr...')

def start():
    mode = input("""select mode:
    1. Celsius to Farenheit
    2. Farenheit to Celsius 
    """)
    if mode == '1':
        tempC = float(input('enter temperature: '))
        CtoF(tempC)
    if mode == '2':
        tempF = float(input('enter temperature: '))
        FtoC(tempF)

while True:
    start()