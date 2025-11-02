#Ch9_Rd2_HW_2of3_ShonH, 9.15 Lab: Winning Team

class Team:
    def __init__(self):
        self.name = 'none'
        self.wins = 0
        self.losses = 0

    # TODO: Define get_win_percentage()
    def get_win_percentage(self):
        total_games = self.wins + self.losses
        if total_games == 0:
            return 0.0
        return self.wins / total_games
    # TODO: Define print_standing()
    def print_standing(self):
        win_percentage = self.get_win_percentage()
        print(f'Win Percentage: {win_percentage:.0%}')
        if win_percentage >= 0.5:
            print(f'Congratulations! Team {self.name} has a winning average!')
        else:
            print(f'Team {self.name} has a losing average.')

if __name__ == "__main__":
    team = Team()
   
    user_name = input('Input the name of the team: ')
    user_wins = float(input('Input the number of wins the team has had: '))
    user_losses = float(input('Input the number of losses the team has had: '))
    
    team.name = user_name
    team.wins = user_wins
    team.losses = user_losses
    
    team.print_standing()