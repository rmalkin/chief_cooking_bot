import telebot

bot = telebot.TeleBot('')

from telebot import types

first_recipe = ["������ � ������� � ��������. ������� ���� �������� ���������� ���������. ��� ����������, ������� ������� �� ������ �����. � �������� � ������� ���� �������� ������������ �����. ����, ��� � �������. �����������, �������� (0,5 �.�. ����), ��������� �� ����� � ��������� �� ���������� ������. ������� ��������� �����. �������� � �������� � ������ � ������."]

second_recipe = ["������ � ������� � �������. ������� ������ � �������� � ��������� �����. ���������� ���� � ������ ������ ����� �� 10 ��������. ���� �� �������� ���� � ��������. ����� ����� ������� ��� ��������� ����� ������� ����, �������� � �� ��� 10 ����� ������������ � ����, ����� � ����� ������� ��������. ������� ������ �� 180 �������� � ����, ���� �����������. ��������� �������� ����� ������� ������������, � ������ - ������� ��������. ����� �����, � ��� �������� ������������ �����. ���� ����� ���������, �� ��� � ��������� ������ ������ ���������� ��������� ������ ����� �����. �������� � ����� ��� � ������, ������ ������ � ����� � ������������, ����������� ���������� �����������. ����������� ������ ��������� �����. � ���������� ������� ������ ���� ����� �� ������ �� 1 ���. ����� �� 20 �� ������ ����� ������ ������, ����� �������� ������� ���������� �������."]

third_recipe = ["������ � ������� � ��������. ������ ����������� �� �������� ����, ���� � ������, �������� �� ����� ������. ��� �������� ����������� �����, �������� �������� ���������. � ��������� �� ���� ���� �������� ����������� ������������ �����. ������ � ��������� ������� ������ � ���������� �� �� ���� ������. ������ ���������� � ���� ���, �������� � ������. ����������, ���������, � ������� 7-8 �����. ����� ����������, ��������� ��� �������� ����� � ��������� � ���������. ������������ � ������� ������ � ����. ������������ ����� � ������� � ������� �� ���������. �������� � ������ ������� ���� ���, ����� ��� ��������� ��������� ����������. ���������� �������� � �������������� ���������� ������� �� 40 �����. �� 10 ����� �� ����� ������������� ������ � ������ �������� �� ������ ����� ���������� �����."]

recipies = [first_recipe, second_recipe, third_recipe]

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "������":

        bot.send_message(message.from_user.id, "������! ������ �� ������ � ����� ���������� ������� � �������� ��� �� ��������� � ���� ������������.")

        keyboard = types.InlineKeyboardMarkup()

        key_chicken = types.InlineKeyboardButton(text='������', callback_data='chicken')

        keyboard.add(key_chicken)

        key_buckwheat = types.InlineKeyboardButton(text='������', callback_data='buckwheat')

        keyboard.add(key_buckwheat)

        key_carrot = types.InlineKeyboardButton(text='�������', callback_data='carrot')

        keyboard.add(key_carrot)

        bot.send_message(message.from_user.id, text='������ ��������, ������� � ���� ���� � ������������', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "������ ������")

    else:

        bot.send_message(message.from_user.id, "� ���� �� �������. ������ /help.")

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    if call.data == 'chicken':

        bot.send_message(call.message.chat.id, first_recipe)

    if call.data == 'buckwheat':

        bot.send_message(call.message.chat.id, second_recipe)

    if call.data == 'carrot':

        bot.send_message(call.message.chat.id, third_recipe)

bot.polling(none_stop=True, interval=0)