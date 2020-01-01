"""Pure data."""

site_title = "Hugo says hello"
default_site_title = "Hugo Omar Rivera Calzadillas"
site_subtitle = "(Hugo O. Rivera)"

phrases = [
  "Welcome, dear guest!",
  "I am a Mexican-American programmer and artist.",
  "I do not speak or write your language, but I wish to learn.",
  "Please visit the English version or the Spanish version of my website.",
  "Thank you for reading.",
  "Blessings to you. I wish you find many interesting websites on your online journey."
]

phrases_translations = {
  'eo': [
      # Google Translate
      'Bonvenon, kara gasto!',
      'Mi estas meksik-usona programisto kaj artisto.',
      'Mi ne parolas aŭ skribas vian lingvon, sed mi deziras lerni.',
      'Bonvolu viziti la anglan version aŭ la hispanan version de mia retejo.',
      'Dankon pro legado.',
      'Benojn al vi.',
      'Mi deziras, ke vi trovos multajn interesajn retejojn en via interreta vojaĝo.'
  ],
  'lfn': [
      'TODO'
  ],
  'jbo': [
      'TODO'
  ],
}

# Maps domain name (TLD) to language name, and optionally a list of ISO 3166 country codes
# ? or X indicates no need for flag emoji

# TODO generate flags based on wikipedia data
#       (based on number of people that speak the language)
languages_with_roots = {
  # 'en': 'English us',
  # 'es': 'Espanol mx es',

  'languages': {
    'fr': 'Français fr ca',
    'it': 'Italiano',
    # NO DOMAIN NAME
    'ch': 'Swiss_German ch de',

    # NO DOMAIN NAME
    'nhn': 'Nahuatl mx',
    'kr': '한국어_(hanguk-eo)',
  },

  'constructured languages': {
    # NO DOMAIN NAME
    'eo': 'esperanto X',
    # NO DOMAIN NAME
    # TODO
    # 'lfn': 'Lingua_Franca_Nova_(LFN) X',
    # NO DOMAIN NAME
    # TODO
    # 'jbo': 'Lojban X',
  },

  'first nations': {
    # NO DOMAIN NAME
    'haw': 'ʻŌlelo_Hawaiʻi us',
    'ht': 'kreyòl_ayisyen',
  },

  'europe': {
    'de': 'German',
    'corsica': 'corsu_(lingua_corsa) fr it',
    'gal': 'galego es',
    'tr': 'İstanbul_Türkçesi',
    'se': '_or_אידיש_(yidish/idish) il',
    'cat': 'català es ad',
    # Thank you, Welsh people
    'cymru': 'Cymraeg_{} X'.format(
      b'\xf0\x9f\x8f\xb4\xf3\xa0\x81\xa7\xf3\xa0\x81\xa2\xf3\xa0\x81\xb7\xf3\xa0\x81\xac\xf3\xa0\x81\xb3\xf3\xa0\x81\xbf'.decode('utf-8')),

  },

  'dutch': {
    'nl': 'Nederlands be nl',
    'za': 'Afrikaans za',
  },

  'it cold': {
    'fi': 'suomi',
  },

  'russian': {
    'ua': "українська_мова_(ukrayins'ka_mova)",
    'ru': 'русский_язык_(rússky_yazýk)',
  },

  'austronesian languages': {
    'ph': 'Filipino',
    # NO DOMAIN NAME
    'ph-ceb': 'Cebuano ph',
  },

  'from the levant': {
    'il': 'עִבְרִית_(Ivrit)',
    'et': 'አማርኛ_(Amarəñña) et',
    'gr': 'ελληνικά_(elliniká)',
    'شبكة': 'اَلْعَرَبِيَّةُ_(al-ʿarabiyyah) eg dz sd iq sa ye sy so tn jo ae ly lb ps om',
  },

  'asian': {
    'zh-yue': '粤语_(yuèyǔ) cn',
    'cn': '官话_(Guānhuà)',
    'vn': 'Tiếng_Việt',
    'th': 'ภาษาไทย_(Thai,_historically_Siamese)',
  },

  'african': {
    # NO DOMAIN NAME
    'za-xh': '[ˈǁʰɔsa]_(Xhosa_(have_fun)) za',
    # NO DOMAIN NAME
    'zulu': 'Zulu za',
  },
}

languages = {l: v for ls in languages_with_roots.values() for l, v in
             ls.items()}

# To separate sentences
lang_with_separator = {
}

no_flag_needed = ['X', '?']


# Maps domain name (TLD) to Google Translate's language code
lang_code_to_googletrans_code = {
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
  'ph-ceb': 'ceb',
  'cymru': 'cy',
  'se': 'yi',
  'ua': 'uk',
  'vn': 'vi',
  'za': 'af',
  'za-xh': 'xh',
}

desired_header_text = '  '.join(phrases)

default_header_text = \
  '[Please visit my English website](/en), [o visita mi sitio web en español.](/es)'
