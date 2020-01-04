#!/usr/bin/env python
"""Translate and render."""

import flag
import progressbar
from googletrans import Translator

import cache
import data


def main():
    """Translate and render."""
    translator = Translator()
    memo = cache.PersistentMemoizationCache(
        cache_name='generate_hugo_config_yaml'
    )
    sort = False
    sort_or_not = sorted if sort else (lambda x: x)

    with open('error.log', 'w') as f:
        for lang_code, lang_data in progressbar.progressbar(
                sort_or_not(data.languages.items())
        ):
            lang_name = lang_data.split(maxsplit=2)[0].replace('_', ' ')

            lang_weight = 3 if lang_code in data.secondary_languages else 4

            flag_codes = lang_data.split()[1:]
            emoji_unneeded = any(
                flag in data.no_flag_needed for flag in flag_codes)

            if len(flag_codes) == 0:
                flag_codes = [lang_code]
            elif len(flag_codes) == 1 and emoji_unneeded:
                flag_codes = []

            flag_emojis = \
                flag.flagize(' '.join(':{}:'.format(f) for f in flag_codes))

            # Something about the UTF-8 encoding of the Ukrainian flag...
            flag_sep = '"' if any(c in 'ua' for c in lang_code) else "'"

            header_text = data.default_header_text
            site_title = data.default_site_title
            try:
                if lang_code in data.lang_code_to_googletrans_code:
                    dest_lang = data.lang_code_to_googletrans_code[lang_code]
                else:
                    dest_lang = lang_code

                if lang_code in data.lang_with_separator:
                    separator = data.lang_with_separator[lang_code]
                else:
                    separator = '  '

                if lang_code in data.phrases_translations:
                    header_text = '{}\n\n{}'.format(
                        separator.join(data.phrases_translations[lang_code]),
                        data.default_header_text)
                else:
                    header_text = separator.join(
                        memo.call(translator.translate,
                                  phrase, src='en', dest=dest_lang).text
                        for phrase in data.phrases)
                    header_text = f"[{header_text}](/)"

                if lang_code in ['it', 'corsica']:
                    header_text = header_text.replace('americana', 'americano')
                if lang_code == 'zulu':
                    header_text = header_text.replace('Unicode', '')
                if lang_code == 'latin':
                    header_text = header_text.replace('Mexicanus', '')\
                        .replace('-American', 'Mexicanus-American')
            except ValueError as e:
                print(f'failed to translate language={lang_code}', e, file=f)
                lang_weight = 3 if lang_code in data.secondary_languages else 9

            try:
                if lang_code in data.site_title_translations:
                    site_title = data.site_title_translations[lang_code]
                else:
                    site_title = memo.call(translator.translate,
                                           data.site_title,
                                           src='en', dest=dest_lang).text
            except ValueError as e:
                print(f'failed to translate title for {lang_code}', e, file=f)
                lang_weight = 3 if lang_code in data.secondary_languages else 9

            print(f"""  '{lang_code}':
    languageName: {flag_sep}{lang_name} {flag_emojis}{flag_sep}
    author: "{data.long_author}"
    title: "{site_title} ({data.short_author})"
    headerText: "{header_text} --- {data.short_author}"
    weight: {lang_weight}
    disableKinds:
      - taxonomy
      - taxonomyTerm
    """)


if __name__ == "__main__":
    main()
