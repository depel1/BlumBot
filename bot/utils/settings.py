from pydantic_settings import BaseSettings, SettingsConfigDict

logo = """

██████  ██      ██    ██ ███    ███     ██████   ██████  ████████
██   ██ ██      ██    ██ ████  ████     ██   ██ ██    ██    ██   
██████  ██      ██    ██ ██ ████ ██     ██████  ██    ██    ██   
██   ██ ██      ██    ██ ██  ██  ██     ██   ██ ██    ██    ██   
██████  ███████  ██████  ██      ██     ██████   ██████     ██   
                                                                 
"""

class Settings(BaseSettings):
	model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

	API_ID: int
	API_HASH: str
	
	GAME_POINTS: list[int] = [100, 200]
	SLEEP_BETWEEN_GAME: list[int] = [10, 20]
	ERRORS_BEFORE_STOP: int = 3
	USE_PROXY_FROM_FILE: bool = False

try:
	config = Settings()
except Exception as error:
	log.error(error)
	config = False