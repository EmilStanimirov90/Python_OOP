class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name not in self.skills:
            self.skills[skill_name] = mana_cost
            return f"Skill {skill_name} added to the collection of the player {self.name}"
        return "Skill already added"

    def player_info(self):
        # result = ''
        # result += f"Name: {self.name}\n"
        # result += f"Guild: {self.guild}\n"
        # result += f"HP: {self.hp}\n"
        # result += f"MP: {self.mp}\n"
        # for skill, mana in self.skills.items():
        #     result += f"==={skill} - {mana}\n"
        #     return result
        result = [f"Name: {self.name}", f"Guild: {self.guild}", f"HP: {self.hp}", f"MP: {self.mp}"]
        for skill, mana in self.skills.items():
            result.append(f"==={skill} - {mana}")
        return '\n'.join(result)
