Toast Chest Alexa Skill
=======================

Introduction
------------
This repository contains the source code for an AWS Lambda Function for an Alexa Skill that requests a drinking/dinner toast from a database and reads it aloud. The database of toasts is hosted with my personal website at http://www.mikeverdicchio.me/chest.



Setting up Alexa Skill
----------------------
To create the Alexa skill, you'll need the [interaction model](source/interaction_model.json), which contains the intents required. Feel free to edit the utterances as you'd like.

Keep note of your Application ID!



Building Deployment Package for AWS Lambda
------------------------------------------
* Python3.6
* python3.6-venv

```
make
```

You will also have to set two environment variables in your Lambda function:
* APPLICATION_ID = your skill ID (from above)
* API_ENDPOINT = http://18.218.74.144/chest/random.json



License
-------
The material in this repository is released under a GNU General Public License v2.0.

Copyright (c) 2018.