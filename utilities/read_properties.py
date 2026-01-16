import configparser


config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get("admin login info", "admin_page_url")
        return url

    @staticmethod
    def get_username():
        return config.get("admin login info", "username")

    @staticmethod
    def get_password():
        return config.get("admin login info", "password")


    @staticmethod
    def get_invalide_username():
        return config.get("admin login info", "invalide_username")