from aiogram.dispatcher.filters import Filter
from create import dp, bot, Dispatcher
from aiogram import types
from telebot import types
import random
import time

total = 150
complication = 0
Botcheat = total - total % 29  


def quantity(message: types.Message):  

    message = int(message)            
    return message





def bot_turn(complication, Botcheat, userCandy):
    global total

    if(complication == 1):
        if(total > Botcheat):
            quantity = total - Botcheat
            return quantity
    
        quantity = 29 - userCandy 

        if(total - quantity < 0):
            quantity = total
            return quantity

    if(complication == 0):
        if(total - quantity < 0):
            quantity = total
            return quantity
        quantity = random.randint(1, 29)
        return quantity



@dp.message_handler(commands=["start","help"])
def welcome(message):
    bot.send_sticker(message.chat.id, sticker='CAACAgEAAxkBAAEE7PVinlWeyx-ZvITlp3KUK4qYG3xnMwACHQAD7cC4MzLG9N5Bwj6GJAQ')
    time.sleep(1)
    bot.send_message(message.chat.id, text='Ох, ёмаё, напугал 😅')
    time.sleep(2)
    bot.send_message(message.chat.id, text='Привет! Я бот Сергей, буду играть с тобой в конфеты 😁')

    main_menu = types.InlineKeyboardMarkup()
    main_menu.row_wigth = 1
    main_menu.add(types.InlineKeyboardButton(text='\U00002728 Главное меню', callback_data='main_menu'))


    
    bot.send_message(message.chat.id, text=' \U0001F4DC Главное меню' + ' ' + message.from_user.first_name, reply_markup=main_menu)


