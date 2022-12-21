import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5596488061:AAFeVhObca6qF9D-7sf52VT38t9cYXt35f0")
    # The Telegram API things
    API_ID = int(os.environ.get("API_ID", 16393106))
    API_HASH = os.environ.get("API_HASH", "061fbf1aff7eecf2edb8434ddbab7a7d")
    # Get these values from my.telegram.org
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 4194304000 #2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(128)
    # default thumbnail to be used in the videos
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ""
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # your telegram id
    OWNER_ID = int(os.environ.get("OWNER_ID", "5295973607"))
    SESSION_NAME = "UPLOADER-X-BOT"
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://bot1:bot1@cluster0.cuyh4kk.mongodb.net/?retryWrites=true&w=majority")
    MAX_RESULTS = "50"
    PREMIUM_USER = os.environ.get("PREMIUM_USER")
