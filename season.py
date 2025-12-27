class Season:

    def __init__(self, season_num, ovr_win, ovr_loss, conf_win, conf_loss, ppg):
        self.season_num = season_num
        self.ovr_win = ovr_win
        self.ovr_loss = ovr_loss
        self.conf_win = conf_win 
        self.conf_loss = conf_loss
        self.ppg = ppg 

    def __str__(self):
        return (
            f"{self.name} | "
            f"OVR: {self.ovr_win}-{self.ovr_loss} | "
            f"CONF: {self.conf_win}-{self.conf_loss} | "
            f"PPG: {self.ppg}"
        )

