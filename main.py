import discord
from bot_logic import gen_pass

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

print(gen_pass(10))

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
    if message.content.startswith('$Como você está?'):
        await message.channel.send("Estou bem, obrigado por perguntar!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

client.run("MTUzNzU1MDgxNjE4ODAzOTE5OA.GLmXnC.ZB5FXnZrqAVM7D141qo9NpNxVCBYsUSmDJjX0E")
