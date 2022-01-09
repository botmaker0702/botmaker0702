from telethon.sync import TelegramClient
from telethon.sessions import StringSession 
from pyrogram import Client 
import telethon.utils

LEGEND_PIC = "https://te.legra.ph/file/4cd4fe720a6bd77481158.jpg"
okbro = input("Enter y or yes continue: ")

if okbro == "y" or "yes":
  print("Choose String Type \n1.Telethon\n2.Pyrogram")
  library = input("\nYour Choice: " )
  if library == "1":
    print("Welcome To Telethon String Generator")
    APP_ID = int(input("Enter APP ID - "))
    API_HASH = input("Enter API HASH - ")
    try:
      with TelegramClient(StringSession(), APP_ID, API_HASH) as bot:
      string_session = bot.session.save()
      bot.send_file("me", LEGEND_PIC, caption=f"`{string_session}`\n\n• __Dont Share String Session With Anyone__\n• __Dont Invite Anyone To Heroku__")
    except Exception as e:
      print(f"{e}")
  elif library == "2":
    print("Welcome To Pyrogram String Session\n")
    APP_ID = int(input("\nEnter Ur APP ID ~: "))
    API_HASH = input("\nEnter Ur API_HASH ~: ")
    try:
      with Client(':memory:', api_id=APP_ID, api_hash=API_HASH) as boy:
        sweetie = boy.export_session_string()
        print("Successfully Pyrogram String Session Has Been Generated \nCheck Ur Saved Message \nIf U Terminate Sessions Then U Have To Generate Gain\nDont Try To Share STRING SESSION with Anyone")
        boy.send_message("me", f"Pyrogram String Session\n\n`{sweetie}`")
    except Exception as e:
      print(f"{e}")
  else:
    print("\nSale Bhsdk Ab Fir Se Start karo & \nChoose 1 For Userbot \nChoose 2 For Pyrogram \n Pahle Run karo fir se Tab 1 ya 2 Koi Ek Select Karna")
