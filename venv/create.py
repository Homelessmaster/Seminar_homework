from aiogram import Bot, Dispatcher, executor, types
import telebot


token = ''
bot = telebot.TeleBot(token)
Bot = Bot(token)

dp = Dispatcher(Bot)