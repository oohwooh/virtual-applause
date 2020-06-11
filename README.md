# Virtual Applause
![Please Clap](pleaseClap.gif)

### SETUP
##### Option 1: running with docker (reccomended)
- Option 1a running from Docker Hub

    run the built container from Docker Hub with the token environment variables:

     `$ docker run -e BOT_TOKEN=DISCORD_TOKEN_HERE oohwooh/virtual-applause:latest`
- Option 1b building and running the Docker image from source

    `git clone https://github.com/oohwooh/virtual-applause.git`

    `cd virtual-applause`

    `docker build . -t virtual-applause`

    `$ docker run -e BOT_TOKEN=DISCORD_TOKEN_HERE virtual-applause`
##### Option 2: running from command line
sorry but you're on your own with this one, have fun. Make sure ffmpeg is installed properly and all that crap.

----------

#### Usage: 
##### How to clap:
send a message with the word "clap" in it. If the bot is connected to a voice channel, then congratulations! You just clapped.
##### How to connect to a voice channel:
The `cl!connect` command connects the bot to your current channel, for clapping.
##### How to disconnect from a voice channel:
The `cl!disconnect` command disconnects the bot from it's connected channel. The bot will also automatically disconnect if it is left alone in a channel


######Customization:
see [CONTRIBUTING.md](CONTRIBUTING.md)