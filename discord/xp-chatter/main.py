from keep_alive import keep_alive
import discord
import os
import time
import asyncio
import discord.ext
from discord.ext import commands
from discord.ext.commands import has_permissions, UserConverter
from replit import db
import random as r
userDB = db['user_stats']
os.system('clear')
print(userDB)
resetting = False

converter = UserConverter()
def save_db():
  db['user_stats'] = userDB
save_db()
def get_keyof(val, dict):
  for key, value in dict.items():
    if val == value:
      return key
async def determine_prefix(client, message):
  guild = message.guild
  if guild:
    if guild.id in db:
      return db[guild.id]
    else:
      return "^"
  else:
    return "^"

intents = discord.Intents(messages=True, members=True, guilds=True, reactions=True)
bot = commands.Bot(command_prefix = determine_prefix, intents=intents)
bot.remove_command('help')
ptom = {'Dog':1, 'Cat':2, 'Parrot':3}
ptod = {'Dog':50, 'Cat':100, 'Parrot':150}
wtom = {'Hands':1, 'Axe':2, 'Sword':3}
lpc = 0
leaderboard_ = None
pgs = []


def profile(user):
  pers = userDB[str(user.id)]
  return discord.Embed(
    title='Profile',
    description=pers['Status'],
    color=discord.Color.purple()
  ).add_field(name='XP', value=pers['XP']
  ).add_field(name='Weapon', value=pers['Weapon']
  ).add_field(name='Weapon Level', value=pers['Weapon Lvl']
  ).add_field(name='Weapons', value=', '.join(pers['Weapons'])
  ).add_field(name='Pet', value=pers['Pet']
  ).add_field(name='Pets', value=', '.join(pers['Pets'])
  ).add_field(name='Multiplier', value=pers['Multiplier']
  ).set_author(name=user.display_name, icon_url=user.avatar_url
  ).set_thumbnail(url=user.avatar_url
  )

def embed(title, description, color=discord.Color.purple()):
  #.set_author(name=name of author, icon_url=pfp link, url=author name link)
  #.set_thumbnail(url=image link)
  #.add_field(name=title of field, value=body text of field, inline=field inline or not(bool))
  #.set_footer(text=footer text)
  return discord.Embed(title=title, description=description, color=color)

def butembed(descrip):
  return embed('But...', descrip)
def errorembed(descrip):
  return embed('Error', descrip, discord.Color.red())

@bot.event
async def on_ready():
  statuses = [discord.Activity(type=discord.ActivityType.listening, name='^help'), discord.Game(name='as an AI against users'), discord.Activity(type=discord.ActivityType.watching, name=str(len(bot.guilds)) + ' servers!')]
  print("I'm in")
  print(bot.user)
  await bot.change_presence(activity=r.choice(statuses))

@bot.event
async def on_guild_join(guild):
  xpchannel = bot.get_channel(863885647244427277)
  await xpchannel.send('I have been added to the ' + str(guild) + ' guild.')
  await xpchannel.send('Guild ID: ' + str(guild.id))
  db[guild.id] = '^'
  channelto = guild.channels[0]
  for i in range(1, len(guild.channels)+1):
    if isinstance(channelto, discord.channel.CategoryChannel):
      channelto = guild.channels[i]
  await channelto.send(embed=discord.Embed(title='Hello!', url='', description='The prefix for this server is {0}. Use `{0}help` for help on this bot. I have created a profile for everyone in this server.'.format(db[guild.id]), color=discord.Color.green()))
  for mem in guild.members:
    if mem.id not in userDB.keys():
      userDB[str(mem.id)] = {
        'XP':0,
        'Weapon':'Hands',
        'Weapon Lvl':1,
        'Weapons':['Hands'],
        'Status':'',
        'Pet':'Dog',
        'Pets':['Dog'],
        'Multiplier':1,
        'Daily Collected':False,
        'Stopped':False,
        'Wins':0
      }
  save_db()


@bot.event
async def on_command_error(ctx, error):
  if 'KeyError' in str(error):
    if 'KeyError: {0}'.format(ctx.author.id) in str(error):
      await ctx.send(embed=errorembed('You don\'t have a profile yet! Use `^start` to create one.'))
    else:
      await ctx.send(embed=errorembed('User does not have a profile yet!!'))
  elif 'You are on cooldown' in str(error):
    await ctx.send(embed=embed('Coooooooldown...', f'You\'re on cooldown! Try again in {round(error.retry_after)} seconds', color=discord.Color.blue()))
  else:
    msg = await ctx.send(embed=errorembed(str(error)))
    await asyncio.sleep(5)
    await msg.delete()
    print(error)



