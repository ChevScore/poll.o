import os
import mysql.connector
import discord
from dotenv import load_dotenv

class Pollo:
    def __init__(self):
        """ Load enviroment variables """
        load_dotenv()
        self.ROOT_PASSWORD = os.getenv('ROOT_PASSWORD')
        self.TOKEN = os.getenv('DISCORD_TOKEN')

    def _connect_database(self):
        """ Connects to the local MySQL Database """
        self.socket = mysql.connector.connect(
                user='root',
                password=self.ROOT_PASSWORD,
                host='localhost',
                database='pollo')

        self.cursor = socket.cursor

    def _check_database_sanity(self):
        pass

    def _load_poll_history(self):
        pass

    def get_guild(self):
        pass

    def run(self):
        self._connect_database()
        self._load_poll_history()
        self._check_database_sanity()