@dp.callback_query_handler(lambda call: True) #проверка на получение callback-ов
def query_handler(call):
    global total 
    global complication

    if call.data == 'main_menu':
        main_menu = types.InlineKeyboardMarkup()
        main_menu.row_width = 1
        main_menu.add(types.InlineKeyboardButton(text = '\🍬 Выбрать банк конфет', callback_data='number_of_candies'))
        main_menu.add(types.InlineKeyboardButton(text = '\😎 Выбрать сложность', callback_data='complication'))
        main_menu.add(types.InlineKeyboardButton(text = '\😎 Начать', callback_data='game'))

        bot.send_message(call.message.chat.id, text=' \U0001F4DC Дневник' + call.from_user.first_name + '\U0001F499', reply_markup=main_menu)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup= None) #убираем кнопки
        bot.answer_callback_query(call.id, text='') #ответ на callback

    elif call.data == 'number_of_candies':

        number_of_candies_menu = types.InlineKeyboardMarkup()
        number_of_candies_menu.add(types.InlineKeyboardButton(text='50', callback_data='Candy_50')) 
        number_of_candies_menu.add(types.InlineKeyboardButton(text='100', callback_data='Candy_100')) 
        number_of_candies_menu.add(types.InlineKeyboardButton(text='150', callback_data='Candy_150')) 
        number_of_candies_menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='main_menu'))

        bot.send_message(call.message.chat.id, text='Предметы', reply_markup=number_of_candies_menu)
        bot.edit_message_reply_markup(call.message.chat.id, reply_markup = None) #Удаление кнопок после ответа
        bot.answer_callback_query(call.id, text='')

    elif call.data == 'Candy_50':
        total = 50
        Candy_50_menu = types.InlineKeyboardMarkup()
        Candy_50_menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='main_menu'))
        bot.send_message(call.message.chat.id, '🏦 банк конфет 50', reply_markup=Candy_50_menu)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup= None) #удаление кнопок после ответа
        bot.answer_callback_query(call.id, text='')

    elif call.data == 'Candy_100': 
        total = 100
        Candy_100_menu = types.InlineKeyboardMarkup()
        Candy_100_menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='main_menu'))
        bot.send_message(call.message.chat.id, '🏦 банк конфет 100', reply_markup=Candy_100_menu)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup= None) #удаление кнопок после ответа
        bot.answer_callback_query(call.id, text='')

    elif call.data == 'Candy_150':
        total = 150
        Candy_150_menu = types.InlineKeyboardMarkup()
        Candy_150_menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='main_menu'))
        bot.send_message(call.message.chat.id, '🏦 банк конфет 150', reply_markup=Candy_150_menu)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup= None) #удаление кнопок после ответа
        bot.answer_callback_query(call.id, text='')

    elif call.data == 'complication':

        complication_menu = types.InlineKeyboardMarkup()
        complication_menu.add(types.InlineKeyboardButton(text='Обычный 🙂', callback_data='complication_normal')) 
        complication_menu.add(types.InlineKeyboardButton(text='Невозможный ☠', callback_data='complication_hard')) 
        complication_menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='main_menu'))

        bot.send_message(call.message.chat.id, text='Предметы', reply_markup=complication_menu)
        bot.edit_message_reply_markup(call.message.chat.id, reply_markup = None) #Удаление кнопок после ответа
        bot.answer_callback_query(call.id, text='')

    elif call.data == 'complication_normal':

        complication = 0

        complication_normal_menu = types.InlineKeyboardMarkup()
        complication_normal_menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='main_menu'))

        bot.send_message(call.message.chat.id, text='Предметы', reply_markup=complication_normal_menu)
        bot.edit_message_reply_markup(call.message.chat.id, reply_markup = None) #Удаление кнопок после ответа
        bot.answer_callback_query(call.id, text='')

    elif call.data == 'complication_hard':

        complication = 1
        
        complication_hard_menu = types.InlineKeyboardMarkup()
        complication_hard_menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='main_menu'))

        bot.send_message(call.message.chat.id, text='Предметы', reply_markup=complication_hard_menu)
        bot.edit_message_reply_markup(call.message.chat.id, reply_markup = None) #Удаление кнопок после ответа
        bot.answer_callback_query(call.id, text='')

    elif call.data == 'game':
        
        bot.send_message(call.message.chat.id, text=f'Банк конфет: {total}')
        bot.send_message(call.message.chat.id, text='Вы можете взять не менее 1 конфеты и не более 28')
        bot.send_message(call.message.chat.id, text='Игра начинается!')


        bot.send_message(call.message.chat.id, text=f'Ход {call.message.from_user.first_name}')
        bot.send_message(call.message.chat.id, text='Введите количество конфет которое забираете, через "/set"')


        @dp.message_handler(commands=['set'])
        async def mes_start(message: types.Message):
            count = int(message.text.split()[1])
            return count
            
        total = total - mes_start()
            
        bot.send_message(call.message.chat.id, text=f'Осталось конфет {total}')
        
        if(total == 0 or total < 0):
            bot.send_message(call.message.chat.id, text=f'Победил {call.message.from_user.first_name}')
            next()
        bot.send_message(call.message.chat.id, text=f'Осталось конфет {total}')



        bot.send_message(call.message.chat.id, text=f'Ход Сергея')

        total = total - bot_turn(complication, Botcheat, mes_start())
        
        if(total == 0 or total < 0):
            bot.send_message(call.message.chat.id, text=f'Победил Сергей')
            next()

        bot.send_message(call.message.chat.id, text=f'Осталось конфет {total}')

                

        
        complication_hard_menu = types.InlineKeyboardMarkup()
        complication_hard_menu.add(types.InlineKeyboardButton(text='\U0001F519 Назад', callback_data='main_menu'))

        bot.send_message(call.message.chat.id, text='Предметы', reply_markup=complication_hard_menu)
        bot.edit_message_reply_markup(call.message.chat.id, reply_markup = None) #Удаление кнопок после ответа
        bot.answer_callback_query(call.id, text='')




@dp.message_handler(text=['Бла', 'Ква', 'бла'])
async def mes_start(message: types.Message):
    global complication
    global total
    await message.answer(f'Бла бла бла')
    


@dp.message_handler()
async def mes_start(message: types.Message):
    global total
    if message.text.isdigit():
        total -= int(message.text)
        await message.answer(f'На столе осталось {total} конфет')
