from typing import Optional, Dict, List

import fire
import sys
import xmltodict


def get_xml_from_pipe():
    if sys.stdin.isatty():
        raise ValueError("No input provided via pipe")
    return sys.stdin.read()


def get_h_str(level: int):
    return "#" * (level + 1)


def print_item(items: List[Dict]):
    for item in items:
        print(f'{get_h_str(int(item["@INDENT"]))} {item["@NAME"]}')
        print("Not read yet.")
        if item.get("ITEM"):
            print_item(item["ITEM"])


def get_md(xml: Optional[str] = None):
    if xml is None:
        xml = get_xml_from_pipe()

    data_dict = xmltodict.parse(xml)

    print_item(data_dict["BOOKMARKS"]["ITEM"])


def main():
    fire.Fire(get_md)


if __name__ == '__main__':
    main()
