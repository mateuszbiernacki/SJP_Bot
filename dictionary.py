import requests
import re


def define_word(word):
    r = requests.get(f'https://sjp.pl/{word}')
    html_document = r.text
    html_definitions = re.findall('<p style="margin: .5em 0; font: medium/1.4 sans-serif; max-width: 32em; ">.*</p>',
                                  html_document)
    def_string = ""

    for definition in html_definitions:
        definition = re.sub('<p style="margin: .5em 0; font: medium/1.4 sans-serif; max-width: 32em; ">', "",
                            definition)
        definition = re.sub('</p>', "", definition)
        definition = re.sub('<br />', "\n", definition)
        def_string += definition + '\n'

    return def_string


if __name__ == '__main__':
    print(define_word(input()))
