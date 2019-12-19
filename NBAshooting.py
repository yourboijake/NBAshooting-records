import pandas
import math

#data is from the NBA Teams Shot Dashboard, for the 2018-2019 season
path = '/Users/jacobdunning/Desktop/NBAstats.xlsx'
nba_stats = pandas.read_excel(path)
name = input("Enter a team name, including where the team is from (i.e. 'Utah Jazz'): ")
index = 0
perc_ratio = 0.0
shooting_ratio = 0.0

name_ok = False
#check if the team the user is looking for is in the database, and identify that team's row (index)
for x in nba_stats['Teams']:
    if name == x:
        name_ok = True
        break
    index += 1

if name_ok == False:
    print("The team you named is not in the directory")
else:
    #perc ratio is ratio of expected values, shooting ratio is the actual ratio of 2 to 3 pt shots
    two_perc = (nba_stats.loc[index, "2FGM"]/nba_stats.loc[index, "2FGA"])
    three_perc = (nba_stats.loc[index, "3PM"]/nba_stats.loc[index, "3PA"])
    perc_ratio = (2*two_perc)/(3*three_perc)
    shooting_ratio = nba_stats.loc[index, "2FGA"]/nba_stats.loc[index, "3PA"]
    print("This team makes", math.trunc(two_perc*100), "% of their two point shots and", math.trunc(three_perc*100), "% of their three point shots")
    print("Ratio of expected value (2's over 3's):", round(perc_ratio, 3))
    print("Ratio of shots attempted (2's over 3's):", round(shooting_ratio, 3))

    #concl is short for conclusion, shows the verdict on teams
    if shooting_ratio > perc_ratio:
        concl = "overshooting"
    elif shooting_ratio == perc_ratio:
        concl = "shooting the correct number of "
    else:
        concl = "undershooting"
    print("The", name, "is", concl, "2-point shots relative to 3 point shots")

    #numbers of teams over, under, correct number of 2's relative to 3's
    num_over = 0
    num_right = 0
    num_under = 0

#calculation for the whole league
for x in range(len(nba_stats.index)):
    perc_ratio = (2 * (nba_stats.loc[index, "2FGM"] / nba_stats.loc[index, "2FGA"])) / (
                3 * (nba_stats.loc[index, "3PM"] / nba_stats.loc[index, "3PA"]))
    shooting_ratio = nba_stats.loc[index, "2FGA"] / nba_stats.loc[index, "3PA"]
    if shooting_ratio > perc_ratio:
        num_over += 1
    elif shooting_ratio == perc_ratio:
        num_right += 1
    else:
        num_under += 1
#print results
print("In the whole league, there are", num_over, "teams that are overshooting 2's,", num_right, "teams that",
    "are shooting the right number of 2's, and there are", num_under, "teams that are undershooting 2's")
