import sys


def txt_importer(path_file):
    if not path_file.endswith('.txt'):
        print('Formato inválido', file=sys.stderr)
        return []

    try:
        with open(path_file, 'r') as file:
            content = file.read()
            lines = content.split('\n')
            return lines
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
        return []
