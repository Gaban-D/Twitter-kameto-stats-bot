from dotenv import load_dotenv
from config import get_twitch_api
from datetime import datetime
import shelve

load_dotenv()
twitchAPI = get_twitch_api()
saved_variables = shelve.open("saved_variables")
date = datetime.now().date()
live = None

try:
    live = twitchAPI.get_streams(user_login=['kamet0'], first=1)['data'][0]
except IndexError:
    print("{date} Kameto is not in live \n".format(date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    saved_variables.close()
    quit()

# Check the current viewer count and save it if its the highest registered
try:
    if live['viewer_count'] > saved_variables["{date} viewer peak".format(date=date)]:
        saved_variables["{date} viewer peak".format(date=date)] = live['viewer_count']
except KeyError:
    # print('Viewer peak key does not exist')
    saved_variables["{date} viewer peak".format(date=date)] = live['viewer_count']

# Check which game is played atm and add it to the games played list if not already done
try:
    if not(live['game_name'] in saved_variables["{date} games played".format(date=date)]):
        saved_variables["{date} games played".format(date=date)] += [live['game_name']]

except KeyError:
    # print('Games played key does not exist')
    saved_variables["{date} games played".format(date=date)] = []
    saved_variables["{date} games played".format(date=date)] += [live['game_name']]

# Used for crontab logging
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ": Current viewers " + str(live['viewer_count']))
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ": Today viewer peak " + str(saved_variables["{date} viewer peak".format(date=date)]))
print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ": Today games played " + str(saved_variables["{date} games played".format(date=date)]) + "\n")

saved_variables.close()
