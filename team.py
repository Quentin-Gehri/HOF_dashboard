class Team:
    
    def __init__(self, name):
        self.name = name
        self.seasons = []
        self.ovr_win = 0
        self.ovr_loss = 0
        self.conf_win = 0
        self.conf_loss = 0
        self.ppg = 0

    def add_season(self, season):
        self.seasons.append(season)

    def calculate_total(self):
        self.ovr_win = 0
        self.ovr_loss = 0
        self.conf_win = 0
        self.conf_loss = 0
        self.ppg = 0

        for season in self.seasons:
            self.ovr_win += season.ovr_win
            self.ovr_loss += season.ovr_loss
            self.conf_win += season.conf_win
            self.conf_loss += season.conf_loss
            self.ppg += season.ppg

        if self.seasons:
            self.ppg /= len(self.seasons)

    def __str__(self):
        if self.seasons:
            totals_str = (
                f"Team: {self.name}\n"
                f"  Total Overall Record : {self.ovr_win}-{self.ovr_loss}\n"
                f"  Total Conference     : {self.conf_win}-{self.conf_loss}\n"
                f"  Average PPG          : {self.ppg:.1f}"
            )
            return totals_str
        else:
            return f"Team: {self.name} (no seasons yet)"
