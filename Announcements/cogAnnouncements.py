# ADDON IMPOTS
import addons.Announcements.init as init

import addons.Announcements.functions.commands.commandSend as commandSend
import addons.Announcements.functions.commands.commandRequirements as commandRequirements

# BOTASSISTANT IMPORTS
from services.serviceLogger import consoleLogger as Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()



class Announcements(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    # INIT GROUP COMMAND
    groupAnnouncements = discordCommands.SlashCommandGroup(init.cogName, "🔶 Group of commands for the Announcements addon.")


    # Verify if the bot has the prerequisites permissions
    @groupAnnouncements.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx)


    # SEND
    @groupAnnouncements.command(name="send", description="Send an announcement to a channel.")
    async def cmdSend(
        self,
        ctx,
        
        channel: discord.Option(discord.TextChannel, channel_types = [discord.ChannelType.news], required=True),
    ):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the send command.", str(ctx.command))
        await commandSend.sendAnnouncement(ctx, channel)

        
# INIT COG
def setup(bot):
    if debug: Logger.debug("Loading cog: " + init.cogName)
    bot.add_cog(Announcements(bot))
