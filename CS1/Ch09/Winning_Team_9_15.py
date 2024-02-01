class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    def print_information(self):
        print("Team name:", self.name)
        print("Wins:", self.wins)
        print("Losses:", self.losses)

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        return self.wins / (self.wins + self.losses)
    
    # TODO: Define print_standing()
    # Win percentage: 0.81
    # Congratulations, Team Ravens has a winning average!

    def print_standing(self):
        # print "Winning percentage:" and the team's winning percentage 
        # rounded to no decimal places, and printed as a proper percentage
        print("Winning percentage: {:.0%}".format(self.get_win_percentage()))
        if self.get_win_percentage() >= 0.5:
            # print "congratulations, team" and the team name, and "has a winning average!"
            print("Congratulations, Team ", self.name, " has a winning average!")
        else:
            print("This team is losing!")


if __name__ == "__main__":
    team = Team()
    print('after creating the object:')
    team.print_information()
   
    user_name = input("Enter team's name:\n")
    user_wins = int(input("Enter number of wins:\n"))
    user_losses = int(input("Enter number of losses:\n"))
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses

    print('after setting the attributes:')
    team.print_information()
    
    team.print_standing()