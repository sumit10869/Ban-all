#Github.com/mrinvisible7

import os
from .. import bot as Invix
from telethon import events, Button

#from ethon.mystarts import start_srb
    
S = '/' + 's' + 't' + 'a' + 'r' + 't'

@Invix.on(events.callbackquery.CallbackQuery(data="set"))
async def sett(event):    
    Invix = event.client
    button = await event.get_message()
    msg = await button.get_reply_message()
    await event.delete()
    async with Invix.conversation(event.chat_id) as conv: 
        xx = await conv.send_message("𝗦𝗲𝗻𝗱 𝗺𝗲 𝗮𝗻𝘆 𝗶𝗺𝗮𝗴𝗲 𝗳𝗼𝗿 𝘁𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹.")
        x = await conv.get_reply()
        if not x.media:
            xx.edit("No media found.")
        mime = x.file.mime_type
        if 'png' not in mime and 'jpg' not in mime and 'jpeg' not in mime:
            return await xx.edit("No image found.")
        await xx.delete()
        t = await event.client.send_message(event.chat_id, 'Trying.')
        path = await event.client.download_media(x.media)
        if os.path.exists(f'{event.sender_id}.jpg'):
            os.remove(f'{event.sender_id}.jpg')
        os.rename(path, f'./{event.sender_id}.jpg')
        await t.edit("𝗧𝗲𝗺𝗽𝗼𝗿𝗮𝗿𝘆 𝘁𝗵𝘂𝗺𝗯𝗻𝗮𝗶𝗹 𝘀𝗮𝘃𝗲𝗱!")
        
@Invix.on(events.callbackquery.CallbackQuery(data="rem"))
async def remt(event):  
    Invix = event.client            
    await event.edit('Trying.')
    try:
        os.remove(f'{event.sender_id}.jpg')
        await event.edit('Removed!')
    except Exception:
        await event.edit("No thumbnail saved.")                        
  
@Invix.on(events.NewMessage(incoming=True, pattern=f"{S}"))
async def start(event):
    text = "👋 𝗛𝗶, 𝗜 𝗮𝗺 '𝐏𝐫𝐢𝐯𝐚𝐭𝐞 𝐕𝐢𝐝𝐞𝐨 𝐒𝐚𝐯𝐞 𝐁𝐨𝐭 🖲️.\n\n♔**𝗢𝘄𝗻𝗲𝗿:** [MR SATYAM](tg://openmessage?user_id=6090912349) \n☏**𝗦𝘂𝗽𝗽𝗼𝗿𝘁:**[CLICK](https://t.me/s_r_c_help_bot)"
    #await start_srb(event, text)
    '''
    await event.reply(text, 
                      buttons=[
                              [Button.inline("𝗦𝗘𝗧 𝗧𝗛𝗨𝗠𝗕.", data="set"),
                               Button.inline("𝗥𝗘𝗠 𝗧𝗛𝗨𝗠𝗕.", data="rem")],        
                              ])                             
    '''                          
    
    await event.reply(text, 
                      buttons=[
                              [Button.inline("✮ 𝗦𝗘𝗧 𝗧𝗛𝗨𝗠𝗕 ✮", data="set"),
                               Button.inline("✮ 𝗥𝗘𝗠 𝗧𝗛𝗨𝗠𝗕 ✮", data="rem")],
                              [Button.url("☠ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗱 𝗕𝘆 ☠", url="tg://openmessage?user_id=6090912349")]])
    
    
