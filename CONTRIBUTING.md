CONTRIBUTING.md
-
Want to add a custom clap noise? It's a simple n step process!

1.) Fork this repo

2.) Move any required `.wav` files into their own folder (inside `audio/`)

3.) Add a line to the end of `cogs/core.py` with the following format:

    bot.add_cog(clapTemplate.genCog(bot, 'NAME', 'PATH', 'EMOJI'))
the variables mean the following: 
- Name: what you want to trigger the sound effect and emoji (e.g. 'clap' or 'carp')
- Path: path to a folder containing audio files (e.g. 'audio/claps`)
- Emoji: The emoji associated with your clap

4.) Create a pull request describing your addition

---
For other things do a pull request however you like im not that picky