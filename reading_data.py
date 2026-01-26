from season import Season 
from team import Team
import time

def find_team(teams, name):
    for team in teams:
        if team.name == name:
            return team
    return None

def process_line(line, season_num):
    words = line.split()
    team_name = words[0].replace(":", "")
    ovr_win_str, ovr_loss_str = words[2].split("-")
    ovr_win, ovr_loss = int(ovr_win_str), int(ovr_loss_str)
    conf_win_str, conf_loss_str = words[3].replace("[", "").replace("]", "").split("-")
    conf_win, conf_loss = int(conf_win_str), int(conf_loss_str)
    ppg = float(words[4].replace("[", "").replace("]", ""))
    return Team(team_name), Season(season_num, ovr_win, ovr_loss, conf_win, conf_loss, ppg)

def create_teams_from_file(filename, season_num, teams):
    file = open(filename)
    for line in file:
        if(line[slice(3)] != "## "):
            if (line[slice(1)] == ":"):
                team, season = process_line(line, season_num)
                team_found = find_team(teams, team.name)
                if team_found is None:
                    team.add_season(season)
                    teams.append(team)
                else: 
                    team_found.add_season(season)

def reading_data():
    teams = []
    for season_num in range(17, 31):
        create_teams_from_file(f"data/S{season_num}.txt", season_num, teams)    
    for team in teams:
        team.calculate_total()
    return teams

if __name__ == "__main__":
    main()