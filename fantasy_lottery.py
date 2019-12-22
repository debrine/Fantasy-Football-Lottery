from random import randint
from time import sleep

LOTTERY_ODDS = [35,30,20,10,4,1]
NUM_PLAYERS = 12
NUM_LOTTERY = 6
YEAR =2020

'''
The generate lottery function accepts a list of the lottery participants in the order
of last place to highest place of the non playoff teams. It then uses random number 
generation along with odds from each position of the draft to select a draft position
for each of the lottery entrants. This function is meant to be viewed in terminal, so 
will use print statements to update the user with which position each entrant is receiving

Args:
list_of_entrants - [str] - list of lottery entrants with last place at index 0, etc...
num_lottery - int - the number of players in the lottery draft
'''
def generate_lottery(list_of_entrants, num_lottery):
    lottery_draw = []
    
    for i in range(NUM_LOTTERY):
        for j in range(LOTTERY_ODDS[i]):
            lottery_draw.append([list_of_entrants[i],LOTTERY_ODDS[i]])
    
    num_tickets = len(lottery_draw)

    print('shuffling tickets')
    #sleep(5)
    for i in range(NUM_LOTTERY):
        selected_index = randint(0, num_tickets-1)
        drawn_ticket = lottery_draw[selected_index]
        print("Congratulations "+ str(drawn_ticket[0]) + " on receiving the number " + str(i+1) + " pick in the " + str(YEAR) + " draft")

        new_list = []
        
        for j in range(len(lottery_draw)):
            if lottery_draw[j] != drawn_ticket:
                new_list.append(lottery_draw[j])
        
        num_tickets -= drawn_ticket[1]
        lottery_draw = new_list
        #sleep(5)


'''
the main function includes basic setup for the lottery by collecting the names of each place and then
handing them to the generate_lottery function
'''
def main():
    
    lottery_entrants = []
    
    for i in range(NUM_LOTTERY):
        lottery_entrants.append(str(input("Please enter the "+ str(NUM_PLAYERS-i)+"th place team: ")))

    generate_lottery(lottery_entrants, NUM_LOTTERY)

main()