#!/usr/bin/env python
import sys

import data
import flag
import progressbar
from googletrans import Translator

googletrans_lang_code = {
    'شبكة': 'ar',
    'kr': 'ko',
    'kp': 'ko',
    'cn': 'zh-cn',
    'zh-yue': 'zh-tw',
    'et': 'am',
    'ph': 'tl',
    'gr': 'el',
    'il': 'iw',
    'gal': 'gl',
    'corsica': 'co',
    'cat': 'ca',
}


def main():
    translator = Translator()

    desired_header_text = '  '.join(data.phrases)
    default_header_text = \
        '[Please visit my English website](/en), [o visita mi sitio web en español.](/es)'
    with open('error.log', 'w') as f:
        for lang_code, lang_data in progressbar.progressbar(sorted(data.languages.items())):
            lang_name = lang_data.split(maxsplit=2)[0].replace('_', ' ')

            flag_codes = lang_data.split()[1:]
            if len(flag_codes) == 0:
                flag_codes = [lang_code]

            flag_emojis = flag.flagize(' '.join(':{}:'.format(f) for f in flag_codes))

            header_text = default_header_text
            try:
                if lang_code in googletrans_lang_code:
                    dest_lang = googletrans_lang_code[lang_code]
                else:
                    dest_lang = lang_code
                header_text = translator.translate(desired_header_text,
                                                   src='en', dest=dest_lang).text
                header_text = f"[{header_text}](/en)"
                if lang_code == 'it':
                    header_text = header_text.replace('americana', 'americano')
            except ValueError as e:
                print(f'failed to translate language={lang_code}', e, file=f)

            print(f"""  '{lang_code}':
    languageName: '{lang_name} {flag_emojis}'
    headerText: "{header_text}\"""")


if __name__ == "__main__":
    main()
