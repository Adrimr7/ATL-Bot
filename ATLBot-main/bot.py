import discord

emoji = '\N{TRIDENT EMBLEM}'
emoji_puerta = '\N{DOOR}'
msg_bienvenida = f'{emoji} Bienvenido a Atlantis Legions!{emoji} '
ruta_imagenes = 'fotos/poseidon.png'
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Arrancando como {0.user}'.format(client))

@client.event
async def on_member_join(miembro):
    embed = discord.Embed(title=" ", description=f"Confiamos que disfrutarás tu estadía en nuestro servidor {miembro.mention}.",
                          color=0x5365c1)
    embed.set_author(name=f"{emoji}¡Bienvenid@ a Atlantis Legions!{emoji}")
    embed.add_field(name="Canales Importantes:", value="", inline=False)
    embed.add_field(name="· <#1056963901113253998>", value="Elige los juegos que más te interesen.", inline=True)
    embed.add_field(name="· <#1007560534062800964>", value="Habla con el resto de los Legionarios.", inline=False)
    embed.add_field(name="· <#1021678126079684621>", value="Descubre juegos crypto.", inline=False)
    embed.add_field(name="· <#1041796351362596934>", value="Entérate todo sobre el mundo crypto.", inline=False)
    #embed.set_footer(text="¡Contigo somos x Legionarios!")
    with open(ruta_imagenes, 'rb') as image:
        await miembro.send(msg_bienvenida, file=discord.File(image))
    servidor = miembro.guild
    canal = discord.utils.get(servidor.channels, name=f'「{emoji_puerta}│𝐁𝐢𝐞𝐧𝐯𝐞𝐧𝐢𝐝𝐚')
    num_personas = servidor.member_count
    if canal is not None:
        embed.set_footer(text=f"¡Contigo somos {num_personas} Legionarios!")
        embed.set_image(url = "https://media.tenor.com/AMEslNj4dDsAAAAC/atlantis.gif")
        #await canal.send(f'{miembro.mention} se ha unido al servidor! {msg_bienvenida}' f' somos {num_personas}')
        with open(ruta_imagenes, 'rb') as image:
            await canal.send(embed=embed)


client.run('TOKEN DEL BOT, NO ES ESTE')
