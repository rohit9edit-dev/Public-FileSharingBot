#    This file is part of the FileSharing distribution.
#    Copyright (c) 2022 kaif-00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in
# <https://github.com/kaif-00z/FileSharingBot/blob/main/License> .


from decouple import config
from dotenv import load_dotenv

load_dotenv()


class Var:
    STORAGE_CHANNEL = config("-1003621538224", cast=int)
    API_HASH = config("2f4aa10016925f92bc74be7336c22502", default=None)
    APP_ID = config("35136171", cast=int)
    BOT_TOKEN = config("8134715094:AAEnvaOZUWgUnPAXO77Qh8K3voEPVqOO2Gw", default=None)
    JOIN_CHAT = config("JOIN_CHAT", default=0, cast=int)

    FORCE_SUB_CHANNEL = config("-1003373869483", default=0, cast=int)

    REDIS_URI = config("REDIS_URI", default=None)
    REDIS_PASS = config("REDIS_PASSWORD", default=None)
    OWNER_ID = config("6774993771", cast=int)
