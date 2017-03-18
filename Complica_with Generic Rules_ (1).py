##Name: Jaehurn Nam
##Net ID: jn1402
##Complica

import random


##Before any function, create the list of lists that would work to create the board

print('WELCOME TO COMPLICA(Game Owner: Jaehurn Nam)')
print()



row = int(input('Type in how many rows you want to create: '))
column = int(input('Type in how many columns you want to create: '))

ll = []
for r in range(row):
    l=[]
    for c in range(column):
        l.append(' ') 
    ll.append(l)


a = len(ll)

inarrow = 4



##Make a function that would print the board every time a user or computer chooses a place to put it in.
def print_board(row, column, ll):

    b = len(l)

    for i in ll:
        print('+-'*(b)+'+')
        row = '|'
        for j in i:
            row += j+'|'
        print(row)
    print('+-'*(b)+'+')

    print()

    
##A function that would ask the user for a place to input and replace it in the list of lists
def user(ll,a,row):
    user = int(input('Type in the column you want to put: '))

    new = ll[a-1]

    c=1

    if ll[0][user-1] == ' ':
        while True:
            if new[user-1] == ' ':
                new[user-1]='X'
                break
            else:
                new = ll[a-c]
            c+=1
    elif ll[0][user-1] != ' ':
        j = row-1
        while j>=1:
            j = int(j)
            ll[j][user-1]=ll[j-1][user-1]
            j -= 1
        ll[0][user-1]='X'
            

    print('')
    print('Renewing the board...')
    print('')
 
    
##A function that randomly generates a choice for the computer to choose a place to put and replace it in list of lists
def computer(ll,column,a):

    print('Computer is randomly making a choice.')
    comp = random.randint(1,column)
    new = ll[a-1]

    d=1

    if ll[0][comp-1] == ' ':
        while True:
            if new[comp-1] == ' ':
                new[comp-1]='O'
                break
            else:
                new = ll[a-d]
            d+=1
    elif ll[0][comp-1] != ' ':
        j = row-1
        while j>=1:
            j = int(j)
            ll[j][comp-1]=ll[j-1][comp-1]
            j -= 1
        ll[0][comp-1]='O'

    print('')
    print('Renewing the board...')
    print('')

##The function to check for winner
def winner(row,column):

    s=0
    d=0


    ##Vertical Check
    for y in range(row):
        x=0
        counter=0
        while x <= column-2:
            if ll[x][y] == ll[x+1][y] and ll[x][y] =='X':
                counter+=1
                if counter == inarrow-1:
                    s=1
            else:
                counter = 0
            x+=1

    for y in range(row):
        x=0
        counter=0
        while x <= column-2:
            if ll[x][y] == ll[x+1][y] and ll[x][y] =='O':
                counter+=1
                if counter == inarrow-1:
                    d=1
            else:
                counter = 0
            x+=1

    ##Horizontal Check
    for x in range(column):
        y=0
        counter=0
        while y <= row-2:
            if ll[x][y] == ll[x][y+1] and ll[x][y] == 'X':
                counter+=1
                if counter == inarrow-1:
                    s=1
            else:
                counter = 0
            y+=1
            
    for x in range(column):
        y=0
        counter=0
        while y <= row-2:
            if ll[x][y] == ll[x][y+1] and ll[x][y] == 'Y':
                counter+=1
                if counter == inarrow-1:
                    d=1
            else:
                counter = 0
            y+=1

                
    ##Choosing win,lose,or tie
    if s + d >=2:
        print('The game is a tie!')
        return True
    elif s + d == 1:
        if s ==1:
            print('You won the game!')
            return True
        elif d==1:
            print('The computer won the game!')
            return True

    return False


##Main function to run everything
def main():

    print_board(row, column, ll)

    ##Loop to run the game until there is a winner
    while True:
        user(ll,a,row)
    
        print_board(row, column, ll)

        if winner(row,column):
            break

        computer(ll,column,a)

        print_board(row, column, ll)

        if winner(row,column):
            break
    

    

main()
