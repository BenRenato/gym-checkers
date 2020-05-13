class Action_Value_Pair:

    def __init__(self, move, value):

        self.move = move
        self.value = value

    def get_action_value_pair(self):

        return self.move, self.value

    def get_value(self):
        return self.value

    def get_action(self):
        return self.move

    def update_value(self, value):
        self.value = value

    def __str__(self):
        return "Move: " + str(self.move) + "Value: " + str(self.value)

    def __repr__(self):
        return "Move: " + str(self.move) + " Value: " + str(self.value) + "\n"