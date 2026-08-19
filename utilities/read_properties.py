import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class read_config:
    @staticmethod
    def getURL():
        url = config.get('login info', 'url')
        return url

    @staticmethod
    def get_username():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def get_lockedOutUser():
        locked_out_user = config.get('login info', 'locked_out_user')
        return locked_out_user

    @staticmethod
    def get_invalidUser():
        invalid_user = config.get('login info', 'invalid_user')
        return invalid_user