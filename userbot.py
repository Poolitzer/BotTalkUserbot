from telethon import TelegramClient, sync, events
from telethon.utils import get_display_name
from time import sleep
from random import choice, random, randint

import logging

logging.basicConfig(filename="log.log", level=logging.ERROR, format="%(asctime)s:%(levelname)s:%(message)s")

api_id = 123456
api_hash = 'JustSomethingkldpo'
text = 'Test'
textname = 'Nothing'
#All the commands in one list
listing = ['`Russian`', '`English`', '`Chatting`', '`Limited`', '`Intro`', '`Askright`', '`Askaway`',
           '`Blocked` (Add A for Android, I for Iphone and D for Desktop)', '`username`', '`rtfm`', '`diy`',
           '`support`', '`description`',
           '`delete` (Reply to the message of me you want to see gone - only works in the group)',
           '`Link` (Add either Ask, Limit or Info, and, if you want, text that then appears before the link)',
           '`Explain`', '`Manybot`', '`NoBots`', '`Search`']
ids = 5

client = TelegramClient('Strato', api_id, api_hash).start()

#All the users allowed to use it
users = ['me', 24421134, 584832386, 80229377, 200344026, 66085837, 336513500, 295152997, 40869593]


async def main(event, text, textname):
    if event.is_reply is True:
        message = await event.get_reply_message()
        ids = await message.reply(text)
    else:
        ids = await event.respond(text)
    if event.out is True:
        await event.delete()
    if event.is_group is True:
        user = await event.get_sender()
        await client.send_message('https://t.me/joinchat/AAAAAEnJQI4KzTVQ928u9g',
                                  '[{}](tg://user?id={}) used {}  [here](https://t.me/BotTalk/{}).'.format(
                                      get_display_name(user), user.id, textname, ids.id), link_preview=False,
                                  silent=True)


async def links(event, text, textname):
    if event.is_reply is True:
        message = await event.get_reply_message()
        expression = event.pattern_match.group(1)
        ids = await message.reply(expression + text)
    else:
        expression = event.pattern_match.group(1)
        ids = await event.respond(expression + text)
    if event.out is True:
        await event.delete()
    if event.is_group is True:
        user = await event.get_sender()
        await client.send_message('https://t.me/joinchat/AAAAAEnJQI4KzTVQ928u9g',
                                  '[{}](tg://user?id={}) used {}  [here](https://t.me/BotTalk/{}).'.format(
                                      get_display_name(user), user.id, textname, ids.id), link_preview=False,
                                  silent=True)


async def gif(event, path, textname):
    if event.is_reply is True:
        message = await event.get_reply_message()
        entity = await message.get_chat()
        ids = await client.send_file(entity, path)
    else:
        entity = await event.get_chat()
        ids = await client.send_file(entity, path)
    if event.out is True:
        await event.delete()
    if event.is_group is True:
        user = await event.get_sender()
        await client.send_message('https://t.me/joinchat/AAAAAEnJQI4KzTVQ928u9g',
                                  '[{}](tg://user?id={}) used {}  [here](https://t.me/BotTalk/{}).'.format(
                                      get_display_name(user), user.id, textname, ids.id), link_preview=False,
                                  silent=True)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Russian$',
                             chats=users + ['@BotTalk', 'https://t.me/joinchat/DG7UjhDZzDhHigAt-QjDLA']))
async def handler(event):
    text = 'Hey there. This is an english only group. Please join @botoid for a Russian one.'
    textname = '__Russian__'
    await main(event, text, textname)
    if random() < 0.10:
        entity = await event.get_chat()
        await client.send_file(entity, r'botoid.mp4')


