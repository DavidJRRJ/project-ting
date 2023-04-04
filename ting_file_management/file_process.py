import sys
from ting_file_management.file_management import txt_importer
from ting_file_management.queue import Queue


def process(path_file, instance: Queue):
    instance_length = len(instance)
    index = 0
    while index < instance_length:
        data_dict = instance.search(index)
        if data_dict["nome_do_arquivo"] == path_file:
            return
        index += 1
    lines_list = txt_importer(path_file)
    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines_list),
        "linhas_do_arquivo": lines_list
    }
    instance.enqueue(file_dict)
    sys.stdout.write(str(file_dict))


def remove(instance: Queue):
    if len(instance) == 0:
        return sys.stdout.write("Não há elementos\n")
    
    rm_dict = instance.dequeue()
    print(f'Arquivo {rm_dict["nome_do_arquivo"]} removido com sucesso\n')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
