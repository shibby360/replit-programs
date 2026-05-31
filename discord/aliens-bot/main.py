import os
import discord
from keep_alive import keep_alive
from replit import db

client = discord.Client()
noprefix = False
megasim = False
megasim_looping = False
megasim_box_send = True
user_started = False
channel_in = False

@client.event
async def on_ready():
  print("I'm in")
  print(client.user)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='~help'))
  msg = await client.get_guild(721060618672537630).get_channel(800937328549429248).fetch_message(800938203182923817)
  await msg.add_reaction(client.get_emoji(806371741702160425))

@client.event
async def on_message(message):
  bot_team = [client.get_user(718537197959250063)]
  if message.author != client.user:
    global noprefix
    global megasim
    global megasim_looping
    global megasim_box_send
    global user_started
    global channel_in
    if noprefix and user_started == message.author and channel_in == message.channel:
      if megasim:
        if not(megasim_looping):
          global r
          import random as r
          global counter
          global brawlers_achieved
          counter = 20
          megasim_looping = True
          brawlers_achieved = ''
        else:
          usernum = message.content
          if usernum == 'x':
            counter = 0
            megasim_box_send = False
            ctxt = ''
            rrtycol = 0
          elif usernum.isnumeric():
            usernum = int(usernum)
            counter -= 1
            megasim_box_send = True
          else:
            megasim_box_send = False
          if megasim_box_send:
            rrs = ['Rosa', 'El Primo', 'Barley', 'Poco']
            suprrs = ['Carl', 'Penny', 'Rico', 'Darryl', 'Jacky']
            epics = ['Piper', 'Frank', 'Nani', 'Pam', 'Bea', 'Bibi', 'Gale', 'Surge', 'Edgar']
            mythics = ['Max', 'Tara', 'Mortis', 'Gene', 'Mr. P', 'Sprout', 'Colette', 'Byron']
            legends = ['Crow', 'Spike', 'Sandy', 'Leon', 'Lou', 'Amber']
            realnum = r.randint(1, 5)
            if usernum == realnum:
              chances = r.randint(1, 15)
              if chances <= 5:
                ctxt = r.choice(rrs)
                rrtycol = discord.Color.green()
              elif chances > 5 and chances <= 9:
                ctxt = r.choice(suprrs)
                rrtycol = discord.Color.blue()
              elif chances > 9 and chances <= 12:
                ctxt = r.choice(epics)
                rrtycol = discord.Color.purple()
              elif chances < 12 and chances <= 14:
                ctxt = r.choice(mythics)
                rrtycol = discord.Color.red()
              elif chances == 15:
                ctxt = r.choice(legends)
                rrtycol = discord.Color.gold()
              brawlers_achieved += ctxt + ', '
            else:
              ctxt = 'NOTHING'
              rrtycol = discord.Color.dark_gold()
            await message.channel.send(embed=discord.Embed(title='Box results', description='You got: ' + ctxt, color=rrtycol).set_footer(text=str(counter) + ' more Mega boxes').set_thumbnail(url='https://aliens-bot-urler.shivankchhaya.repl.co/'+ctxt.replace(' ', '_')+'_Skin-Default.png').set_author(name=message.author.display_name+"'s boxes", icon_url=message.author.avatar_url))
          if counter <= 0:
            listed = list(brawlers_achieved)
            listed[-1] = ''
            listed[-2] = ''
            brawlers_achieved = ''.join(listed)
            megasim = False
            noprefix = False
            megasim_looping = False
            if brawlers_achieved != []:
              await message.channel.send(embed=discord.Embed(title='End results', description='You got: ' + brawlers_achieved))
            else:
              await message.channel.send(embed=discord.Embed(title='End results', description='You got: Coins and power points'))
    else:
      prefix = db[message.guild.id]
      lenpre = len(prefix)
      embedcol = discord.Color.green()
      user = message.author.display_name
      if prefix in message.content:
        cmd = message.content.strip(prefix)
        cmdname = cmd[:cmd.find(' ')]
        if cmd.startswith('backwards') or cmd.startswith('bkwds'):
          await message.channel.send(message.content[(lenpre+len(cmdname)+1):][::-1])
        elif cmd.startswith('me'):
          dude = client.user
          embedder = discord.Embed(title='My stuff', color=embedcol)
          embedder.set_author(name=dude.display_name, icon_url=dude.avatar_url)
          embedder.set_thumbnail(url=dude.avatar_url)
          embedder.add_field(name='Name', value=dude.display_name, inline=True)
          embedder.add_field(name='Tag', value=dude.discriminator, inline=True)
          await message.channel.send(embed = embedder)
        elif cmd.startswith('happy'):
          await message.channel.send(':smile:')
        elif cmd.startswith('sad'):
          await message.channel.send(':frowning:')
        #FIX UP HELP!!!!
        elif cmd.startswith('help'):
          helppage = discord.Embed(title='Help', color=embedcol)
          helppage.add_field(name='`backwards`', value='bruh')
          await message.channel.send(embed = helppage)#.set_footer(text='This is not the correct version'))
          await message.channel.send('The help page is currently in development. Sorry for the inconvenience.')
        elif cmd.startswith('echo'):
          await message.channel.send(message.content[lenpre+5:])
        elif cmd.startswith('spam'):
          if message.guild.id not in [437048931827056642]:
            for i in range(int(message.content[-3:])):
              await message.channel.send(message.content[lenpre+5:-4])
          else:
            await message.channel.send('Disabled in this server')
        elif cmd.startswith('greet'):
          await message.channel.send('Hello ' + str(user) + '!')
        elif cmd.startswith('invite'):
          await message.channel.send(embed = discord.Embed(title='Invite links', url='', description='Bot link: https://discord.com/api/oauth2/authorize?client_id=751646225002135662&permissions=1544027255&scope=bot\nServer invite link: https://discord.gg/mU2mrFFuKb', color=embedcol))
        elif cmd.startswith('scream'):
          await message.channel.send(message.content[lenpre+6:].upper())
        elif cmd.startswith('countdown') or cmd.startswith('ctdwn'):
          import time
          count = int(cmd[lenpre+len(cmdname)+1:lenpre+len(cmdname)+5])
          for i in range(count, 0, -1):
            await message.channel.send(str(i))
            time.sleep(1)
          await message.channel.send('Done!')
        elif cmd.startswith('gimme meme'):
          import random as r
          num = r.randint(0, 3)
          file = discord.File("weird pics/weird pic({0}).jpeg".format(num), filename="weird pic({0}).jpeg".format(num))
          await message.channel.send(file=file)
        elif cmd.startswith('prefix'):
          if not isinstance(message.channel, discord.channel.DMChannel):
            for role in message.author.roles:
              if role.permissions.value in [2146959359, 66568]:
                can_do = True
              else:
                can_do = False
            if can_do: 
              db[message.guild.id] = message.content[lenpre+7:]
              await message.channel.send("Prefix set to \"{0}\"!".format(message.content[lenpre+7:]))
            else:
              await message.channel.send('You do not have the rights to do this.')
        elif cmd.startswith('dm'):
          await message.author.send('Hello!')
        elif cmd.startswith('my stuff'):
          message.mentions.append(message.author)
          if len(cmd) > 8:
            dude = message.mentions[0]
          else:
            dude = message.author
          embedder = discord.Embed(title='User\'s stuff', color=embedcol)
          embedder.set_author(name=dude.display_name, icon_url=dude.avatar_url)
          embedder.set_thumbnail(url=dude.avatar_url)
          embedder.add_field(name='Name', value=dude.display_name, inline=True)
          embedder.add_field(name='Tag', value=dude.discriminator, inline=True)
          await message.channel.send(embed = embedder)
        elif cmd.startswith('time'):
          import time
          await message.channel.send(time.ctime(time.time()))
        elif cmd.startswith('brawl stars box sim') or cmd.startswith('BSBS'):
          counter = 20
          noprefix = True
          megasim = True
          user_started = message.author
          channel_in = message.channel
          await message.channel.send(embed=discord.Embed(title='Box Sim', description='Send numbers 1 - 5 or x to quit.').set_thumbnail(url='https://aliens-bot-urler.shivankchhaya.repl.co/mega%20box.jpg'))
        elif cmd.startswith('suggest'):
          for user in bot_team:
            await client.get_user(user.id).send(str(message.author) + ' from ' + str(message.guild) + ' said ' + message.content[lenpre+8:] + '\nUser ID: ' + str(message.author.id))
        elif cmd.startswith('BOOM'):
          await message.channel.send('Nukeing...')
          messages_in_channel = await message.channel.history(limit=None).flatten()
          for msg in messages_in_channel:
            await msg.delete()
          await message.channel.send('NUKED\nhttps://aliens-bot-flies.shivankchhaya.repl.co/xplsn.gif')
        elif cmd.startswith('eval'):
          try:
            exec(message.content[lenpre+5:])
          except Exception as e:
            await message.channel.send(e)
          else:
            await message.channel.send('No errors!')
        elif cmd.startswith('my roles'):
          print(message.author.roles)
          for role in message.author.roles:
            print(role.permissions.value)
        elif cmd.startswith('emojify'):
          txt = cmd[8:]
          newtext = []
          for i in txt:
            if i == ' ':
              newtext.append(' ')
              continue
            newtext.append(':regional_indicator_{0}:'.format(i))
          await message.channel.send(''.join(newtext))
        elif cmd.startswith('searchup'):
          await message.content.send(
            'https://www.google.com/search?q={0}&rlz=1CAJIKU_enUS913US915&oq={0}&aqs=chrome..69i57j0i433j0j0i131i433j69i60.1462j0j7&sourceid=chrome&ie=UTF-8&safe=active&ssui=on'.format(cmd[9:].replace(' ', '+'))
          )
        else:
          await message.channel.send(embed=discord.Embed(title='Error', url='', description='No command found: ' + cmd, color=discord.Color.red()))
      elif client.user in message.mentions:
        await message.channel.send(embed=discord.Embed(title='Hello!', url='', description='The prefix for this server is {0}. Use `{0}help` for help on this bot.'.format(db[message.guild.id]), color=discord.Color.green()))

@client.event
async def on_guild_join(guild):
  await client.get_guild(721060618672537630).get_channel(800922027577835572).send('I have been added to the ' + str(guild) + ' guild.')
  db[guild.id] = '~'
  await guild.channels[0].send(embed=discord.Embed(title='Hello!', url='', description='The prefix for this server is {0}. Use `{0}help` for help on this bot.'.format(db[guild.id]), color=discord.Color.green()))
@client.event
async def on_guild_remove(guild):
  await client.get_guild(721060618672537630).get_channel(800922027577835572).send('I have left/been kicked from the ' + str(guild) + ' guild.')
  del db[guild.id]
@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.channel == client.get_guild(721060618672537630).get_channel(800937328549429248) and str(reaction.emoji.id) == '806371741702160425':
    role = discord.utils.get(reaction.message.guild.roles, name="norm")
    await user.add_roles(role)
@client.event
async def on_dbl_vote(data):
  print(data)

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)