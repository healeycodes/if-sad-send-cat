# If Sad Send Cat
> My blog post: [When I'm Sad My Computer Sends Me Cats](https://healeycodes.com/when-im-sad-my-computer-sends-me-a-cat)

If you're sad in front of your computer, this project will send a random cat to your phone. It was an evening project to glue together a few APIs.

Hopefully this prototype can be used as inspiration for your fun ideas.

## How?
- It runs locally and captures your webcam through a browser
- Emotions are tracked via [vladmandic/human](https://github.com/vladmandic/human)
- Cats are provided by The Cat API. Notifications via [Pushover](https://pushover.net/)

## Setup/Run

- Create an `.env` file with `PUSHOVER_API_KEY` and `PUSHOVER_USER_KEY` 
- `pip install -r requirements`
- `python server.py`
- Go to `http://localhost:8080`
- Be sad
- Receive cat

## Debug Log

![Side by side comparison of the debug log when I'm happy vs. when I'm sad.](https://github.com/healeycodes/if-sad-send-cat/blob/main/web/happysad.png)

## Notification

![A notification on my phone of "Marcus", a cat, who "needs my attention".](https://github.com/healeycodes/if-sad-send-cat/blob/main/web/catalert2.png)

