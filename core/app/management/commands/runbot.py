from django.core.management.base import BaseCommand

import asyncio
import logging

from app.bot.main import bot

class Command(BaseCommand):
    help = "Запуск бота"

    def handle(self, *args, **options):
        try:
            asyncio.run(bot.polling(non_stop=True))
        except Exception as err:
            logging.error(f'Error: {err}')