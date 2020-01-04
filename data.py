"""Pure data."""

# TODO make this into an autogenerated article?
# or an observable notebook?
# tables of data...
# import data from Python...
# or export to JS...

# a few more popular languages:
# TODO marathi (india)
# TODO wu chinese
# TODO turkish
# TODO urdu
# TODO javanese, indonesian
# TODO persian
# TODO bhojpuri (india)
# TODO min najn chinese, hakka chinese, hjn chinese, xiang chinese, gan chinese
# TODO yoruba (niger)
# TODO odia (india)
# TODO burmese
# TODO maithili (india)
# TODO burmese
# TODO uzbek
# TODO pashto

long_author = "Hugo Omar Rivera Calzadillas"
short_author = "Hugo O. Rivera"
site_title = "Hugo says hello"
default_site_title = "Hugo Omar Rivera Calzadillas"

phrases = [
  "Welcome, dear guest!",
  "I am a Mexican-American programmer and artist.",
  "I do not speak or write your language, but I wish to learn.",
  "Please visit the English version or the Spanish version of my website.",
  "Thank you for reading.",
  "Blessings to you. I wish you find many interesting websites on your online "
  "journey.",
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
      'Mi deziras, ke vi trovos multajn interesajn retejojn en via interreta '
      'vojaĝo.'
  ],
  'lfn': [
      'TODO'
  ],
  'jbo': [
      'TODO'
  ],
}

# Maps domain name (TLD) to language name, and optionally a list of ISO 3166
# country codes.
# ? or X indicates no need for flag emoji

primary_languages = ["en", "es"]
secondary_languages = "fr it ch-de de kr jbo nhn tar".split()

