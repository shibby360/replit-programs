from keep_alive import keep_alive
import discord
import os
import time
import discord.ext
from discord.ext import commands
from discord.ext.commands import has_permissions, UserConverter
import discord
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from replit import db
import random as r
try:
  import ShdwDB
except ModuleNotFoundError:
  os.system('pip install ShdwDB')
  import ShdwDB
userDB = ShdwDB.retrieve('User stats', 'user_stats')
userDB.def_val = 0
arrows = ['➡️', '⬅️', '⬇️', '⬆️']
os.system('clear')
print(userDB)
def save_stats():
  global userDB
  userDB.save('user_stats')
  userDB = ShdwDB.retrieve('User stats', 'user_stats')
save_stats()
side = 100
def check_where(x, y):
  places = {
    'Animal grounds':{'x':side//2, 'y':0, 'width':side//2, 'height':side//2},
    'Start':{'x':0, 'y':0, 'width':side//4, 'height':side//4},
    'Forest':{'x':0, 'y':side//2, 'width':side//4, 'height':side//2},
    'Sea':{'x':side//4, 'y':0, 'width':side//4, 'height':side},
    'Vehicle grounds':{'x':0, 'y':side//4, 'width':side//4, 'height':side//4},
    'House':{'x':side//2, 'y':side//2, 'width':side//4, 'height':side//4}
  }
  for place in places:
    placer = places[place]
    xin = x in range(placer['x'], placer['width']+placer['x'])
    yin = y in range(placer['y'], placer['height']+placer['y'])
    if xin and yin:
      return place
  return 'the middle of nowhere'


async def determine_prefix(client, message):
  guild = message.guild
  if guild:
    if guild.id in db:
      return db[guild.id]
    else:
      return "a!"
  else:
    return "a!"

intents = discord.Intents(messages=True, members=True, guilds=True, reactions=True)
bot = commands.Bot(command_prefix = 'a!', intents=intents)
bot.remove_command('help')

@bot.event
async def on_ready():
  DiscordComponents(bot, change_discord_methods=True)
  print('wassup')
  print(bot.user)

@bot.command(aliases=['reset'])
async def start(ctx):
  await ctx.send('Created/Reset your profile!')
  userDB.add_column(str(ctx.author.id))
  for i in userDB.data:
    for j in userDB.data[i]:
      userDB.data[i][j] = 0
  userDB.set(str(ctx.author.id), 'health', 100)
  save_stats()

@bot.command(aliases=['a'])
async def adventure(ctx):
  await ctx.send(type=InteractionType.ChannelMessageWithSource, content="Message Here", components=[Button(style=ButtonStyle.URL, label="Example Invite Button", url="https://google.com"), Button(style=ButtonStyle.blue, label="Default Button", custom_id="button")])
  if userDB.get_value(str(ctx.author.id), 'sleeping'):
    await ctx.send('You\'re in bed getting you\'re beauty rest! Use `wakeup` to get out of that bed!')
    return
  msg = await ctx.send('React with the direction you want to go!')
  userDB.set(str(ctx.author.id), 'adv msg id', msg.id)
  for i in arrows:
    await msg.add_reaction(f'{i}')
  await msg.add_reaction('🛑')
  await msg.add_reaction('🔄')
  save_stats()


@bot.command()
async def wakeup(ctx):
  userDB.set(str(ctx.author.id), 'sleeping', False)
  await ctx.send('Wakey wakey...')
  save_stats()

@bot.command()
async def heal(ctx):
  userDB.set(str(ctx.author.id), 'health', 100)
  save_stats()

@bot.event
async def on_reaction_add(reaction, user):
  if reaction.message.id in userDB.get_row('adv msg id').values() and user != bot.user:
    for i in userDB.data.keys():
      if reaction.message.id == userDB.get_value(i, 'adv msg id'):
        x = userDB.get_value(i, 'x')
        y = userDB.get_value(i, 'y')
        t = userDB.get_value(i, 'timber')
        f = userDB.get_value(i, 'food')
        h = userDB.get_value(i, 'health')
        l = userDB.get_value(i, 'house')
        await reaction.message.edit(content='...')
        emojo = str(reaction.emoji)
        if emojo == arrows[0]:
          userDB.set(i, 'x', x+5)
        elif emojo == arrows[1]:
          userDB.set(i, 'x', x-5)
        elif emojo == arrows[2]:
          userDB.set(i, 'y', y+5)
        elif emojo == arrows[3]:
          userDB.set(i, 'y', y-5)
        elif emojo == '🛑':
          await reaction.message.channel.send('Your adventure has ended.')
          userDB.set(i, 'adv msg id', 0)
          save_stats()
          return
        if userDB.get_value(i, 'vehicling'):
          if emojo == '⬜':
            userDB.set(i, 'x', 5)
            userDB.set(i, 'y', 5)
          elif emojo == '🌲':
            userDB.set(i, 'x', 5)
            userDB.set(i, 'y', side//2+5)
          elif emojo == '🪓':
            userDB.set(i, 'x', side//2+5)
            userDB.set(i, 'y', 5)
          elif emojo == '🏠':
            userDB.set(i, 'x', side//2+5)
            userDB.set(i, 'y', side//2+5)
          await reaction.message.remove_reaction('⬜', bot.user)
          await reaction.message.remove_reaction('🌲', bot.user)
          try:
            await reaction.message.remove_reaction('🪓', bot.user)
            await reaction.message.remove_reaction('🏠', bot.user)
          except:
            pass
          userDB.set(i, 'vehicling', False)
        if userDB.get_value(i, 'in house'):
          if emojo == '🌙':
            userDB.set(i, 'sleeping', True)
            userDB.set(i, 'adv msg id', 0)
            await reaction.message.channel.send('You are sleeping, use command `wakeup` to wake up.')
            return
          elif emojo == '🥫':
            i = str(user.id)
            if f <= 0:
              await reaction.message.edit(content=reaction.message.content+'\nNot enough food!')
              return
            if h >= 100:
              await reaction.message.edit(content=reaction.message.content+'\nHealth is maxed out!')
              return
            userDB.set(i, 'food', f-1)
            userDB.set(i, 'health', h+10)
            f = userDB.get_value(i, 'food')
            h = userDB.get_value(i, 'health')
          elif emojo == '👷':
            t = userDB.get_value(i, 'timber')
            l = userDB.get_value(i, 'house')
            if t <= 0:
              await reaction.message.edit(content=reaction.message.content+'\nNot enough timber!')
            else:
              userDB.set(i, 'timber', t-30)
              userDB.set(i, 'house', l+1)
          elif emojo == '🥬':
            a = userDB.get_value(i, 'algae')
            l = userDB.get_value(i, 'house')
            if a <= 0:
              await reaction.message.edit(content=reaction.message.content+'\nNot enough algae!')
            else:
              userDB.set(i, 'algae', 0)
              userDB.set(i, 'house', l+1)
          await reaction.message.remove_reaction('🌙', bot.user)
          await reaction.message.remove_reaction('🥫', bot.user)
          userDB.set(i, 'in house', False)
        if check_where(x, y) == 'Animal grounds':
          animal = r.choice(['Bear', 'Chicken'])
          if animal == 'Bear':
            await reaction.message.edit(content=reaction.message.content+'\nYou encountered a Bear :bear:!\nIt attacked you. :axe:\n-10 :hearts:')
            userDB.set(i, 'health', h-10)
            if userDB.get_value(i, 'health') <= 0:
              await reaction.message.channel.send('You died. :skull_crossbones:')
              userDB.set(i, 'adv msg id', 0)
          elif animal == 'Chicken':
            await reaction.message.edit(content=reaction.message.content+'\nYou encountered a Chicken :chicken:!\nYou killed it! :axe:\n+1 :canned_food:')
            userDB.set(i, 'food', f+1)
            if f+1 > l:
              userDB.set(i, 'food', l)
        elif check_where(x, y) == 'Forest':
          if r.choice([0, 1]):
            await reaction.message.edit(content=reaction.message.content+'\nYou chopped down a tree. :evergreen_tree:\n+1 :wood:')
            userDB.set(i, 'timber', t+1)
        elif check_where(x, y) == 'Sea':
          await reaction.message.edit(content=reaction.message.content+'\nYou\'re swimming in the sea! :swimmer:')
          if r.choice([0,0,0,0,0,0,0,0,0,1]):
            await reaction.message.edit(content=reaction.message.content+'\nYou got some algae!')
            userDB.set(i, 'algae', 1)
        elif check_where(x, y) == 'Vehicle grounds':
          vehicle = r.choice(['car', 'plane'])
          await reaction.message.edit(content=reaction.message.content+'\nYou got a ' + vehicle + '!')
          userDB.set(i, 'vehicling', True)
          if vehicle == 'car':
            await reaction.message.edit(content=reaction.message.content+'\nWhere do you want to go with your car :red_car:? React with ⬜ for start, and react with 🌲 to go to the forest.')
            await reaction.message.add_reaction('⬜')
            await reaction.message.add_reaction('🌲')
          if vehicle == 'plane':
            await reaction.message.edit(content=reaction.message.content+'\nWhere do you want to go with your plane :airplane:? React with ⬜ for start, and react with 🌲 to go to the forest, and 🪓 to go to the Animal grounds, and 🏠 to go home.')
            await reaction.message.add_reaction('⬜')
            await reaction.message.add_reaction('🌲')
            await reaction.message.add_reaction('🪓')
            await reaction.message.add_reaction('🏠')
        elif check_where(x, y) == 'House' and l:
          userDB.set(i, 'in house', True)
          await reaction.message.edit(content=reaction.message.content+'\nYou are at your house :house:. Do you want to sleep :crescent_moon:, or eat :canned_food:, or upgrade your house :construction_worker:(Use :leafy_green: for instant upgrade)?: ')
          await reaction.message.add_reaction('🌙')
          await reaction.message.add_reaction('🥫')
          await reaction.message.add_reaction('👷')
          await reaction.message.add_reaction('🥬')
        x = userDB.get_value(i, 'x')
        y = userDB.get_value(i, 'y')
        t = userDB.get_value(i, 'timber')
        f = userDB.get_value(i, 'food')
        h = userDB.get_value(i, 'health')
        a = userDB.get_value(i, 'algae')
        await reaction.message.edit(content=reaction.message.content+'\nYou are in: ' + check_where(x, y) + '\nx: ' + str(x) + '\ny: '+ str(y) + '\nTimber :wood:: ' + str(t) + '\nFood :canned_food:: ' + str(f) + '\nHealth :hearts:: ' + str(h) + '\nHouse Level :house:: ' + str(l) + '\nAlgae :leafy_green:: ' + str(a))
  save_stats()

#Invite: https://discord.com/api/oauth2/authorize?client_id=879499387787706388&permissions=259846043712&scope=bot
keep_alive()
token = os.environ.get("bot_secret")
bot.run(token)