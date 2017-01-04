Wiktionary Bot
======================

A telegram bot that fetches word definitions from English Wiktionary.

Uses [Telepot](http://telepot.readthedocs.io/en/latest/) and
[WiktionaryParser](https://github.com/Suyash458/WiktionaryParser)

Was initially intended to only look up Russian words, but adding full lookup was simple.

Use it like this:
```/define <word> <language>```

Some wiktionary entries are very long, so it will provide a link if the entry exceeds Telegram's
character limit.  
