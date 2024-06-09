def link_id_from_link(link: str) -> str:
    return link[32:]


def format_script(script_list: list[dict]) -> str:
    script = ""
    for i in script_list:
        script = script + i['text'] + ' '

    return script