@client.on(events.NewMessage(from_users=users, pattern='(?i)English$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Hey there. This is an english, telegram bot development related group. Please don't speak in any other " \
           "language here. "
    textname = '__English Only__'
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Chatting$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Hello. This group is about developing bots for telegram. If you just want to chat, consider joining " \
           "@publictestgroup or @snowballfight. "
    textname = '__No chatting__'
    await main(event, text, textname)
    if random() < 0.10:
        entity = await event.get_chat()
        await client.send_file(entity, r'wang.mp4')


@client.on(events.NewMessage(from_users=users, pattern='(?i)Limited$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "If you want to learn more about limits and how to avoid them, check out this awesome guide: " \
           "http://telegra.ph/So-your-bot-is-rate-limited-01-26. "
    textname = '__Your bot is limited__'
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Limited (.+)', chats=users + ['@BotTalk']))
async def handler(event):
    text = " http://telegra.ph/So-your-bot-is-rate-limited-01-26"
    textname = "__Limited Link__"
    await links(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Intro$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Hey there. Have a look at this page to get an overview about Telegram Bots and what you need for them: " \
           "http://telegra.ph/Introduction-to-bot-programming-02-21. "
    textname = "__Rico's introduction guide__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Intro (.+)', chats=users + ['@BotTalk']))
async def handler(event):
    text = " http://telegra.ph/Introduction-to-bot-programming-02-21"
    textname = "__Intro Link__"
    await links(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Askright$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Please ask your question again. We need some technical informations to be able to help you. Have a look " \
           "at this article if you are unsure what to provide (Hint: The more the better ;P): " \
           "http://telegra.ph/How-not-to-ask-technical-questions-05-10. "
    textname = "__Technical questions__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Askright (.+)', chats=users + ['@BotTalk']))
async def handler(event):
    text = " http://telegra.ph/How-not-to-ask-technical-questions-05-10"
    textname = "__Technical question Link__"
    await links(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Askaway$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Hey there. Please don't ask to ask. Just fire your question away and someone will hopefully be able to " \
           "answer it :) "
    textname = "__Don't ask to ask__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)rtfm$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Please have a look at https://core.telegram.org/bots/api, every method is explained there."
    textname = "__Read the manual. Please__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)diy$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "I'm sorry, but we won't build the bot for you. Please read the docs at least, and come back if you run " \
           "into an error or have a specific question to something, thanks. "
    textname = "__Do it yourself__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)username$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "There is no way for you to change the username of your bot. You can ask @BotSupport, but they will need " \
           "some time to answer. If you don't mind loosing users/groups, you can always create a new bot with your " \
           "desired username in @BotFather and change the token in your skript. "
    textname = "__Change username__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Blocked$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "This is a known issue with BotFather at the moment. Please block and unblock it, it will work then. If " \
           "you don't know how, tell us your device and I will send you a little How-To video. "
    textname = "__Botfather and blocked__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)BlockedI$', chats=users + ['@BotTalk']))
async def handler(event):
    path = r'IOSBlocked.MOV'
    textname = "__Botfather and IPhone__"
    await gif(event, path, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)BlockedA$', chats=users + ['@BotTalk']))
async def handler(event):
    path = r'AndroidBlocked.mp4'
    textname = "__Botfather and Android__"
    await gif(event, path, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)BlockedD$', chats=users + ['@BotTalk']))
async def handler(event):
    path = r'DesktopBlocked.mp4'
    textname = "__Botfather and Desktop__"
    await gif(event, path, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Support$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "This is not a general support group. Please ask your local support team via settings => ask a question. " \
           "Thanks :) "
    textname = "__No support here__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)LinkIntro$', chats=users + ['@BotTalk']))
async def handler(event):
    text = " http://telegra.ph/Introduction-to-bot-programming-02-21"
    textname = "__Intro Link__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)LinkAsk$', chats=users + ['@BotTalk']))
async def handler(event):
    text = " http://telegra.ph/How-not-to-ask-technical-questions-05-10"
    textname = "__Technical question Link__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)LinkLimit$', chats=users + ['@BotTalk']))
async def handler(event):
    text = " http://telegra.ph/So-your-bot-is-rate-limited-01-26"
    textname = "__Limited Link__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Description$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "This group is about developing bots for Telegram. Have a look at the description and the pinned message " \
           "to get the idea about it. "
    textname = "__Description__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Explain$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Hello. Your question/problem seems very unclear, please explain what you mean so we can help you, thanks :)"
    textname = "__explain yourself__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)manybot$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Hello there. I'm sorry to redirect you, but this group won't be able to help you with any problems " \
           "regarding manybot/chatfuelbot or any similar service. Kindly contact their support or start developing a " \
           "real telegram bot :) "
    textname = "__We no manybot__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)nobots$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Hello there. We discussed about adding bots to this chat some times already. The admins decided that they " \
           "won't do it, mainly because bots can make mistakes and they dont want to be responsible for that. Its up " \
           "to them, they made a decision, and further discussing is considered offtopic :) "
    textname = "__We no bot__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)search$', chats=users + ['@BotTalk']))
async def handler(event):
    text = "Hi. This group is not about searching bots, it's about developing new ones. We understand that this is " \
           "maybe not something you want to do. Please use google or any other search engine instead if you want to " \
           "find existing ones. There are a lot of helpful fan made sites out there which will let you find your " \
           "desired bot. "
    textname = "__We no manybot__"
    await main(event, text, textname)


@client.on(events.NewMessage(from_users=users, pattern='(?i)Delete$', chats='@BotTalk'))
async def handler(event):
    if event.is_reply is True:
        message = await event.get_reply_message()
        if message.out is True:
            await message.delete()
            user = await event.get_sender()
            if event.is_group:
                await client.send_message('https://t.me/joinchat/AAAAAEnJQI4KzTVQ928u9g',
                                          '[{}](tg://user?id={}) used Delete.'.format(get_display_name(user), user.id),
                                          link_preview=False, silent=True)
            else:
                pass
        else:
            await event.reply("Try to reply to a message from me next time, hmm?")
    else:
        await event.reply("Reply to a message with this command, thanks.")


@client.on(events.NewMessage(from_users=users, pattern='(?i)Stopbot$', chats=users + ['@BotTalk']))
async def handler(event):
    user = await event.get_sender()
    await event.reply("Bot disconnected")
    await client.send_message('https://t.me/joinchat/AAAAAEnJQI4KzTVQ928u9g',
                              'Bot disconnected by [{}](tg://user?id={}).'.format(get_display_name(user), user.id),
                              link_preview=False)
    await client.disconnect()


@client.on(events.NewMessage(chats=users, pattern='(?i)help$'))
async def helphandler(event):
    listes = ", ".join(listing)
    await event.reply(
        'Thanks for using the userbot. The available "commands" are: {}. **Stopbot** will always work and disconnect '
        'the bot, in case it runs amok. Feel free to try them out in this chat and tell me when I should add '
        'something, when I made a mistake or should rewrite a string :)'.format(listes))


@client.on(events.NewMessage(outgoing=True, pattern='jeffwish'))
async def spam(event):
    x = 0
    y = 0
    while x is not 20:
        await event.respond('/GetWellSoonJeff')
        sleep(0.5)
        x += 1
        y += 1
        if y is 4:
            sleep(2)
            y = 0
        else:
            pass


@client.on(events.NewMessage(from_users=218011713, pattern='Poolitzer'))
async def robby(event):
    numbers = randint(0, 11)
    entity = await event.get_chat()
    if numbers is 4:
        await client.send_file(entity, r'{}.mp4'.format(numbers), caption="Credits to Shai", reply_to=event.message.id)
    else:
        await client.send_file(entity, r'{}.mp4'.format(numbers), reply_to=event.message.id)


client.run_until_disconnected()