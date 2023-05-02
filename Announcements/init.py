# Github informations
enableGithub = True
author = "Ted-18"
repository = "Bot.Assistant-Announcements"
version = "1.1.1"

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "announcements"

# Name of the file containing the cog
cogFile = "cogAnnouncements"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python",
    "requests"
]

# List of addons required by the addon
addonDependencies = [
    "Configuration"
]

# List of permissions required by the addon
addonPermissions = [
    "send_messages"
]

commandPermissions = {
    # Permission to check the addon's permissions
    "cmdRequirements" : "discord.permission.manage_guild",

    # Permission to send an announcement
    "cmdAnnouncementSend" : "discord.permission.manage_messages"
}