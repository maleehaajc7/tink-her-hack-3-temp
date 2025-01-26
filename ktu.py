from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application,Updater,CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler
import sqlite3
# import os
# print(os.path.exists("files.db")) --to check if the file existin sme direcotory


TOKEN: Final = '7719128453:AAFFGeoHkWYc_ue9jaahojXD6QQh6O3OdNM'
BOT_USERNAME: Final = '@trialleeBot'

#commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hey dude😊! \nTired of browsing for notes let\'s make this simple for U😉. \nTo know how I work type /help ')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Follow my guidanceee❗❗ \n\n ➡️For specifying the university: SELECT /university\n➡️For notes : plz enter the course code and module number in the format: CS201 1.\n➡️For syllabus: Send the scheme and course code\n\n(PS:I need your help to help U😁🙌)')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!') 

#university

async def university_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Oh! You have come this far🥳!!\nNow SELECT your University\n\n➡️For KTU University : select /ktu\n➡️For Calicut University : select /calicut') 

#ktu univ
async def ktu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('SELECT as you wish SON!🙂‍↕️\n\n➡️For NOTES : Select /notes\n➡️For SYLLABUS : Select /syllabus') 

#calicut univ
async def calicut_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('SELECT as you wish SON!🙂‍↕️\n\n➡️For NOTES : Select /notes\n➡️For SYLLABUS : Select /syllabus')    

#ktu notes
async def notes_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Enter the course code and module number (eg:-EST102 3)')         

#ktu syllabus
async def syllabus_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Enter the scheme and course code (eg:-2019 EST102)') 


# sql

def get_notes(course_code: str, module_number: str = None) -> list:
    
    conn = sqlite3.connect("files.db")
    cursor = conn.cursor()
    
    if module_number:
       cursor.execute(
           "SELECT drive_link,description FROM Notes WHERE course_code LIKE ? AND module_number = ?",(f"%{course_code}%",module_number)
       )
        

    else:
        cursor.execute(
        "SELECT drive_link, description FROM Notes WHERE course_code LIKE ?",
        (f"%{course_code}%",)
        )    

    results = cursor.fetchall()
    conn.close()
    return results

def get_syllabus_by_scheme(scheme):
    conn = sqlite3.connect("files.db")
    cursor = conn.cursor()
    cursor.execute("SELECT drive_link, description FROM Syllabus WHERE scheme = ?", (scheme,))
    results = cursor.fetchall()
    conn.close()
    return results

def get_syllabus(scheme: str, course_code: str = None) -> str:
    
    conn = sqlite3.connect("files.db")
    cursor = conn.cursor()
    
    if course_code:
        cursor.execute(
        "SELECT drive_link, description FROM Syllabus WHERE scheme LIKE ? AND course_code = ?",
        (f"%{scheme}%", course_code)
    )
        
    else:
        cursor.execute(
        "SELECT drive_link, description FROM Syllabus WHERE scheme LIKE ?",
        (f"%{scheme}%",)
        )

    results = cursor.fetchall()
    conn.close()
    return results



#responses    


# async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     text = update.message.text.strip()
#     parts = text.split()

#     if len(parts) == 2:
#         course_code, module_number = parts
#         notes = get_notes(course_code, module_number)
#     elif len(parts) == 1:
#         course_code = parts[0]
#         notes = get_notes(course_code)
#     else:
#         await update.message.reply_text("Invalid format. Please use: CS201 1 or just CS201", parse_mode='Markdown')
#         return

#     if notes:
#         keyboard = []
#         response_text = f"📚 Notes for {course_code.upper()}:\n"
#         for i, (link, desc) in enumerate(notes, start=1):
#             response_text += f"{i}. {desc}\n"
#             keyboard.append([InlineKeyboardButton(f"Download {desc}", url=link)])

#         # Inline buttons for the download links
#         reply_markup = InlineKeyboardMarkup(keyboard)
#         await update.message.reply_text(response_text, reply_markup=reply_markup, parse_mode='Markdown')
#     else:
#         await update.message.reply_text("No notes found for the given input.")

