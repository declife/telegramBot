#!/usr/bin/env python
import binascii
import json

text = "/start      the start command;\n" \
       "/google     github repo of googletest;\n" \
       "/tornado    github repo of tornado;\n" \
       "/command    my all commands"

number2hex = {'0': 0, '1': 1, '2': 2, '3': 3,
              '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'a': 10, 'b': 11,
              'c': 12, 'd': 13, 'e': 14, 'f': 15
              }


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
    if '\\' in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=decode(update.message.text))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=encode(update.message.text))


def encode(context):
    return str(context.encode('unicode-escape')).replace('\'', '').replace('b', '').replace('\\\\', '\\')


def decode(context):
    i = 0
    xt = bytearray((len(context)))
    for item in context:
        xt[i] = int.from_bytes(bytes(item, 'utf-8'), byteorder='big', signed=True)
        i += 1

    return xt.decode('unicode-escape')
