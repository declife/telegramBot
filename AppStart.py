#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import logging
from telegram.ext import Updater
from Callback.Register import register_handler

# REQUEST_KWARGS = {
#     # "USERNAME:PASSWORD@" is optional, if you need authentication:
#     'proxy_url': 'http://127.0.0.1:7890/',
# }


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
    updater = Updater(token='1114865886:AAGvoN6GZoykqzVQNrG7NjiUhNrs1HC9Igg',
                      use_context=True)
                      # use_context=True,
                      # request_kwargs=REQUEST_KWARGS)
    register_handler(updater)
    updater.start_polling(timeout=5)


if __name__ == '__main__':
    main()
