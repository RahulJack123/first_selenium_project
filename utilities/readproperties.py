import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURl():
        url = config.get('Default', 'baseURl')
        return url

    @staticmethod
    def getUserMail():
        username = config.get('Default', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('Default', 'password')
        return password
