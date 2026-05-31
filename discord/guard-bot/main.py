import discord
from keep_alive import keep_alive
import os
import discord.ext
from discord.ext import commands
from discord.ext.commands import has_permissions
from replit import db

async def determine_prefix(client, message):
	guild = message.guild
	if guild:
		if guild.id in db:
			return db[guild.id]['prefix']
		else:
			return ":"
	else:
		return ":"
    
intents = discord.Intents(messages=True, members=True, guilds=True, reactions=True)    
bot = commands.Bot(command_prefix=determine_prefix, intents=intents)
bot.remove_command('help')
os.system('clear')

@bot.event
async def on_ready():
  print('Im in')
  print(bot.user)

@bot.event
async def on_message(message):
  await bot.process_commands(message)
  if message.guild != discord.channel.DMChannel and message.author != bot.user:
    msgupper = 0
    for letter in message.content:
      if letter.isupper():
        msgupper += 1
    if msgupper == 15 and db[message.guild.id]['Caps Ban']:
      await message.author.send('You used too many caps in your message!')
      await message.delete()
    if db[message.guild.id]['Cuss Ban']:
      words = eval(os.getenv('words'))
      for word in words:
        if word in message.content.lower():
          await message.author.ban()
    if db[message.guild.id]['Links to ban'] and ':start' not in message.content:
      for link in db[message.guild.id]['Links to ban']:
        if link in message.content:
          await message.delete()
          await message.channel.send('Those links are not allowed in this server!')

@bot.event
async def on_command_error(ctx, error):
  await ctx.send(error)

@bot.event
async def on_raw_reaction_add(reaction):
  if reaction.message_id == 718537197959250063:
    roletoadd = discord.utils.get(reaction.member.guild.roles, id=800922768995909702)
    await reaction.member.add_roles(roletoadd)


@bot.command()
async def help(ctx, command=False):
  if not command:
    helper = discord.Embed(title='Help', color=discord.Color.gold(), description='Command prefix: {}'.format(db[ctx.guild.id]['prefix'])).add_field(name='`start`', value='Create your server rulebook.').add_field(name='`bancaps`', value='If a user uses too many caps in their message, delete their message and warn them.').add_field(name='`bancuss`', value='If a user cusses in their message, ban them.').add_field(name='`unbancaps`', value='Disable the caps feature.').add_field(name='`unbancuss`', value='Disable the cuss feature.').add_field(name='`suggest`', value='Suggest a feature.')
  await ctx.send(embed=helper)

@bot.command()
async def start(ctx):
  db[ctx.guild.id] = {'Caps Ban':True, 'Cuss Ban':True, 'prefix':':', 'Links Ban':True, 'Links to ban':[]}
  await ctx.send('Created your server rulebook!')

@bot.command()
@has_permissions(administrator=True)
async def bancaps(ctx):
  val = db[ctx.guild.id]
  val['Caps Ban'] = True
  db[ctx.guild.id] = val
  await ctx.send('Banned Capsers!')

@bot.command()
@has_permissions(administrator=True)
async def bancuss(ctx):
  val = db[ctx.guild.id]
  val['Cuss Ban'] = True
  db[ctx.guild.id] = val
  await ctx.send('Banned bad words!')

@bot.command()
@has_permissions(administrator=True)
async def prefix(ctx, prefix):
  val = db[ctx.guild.id]
  val['prefix'] = prefix
  db[ctx.guild.id] = val
  await ctx.send('Changed prefix!')

@bot.command()
@has_permissions(administrator=True)
async def unbancaps(ctx):
  val = db[ctx.guild.id]
  val['Caps Ban'] = False
  db[ctx.guild.id] = val
  await ctx.send('Unbanned Capsers!')

@bot.command()
@has_permissions(administrator=True)
async def unbancuss(ctx):
  val = db[ctx.guild.id]
  val['Cuss Ban'] = False
  db[ctx.guild.id] = val
  await ctx.send('Unbanned bad words!')

@bot.command()
@has_permissions(administrator=True)
async def banlinks(ctx, *links):
  val = db[ctx.guild.id]
  val['Links to ban'] = list(links)
  db[ctx.guild.id] = val
  await ctx.send('Banned given links!')

@bot.command()
@has_permissions(administrator=True)
async def unbanlinks(ctx, *links):
  val = db[ctx.guild.id]
  for i in val['Links to ban']:
    if i in links:
      val['Links to ban'].remove(i)
  db[ctx.guild.id] = val
  await ctx.send('Unbanned given links!')

@bot.command()
async def suggest(ctx, stuff):
  await ctx.send('Sent your feedback!')
  await (await bot.fetch_user(718537197959250063)).send(f'{ctx.author} from {ctx.guild} said {stuff}')

@bot.command()
async def view(ctx):
  await ctx.send(db[ctx.guild.id])

@bot.command()
async def delete(ctx):
  del db[ctx.guild.id]
  await ctx.send('Deleted your server rulebook.')
  
keep_alive()
bot.run(os.getenv('token'))

#invite link: https://discord.com/api/oauth2/authorize?client_id=817132940860456970&permissions=8&scope=bot