# Preview Fixer Telegram Bot
### A telegram bot that using other projects adds dd to Instagram links, fixup to X links and fx to Twitter links.

Adding above words will fix preview links for these links. This bot will do this automatically.
This bot can be added to groups or be used in personal messages.



Source for fixup and fx:
https://github.com/FixTweet/FxTwitter

Source for ddinstagram:
https://github.com/Wikidepia/InstaFix



## Self Hosting:

In order to self host the bot. You should get a bot token from the botfather.
Then edit the `previewfixerbot.py` and replace your token inside it.
Install python-telegram-bot
`pip3 install python-telegram-bot==13.7`
Note that later versions of python-telegram-bot will probably not work with this code.


*If you want to add this bot to groups give it access to reading messages in groups from the botfather bot*