async def handle_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    parts = text.split()

    if len(parts) == 2:
        # Check if the first part is numeric (indicating scheme)
        if parts[0].isdigit():
            scheme, course_code = parts
            syllabus = get_syllabus(scheme, course_code)
            if syllabus:
                response_text = f"📘 Syllabus for {course_code.upper()} ({scheme} scheme):\n"
                keyboard = []
                for i, (link, desc) in enumerate(syllabus, start=1):
                    response_text += f"{i}. {desc}\n"
                    keyboard.append([InlineKeyboardButton(f"Download {desc}", url=link)])
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_text(response_text, reply_markup=reply_markup, parse_mode='Markdown')
            else:
                await update.message.reply_text("No syllabus found for the given scheme and course code.")
        else:
            course_code, module_number = parts
            notes = get_notes(course_code, module_number)
            if notes:
                response_text = f"📚 Notes for {course_code.upper()}:\n"
                keyboard = []
                for i, (link, desc) in enumerate(notes, start=1):
                    response_text += f"{i}. {desc}\n"
                    keyboard.append([InlineKeyboardButton(f"Download {desc}", url=link)])
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_text(response_text, reply_markup=reply_markup, parse_mode='Markdown')
            else:
                await update.message.reply_text("No notes found for the given input.")
    elif len(parts) == 1:
        if parts[0].isdigit():  # If input is a scheme
            scheme = parts[0]
            syllabus = get_syllabus_by_scheme(scheme)
            if syllabus:
                response_text = f"📘 Syllabus for the {scheme} scheme:\n"
                keyboard = []
                for i, (link, desc) in enumerate(syllabus, start=1):
                    response_text += f"{i}. {desc}\n"
                    keyboard.append([InlineKeyboardButton(f"Download {desc}", url=link)])
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_text(response_text, reply_markup=reply_markup, parse_mode='Markdown')
            else:
                await update.message.reply_text(f"No syllabus found for the {scheme} scheme.")
        else:  # If input is a course code
            course_code = parts[0]
            notes = get_notes(course_code)
            if notes:
                response_text = f"📚 Notes for {course_code.upper()}:\n"
                keyboard = []
                for i, (link, desc) in enumerate(notes, start=1):
                    response_text += f"{i}. {desc}\n"
                    keyboard.append([InlineKeyboardButton(f"Download {desc}", url=link)])
                reply_markup = InlineKeyboardMarkup(keyboard)
                await update.message.reply_text(response_text, reply_markup=reply_markup, parse_mode='Markdown')
            else:
                await update.message.reply_text("No notes found for the given input.")
    else:
        await update.message.reply_text(
            "Invalid format. Please use:\n"
            "- CS201 1 for notes\n"
            "- 2015 CS201 for syllabus\n"
            "- 2015 for syllabus of the 2015 scheme",
            parse_mode='Markdown',
        )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #this will inform as whether its grp or prte chat
    message_type : str = update.message.chat.type

    #messge that is incoming(tht cn actully processd)
    text: str = update.message.text

    #a useful print statmnt for debugging
    print(f'User (update.message.chat.id) in {message_type}: "{text}"') # we get the user ID snding the msg

    if message_type == 'group' :
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip() #we wnt to replace the username coz we dont wnt it to b processd as part of messg(replced wth an empty strng)

            # to make sure thers mo whte spacing leading or ending we cll strip

            await handle_response(update,context)

        else:
            return

    else:
        #ths wll work for all privte chats
        await handle_response(update,context)       

    #for debugging,
    # print('Bot:', response)
    # await update.message.reply_text(response)


#used for logging errors  
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}') 

if __name__ == '__main__':

    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    #commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('university', university_command))
    app.add_handler(CommandHandler('ktu', ktu_command))
    app.add_handler(CommandHandler('calicut', calicut_command))
    app.add_handler(CommandHandler('notes', notes_command))
    app.add_handler(CommandHandler('syllabus', syllabus_command))


    #messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    
    #errors
    app.add_error_handler(error)


    #for checking constntly on updates on whethr theres a new message or smthng we hve to respond to

    print('Polling...') #so will get sme feedback in console when  run the bot so it doesnt look blnk when startd (ie; will neverknow the bot is running)
    
    app.run_polling(poll_interval = 3) #checks every 3 secnds for new msgs