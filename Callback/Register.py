#!/usr/bin/env python
from telegram.ext import CommandHandler, MessageHandler, Filters

from Callback.Callback import start, qa, tornado, command, echo


def register_handler(updater):
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    qa_handler = CommandHandler('google', qa)
    tornado_handler = CommandHandler('tornado', tornado)
    command_handler = CommandHandler('command', command)
    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(qa_handler)
    dispatcher.add_handler(tornado_handler)
    dispatcher.add_handler(command_handler)
    dispatcher.add_handler(echo_handler)

