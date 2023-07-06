from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSORS = {
        1: 1520000,
        2: 820000,
        3: 20000,
        4: 20000,
        5: 20000,
        6: 20000,
        7: 20000,
        8: 20000,
        10: 10000,
    }

    EXPENSES_PER_RACE = 250000

    def __init__(self, budget: int) -> None:
        super().__init__(budget)
        self.budget = budget

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        revenue = 0
        if race_pos in RedBullTeam.SPONSORS.keys():
            reward = RedBullTeam.SPONSORS[race_pos]
            revenue += reward

        revenue -= RedBullTeam.EXPENSES_PER_RACE
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. " \
               f"Current budget {self.budget}$"
