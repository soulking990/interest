
def interest(money,rate,duration):
    for x in range(int(duration)-1):
        money  = money + money * rate/100
        
    return money
        
        
def user(string):
    while True:
        try:
            ask = input(string)
            int(ask)
            return int(ask)
        except:
            print('please try again')
            
def replay():
    global play
    result = ['y','n']
    while True:
        ask = input('would you like to keep using?y or n:')
        if ask in result:
            if ask == 'y':
                play = True
                break
            else:
                play = False
                break
        else:
            print('wrong answer')
            
            
            
play = True
while play:
    money  = user('how much money do you have in the bank?($):')
    rate = user('what is your rate of interest?')
    duration = user('how long do you plan on keeping this money?:')
    i = interest(money,rate,duration)
    print(f'the total amount of money you will have from {duration} years with a {rate} percent rate is : \n starting point: {money} \n ending point: {i}')
    replay()

