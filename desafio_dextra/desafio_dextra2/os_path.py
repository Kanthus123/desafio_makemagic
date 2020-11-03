import os.path

def configuracao_path():
    config_path = os.path.abspath(
        os.path.join(os.sep, os.path.abspath(os.path.dirname(__file__)), 'configuracao',
                     '.databaseconfig.json'))
    return config_path

