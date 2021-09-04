import random
def play():
    user = input("What\'s your choice???r' for rock,'p' for paper,'s' for scissors\n ").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'
    if is_win(user,computer):
        return 'you won!'

    return 'you lost!'
# r>s, s>p, p>r
# true if player wins
def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(play())
