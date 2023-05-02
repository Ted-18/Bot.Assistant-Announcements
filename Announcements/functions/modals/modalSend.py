import contextlib
import re
import requests


import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()

class Send(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(
                discord.ui.InputText(
                    label="Title",
                    placeholder="Title of the announcement",
                    style=discord.InputTextStyle.short,
                    max_length=256,
                    required=True
                )
            )
        
        self.add_item(
                discord.ui.InputText(
                    label="Description",
                    placeholder="Description of the announcement",
                    style=discord.InputTextStyle.long,
                    max_length=2048,
                    required=True
                )
            )
        
        self.add_item(
            discord.ui.InputText(
                label="Image URL",
                placeholder="URL of the image",
                style=discord.InputTextStyle.long,
                max_length=2048,
                required=False
            )
        )

        self.add_item(
                discord.ui.InputText(
                    label="Add Everyone?",
                    placeholder="True or False",
                    style=discord.InputTextStyle.short,
                    max_length=256,
                    required=True
                )
            )
    
    async def callback(self, interaction: discord.Interaction):


        if self.children[2].value != "":

            self.isImageURL = True
            

            # Verify if the URL is a valid image URL
            pattern = re.compile("(?:http\:|https\:)?\/\/.*\.(?:png|jpg)")
            
            if not pattern.match(self.children[2].value):
                self.isImageURL = False
        

            # Verify if the URL is a valid URL
            urlCheck = requests
            
            try:
                urlCheck = requests.get(self.children[2].value)
            except:
                urlCheck.status_code = 404


            if urlCheck.status_code == 404:
                self.isImageURL = False
                
        else:
            self.isImageURL = "None"



        # Verify if children[3] is "True" or "False" ignoring case
        patern = re.compile(r"true|false", re.IGNORECASE)

        if not patern.match(self.children[3].value):
            self.children[3].value = "False"



        with contextlib.suppress(discord.HTTPException):
            await interaction.response.send_message()
