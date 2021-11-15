class Player_class:
    """Player data and behavior."""
    def __init__(self):
        self.data = []
        self.name = 'name'

    def set_name(self,your_name):
        self.name = your_name

    def get_name(self):
        return self.name