# TODO generate flags based on wikipedia data
#       (based on number of people that speak the language)
languages_with_roots = {
  # 'en': 'English ' + \
  #       'us pr gb nz au ie  ca fj lr sg tt  ' + \
  #       'hk gu as ai bm vg ky cw fk mp tc vi  ',
  # 'es': 'Espanol mx pr es sv gt cl ar bo pa py ve gq co pe do',

  'constructured languages': {
    # NO DOMAIN NAME
    'eo': 'esperanto X',

    # NO DOMAIN NAME
    # TODO
    'lfn': 'Lingua_Franca_Nova_(LFN) X',

    # NO DOMAIN NAME
    # TODO
    'jbo': 'Lojban X',

    # creole
    'ht': 'kreyòl_ayisyen',
  },

  'first nations': {
    'nhn': 'Nahuatl mx',
    'tar': "Rarámuri_ra'ícha_or_Ralámuli_ra'ícha_(Tarahumara) mx",
    'nv': 'Diné_bizaad_or_Naabeehó_bizaad_(Navajo) us',
    'chr': 'ᏣᎳᎩ_ᎦᏬᏂᎯᏍᏗ_Tsalagi_Gawonihisdi_(Cherokee) us',
    'haw': 'ʻŌlelo_Hawaiʻi us',

    # Yucatan
    # https://en.wikipedia.org/wiki/Yucatec_Maya_language
    'yua': 'mayaʼ_tʼàan_or_Yukatek_Maya mx',

    # Oaxaca
    # https://en.wikipedia.org/wiki/Zapotec_languages
    'zap': 'Zapotec mx',
    # https://en.wikipedia.org/wiki/Mixe_languages
    'mixe': 'Mixe mx',

    'vmz': 'Mazatlán_Mazatec mx',

    # language isolate
    'huv': 'Huave mx',

    # Oaxaca y Puebla
    # https://en.wikipedia.org/wiki/Tec%C3%B3atl_Mazatec
    'maa': 'Tecóatl_Mazatec_or_Eloxochitlán_Mazatec mx',
    'pbm': 'Tecóatl_Mazatec_or_Eloxochitlán_Mazatec mx',

    # https://en.wikipedia.org/wiki/Awakatek_language
    'agu': "qaʼyol_or_Awakatek_or_Coyotin_or_Chalchitec mx gt",

    # Central altiplano region
    # https://en.wikipedia.org/wiki/Otomi_language
    'oto': 'otomitl_or_Hñähñú_or_Ñañhų_(Otomí) mx',

    # Michoacan, Lake Pátzcuaro
    # language isolate
    # https://en.wikipedia.org/wiki/Pur%C3%A9pecha_language
    'tsz': 'Purépecha_or_Tarascan mx',
    'pua': 'Purépecha_or_Tarascan mx',

    # TX, OK, Coahuila, Sonora
    # Spoken by the Kickapoo in us and mexico
    # Some 145 of the tribe members chose to become U.S. citizens and the
    # remaining 500 or so chose to obtain Mexican citizenship.[7]
    'kic': 'Fox_or_Mesquakie_Meskwaki mx us',
  },

  'europe': {
    'latin': 'lingua_latīna_🏛️ X',
    'pt': 'português pt br',
    'fr': 'Français fr ca',
    'it': 'Italiano',
    # NO DOMAIN NAME
    'ch-de': 'Swiss_German ch de',
    'de': 'Deutsch',

    'dk': 'dansk',

    'corsica': 'corsu_(lingua_corsa) fr it',
    'gal': 'galego es',
    'tr': 'İstanbul_Türkçesi',
    'yiddish': 'ייִדיש_יידיש_or_אידיש_(yidish/idish) il',
    'cat': 'català es ad',
    'ie': 'Gaeilge_(Irish)',
    'pl': 'język_polski',
    # Thank you, Welsh people
    'cymru': 'Cymraeg_{} X'.format(
      b'\xf0\x9f\x8f\xb4\xf3\xa0\x81\xa7\xf3\xa0\x81\xa2\xf3\xa0\x81\xb7\xf3\xa0\x81\xac\xf3\xa0\x81\xb3\xf3\xa0\x81\xbf'.decode('utf-8')),

    'ro': 'limba_română',

    'scot': 'Gàidhlig_(Scots_Gaelic)_{} X'.format(
      b'\xf0\x9f\x8f\xb4\xf3\xa0\x81\xa7\xf3\xa0\x81\xa2\xf3\xa0\x81\xb3\xf3\xa0\x81\xa3\xf3\xa0\x81\xb4\xf3\xa0\x81\xbf'.decode('utf-8')),

    'lu': 'Letzeburgesch',
  },

  'dutch': {
    'nl': 'Nederlands be nl',
    'za': 'Afrikaans za',
  },

  'it cold': {
    'fi': 'suomi',
    'se': 'svenska',
  },

  'russian': {
    'ua': "українська_мова_(ukrayins'ka_mova)",
    'ru': 'русский_язык_(rússky_yazýk)',
  },

  'austronesian languages and other pacific islands': {
    'ph': 'Filipino',
    # NO DOMAIN NAME
    'ph-ceb': 'Cebuano ph',
    'ws': 'Gagana_Sāmoa',
  },

  'from the levant': {
    'il': 'עִבְרִית_(Ivrit)',
    'et': 'አማርኛ_(Amarəñña) et',
    'gr': 'ελληνικά_(elliniká)',
    'شبكة': 'اَلْعَرَبِيَّةُ_(al-ʿarabiyyah) ' + \
            'eg dz sd iq sa ye sy so tn jo ae ly lb ps om',
  },

  'asian': {
    'zh-yue': '粤语_(yuèyǔ) cn',
    'cn': '官话_(Guānhuà)',
    'vn': 'Tiếng_Việt',
    'th': 'ภาษาไทย_(Thai,_historically_Siamese)',
    'kr': '한국어_(hanguk-eo)',
    'jp': '日本語_(Nihongo)',
    'hmong': 'Hmoob_(Hmong) X',
    'mn': 'ᠮᠣᠩᠭᠣᠯ_ᠬᠡᠯᠡ_or_монгол_хэл_(mongol_khel)',
  },

  'african': {
    # NO DOMAIN NAME
    'za-xh': '[ˈǁʰɔsa]_(Xhosa_(have_fun)) za',
    # NO DOMAIN NAME
    'zulu': 'Zulu za',
    'so': 'Af-Soomaali',

    # TODO igbo, swahili, somali, sesotho, shona, hausa, chichewa
  },

  'madagascar and shri lanka': {
    'mg': 'Malagasy',
    'lk': 'සිංහල_(Sinhala)',
  },

  'india': {
    'np': 'नेपाली_(Nepali) np',

    'भारत': 'मानक_हिन्दी_(Mānak_Hindī) in',
    'hi': 'मानक_हिन्दी_(Mānak_Hindī) in',

    'bd': 'বাংলা_(Bengali) bd in',
    # Indian Dravidian language spoken predominantly by people of Karnataka in
    # southwestern India, and by significant linguistic minorities in the
    # states of Maharashtra, Andhra Pradesh, Tamil Nadu, Telangana, Kerala
    # and abroad
    'kn': 'ಕನ್ನಡ_(Kannada) in',
    'ml': 'മലയാളം_(Malayalam) in',
    'ભારત': 'ગુજરાતી_(Gujarati) in',
    'ਭਾਰਤ': 'ਪੰਜਾਬੀ_or_پن٘جابی_(Punjabi) in',
    'te': 'తెలుగు_(Telugu) in',
    'இந்தி': 'தமிழ்_(Tamil) in lk',
    'sd': 'سنڌي‎_सिन्(Sindhi) in',
  },
}

languages = {l: v for ls in languages_with_roots.values() for l, v in
             ls.items()}

# To separate sentences
lang_with_separator = {}

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
  'yiddish': 'yi',
  'ua': 'uk',
  'vn': 'vi',
  'za': 'af',
  'za-xh': 'xh',
  'ie': 'ga',
  'hmong': 'hmn',
  'dk': 'da',
  'latin': 'la',
  'np': 'ne',
  'இந்தி': 'ta',
  'se': 'sv',
  'lk': 'si',
  'ws': 'sm',
  'scot': 'gd',
  'bd': 'bn',
  'ભારત': 'gu',
  'भारत': 'hi',
  'ਭਾਰਤ': 'pa',
  'இந்தி': 'ta',
  'lu': 'lb',
  'jp': 'ja',
}

desired_header_text = '  '.join(phrases)

default_header_text = '[Please visit my English website](/en), ' + \
    '[o visita mi sitio web en español.](/es)'
