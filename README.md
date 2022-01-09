# PSARIP RSS DICORD BOT

## Introduction

This is a Discord bot which sends a message to a channel whenever a new movie/series episode is released on [PSArips](https://psa.pm/).

### What is PSArips?
PSArips is a platform which publishes movies/series episodes in high quality on small files for free.

## Hosting Issues

Unfortunately, this bot has to be run locally. When it's ran on a host, CloudFlare issues are present and I currently don't know how to fix them.
If you know how to fix these issues, please make a [pull request](https://github.com/D3CRYPT360/PSARIP_Discord_bot/pulls) or create an [issue](https://github.com/D3CRYPT360/PSARIP_Discord_bot/issues) for discussion. Any help will be gladly appreciated! :)

## Installation

**USING A VIRTUAL ENVIROMENT IS HIGHLY RECOMMENDED!**

### Getting Source Code
```cli
$ git clone git://github.com/D3CRYPT360/PSARIP_Discord_bot.git
```

### Installing Dependencies
```cli
$ pip3 install -r requirements.txt
```

## Running Bot

### Setting Up Configs
1. Rename `.env.example` to `.env`
2. Change `BOT_TOKEN` to your Discord bot token
3. Add your channel(s) to `CHANNELS` *(multiple channels are supported)*

### Starting
```cli
$ python3 main.py
```
