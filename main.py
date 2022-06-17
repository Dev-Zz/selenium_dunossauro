import discord

client = discord.Client()


@client.event
async def on_ready():
  print('Roof! Rooof!')

@client.event
async def on_message(message):
  message.content.upper()  
  if message.author == client.user:
   return
  if message.content == 'BACANA':
    await message.channel.send('Bacana!')
  if message.content == 'quem é o bom garoto?':
    await message.channel.send('Roof! Roof!')

client.run('OTg2ODY0MTA2MjMxNDQzNDk2.GwLh5S.Hq9MsNKn_Jc848htGIlM2OSuIOseuPoR1W1Wk0')