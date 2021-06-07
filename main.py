from config import get_twitter_api
from datetime import datetime, timedelta
from config import get_twitch_api

twitter_api = get_twitter_api()
twitch_api = get_twitch_api()

streamer_id = twitch_api.get_users(logins=['kamet0'])['data'][0]['id']


def get_most_viewed_clip(broadcaster_id=streamer_id, start_date=datetime.now() - timedelta(days=1), end_date=datetime.now() - timedelta(days=1)):
    # get_clips() does not support datetime.now().date() so we set the time manually to achieve the same result
    start_date = start_date.replace(hour=0, minute=0, second=0)
    end_date = end_date.replace(hour=23, minute=59, second=59)

    return twitch_api.get_clips(broadcaster_id=broadcaster_id, first=1, started_at=start_date, ended_at=end_date)['data'][0]


videos = twitch_api.get_videos(user_id=streamer_id, first=10)
view_count = 0
stream_duration_list = []

# calculate the total view count and store streams durations in a list
for video in videos['data']:
    video_date = datetime.strptime(video["created_at"], '%Y-%m-%dT%H:%M:%SZ')

    # check if the video was created yesterday
    if video_date.date() == datetime.now().date() - timedelta(days=1):
        view_count += video['view_count']

        try:
            stream_duration_list.append(datetime.strptime(video["duration"], '%Hh%Mm%Ss'))
        except ValueError:
            try:
                stream_duration_list.append(datetime.strptime(video["duration"], '%Mm%Ss'))
            except ValueError:
                stream_duration_list.append(datetime.strptime(video["duration"], '%Ss'))

# Calculate the total stream duration
total_duration = timedelta(seconds=0)
for duration in stream_duration_list:
    total_duration += timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)

# Post a tweet
twitter_api.update_status("Hier Kameto a stream pendant " + str(total_duration) + " durant lesquelles il a comptabilisé un total de "
                          + str(view_count) + " vues \nSon clip le plus populaire  était:" + get_most_viewed_clip()['url'])
