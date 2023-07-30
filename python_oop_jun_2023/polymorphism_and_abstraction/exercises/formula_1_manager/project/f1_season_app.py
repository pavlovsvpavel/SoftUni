from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self) -> None:
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int) -> str:
        valid_teams = ["Red Bull", "Mercedes"]

        if team_name not in valid_teams:
            raise ValueError("Invalid team name!")

        if team_name == valid_teams[0]:
            self.red_bull_team = RedBullTeam(budget)

        elif team_name == valid_teams[1]:
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int) -> str:
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        if red_bull_pos < mercedes_pos:
            winner = "Red Bull"
        else:
            winner = "Mercedes"

        return f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. " \
               f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. " \
               f"{winner} is ahead at the {race_name} race."