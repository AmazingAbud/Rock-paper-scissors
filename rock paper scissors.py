import random
x=['rock','paper','scissors','hammer']
us=0
cs1=0

while True:
    ui=str(input('Choose your weapon from rock,paper or scissors or hammer ,or q to quit.'))
    if ui=='q':
        break
    cs=random.choice(x)
    print('the user has chosen',ui)
    print('the computer has chosen',cs)
    if ui==cs:
         print('its a draw')
    elif(ui=="paper" and cs=='rock'):
        print('the paper covers the rock.The user wins!!!')
        us=us+1
        cs1=cs1-1
    elif(ui=="rock" and cs=='scissors'):
        print('the rock crushes the scissors. Nice round!You win!')
        us=us+1
        cs1=cs1-1
    elif(ui=='scissors'and cs=='paper'):
          print('The scissors cuts the paper. A classic game ending!')
          us=us+1
          cs1=cs1-1
    elif(ui=='hammer'and cs=='paper'):
        print('OH NO! Sorry but hammer will not tear a paper! Cpu wins!')
        us=us-1
        cs1=cs1+1
    elif(ui=='hammer'and cs=='scissors'):
        print('A hammer can crush a scissors, but a scissors cannot cut a hammer! User wins!')
        us=us+1
        cs1=cs1-1
    elif(ui=='hammer'and cs=='rock'):
        print('A hammer and a rock are both strong things, so there is no clear winner here!')
   
    else:
          print('The CPU wins!')
          cs1=cs1+1
          us=us-1
    print(cs1,'is the cpu score')
    print(us,'is the user score')
           

    



    
    