@bot.event
async def on_message(message):
  if str(message.author.id) not in userDB:
    userDB[str(message.author.id)] = {
      'XP':0,
      'Weapon':'Hands',
      'Weapon Lvl':1,
      'Weapons':['Hands'],
      'Status':'',
      'Pet':'Dog',
      'Pets':['Dog'],
      'Multiplier':1,
      'Daily Collected':False,
      'Stopped':False,
      'Wins':0
    }
  if resetting:
    if message.content == 'Yes':
      userDB[str(message.author.id)] = {
        'XP':0,
        'Weapon':'Hands',
        'Weapon Lvl':1,
        'Weapons':['Hands'],
        'Status':'',
        'Pet':'Dog',
        'Pets':['Dog'],
        'Multiplier':1,
        'Daily Collected':False,
        'Stopped':False,
        'Wins':0
      }
      await message.channel.send('You profile has been reset {0}!'.format(message.author.mention))
    elif message.content == 'No':
      await message.channel.send('You profle was not reset.')
  elif bot.user in message.mentions:
    await message.channel.send(embed=discord.Embed(title='Hello!', url='', description='The prefix for this serber is {0}. Use `{0}help` for help on this bot. This bot\'s website is: https://xp-chatter.shivankchhaya.repl.co.'.format(db[message.guild.id]), color=discord.Color.green()))
  elif str(message.author.id) in userDB and not(userDB[str(message.author.id)]['Stopped']):
    userDB[str(message.author.id)]['XP'] += len(message.content.split(' '))*userDB[str(message.author.id)]['Multiplier']
    if userDB[str(message.author.id)]['XP'] >= 150:
      userDB[str(message.author.id)]['XP'] %= 150
      userDB[str(message.author.id)]['Weapon Lvl'] += 1
  if isinstance(message.channel, discord.channel.DMChannel) and message.author != bot.user:
    me = await bot.fetch_user(718537197959250063)
    await me.send(str(message.author) + ' said ' + message.content + '\nUser ID: ' + str(message.author.id))
  save_db()
  await bot.process_commands(message)

@bot.event
async def on_message_edit(before, after):
  await bot.process_commands(after)

@bot.event
async def on_reaction_add(reaction, user):
  global lpc
  if reaction.message == leaderboard_ and user != bot.user:
    if reaction.emoji == '➡️':
      lpc += 1
      if lpc >= len(pgs):
        lpc = len(pgs) - 1
    elif reaction.emoji == '⬅️':
      lpc -= 1
      if lpc <= 0:
        lpc = 0
    await leaderboard_.edit(embed=embed('Leaderboard by Weapon Level', ''.join(pgs[lpc])))

@bot.command(name='help')
async def helpme(ctx, command=None):
  if command == None:
    await ctx.send(embed=discord.Embed(title='Help', description='Command prefix: {0}'.format(db[ctx.guild.id]), color=discord.Color.purple()).add_field(name='`start`', value='Make a profile for yourself.').add_field(name='`prof`', value='View your profile.').add_field(name='`rem`', value='Remove amount XP from user. This is only abailable to Administrators.').add_field(name='`feedback` aka fdbk', value='Give some feedback or suggest something.(Or dm the bot to do the same thing)').add_field(name='`leader`', value='Show the global leaderboard by levels.').add_field(name='`fight`', value='Fight another user for XP. The fighting is done by the bot(Letting you fight someone who is offline).').add_field(name='`roll`', value='Roll a dice to get or lose some XP.').add_field(name='`daily`', value='Collect your daily reward. This is only abailable after 12:00 PM in PST time.').add_field(name='`shop`', value='Show the shop.').add_field(name='`buy`', value='Buy something from the shop.').add_field(name='`change_weapon`', value='Change your current weapon.').add_field(name='`prefix`', value='Set a custom prefix for your server.').add_field(name='`reset`', value='Reset your profile.').add_field(name='`change_bot_status`', value='Change the bot\'s status').add_field(name='`status`', value='Change you own status').add_field(name='`getStatus`', value='Get a status. Specify category as game or discord. Default is game. If category is game, get a status for the game. If category is discord, get a status for discord.'))
  else:
    pass

