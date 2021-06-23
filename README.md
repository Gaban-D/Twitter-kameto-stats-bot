# About

This program is used to fetch data from a twitch channel with twitch api and post a daily tweet about those data

⚠⚠⚠WARNING: Using this may get your twitter account shadowbanned, i'm trying to fix this

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the bot and his requirements.

```bash
git clone https://github.com/Gabann/Twitch-stats-to-twitter-bot.git
cd Twitch-stats-to-twitter-bot
pip install requirements.txt 
```

## Usage

First you need to edit the .env file with your twitch and twitter api keys

For your twitch and twitter consumer keys you'll need to create a developper account on both sites: 

Twitter - https://developer.twitter.com/en/apply-for-access

Twitch - https://dev.twitch.tv/
 
Then for the twitter access key you can get it via shell

```bash
python3 get_access_token.py
```

<br/><br/>
After setting your api keys you can post tweets with main.py (It is reccomended to automate this task to run once a day)

At the time of writing twitch api doesn't support viewer peak and games played, if you want the bot to tweet about those datas you'll have to execute save_current_stream_stats.py every ~5 min approx

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
