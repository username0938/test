from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot import bot,dp
from configurebot import cfg

tehchatid = cfg['teh_chat_id']
message_sended = cfg['question_ur_question_sended_message']

class FSMQuestion(StatesGroup):
	text = State()

# Обработчики
async def newquestion(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		if (message.content_type == 'photo'):
			data['text'] = message.caption
		else:
			data['text'] = message.text
	await state.finish()
	if(message.chat.username == None):
		who = "Без юзернейма"
	else:
		who = "@"+message.chat.username
	question = data['text']
	if(message.content_type=='photo'):
		ph = message.photo[0].file_id
		await message.reply(f"{message_sended}",
							parse_mode='Markdown')
		await bot.send_photo(tehchatid, ph, caption=f"✉ | Нове повідомлення\nОт: {who}\nЗміст: `{data['text']}`\n\n📝 Щоб відповісти введіть: `/відповісти {message.chat.id} текст...`",parse_mode='Markdown')
	else:
		await message.reply(f"{message_sended}",
							parse_mode='Markdown')
		await bot.send_message(tehchatid,
							   f"✉ | Нове повідомлення\nОт: {who}\nЗміст: `{data['text']}`\n\n📝 Щоб відповісти введіть: `/відповісти {message.chat.id} текст...`",
							   parse_mode='Markdown')

def register_handler_FSM():
	dp.register_message_handler(newquestion,state=FSMQuestion.text, content_types=['photo', 'text'])