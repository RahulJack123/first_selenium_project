import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class Readconfig:
    @staticmethod
    def GetAppUrl():
        url = config.get('Assignment', 'baseurl')
        return url

    @staticmethod
    def GetClinicCode():
        cli_code = config.get('Assignment', 'clinic_code')
        return cli_code

    @staticmethod
    def GetUsername():
        username = config.get('Assignment', 'username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('Assignment', 'password')
        return password