@bot.command()
async def prof(ctx, *user):
  if user == ():
    user = ctx.author
  else:
    user = ' '.join(user)
    user = await converter.convert(ctx, user)
  await ctx.send(embed=profile(user))
  save_db()

@bot.command()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def rem(ctx, user=None, amount=None):
  if user == None:
    if amount == None:
      await ctx.send(embed=embed('`^rem`', 'rem *user amount*\nRemove amount XP from user. This is only available to Administrators.'))
    else:
      await ctx.send(embed=butembed('Where\'s the amount?'))
  else:
    user = await converter.convert(ctx, user)
    amount = int(amount)
    await ctx.send('Subtracted XP!')
    userDB[str(user.id)]['XP'] -= amount
    if userDB[str(ctx.author.id)]['XP'] < 0:
      userDB[str(ctx.author.id)]['XP'] = abs(userDB[str(ctx.author.id)]['XP'] + 150)
      userDB[str(ctx.author.id)]['Weapon Lvl'] -= amount // 150
  save_db()  

@bot.command()
async def give(ctx, user=None, amount=None):
  if user == None:
    if amount == None:
      await ctx.send(embed=embed('`^give`', 'give *user amount*\nGive amount xp to user.'))
    else:
      await ctx.send(embed=butembed('Where\'s the amount?'))
  else:
    user = await converter.convert(ctx, user)
    amount = int(amount)
    await ctx.send('Gave XP!')
    userDB[str(user.id)]['XP'] += amount
    if userDB[str(user.id)]['XP'] >= 150:
      userDB[str(user.id)]['XP'] %= 150
      userDB[str(user.id)]['Weapon Lvl'] += 1
    userDB[str(ctx.author.id)]['XP'] -= amount
    if userDB[str(ctx.author.id)]['XP'] < 0:
      userDB[str(ctx.author.id)] = abs(userDB[str(ctx.author.id)]['XP'] + 150)
      userDB[str(ctx.author.id)]['Weapon Lvl'] -= amount // 150
  save_db()

@bot.command(aliases=['fdbk'])
async def feedback(ctx, info):
  me = await bot.fetch_user(718537197959250063)
  await me.send(str(ctx.author) + ' from ' + str(ctx.guild) + ' said ' + info + '\nUser ID: ' + ctx.author.id)

@bot.command()
async def leader(ctx, by=None):
  bye = ''
  if str(by).lower() == 'weapon level':
    bye = 'Weapon Lvl'
  elif str(by).lower() == 'wins':
    bye = 'Wins'
  else:
    await ctx.send(embed=embed('`^leader`', 'leader *by*\nShow the global leader by either Weapon Level or Wins.'))
  global leaderboard_
  global pgs
  global lpc
  lpc = 0
  players = {}
  for i in userDB:
    players[i] = userDB[i][bye]
  player_ids = list(players.keys())
  player_lvs = list(players.values())
  player_lvs.sort()
  alls = []
  for j in range(1, len(player_ids)+1):
    k = player_ids[j-1]
    user = await bot.fetch_user(k)
    if j == 1:
      alls.append('🥇 ' + str(user) + ': ' + str(players[k]) + '\n')
    elif j == 2:
      alls.append('🥈 ' + str(user) + ': ' + str(players[k]) + '\n')
    elif j == 3:
      alls.append('🥉 ' + str(user) + ': ' + str(players[k]) + '\n')
    elif j == 4:
      alls.append(':four:. ' + str(user) + ': ' + str(players[k]) + '\n')
    elif j == 5:
      alls.append(':five:. ' + str(user) + ': ' + str(players[k]) + '\n')
    else:
      alls.append(str(j) + '. ' + str(user) + ': ' + str(players[k]) + '\n')
  al_l = alls[5:]
  pgs.append(alls[:5])
  listr = []
  for i in range(1, len(al_l)+1):
    if i % 10 != 0:
      listr.append(al_l[i-1])
    elif i % 10 == 0:# i % x; x is amount in each page
      listr.append(al_l[i-1])
      pgs.append(listr)
      listr = []
  if len(pgs) == 1:
    pgs.append(al_l)
  leaderboard_ = await ctx.send(embed=embed('Leaderboard by Weapon Level', ''.join(pgs[lpc])))
  await leaderboard_.add_reaction('⬅️')
  await leaderboard_.add_reaction('➡️')
  


