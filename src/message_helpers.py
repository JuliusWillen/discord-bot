import datetime


def message_contains(message, triggers):
    # check if message contains any of the triggers
    for trigger in triggers:
        if trigger in message:
            return True


def should_respond(message, user):
    if message.author == user:
        return False
    elif message.author.bot:
        return False
    else:
        timestamp = message.created_at
        now = datetime.datetime.now(datetime.timezone.utc)
        time_diff = (now - timestamp).total_seconds()
        if time_diff > 2:
            return False
        return True
