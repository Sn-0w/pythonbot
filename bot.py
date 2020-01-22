@client.command(pass_context = True)
async def dm(ctx, member : discord.Member = None, *, message):
    if not ctx.message.author.server_permissions.administrator:
        return
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to DM!")
if member == "@everyone":
    for server_member in ctx.message.server.members:
        await client.send_message(server_member, message)
    else:
        await client.send_message(member, message)
