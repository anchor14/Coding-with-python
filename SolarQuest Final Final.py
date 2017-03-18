##Jaehurn Nam/jn1402
##Solarquest

fp = open('solarquest.csv')
header = fp.readline().strip().split(',')

import random

class Board():
    def __init__(self):

        self.board = []

        for row in fp:
            row = row.strip().split(',')
            lined = {}
            for j in range(len(header)):
                key = header[j]
                value = row[j]
                lined[key] = value
            lined['owner'] = None
            lined['occupants'] = []
        
            if lined['type'] == 'federaton station':
                self.fuelstation = True
            else:
                self.fuelstation = False

            self.board.append(lined)


        fp.close()
       


    def __str__(self):
        emptystr = ''
        for x in self.board:
            if x['fuel']:
                x['fuel'] = x['fuel'] + '*'
        
        for x in self.board:
            emptystr += x['position'] + ' ' + x['name'] + ' ' + x['fuel'] + ' ' + str(x['occupants']) + '\n'

        return emptystr

board = Board()
print(board)


class Player():
    def __init__(self, name, location):
        self.name = name
        self.location = int(location)
        self.money = 1500
        self.fuel = 12
        self.fuel_stations = 0
        self.owned = []
        self.active = True

    def move(self, board):
        if self.name in board.board[self.location]['occupants']:
            board.board[self.location]['occupants'].remove(self.name)
        die = random.randint(2,12)

        spaces = die
        print('The number of moves you got is: ', spaces)
        for giraffe in range(spaces-1):
            self.location += 1
            self.fuel -= 1
            self.location = int(self.location) % len(board.board)
            
            
            if len(board.board[self.location]['next']) > 2:
                
                zebra = board.board[self.location]['next'].split(';')
                
                
                loclist = []
                for x in zebra:
                    x = int(x)
                    loclist.append(x)

                orbitq = input('Do you want to leave the orbit? (Y/N): ')

                
                if orbitq == 'Y':
                    self.location = loclist[1]
       
      
                else:
                    self.location = loclist[0]
      

            if self.location == 0:
                self.money += 500

        
        board.board[self.location]['occupants'].append(self.name)
           
                       


    def pay_rent(self):
        # jsw7 global okay
        renttopay = board.board[self.location]['rent']
        
        if self.money < renttopay:
            board.board[self.location]['owner'].money += self.money
            self.active = False
        else:
            board.board[self.location]['owner'].money += renttopay
            self.money -= renttopay
            

    def buy_fuel(self):
        fcost = board.board[self.location]['fuel'].strip('*')
        print('The amount of fuel you have is: ', self.fuel)
        famt = int(self.fuel)

     
        
        if fcost:
            print('The price of fuel at this place is: ' + fcost)
            while famt:
                    ffu = int(input('How much fuel do you want to purchase?: '))
                    if 0 < ffu:
                        newfuel = int(ffu) * int(fcost)
                        self.money -= int(newfuel)
                        self.fuel += ffu
                        other = board.board[self.location]['owner']
                        other.money += int(newfuel)
                        break
                        
                    else:
                        print('Sorry, the fuel amount you selected is not valid.')


        else:
            if not fcost:
                print('You cannot buy fuel at this location.')

            if famt == 0:
                self.active = False


    def buy_property(self):
        prp = board.board[self.location]
        prpurchase = board.board[self.location]['purchase']


        if prpurchase:
            pfu = input('Would you like to buy the property? (Y/N): ')
            if not board.board[self.location]['owner']:
                if pfu == 'Y':
                    if self.money >= int(prpurchase):
                        self.money -= int(prpurchase)
                        board.board[self.location]['owner'] = self
                        self.owned.append(self.location)
                    else:
                        print('Sorry, you do not have enough money to buy the property.')
        else:
            print('You cannot buy this property.')


    def __str__(self):
        return 'name: ' + self.name + '\n' + 'location: ' + str(self.location) + '/' + board.board[self.location]['name'] + '\n' + 'money: ' + str(self.money) + '\n' + 'fuel: ' + str(self.fuel) + '\n' + 'fuel stations: ' + str(self.fuel_stations) + '\n' + 'owned: ' + str(self.owned)


print('Hi, Welcome to SolarQuest!!')
print()


pp = []
pn = []

name = True

while name:
    name = input('Enter your name(hit enter if there is no more players to add): ')
    pp.append(Player(name,board.board[0]['position']))


pp.pop()
print()


iswinner = True

numberofturn = 0
while iswinner:
    if len(pp) == 1:
        iswinner = False
        break
    
    count = 0
    for p in pp:
        count += p.active

    if count <= 1:
        break

    
    for p in pp:
        movecnt = 0

            
        while p.active:
            if p.money < 0 or p.fuel <0:
                p.active = False
                pp.remove(p)
            print()
            print('___________________________________','\n')
            print('This is ' + p.name + "'s turn!!")
            print()

            print('Where you are: ' + str(p.location) + '/' + board.board[p.location]['name'])
            if board.board[p.location]['purchase']:
                print('Price: ' + board.board[p.location]['purchase'])
            if board.board[p.location]['rent']:
                print('Rentfee: ' + board.board[p.location]['rent'])
            if board.board[p.location]['fuel']:
                print('Fuel price: ' + board.board[p.location]['fuel'])
            if board.board[p.location]['owner']:
                print('Owner: ' + str(board.board[p.location]['owner']))

            print()
            usr = int(input('Options'+'\n'+'0: Purchase Property'+'\n'+'1: Get Fuel'+'\n'+'2: Plant fuel station'+ '\n'+ '3: Move!'+'\n'+ '4: Board information'+ '\n'+ '5: Player Information'+ '\n'+ '6: End Turn' + '\n' + '\n' + 'Your choice: '))
            print()

            

            
            if usr == 0:
                p.buy_property()
            elif usr == 1:
                p.buy_fuel()
            elif usr ==2:            
                p.fuel_stations += 1
            elif usr == 3:
                movecnt += 1
                if movecnt > 1:
                    print('You cannot move anymore. Select another option.')
                    print()
                else:
                    p.move(board)

            elif usr == 4:
                print(board)
                                  
            elif usr == 5:
                print(p)
            elif usr == 6:
                break


        print('___________________________________','\n')
 
 

print(pp[0].name + ' is the winner!!')
