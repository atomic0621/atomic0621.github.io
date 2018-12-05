import time
def game():
    time.sleep(3)
    print('WELCOME TO THE GAME')
    time.sleep(1)
    print('Your name is Cornelius Hubertson')
    time.sleep(2)
    print('You see Mr.Mawhorter gave you a zero on an assignment that you did.')
    time.sleep(2)
    choice1=raw_input('Do you write an Email or do you ignore it?(email/ignore)')
    while choice1 != 'email' and choice1 !='ignore':
        choice1=raw_input('Are you dumb?')
    if choice1==('ignore'):
        print ('You go to bed but your mom wakes you up 30 mins later and beats you for having a low grade')       
    elif choice1==('email'):    
        choice2=raw_input('Do you write an angry or neutral e-mail?(angry/neutral)')
        while choice2 != 'neutral' and choice2 !='angry':
            choice2=raw_input('Are you dumb?')
        if choice2==('angry'):
            print('Mr.Mawhorter responds and calls you stoopid')
        elif choice2==('neutral'):
            print('Mr.Mawhorter responds to you and tells you to talk to him after class')   
    time.sleep(4)
    print('The next day...')
    time.sleep(3)
    print('you see Mr.Mawhorter in his car')
    choice3=raw_input('Do you slice his throat or slice his tires?(throat/tires)')
    while choice3 != 'throat' and choice3 !='tires':
        choice3=raw_input('Are you dumb?')
    if choice3==('throat'):
        print('He dies')
        time.sleep(1)
        print('THE END')
    elif choice3==('tires'):
        print('He sees you and says what the\'\' $@&*%$ is wrong with you?\'\'')
        time.sleep(1)
        print('He sends you to the office and you get expelled')
        time.sleep(1)
        print('THE END')