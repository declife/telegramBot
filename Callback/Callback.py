#!/usr/bin/env python

text = "/start      the start command;\n" \
       "/google     github repo of googletest;\n" \
       "/tornado    github repo of tornado;\n" \
       "/command    my all commands"


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")


def qa(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='https://github.com/google/googletest')


def tornado(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="https://github.com/tornadoweb/tornado/\
                             tree/stable")


def command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)


def echo(update, context):
    if 'github' in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="https://github.com/explore")
    if 'hi' in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="hello, dear, I love you")
