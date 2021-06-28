from telethon import *
import random
import logging
from .. import loader, utils
import asyncio

logger = logging.getLogger(__name__)



class YourMod(loader.Module):
    """Description for module"""  # Translateable due to @loader.tds
    strings = {"name": "cw"}



   
    async def scwcmd(self,event):
        await event.delete()
        
        
        
     

        await event.respond("🕹 Действия")
        await asyncio.sleep(1)  
        await event.respond("👮 Патрулируем")

        await asyncio.sleep(666)  

        await event.respond("🕹 Действия")
        await asyncio.sleep(1)  
        await event.respond("👮 Патрулируем")

        await asyncio.sleep(666)
          
        await event.respond("🕹 Действия")
        await asyncio.sleep(1)  
        await event.respond("👮 Патрулируем")
        
