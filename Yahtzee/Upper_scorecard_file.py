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

    def get_unfilled_categories(self):
        list_of_unfilled_categories = []
        for category, score in self.upper_scorecard.items():
            if score is None:
                list_of_unfilled_categories.append(category)
        return list_of_unfilled_categories
        