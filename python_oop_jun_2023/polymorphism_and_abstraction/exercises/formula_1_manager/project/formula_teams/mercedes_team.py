from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    SPONSORS = {
        1: 1100000,
        2: 600000,
        3: 600000,
        4: 100000,
        5: 100000,
        6: 50000,
        7: 50000,
    }

    EXPENSES_PER_RACE = 200000

    def __init__(self, budget: int) -> None:
        super().__init__(budget)
        self.budget = budget

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0
        if race_pos in MercedesTeam.SPONSORS.keys():
            reward = MercedesTeam.SPONSORS[race_pos]
            revenue += reward

        revenue -= MercedesTeam.EXPENSES_PER_RACE
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. " \
               f"Current budget {self.budget}$"
