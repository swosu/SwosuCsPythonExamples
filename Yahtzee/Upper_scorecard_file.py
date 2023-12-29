class Upper_Scorecard_class():
    def __init__(self):
        self.upper_scorecard = {
            "Aces": None,
            "Twos": None,
            "Threes": None,
            "Fours": None,
            "Fives": None,
            "Sixes": None,
        }

        self.upper_scorecard_values = {
            "Aces": 1,
            "Twos": 2,
            "Threes": 3,
            "Fours": 4,
            "Fives": 5,
            "Sixes": 6,
        }

    def get_unfilled_categories(self):
        list_of_unfilled_categories = []
        for category, score in self.upper_scorecard.items():
            if score is None:
                list_of_unfilled_categories.append(category)
        return list_of_unfilled_categories
    
    def get_possible_scores_for_unfilled_categories(self, dice):
        possible_scores = {}
        list_of_unfilled_categories = self.get_unfilled_categories()
        for category in list_of_unfilled_categories:
            possible_scores[category] = self.get_score_for_category(category, dice)
            print('for ', category, ' score is ', possible_scores[category])
        return possible_scores
    
    def get_score_for_category(self, category, dice):
        score = 0
        category_value = self.upper_scorecard_values[category]
        for die in dice:
            if die == category_value:
                score += die
        return score
        