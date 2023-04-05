def exists_word(word, instance):
    count_list = [
        info for index in range(len(instance))
        if (info := instance.search(index))
        and (file_lines := info["linhas_do_arquivo"])
        and (
            info := {
                "palavra": word,
                "arquivo": info["nome_do_arquivo"],
                "ocorrencias": [
                    {"linha": line_index + 1}
                    for line_index, line in enumerate(file_lines)
                    if word.lower() in line.lower()
                ],
            }
        )
        and info["ocorrencias"]
    ]
    return count_list


def search_by_word(word, instance):
    count_list = [
        {
            "palavra": word,
            "arquivo": instance.search(index)["nome_do_arquivo"],
            "ocorrencias": [
                {"linha": line_index + 1, "conteudo": line}
                for line_index, line in enumerate(
                    instance.search(index)["linhas_do_arquivo"]
                )
                if line.lower().count(word.lower()) > 0
            ],
        }
        for index in range(len(instance))
        if any(
            line.lower().count(word.lower()) > 0
            for line in instance.search(index)["linhas_do_arquivo"]
        )
    ]

    return count_list
