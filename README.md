<!--suppress ALL, HtmlUnknownAnchorTarget -->

<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<h3 align="center">Twitter bot to twitch stats</h3>


<div align="center">
  <p>
    A shell twitter bot that post daily about twitch.tv channel data
    <br />
    <a href="https://github.com/Gabann/Twitter-bot-twitch-stats/tree/main/documentation"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/gabann/Twitter-bot-twitch-stats/issues">Report Bug</a>
    ·
    <a href="https://github.com/gabann/Twitter-bot-twitch-stats/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About the Project

This app is used to fetch data from a twitch channel with twitch api and post a tweets about those data


### Features

- Fetch data from a twitch channel with twitch api and save it locally
- Post tweets about saved data

### Built With

[![Python][python-shield]][python-url]
[![PiP][pip-shield]][pip-url]
[![Twitch API][twitch-api-shield]][twitch-api-url]
[![Twitter API][twitter-api-shield]][twitter-api-url]
[![Dotenv][dotenv-shield]][dotenv-url]

<div align="right"><a href="#readme-top">back to top</a></div>


<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

[Python 3](https://www.python.org/downloads/)

[Pip](https://pypi.org/project/pip/)

### Installation

```bash
git clone https://github.com/Gabann/Twitter-bot-twitch-stats.git
cd Twitch-stats-to-twitter-bot
pip install -r requirements.txt

sudo locale-gen fr_FR
sudo locale-gen fr_FR.UTF-8
```

<div align="right"><a href="#readme-top">back to top</a></div>


<!-- USAGE EXAMPLES -->

## Usage

First you need to edit the .env file with your twitch and twitter api keys

Twitter - https://developer.twitter.com/en/apply-for-access

Twitch - https://dev.twitch.tv/

For the twitter access key you can get it via shell

```bash
python3 get_access_token.py
```

After setting your api keys you can post tweets with main.py (We recommend to automate this task)

At the time of writing twitch api doesn't support viewer peak and games played, if you want the bot to tweet about those datas you'll 
have to automate the execution of save_current_stream_stats.py as well


<div align="right"><a href="#readme-top">back to top</a></div>

<!-- CONTRIBUTING -->

## Contributing

We welcome contributions from everyone! Follow these steps to contribute:

1. **Fork** the repository.
2. **Clone** the forked repository to your local machine.
3. **Create a new branch** for your contribution.
4. **Make your changes** and **commit** them.
5. **Push** your changes to your forked repository.
6. **Open a pull request** to the main project repository.

### Contribution Guidelines

- Discuss significant changes by opening an issue first.
- Follow the existing code style and structure.
- Write clear commit messages and document your code.
- Ensure changes don't break existing functionality.
- Update documentation if necessary.

<div align="right"><a href="#readme-top">back to top</a></div>


<!-- LICENSE -->

## License

Distributed under the 'LICENSE' License. See [`LICENSE`](https://github.com/Gabann/Twitter-bot-twitch-stats/blob/master/LICENSE) for more 
information.

<div align="right"><a href="#readme-top">back to top</a></div>


<!-- CONTACT -->

## Contact

- [![Twitter][gmail-shield]][gmail-url]
- [![LinkedIn][linkedin-shield]][linkedin-url]
- [![Twitter][twitter-shield]][twitter-url]

<div align="right"><a href="#readme-top">back to top</a></div>


---------------------------------------------------------------

[repo-link]: https://github.com/Gabann/Twitter-bot-twitch-stats

[contributors-shield]: https://img.shields.io/github/contributors/gabann/Twitter-bot-twitch-stats.svg?style=for-the-badge

[contributors-url]: https://github.com/gabann/Twitter-bot-twitch-stats/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/gabann/Twitter-bot-twitch-stats.svg?style=for-the-badge

[forks-url]: https://github.com/gabann/Twitter-bot-twitch-stats/network/members

[stars-shield]: https://img.shields.io/github/stars/gabann/Twitter-bot-twitch-stats.svg?style=for-the-badge

[stars-url]: https://github.com/gabann/Twitter-bot-twitch-stats/stargazers

[issues-shield]: https://img.shields.io/github/issues/gabann/Twitter-bot-twitch-stats.svg?style=for-the-badge

[issues-url]: https://github.com/gabann/Twitter-bot-twitch-stats/issues

[license-shield]: https://img.shields.io/github/license/gabann/Twitter-bot-twitch-stats.svg?style=for-the-badge

[license-url]: https://github.com/gabann/Twitter-bot-twitch-stats/blob/master/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/gabin-deboulogne/

[twitter-shield]: https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white

[twitter-url]: https://twitter.com/gabandev

[gmail-shield]: https://img.shields.io/badge/Gmail-EA4335.svg?style=for-the-badge&logo=Gmail&logoColor=white

[gmail-url]: mailto:gabin.deboulogne@gmail.com

[python-shield]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

[python-url]: https://www.python.org/

[pip-shield]: https://img.shields.io/badge/Pip-3776AB?style=for-the-badge&logo=pypi&logoColor=white

[pip-url]: https://pypi.org/project/pip/

[twitch-api-shield]: https://img.shields.io/badge/Twitch-API-9146FF?style=for-the-badge&logo=twitch&logoColor=white

[twitch-api-url]: https://dev.twitch.tv/

[twitter-api-shield]: https://img.shields.io/badge/Twitter-API-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white

[twitter-api-url]: https://developer.twitter.com/

[dotenv-shield]: https://img.shields.io/badge/Dotenv-315?style=for-the-badge&logo=dotenv&logoColor=white

[dotenv-url]: https://pypi.org/project/python-dotenv/
