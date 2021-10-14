# MLH_LearnDay_Connect_Two_API-s
Project completed using autocode.com allow a discord bot to access youtube and play music via the discord voice channel.  
  
> **The files included in this directory are included in the [tutorial](https://autocode.com/guides/how-to-build-a-discord-music-bot/#new-autocode-project) for creating a discord music bot provided by autocode.com, and are not of my own creation.**  


### create.js  

This file contains the endpoint that connects to the youtube search and download API's to allow a discord bot to: Play a song, Stop a song, Pause a song, and Resume a song.  
Additionally, it allows a user to add songs to a queue to play later.  It works via messages displayed in the discord server that match the following formats: !play, !stop, !pause, !resume, and !queue.  The play and queue functions require input to be interpreted by the program and sent to the youtube search API.


### finished.js  

This file contains the endpoint that tells the bot what to do with songs in the queue when the previous song finishes playing.  The code provided via the tutorial is mostly correct, but assumes that the developer used the following code before assigning the queueKey, `let event = 'context.params.event';`.  As such, I changed the implementation of the line defining the queueKey to read: ``let queueKey = `${context.params.event.guild_id}:musicQueue`;``
