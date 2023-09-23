import telebot
from telebot import types
import db
from answer_determinator import calculate_question_answer_similarity



mega_answers = [db.context_theme_1,db.context_theme_2,db.context_theme_3,db.context_theme_4,db.context_theme_5]
mega_questions = [db.question_theme_1,db.question_theme_2,db.question_theme_3,db.question_theme_4,db.question_theme_5]



token='6454153610:AAHls4ETAzsBSc7Je1CQvhuI_lJ8C-VMrrQ'
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  markup = types.InlineKeyboardMarkup(row_width=1)
  button1 = types.InlineKeyboardButton(db.rows[0].get("Themes"),callback_data='1')
  button2 = types.InlineKeyboardButton(db.rows[1].get("Themes"),callback_data='2')
  button3 = types.InlineKeyboardButton(db.rows[2].get("Themes"),callback_data='3')
  button4 = types.InlineKeyboardButton(db.rows[3].get("Themes"),callback_data='4')
  button5 = types.InlineKeyboardButton(db.rows[4].get("Themes"),callback_data='5')
  markup.add(button1,button2,button3,button4,button5)
  bot.send_message(message.chat.id,"Здраствуйте, пожайлуста выберите наиболее подходящую под ваш вопрос тему",reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
  if call.message:
    if call.data == '1':
      print(db.rows[0].get("Themes"))
      bot.send_message(call.message.chat.id,'Вы выбрали вопросы по теме: '+db.rows[0].get("Themes"))
      id = db.rows[0].get("ID_Q")
      id_helper = 0
     
      # context = все вопросы данной темы через 
     

    elif call.data == '2':
      print(db.rows[1].get("Themes"))
      bot.send_message(call.message.chat.id,'Вы выбрали вопросы по теме: '+db.rows[1].get("Themes"))
      id = db.rows[1].get("ID_Q")
      id_helper = 1
      
    elif call.data == '3':
      print(db.rows[2].get("Themes"))
      bot.send_message(call.message.chat.id,'Вы выбрали вопросы по теме: '+db.rows[2].get("Themes"))
      id = db.rows[2].get("ID_Q")
      id_helper = 2

    elif call.data == '4':
      print(db.rows[3].get("Themes"))
      bot.send_message(call.message.chat.id,'Вы выбрали вопросы по теме: '+db.rows[3].get("Themes"))
      id = db.rows[3].get("ID_Q")
      id_helper = 3

    elif call.data == '5':
      print(db.rows[4].get("Themes"))
      bot.send_message(call.message.chat.id,'Вы выбрали вопросы по теме: '+db.rows[4].get("Themes"))
      id = db.rows[4].get("ID_Q")
      id_helper = 4
    bot.send_message(call.message.chat.id,'Пожайлуста задайте свой вопрос')
    @bot.message_handler(content_types='text')
    def pesik(message):
      innerindex = 0
      outerindex = 0
      bot.send_message(message.chat.id,"Пожалуйста немного подождите, ИИ обрабатывает ваш вопрос..." )
      for question2 in mega_questions[id_helper]:
        
        print(calculate_question_answer_similarity(message.text,question2))
        if calculate_question_answer_similarity(message.text,question2) > 75.0:
            print(question2)
            bot.send_message(message.chat.id,mega_answers[id_helper][mega_answers.index(question2)])
            break
        else:
          bot.send_message(message.chat.id,"К сожалению не удалось ответить на указанный вопрос. Пожалуйста сформулируйте вопрос более точно.")
          break
bot.infinity_polling()