@bot.command()
@commands.cooldown(1, 20, commands.BucketType.user)
async def fight(ctx, *user):
  if user == ():
    await ctx.send(embed=embed('`^fight`', 'fight *user*\nFight a user for XP. The fighting is done by the bot. User can either be a mention or username#tag.'))
  else:
    user = ' '.join(user)
    if '#' in user:
      for member in bot.get_all_members():
        if member.discriminator == str(user).split('#')[1]:
          user = member
    else:
      user = await converter.convert(ctx, user)
    if user.bot:
      await ctx.send(embed=butembed('Why would you be fighting a bot?'))
      return
    p1 = userDB[str(user.id)]
    p2 = userDB[str(ctx.author.id)]
    p1_health = p1['Weapon Lvl'] * 80
    p2_health = p2['Weapon Lvl'] * 80
    p1_mult = wtom[p1['Weapon']]
    p2_mult = wtom[p2['Weapon']]
    p1_inc = ptod[p1['Pet']]
    p2_inc = ptod[p2['Pet']]
    p1_weap_dmg = p1['Weapon Lvl'] * p1_mult
    p2_weap_dmg = p2['Weapon Lvl'] * p2_mult
    while p1_health > 0 and p2_health > 0:
      #P1 -> getting challenged/user
      #P2 -> challenger/ctx.author
      p1_health -= p2_weap_dmg + p2_inc
      if p1_health <= 0:
        await user.send(str(ctx.author) + ' challenged you.\nYou lost.')
        await user.send(embed=profile(ctx.author))
        await ctx.send('You win!')
        p2['XP'] += 80
        if userDB[str(ctx.author.id)]['XP'] >= 150:
          userDB[str(ctx.author.id)]['Weapon Lvl'] += 1
          userDB[str(ctx.author.id)]['XP'] %= 150
        p2['Wins'] += 1
        p1['Weapon Lvl'] -= 1
        if p1['Weapon Lvl'] <= 1:
          p1['Weapon Lvl'] = 1
        break
      p2_health -= p1_weap_dmg + p1_inc
      if p2_health <= 0:
        await user.send(str(ctx.author) + ' challenged you.\nYou Won!')
        await user.send(embed=profile(ctx.author))
        await ctx.send('You lost.')
        p1['XP'] += 80
        if userDB[str(ctx.author.id)]['XP'] >= 150:
          userDB[str(ctx.author.id)]['Weapon Lvl'] += 1
          userDB[str(ctx.author.id)]['XP'] %= 150
        p1['Wins'] += 1
        p2['Weapon Lvl'] -= 1
        if p1['Weapon Lvl'] <= 1:
          p1['Weapon Lvl'] = 1
  save_db()

@bot.command()
async def roll(ctx):
  num = r.randint(1, 6)
  change = r.choice(['gained', 'lost'])
  await ctx.send('You {0} {1} XP!'.format(change, num*20*userDB[str(ctx.author.id)]['Multiplier']))
  if change == 'gained':
    userDB[str(ctx.author.id)]['XP'] += num*20*userDB[str(ctx.author.id)]['Multiplier']
    if userDB[str(ctx.author.id)]['XP'] >= 150:
      userDB[str(ctx.author.id)]['XP'] %= 150
      userDB[str(ctx.author.id)]['Weapon Lvl'] += 1
  if change == 'lost':
    userDB[str(ctx.author.id)]['XP'] -= num*20*userDB[str(ctx.author.id)]['Multiplier']
    if userDB[str(ctx.author.id)]['XP'] < 0:
      userDB[str(ctx.author.id)]['XP'] = abs(userDB[str(ctx.author.id)]['XP'] + 150)
      userDB[str(ctx.author.id)]['Weapon Lvl'] -= num*20*userDB[str(ctx.author.id)]['Multiplier'] // 150
  save_db()

@bot.command()
async def daily(ctx):
  os.environ['TZ'] = 'US/Pacific'
  time.tzset()
  if int(time.ctime()[11:13]) >= 12:
    if not userDB[str(ctx.author.id)]['Daily Collected']:
      userDB[str(ctx.author.id)]['XP'] += 100
      await ctx.send('Collected your daily reward!')
      userDB[str(ctx.author.id)]['Daily Collected'] = True
    else:
      await ctx.send('You cannot collect your reward.')
  else:
    await ctx.send('You cannot collect your reward.')
  save_db()

