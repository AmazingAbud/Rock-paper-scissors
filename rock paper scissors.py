import random
x=['rock','paper','scissors','hammer']
us=0
cs1=0
print('Welcome to Rock,Paper and Scissors game!')
while True:
    ui=str(input('Choose your weapon from rock,paper or scissors or hammer ,or q to quit.'))
    if ui=='q':
        break
    cs=random.choice(x)
    print('the user has chosen',ui)
    print('the computer has chosen',cs)
    if ui==cs:
         print('its a draw')
    elif(ui=="paper" and cs=='rock') or (ui=="rock" and cs=='scissors')or(ui=='scissors'and cs=='paper'):
          print('the user wins')
    us=us+1 
    else:
          print('the CPU wins')
    cs1=cs1+1

    
print(cs1,'is the cpu score')
print(us,'is the user score')
    
    

