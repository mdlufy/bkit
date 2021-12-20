from enum import Enum



token = '2116447075:AAGaAObBa1r_XlmRMRYuW1j3nT6Ul53ZiiM'
db_file = 'database.vdb'


class States(Enum):

    S_START = "0"  # Начало нового диалога
    S_ENTER_NAME = "1" # Ввод имени
    S_ENTER_AGE = "2" # Ввод возраста