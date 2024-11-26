import time  
import logging
import random  
import json,requests  
import telebot 
from datetime import datetime 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton 
import bd 
from pytz import timezone 
 
api_key = '7548779525:AAFj9nggEywKptp3GDhm5g8CnDZwDsWRg2M'  # TOKEN ID DO SEU BOT [https://t.me/BotFather] 
chat_id = '-1002407440587'  # SEU ID #################################### 
bot = telebot.TeleBot(token=api_key) 
 
message_ids1 = True
mensage_delete1 = False
dados = True

def ALERT_GALE1(): 
        tz = timezone('America/Sao_Paulo') 
        now = datetime.now(tz) 
        h = datetime.now().hour 
        m = datetime.now().minute+1 
        s = datetime.now().second 
 
        if m > 59: 
            h += 1 
            m = 0 
 
        if h <= 9: 
            h = f'0{h}' 
        if m <= 9: 
            m = f'0{m}' 
        if s <= 9: 
            s = f'0{s}' 
        message_id = bot.send_message(chat_id=chat_id, text=f'''
        ✅ Gerando Oportunidades ''').message_id 
        message_ids1 = message_id
        mensage_delete1 = False
        return   
 
def DELET_GALE1(): 
        if bd.mensage_delete1 == True: 
            bot.delete_message(chat_id=chat_id, message_id=bd.message_ids1) 
            bd.mensage_delete1 = False 
 
while True:
    tz = timezone('America/Sao_Paulo') 
    now = datetime.now(tz) 
    h = datetime.now().hour 
    m = datetime.now().minute+4 
    s = datetime.now().second 
 
    if m > 59: 
        h += 1 
        m = 0 
 
    if h <= 9: 
        h = f'0{h}' 
    if m <= 9: 
        m = f'0{m}' 
    if s <= 9: 
        s = f'0{s}' 
    print(f'{h}:{m}:{s}') 
    #hora = datetime.datetime.now().strftime("%H:%M") 
    cores = ['💣','💣','💣','💎','💣','💣','💣','💎','💣','💣','💣','💣','💎','💣','💣','💣','💣','💣','💣','💣','💣','💎','💣','💣','💣'] 
 
    for i in range(25): 
        sample = random.sample(cores, k=25) 
        print(sample[0], sample[1], sample[2], sample[3], sample[4], sample[5], sample[6], sample[7], sample[8], sample[9], sample[10], sample[11], sample[12], sample[13], sample[14], sample[15], sample[16], sample[17], sample[18], sample[19], sample[20], sample[21], sample[22],sample[23], sample[24]) 
     
    def button_link(): 
                             
        markup = InlineKeyboardMarkup() 
 
        markup.row_width = 3 
        markup.add(InlineKeyboardButton(text=f"📲 JOGUE AQUI",url="https://mercedes-pg.fun/register?code=0130816352"))
        return markup 
    
    # Enviando mensagem com a imagem
    with open('logo.png', 'rb') as photo:
        dados = bot.send_photo(
            chat_id=chat_id, 
            photo=photo,
            caption=f''' 
✅ SINAIS GERADOS COM 97,8% DE ASSERTIVIDADE:
➡️ Aposte com 3 💣.

{random.choice(sample[0])}{random.choice(sample[1])}{random.choice(sample[2])}{random.choice(sample[3])}{random.choice(sample[4])}
{random.choice(sample[5])}{random.choice(sample[6])}{random.choice(sample[7])}{random.choice(sample[8])}{random.choice(sample[9])}
{random.choice(sample[10])}{random.choice(sample[11])}{random.choice(sample[12])}{random.choice(sample[13])}{random.choice(sample[14])}
{random.choice(sample[15])}{random.choice(sample[16])}{random.choice(sample[17])}{random.choice(sample[18])}{random.choice(sample[19])}
{random.choice(sample[20])}{random.choice(sample[21])}{random.choice(sample[22])}{random.choice(sample[23])}{random.choice(sample[24])}

🕹 Tentativas 3
🖥  Plataforma : MERCERDES-PG
💣 Minas: 3
⏰ Valido por 4 minutos
🔔 GANHE bônus de 100% no primeiro depósito!''',      
            reply_markup=button_link()
        )
    
    time.sleep(240)#240

    bot.send_message(
        chat_id=chat_id, 
        text=f'''
💎 Sinal Confirmado 💎
✅ 𝐆𝐑𝐄𝐄𝐍 ✅
⏱ Finalizado                                                    
''', 
        reply_to_message_id=dados.message_id
    )
    time.sleep(60)#60
    #ALERT_GALE1()
    time.sleep(10)#10
    #DELET_GALE1()
    time.sleep(50)#50
