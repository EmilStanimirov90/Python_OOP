from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    def __init__(self, name: str):
        super().__init__(name, 120)

    def miss(self, time_to_catch: int):
        self.oxygen_level -= int(time_to_catch * 0.6)
        if self.oxygen_level < 0:
            self.oxygen_level = 0

    def renew_oxy(self):
        self.oxygen_level = 120
