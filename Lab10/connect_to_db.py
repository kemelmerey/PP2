from configparser import ConfigParser
from config import config
def get_db_params(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)
    if parser.has_section(section):
        return dict(parser.items(section))
    else:
        raise Exception(f'Section {section} not found in {filename}')

params = get_db_params()
