#!/usr/bin/env python
"""Translate and render."""

import random
from urllib.parse import quote

import data
from cache import PersistentMemoizationCache
from flag import flagize
from googletrans import Translator
from iso3166 import countries
from progressbar import ProgressBar

translator = Translator()
memo = PersistentMemoizationCache(cache_name='generate_hugo_config_yaml')
sort = True
sort_or_not = sorted if sort else (lambda x: x)

secondary_weight = 5

def main():
    """Translate and render."""
    weight = 0

    i = 0
    bar = ProgressBar(max_value=len(data.languages))

    for root, languages in data.languages_with_roots.items():
        weight += 10
        for code, lang_data in sort_or_not(languages.items()):
            bar.update(i)
            i += 1

            lang_name = lang_data.split(maxsplit=2)[0].replace('_', ' ')

            lang_weight = secondary_weight \
                if code in data.secondary_languages else weight

            flag_codes = lang_data.split()[1:]
            emoji_unneeded = any(
                flag in data.no_flag_needed for flag in flag_codes)

            if len(flag_codes) == 0:
                flag_codes = [code]
            elif len(flag_codes) == 1 and emoji_unneeded:
                flag_codes = []

            flag_emojis = \
                flagize(' '.join(
                    '<span>:{}:</span>'.format(f) for f in flag_codes),
                        subregions=True)

            custom_flags = "mx us".split()
            named = [
                (code, countries.get(''.join(code.split('-')[:1])).name)
                for code in flag_codes + custom_flags
            ]
            random.shuffle(named)
            linked_flag_emojis = \
            ' '.join([
                "[{}](https://duckduckgo.com/?q={} '{}')".format(
                    flagize(f':{code}:', subregions=True),
                    quote(name),
                    name.replace("'", "\\'")
                ) for code, name in named
            ])

            # Something about the UTF-8 encoding of the Ukrainian flag...
            flag_sep = '"' if any(c in 'ua' for c in code) else "'"

            header_text = data.default_header_text
            site_title = data.default_site_title

            if code in data.lang_code_to_googletrans_code:
                dest_lang = data.lang_code_to_googletrans_code[code]
            else:
                dest_lang = code

            if code in data.lang_with_separator:
                separator = data.lang_with_separator[code]
            else:
                separator = '  '

            try:
                if code in data.site_title_translations:
                    site_title = data.site_title_translations[code]
                else:
                    site_title = memo.call(translator.translate,
                                           data.site_title,
                                           src='en', dest=dest_lang).text
            except ValueError as e:
                with open('error.log', 'a') as f:
                    print(f'failed to translate title for {code}', e, file=f)

            try:
                if code in data.phrases_translations:
                    header_text = '{}   {}'.format(
                        separator.join(data.phrases_translations[code]),
                        data.default_header_text)
                else:
                    header_text = separator.join(
                        memo.call(translator.translate,
                                  phrase, src='en', dest=dest_lang).text
                        for phrase in data.phrases)
                    header_text = f"[{header_text}](/) " + data.default_header_text

                if code in ['it', 'corsica']:
                    header_text = header_text.replace('americana', 'americano')
                if code == 'zulu':
                    header_text = header_text.replace('Unicode', '')
                if code == 'latin':
                    header_text = header_text.replace('Mexicanus', '')\
                        .replace('-American', 'Mexicanus-American')
            except ValueError as e:
                with open('error.log', 'a') as f:
                    print(f'failed to translate language={code}', e, file=f)
                lang_weight = secondary_weight \
                    if code in data.secondary_languages else weight + 5

            print(f"""  '{code}':
    languageName: {flag_sep}{lang_name} {flag_emojis}{flag_sep}
    author: "{data.long_author}"
    title: "{site_title} ({data.short_author})"
    headerText: "{header_text} --- {data.short_author} {linked_flag_emojis}"
    weight: {lang_weight}
    disableKinds:
      - taxonomy
      - taxonomyTerm
    """)


if __name__ == "__main__":
    main()
