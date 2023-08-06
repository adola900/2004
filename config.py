from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "26077415"))
API_HASH = getenv("API_HASH", "d38231af75187c78cf3db151b4a1eaf4")
BOT_TOKEN = getenv("BOT_TOKEN", "6178372880:AAH8X8gFewq9vUDlH12lBDoMOo-CTdAHRzU")
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1wBu332J65DzKaW2TLY2brd2INq15TnFkqG3-FHesrslyHdLQroImshVY6YEeeO7Pn1qge7bDbE71oPUCT4iDIkxfyhQ30bC0c5jXd2SpIxo9r0WceKQHtfY57puMxs6BXpO3gEfGesZgqmCDyVCyZbvmvNCjtjWja68N6-4rpaov-gId8GjjgItugCJjprjy8oi99HQMf49IjuKgfYW1KAOblmpaDPhMtVmDRWIj2ToZmJ5AD12ptsKwtRxYeQKm5hcVaBQSLyVkhJui4vHoHCMcGWtCLmxEJkUGEYXb-YF4LTJPmc0IPjS50tBl3ZunSH56YnBqU4OGexROgUQl4mE68=")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "adel_hamed_1")
ALIVE_NAME = getenv("ALIVE_NAME", "song")
BOT_USERNAME = getenv("BOT_USERNAME", "DOLA_MUSIC_BOT")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/STKR2/2004")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "d3m_dola")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "dolaadelbot")

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "1854384004").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
