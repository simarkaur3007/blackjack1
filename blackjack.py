import random
import tkinter as tk
number_of_wins,number_of_losses=0,0 #keeps track of overall score
def track_score(print_text):
    global number_of_wins, number_of_losses
    if "win" in print_text:
         number_of_wins +=1 #will add all the wins to counter
    elif "lose" in print_text:
         number_of_losses+=1 #will add all losses to counter
    text_label.config(text=print_text)
    score_label.config(
                                              text= f"wins:{number_of_wins} losses:{number_of_losses}" #shows the wins and losses numerically
                                       )
cardnames = [ "A","2", "3", "4", "5","6", "7", "8", "9","10", "J", "Q", "K"] #creating the cards
cardvalues = {
    'A': 11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,'10':10, 'J':10, 'Q':10, 'K':10} #assigning point values for each type of card
deck = list(cardvalues.keys()) * 4 #4 cards of each number
random.shuffle (deck) #shuffles the cards
player_cards = [deck.pop(0), deck.pop (0)] #gives the player the first two cards from the deck (0 is the the assigned value from the list)
dealer_cards = [deck.pop(0), deck.pop (0)]#gives the dealer the next two cards from the deck (0 is the assigned value from list)
def calculate_points(points):
    total =0   #calculates the total value of cards
    total_A =0 #calculates the total aces in hand
    for card in points: #function for different card value results
        total += cardvalues [card]
        if card == 'A': #checks if A is in hand
         total_A +=1 #keeps track of the number of A in hand
    while total>21 and total_A>0:
        total-=10 #if total is over 21, subtract 10 from total (since A is switched from 11 to 1)
        total_A-=1 #keeps track of the number of A adjusted (tracks the adjustment made above)
    return total #shows the total points of the player
def update_display():
    player_label.config(text= "Player's cards: "+"".join(player_cards))  #defining the function for updating players cards
    dealer_label.config(text= "Dealer's cards: "+"".join(dealer_cards)) #defining the function for updating dealers cards
def hit():
    player_cards.append(deck.pop(0)) #Adds the card from the top of the deck to the player's hand
    update_display() #shows all the cards in hand now
    if calculate_points(player_cards)>21:
        text_label.config(text="You lose") #if the player's totoal point are over 21, the graphics display shows the player loses
        track_score("you lose:(")
        hit_btn.config(state="disabled") #disables the hit button 
        stand_btn.config(state="disabled") #disables the stand button
def stand():
            update_display()#shows dealers card that was hidden
            while calculate_points (dealer_cards) <16: #will allow dealer to keep getting a card until they have a total of less than 17
                dealer_cards.append(deck.pop(0)) #takes the card from the top of the deck for the dealer
                update_display() #shows all the delaers cards
                dealer_total=calculate_points(dealer_cards) #calculates dealer's total points
                player_total=calculate_points(player_cards) #calculates player's total points
root =tk.Tk()
root.title("Blackjack")
player_label = tk.Label(root, text="", font=("Times New Roman", 20 ))#chooses font and size for player label in game
player_label.pack(pady=7)#vertical padding above and below player label
dealer_label=tk.Label(root, text="", font=("Times New Roman", 20) )#chooses font and size for dealer label
dealer_label.pack(pady=7)#verical padding below and above dealer label
text_label=tk.Label(root, text="", font=("Times New Roman", 20, "bold"))#chooses font and size for result label
text_label.pack(pady=14)
score_label=tk.Label(root, text="number_of_wins:{wins} number_of_losses:{loses}", font=("Times New Roman", 16))#chooses font and size to display win/lose score
score_label.pack(pady=6)
btn_frame=tk.Frame(root)
btn_frame.pack(pady=14)
hit_btn=tk.Button(btn_frame, text="Hit", width=12, command=hit) #hit button dimensions
hit_btn.pack(side="left",padx=12)
stand_btn=tk.Button(btn_frame, text="Stand", width=12, command=stand) #stand button dimensions
stand_btn.pack(side="right", padx=12)
update_display()
root.mainloop()


