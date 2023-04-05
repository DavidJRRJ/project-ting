def exists_word(word, instance):
    instance_length = len(instance)
    count_list = []
    for index in range(instance_length):
        current_dict = instance.search(index)
        file_lines = current_dict["linhas_do_arquivo"]
        info = {"palavra": word,
                "arquivo": current_dict["nome_do_arquivo"], "ocorrencias": []}
        for line_index, line in enumerate(file_lines):
            if word.lower() in line.lower():
                info["ocorrencias"].append({"linha": line_index + 1})
    if info["ocorrencias"]:
        count_list.append(info)
    return count_list


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
