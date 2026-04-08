from settings import settings
from logs import Logger


def main():



    Logger.info("START")

    Logger.debug(f"App name: {settings.app_name}")
    Logger.info(f"Connected to: {settings.database_url}")


    if settings.my_secret_key:
        Logger.info(" Secret key loaded successfully")



    Logger.warning("This is a sample warning")
    Logger.info("Application finished successfully")


# This is the entry point
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        Logger.critical(f" Application crashed: {e}")
        raise