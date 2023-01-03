import os
import mysql.connector
import discord
from dotenv import load_dotenv

# .ENV
load_dotenv()
ROOT_PASSWORD = os.getenv('ROOT_PASSWORD')
TOKEN = os.getenv('DISCORD_TOKEN')

# SQL DATABASE CONNECTION
socket = mysql.connector.connect(
        user='root', 
        password=ROOT_PASSWORD, 
        host='localhost', 
        database='pollo')

cursor = socket.cursor()
