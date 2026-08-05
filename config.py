from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 0))
        self.API_HASH = getenv("API_HASH")

        self.BOT_TOKEN = getenv("BOT_TOKEN")
        self.MONGO_URL = getenv("MONGO_URL")

        self.LOGGER_ID = int(getenv("LOGGER_ID", 0))
        self.OWNER_ID = list(map(int, getenv("OWNER_ID", "").split(",")))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))
        self.STICKER_ID = getenv("STICKER_ID", "")
        self.SESSION1 = getenv("SESSION", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Alfabots_update")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Alfabots_support")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/ynwsxi.png")
        self.START_IMG = getenv("START_IMG", "").split()
        # Video shown when the bot starts / responds to /start. Set START_VIDEO
        # in your .env to a direct video URL (or file_id). If empty, falls
        # back to START_IMG photo, then plain text.
        self.START_VIDEO = getenv("START_VIDEO", "").split()

        # ------------------------------------------------------------------
        # Premium custom emoji icons — one per button, hardcoded here.
        # No .env involved: just edit the ID string for the key you want
        # to change. Same fallback placeholder ID everywhere until you
        # replace them with real premium emoji document_ids.
        # Bot owner account needs an active Telegram Premium subscription,
        # otherwise Telegram drops the icon and buttons show plain text.
        # ------------------------------------------------------------------
        self.PREMIUM_EMOJI_IDS = {
            "autoplay":        "5249019346512008974",
            "help_back":       "5253911945622332753",
            "help_close":      "5255831443816327915",
            "help_admins":     "5255772095958229697",
            "help_auth":       "5253647062104287098",
            "help_blist":      "5253864872780769235",
            "help_lang":       "5253775593295588000",
            "help_ping":       "5253780051471642059",
            "help_play":       "5256166227927115475",
            "help_queue":      "5255934767844567828",
            "help_stats":      "5256160369591723706",
            "help_sudo":       "5253836448687204081",
            "lang_select":     "6088942523852525046",
            "ping":            "5253780051471642059",
            "play_queued":     "5256166227927115475",
            "queue_toggle":    "5253877736207821121",
            "add_me":          "5253651477330667400",
            "help_open":       "5255741073409452371",
            "support":         "5256113064821926998",
            "channel":         "5253884483601442590",
            "source_menu":     "5255977030322760582",
            "language_menu":   "5999317873623831250",
            "source_owner":    "6091676373615644521",
            "source_dev":      "6089403360958484139",
            "source_code":     "6089087685157196246",
            "source_question": "6089344700295155014",
            "source_back":     "5253911945622332753",
            "source_close":    "5253911945622332753",
            "yt_copy":         "6089218316587503561",
            "yt_open":         "6089218316587503561",
        }

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
