# If Sad Send Cat

If you're sad in front of your computer, this project will send a cat to your phone. It was an evening project to glue together a few APIs.

## How?
- It runs locally and captures your webcam through a browser
- Emotions are tracked via [vladmandic/human](https://github.com/vladmandic/human)
- Cats are provided by The Cat API. Notifications via [Pushover](https://pushover.net/)

Hopefully this draft code can be used as inspiration for your fun ideas.

## Setup/Run

- Create an `.env` file with `PUSHOVER_API_KEY` and `PUSHOVER_USER_KEY` 
- `pip install -r requirements`
- `python server.py`
- Go to `http://localhost:8080`
- Be sad
