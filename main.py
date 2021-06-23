from config import get_twitter_api
from datetime import datetime, timedelta
from config import get_twitch_api, save_path
from stats import Stats
import shelve

twitter_api = get_twitter_api()
twitch_api = get_twitch_api()

date_to_check = datetime.now() - timedelta(days=1)
streamer_id = twitch_api.get_users(logins=['kamet0'])['data'][0]['id']


def get_most_viewed_clip(broadcaster_id=streamer_id, start_date=date_to_check, end_date=date_to_check):
	# get_clips() does not support datetime.now().date() so we set the time manually to achieve the same result
	start_date = start_date.replace(hour=0, minute=0, second=0)
	end_date = end_date.replace(hour=23, minute=59, second=59)

	# In case no clips were found
	try:
		return twitch_api.get_clips(broadcaster_id=broadcaster_id, first=1, started_at=start_date, ended_at=end_date)['data'][0]['url']

	except IndexError:
		return "Aucun miskine"


videos = twitch_api.get_videos(user_id=streamer_id, first=10)['data']
streams = Stats()

# calculate the total view count and store streams durations in a list
for video in videos:
	video_date = datetime.strptime(video["created_at"], '%Y-%m-%dT%H:%M:%SZ')

	# check if the video was created yesterday
	if video_date.date() == date_to_check.date():
		streams.view_count += video['view_count']

		try:
			streams.streams_durations_array.append(datetime.strptime(video["duration"], '%Hh%Mm%Ss'))

		except ValueError:
			try:
				streams.streams_durations_array.append(datetime.strptime(video["duration"], '%Mm%Ss'))

			except ValueError:
				streams.streams_durations_array.append(datetime.strptime(video["duration"], '%Ss'))

try:
	# Load the saved variables
	saved_variables = shelve.open(fr'{save_path}')
	viewer_peak = format(saved_variables["{date} viewer peak".format(date=date_to_check.date())], ',d')
	played_games_string = ", ".join(saved_variables["{date} games played".format(date=date_to_check.date())])
	saved_variables.close()

except KeyError:
	print("{date} - Error: Couldn't get the saved variables".format(date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
	# HACK dirty way to ensure the script will be executed even if the saved variable couldn't be loaded
	viewer_peak = "Inconnu"
	played_games_string = "Inconnu"


if streams.view_count == 0:
	print("{date} - No videos were found".format(date=datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
	tweet = twitter_api.update_status('Le {date} Kameto était en day off'.format(date=date_to_check.strftime('%d/%m/%Y')))

else:
	tweet = twitter_api.update_status(
		'Stats de Kameto le {date}:'
		'\n⏰ Durée de stream : {stream_duration}'
		'\n🔥 Peak de viewers : {viewer_peak}'
		'\n👀 Total de vues : {view_count}'
		'\n🕹️ Jeux streamés : {played_games}'
		'\n🎬 Top clip du jour :{clip_url}'
		.format(
			date=date_to_check.strftime('%d/%m/%y'),
			stream_duration=streams.calculate_total_streams_duration(),
			viewer_peak=viewer_peak,
			view_count=format(streams.view_count, ',d'),
			played_games=played_games_string,
			clip_url=get_most_viewed_clip()))

print("{date} Tweet successfully posted at {url}".format(date=datetime.now().strftime("%d/%m/%Y %H:%M:%S"), url=tweet.entities['urls'][0]['expanded_url']))