@bot.command()
async def shop(ctx):
  itms = {
    'Hands':{'Cost':0, 'Bio':'Damage: Weapon Lvl x 1'},
    'Axe':{'Cost':50, 'Bio':'Damage: Weapon Lvl x 2'},
    'Sword':{'Cost':100, 'Bio':'Damage: Weapon Lvl x 3'},
    'Dog':{'Cost':0, 'Bio':'Multiplier: 1, Damage increase: 50'},
    'Cat':{'Cost':150, 'Bio':'Multiplier: 2, Damage increase: 100'},
    'Parrot':{'Cost':200, 'Bio':'Multiplier: 2, Damage increase: 150'}
  }
  for i in itms:
    for j in userDB[str(ctx.author.id)]['Weapons']:
      if i == j:
        itms[i]['Cost'] = 'Purchased'
  for i in itms:
    for j in userDB[str(ctx.author.id)]['Pets']:
      if i == j:
        itms[i]['Cost'] = 'Purchased'

  for k in itms:
    await ctx.send(
    '''
```
Item: {0}
Cost: {1}
Description: {2}```
    '''
    .format(k, itms[k]['Cost'], itms[k]['Bio'])
    )

@bot.command()
async def buy(ctx, item=None):
  itms = {
    'Hands':{'Cost':0, 'Bio':'Damage: Weapon Lvl x 1'},
    'Axe':{'Cost':50, 'Bio':'Damage: Weapon Lvl x 2'},
    'Sword':{'Cost':100, 'Bio':'Damage: Weapon Lvl x 3'},
    'Dog':{'Cost':0, 'Bio':'Multiplier: 1, Damage increase: 50'},
    'Cat':{'Cost':150, 'Bio':'Multiplier: 2, Damage increase: 100'},
    'Parrot':{'Cost':200, 'Bio':'Multiplier: 2, Damage increase: 150'}
  }
  for i in itms:
    for j in userDB[str(ctx.author.id)]['Weapons']:
      if i == j:
        itms[i]['Cost'] = 'Purchased'
  for i in itms:
    for j in userDB[str(ctx.author.id)]['Pets']:
      if i == j:
        itms[i]['Cost'] = 'Purchased'
  if item == None:
    await ctx.send(embed=embed('`^buy`', 'buy *item*\nBuy an item from the shop'))
  else:
    if item in itms:
      if itms[item]['Cost'] == 'Purchased':
        await ctx.send('You have already purchased this item!')
      else:
        await ctx.send('Successfully bought: {0}'.format(item))
        userDB[str(ctx.author.id)]['XP'] -= itms[item]['Cost']
        if userDB[str(ctx.author.id)]['XP'] < 0:
          userDB[str(ctx.author.id)] = abs(userDB[str(ctx.author.id)]['XP'] + 150)
          userDB[str(ctx.author.id)]['Weapon Lvl'] -= itms[item]['Cost'] // 150
    if item in ['Cat', 'Parrot']:
      userDB[str(ctx.author.id)]['Pets'].append(item)
    if item in ['Axe', 'Sword']:
      userDB[str(ctx.author.id)]['Weapons'].append(item)
  save_db()

@bot.command()
async def change_weapon(ctx, weapon=None):
  if weapon == None:
    await ctx.send(embed=embed('`^change_weapon`', 'change_weapon *weapon*\nChange your current weapon'))
  else:
    if weapon in userDB[str(ctx.author.id)]['Weapons']:
      userDB[str(ctx.author.id)]['Weapon'] = weapon
      await ctx.send('Changed current weapon to {0}'.format(weapon))
    else:
      await ctx.send('You don\'t have that weapon!')
  save_db()

@bot.command()
async def change_pet(ctx, pet=None):
  if pet == None:
    await ctx.send(embed=embed('`^change_pet`', 'change_pet *pet*\nChange your current pet'))
  else:
    if pet in userDB[str(ctx.author.id)]['Pets']:
      userDB[str(ctx.author.id)]['Pet'] = pet
      await ctx.send('Changed current pet to {0}'.format(pet))
      userDB[str(ctx.author.id)]['Multiplier'] = ptom[pet]
    else:
      await ctx.send('You don\'t have that pet!')
  save_db()

