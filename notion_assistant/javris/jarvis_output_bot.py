# jarvis output bot
from typing import List

import config
from jarvis import Jarvis
# example: links for quick access relevant at this time of day (e.g. Siri)
# auto-cleanup all other clutter messages
from notion_assistant.javris.telegram_client import TelegramClient
# example: daily agenda.
from notion_assistant.javris.temp import telegram_decorator


def telegram_command(commands: List[str]):
    if isinstance(commands, str):
        commands = [commands]

    def wrapper(func):
        # add func to registry
        for command in commands:
            JarvisOutputBot.commands[command] = func.__name__
        return func

    return wrapper


class JarvisOutputBot:
    commands = dict()

    def __init__(self, jarvis):
        # init config values: telegram token etc.

        self.jarvis = jarvis
        self.notion_client = jarvis.notion_client

        self.telegram_client = TelegramClient(config.telegram_sts_token)

    @telegram_command(['daily_diary', 'diary'])
    def get_daily_diary(self):
        # todo: replace hardcode with config sourced from notion table
        return "https://www.notion.so/lavrovs/Daily-Diary-f13e3e2a11014da7b8d875d71b9d6b20"

    @telegram_command(['daily_plans', 'plans', 'schedule'])
    def get_daily_plans(self):
        # todo: replace hardcode with config sourced from notion table
        return "https://www.notion.so/lavrovs/Daily-Plans-fbb2c8966f1c47ebb257eb2b34ba30c2"

    def run(self):
        # register telegram handlers
        # - none for now. ? Or do 'diary' and other app lookup here instead of input?

        # background processes
        # - daily agenda
        # - recommended apps

        # todo: auto-cleanup old messages / clutter

        for command, func_name in self.commands.items():
            func = self.__getattribute__(func_name)
            func = telegram_decorator(func)  # todo: rename to parse_telegram_command_decorator @akudrinskiy
            self.telegram_client.add_handler(command, func)

        # launch telegram bot
        self.telegram_client.run(blocking=False)


Jarvis.registered_plugins.append(JarvisOutputBot)
