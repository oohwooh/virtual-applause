# Virtual Applause
![Please Clap](pleaseClap.gif)

# SETUP
## Option 1: running with docker (reccomended)
- Option 1a running from Docker Hub
run the built container from Docker Hub with the token environment variables:

`$ docker run -e BOT_TOKEN=DISCORD_TOKEN_HERE oohwooh/virtual-applause:latest`
- Option 1b building and running the Docker image from source

`git clone https://github.com/oohwooh/virtual-applause.git`

`cd virtual-applause`

`docker build . -t virtual-applause`

`$ docker run -e BOT_TOKEN=DISCORD_TOKEN_HERE virtual-applause`
## Option 2: running from command line
sorry but you're on your own with this one, have fun. Make sure ffmpeg is installed properly and all that crap.
# Commands: 
## cl!connect
`cl!connect` connects the bots to your current channel, for clapping.

