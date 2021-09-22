# PSARIP RSS DICORD BOT

## Introduction

> This is a discord bot which sends to a channel whenever a new movie / series episode is released on https://x265.club/ (aka PSARIPS) which is a platform which publishes movies / series episodes in the most highest quality with the lowest file size in multiple options to download for free.

## Quick Note!!!!!!!

> Unfortunately this bot has to be run locally on your device this means it's not possible to host the bot in a VPS, when I try to host on a server I run into cloud flare issues which I have no clue how to get around (I have tried a lot of methods and spent well over 10 hours to find a work around). If you know how to do so please make a [Pull Request](https://github.com/D3CRYPT360/PSARIP/pull) or would like to discuss feel free to create an [Issue](https://github.com/D3CRYPT360/PSARIP/issues/new). any help will be gladly appreciated :)

## Installation

> You could and I highly request you create a virtual environment to run the script and install the dependencies.
 ```cli
$ git clone https://github.com/D3CRYPT360/PSARIP_Discord_bot
```
```cli
$ pip3 install -r requirements.txt
```

## Running

Rename the `.env.example` to `.env` and replace `YOUR_TOKEN` with your bots token.

Put your channel id in the `CHANNEL_ID` list in the main.py file. you can put more than 1 channel as multiple channels are supported. 

```cli
$ python3 main.py
```
If you are on Windows use `py` instead of `python3` and `pip` instead of `pip3` and it should work.

## TO DO
- [x] Add multiple channel support
- [ ] Somehow get over the cloudflare stuff
