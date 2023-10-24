from decouple import config


class Settings:
    DATABASE_HOST = config('DATABASE_HOST')
    DATABASE_NAME = config('DATABASE_NAME')
    DATABASE_USER = config('DATABASE_USER')
    DATABASE_PASSWORD = config('DATABASE_PASSWORD')
    DATABASE_PORT = config('DATABASE_PORT')


settings = Settings()
