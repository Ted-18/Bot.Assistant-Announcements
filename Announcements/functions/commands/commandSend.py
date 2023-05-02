import addons.Announcements.functions.modals.modalSend as modalSend

import addons.Announcements.settings.settingColors as settingColors
import addons.Announcements.settings.settingThumbnail as settingThumbnail

import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

async def sendAnnouncement(ctx, channel):
    
    # PERMISSIONS CHECK
    import addons.Announcements.functions.services.servicePermission as servicePermission
    if await servicePermission.permissionCheck(ctx, "cmdAnnouncementSend") == False:
        return

    # COMMAND

    # Send the modal
    modal = modalSend.Send(title = "Send an announcement")
    await ctx.send_modal(modal)
    await modal.wait()

    # Get the values
    title = modal.children[0].value
    description = modal.children[1].value
    image = modal.children[2].value
    addEveryone = modal.children[3].value

    # Send the announcement
    embed = discord.Embed(
        title=title,
        description=description,
        color=settingColors.yellow
    )

    embed.set_author(name="Announcement", icon_url=settingThumbnail.loudSpeakerIcons)

    embed.set_footer(text=ctx.author.name, icon_url=ctx.author.display_avatar)

    # Verify if the URL is a valid image URL
    if modal.isImageURL == True:
        embed.set_image(url=image)
    elif modal.isImageURL == False:
        embed.set_image(url="https://i.imgur.com/GwEhbUt.png")        

    
    # Send the announcement 
    if addEveryone.lower() == "true":
        await channel.send("@everyone", embed=embed)
    else:
        await channel.send(embed=embed)

    



