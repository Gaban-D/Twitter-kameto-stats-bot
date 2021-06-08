from config import get_twitter_api
from datetime import datetime, timedelta
from config import get_twitch_api
from Streams import Streams

twitter_api = get_twitter_api()
twitch_api = get_twitch_api()

date_to_check = datetime.now() - timedelta(days=5)
streamer_id = twitch_api.get_users(logins=['kamet0'])['data'][0]['id']


def get_most_viewed_clip(broadcaster_id=streamer_id, start_date=date_to_check, end_date=date_to_check):
	# get_clips() does not support datetime.now().date() so we set the time manually to achieve the same result
	start_date = start_date.replace(hour=0, minute=0, second=0)
	end_date = end_date.replace(hour=23, minute=59, second=59)

	return twitch_api.get_clips(broadcaster_id=broadcaster_id, first=1, started_at=start_date, ended_at=end_date)['data'][0]


videos = twitch_api.get_videos(user_id=streamer_id, first=5)['data']
streams = Streams()

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


if streams.view_count == 0:
	print("No video were found")
	tweet = twitter_api.update_status('Le {date} Kameto était en day off'.format(date=date_to_check.strftime('%d/%m/%Y')))

else:
	tweet = twitter_api.update_status('Stats de Kameto le {date} :'
							  '\n⏰ Durée totale des streams : {stream_duration}'
							  '\n👀 Total de vues : {view_count}'
							  '\n🎬 Clip le plus populaire du jour : {clip_url}'
							  .format(date=date_to_check.strftime('%d/%m/%Y'),
									  stream_duration=streams.calculate_total_streams_duration(),
									  view_count=streams.view_count,
									  clip_url=get_most_viewed_clip()['url']))

	print("Tweet successfully posted at " + tweet.entities['urls'][0]['expanded_url'])
