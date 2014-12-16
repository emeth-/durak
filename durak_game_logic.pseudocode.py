turn_number = 0
turn_timer = 60
deck = []
players = []
player_cards = {}
shuffle_deck()
shuffle_players()
defender_id = -1
attacker_id = -1
bottom_trump_card = None
attack_cards_on_table = []
successfully_defended = False
attack_made = False
defense_started = False
defense_timer = 0

def check_if_loser():
    total_valid_player = 0
    for i in range(players.length):
        while player_cards[i].length > 0:
            total_valid_player += 1
    if total_valid_player == 0 or total_valid_player == 1:
        return True
    else:
        return False

def get_each_player_up_to_6_cards():
    for i in range(players.length):
        index = (attacker_id + i) % players.length
        while player_cards[index].length < 6 and deck.length > 0:
            player_cards[index].append(deal_card())


def move(turn_number):
    if turn_number == 1:
        determine_attacker_and_defender()
        bottom_trump_card = deal_card()

    get_each_player_up_to_6_cards()

    if check_if_loser():
        end_game()

    if turn_number > 1:
        determine_attacker_and_defender()

    wait_for_attacker()

    wait_for_defense()

def submit_attack(cards):
    if cards.length == 0:
        #remove random card from attacker hand, add to attack_cards_on_table
    else:
        #remove cards from attacker hand, add to attack_cards_on_table
    attack_made = True

def wait_for_attacker():
    attack_made = False
    timer = 0
    while True:
        time.sleep(1)
        timer += 1
        if attack_made:
            return
        if timer >= 60:
            submit_attack([])

def submit_bonus_attack(cards):
    #ensure valid move
    #remove cards from attacker hand, add to attack_cards_on_table
    defense_timer = 60

def submit_defense(defender_card, attack_card):
    #check if defender card can beat attacker card, throw error if not.
    defense_started = True
    #remove defender card from defender hand, add to attack_cards_on_table
    defense_timer = 60

def submit_bounce(defender_cards, attack_cards):
    #check if defender cards match attack_cards in numerical value, throw error if not.
    determine_attacker_and_defender() #shift the attacker and defender ids forwards
    get_each_player_up_to_6_cards()
    #leave the current cards on the table for the next person to defend against

def wait_for_defense():
    defense_timer = 0
    while True:
        time.sleep(1)
        timer += 1
        if defense_timer >= 60:
            if all_cards_defended():
                successfully_defended = True
                #kill cards on table
                #end turn

def all_cards_defended():
    #check if all attack cards on the table are successfully defended

def get_next_player_with_cards(id):
    key = id+1
    while player_cards[key].length == 0:
        key += 1
    return key

def determine_attacker_and_defender():
    if defender_id == -1 and attacker_id == -1:
        #first turn
        attacker_id = random.choice(players)
        defender_id = get_next_player_with_cards(attacker_id)
    else:
        #not first turn
        if successfully_defended:
            attacker_id = defender_id
            defender_id = get_next_player_with_cards(defender_id)
            successfully_defended = False





while True:
    turn_number += 1
    turn_timer = 60
    move(turn_number)