@bot.command()
@has_permissions(administrator=True)
async def prefix(ctx, prefix=None):
  if not isinstance(ctx.channel, discord.channel.DMChannel):
    if prefix == None:
      await ctx.send(embed=embed('`^prefix', 'preifx *prefix*\nSet a private prefix for your server'))
    else:
      db[ctx.guild.id] = prefix
      await ctx.send("Prefix set!")

@bot.command()
async def reset(ctx):
  await ctx.send('Are you sure you want to reset your entire profile? Type "Yes" for yes and "No" for no.')
  global resetting
  resetting = True

@bot.command()
async def change_bot_status(ctx):
  statuses = [discord.Activity(type=discord.ActivityType.listening, name='^help'), discord.Game(name='as an AI against users'), discord.Activity(type=discord.ActivityType.watching, name=str(len(bot.guilds)) + ' servers!')]
  await bot.change_presence(activity=r.choice(statuses))

@bot.command()
async def status(ctx, *newStatus):
  if newStatus == ():
    await ctx.send(embed=embed('`^status', 'status *status*\nChange your status to status.'))
  else:
    userDB[str(ctx.author.id)]['Status'] = ' '.join(newStatus)
    await ctx.send('Set your status!')
  save_db()

@bot.command()
async def getStatus(ctx, category='game'):
  category = category.lower()
  if category == 'game':
    custom_random = r.choice(['custom', 'random'])
    if custom_random == 'random':
      running = True
      break_Count = 0
      which = r.choice(['Weapon', 'Weapon Lvl', 'Weapons'])
      while running:
        if which == 'Weapon':
          if userDB[str(ctx.author.id)]['Weapon'] == 'Sword':
            await ctx.send('I got dem sworddddddddddddddd')
            running = False
          else:
            which = r.choice(['Weapon Lvl', 'Weapons'])
            break_Count += 1
        if which == 'Weapon Lvl':
          if userDB[str(ctx.author.id)]['Weapon Lvl'] >= 25:
            await ctx.send('Flexing my level {0} {1}.'.format(userDB[str(ctx.author.id)]['Weapon Lvl'], userDB[str(ctx.author.id)]['Weapon']))
            running = False
          else:
            which = r.choice(['Weapon', 'Weapons'])
            break_Count += 1
        if which == 'Weapons':
          if len(userDB[str(ctx.author.id)]['Weapons']) == 3:
            await ctx.send('Flexing with all dem three weapooonnns')
            running = False
          else:
            which = r.choice(['Weapon', 'Weapon Lvl'])
            break_Count += 1
        if break_Count == 4:
          await ctx.send('tryna {}'.format(r.choice(['get to lvl 25', 'get all the weapons', 'get my weapons to 25', 'get the sword', 'get da parroooot'])))
          break
    if custom_random == 'custom':
      async def f1():
        await ctx.send('grinding my {}'.format(userDB[str(ctx.author.id)]['Weapon']))
      async def f2():
        await ctx.send('Weap lvl {}, here i come!!!!!'.format(userDB[str(ctx.author.id)]['Weapon Lvl'] + 25))
      await r.choice([f1, f2])()
  if category == 'discord':
    await ctx.send('Under construction.')
  await ctx.send('Just copy and paste!!')

@bot.command()
async def stop(ctx):
  await ctx.send('You cannot earn XP anymore. Use `^unstop` to start earning XP.')
  userDB[str(ctx.author.id)]['Stopped'] = True
  save_db()
@bot.command()
async def unstop(ctx):
  await ctx.send('You can earn XP now. You `^stop` to stop earning XP.')
  userDB[str(ctx.author.id)]['Stopped'] = False
  save_db()

@bot.command()
async def invite(ctx):
  await ctx.send('Invite link: https://discord.com/api/oauth2/authorize?client_id=804197228390514799&permissions=2081422583&scope=bot\nSupport server link: https://discord.gg/KHgShhxCn2')

@bot.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def test(ctx):
  await ctx.send(
    'Devving'
  )


#Invite link: https://discord.com/api/oauth2/authorize?client_id=804197228390514799&permissions=2081422583&scope=bot
#Geo Dash world music: https://discord.com/channels/@me/722516685445267488/876234644134170685
keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
bot.run(token)