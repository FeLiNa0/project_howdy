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
site_title = f"Hello! {short_author} is my name"
default_site_title = "Hugo Omar Rivera Calzadillas"

# https://omniglot.com/language/phrases/index.htm
site_title_translations = {
    # http://www.questconnect.org/tara_dictionary.htm
    # https://www.academia.edu/8173744/Tarahumara_Phrases
    'tar': f"Kuira-bá! Nijé koriwe {short_author}, chabochi. Wimena Nijé.",
    'nhn': f'Nitlze! Nehua notōcā {short_author}.',
    # https://www.omniglot.com/language/phrases/navajo.php
    # http://www.suduva.com/dineh_conversation.htm
    'nv': f"Yá'át'ééh! Shí éí {short_author} yinishyé.",
    'haw': f"Aloha! ʻO {short_author} koʻu inoa.",
    'lkt': f"Hau! {short_author} emáčiyapi.",
    'jbo': f"coi! mi'e {short_author}.",
    'lfn': f"Ало! Ме ном ес {short_author}.",
    # https://www.omniglot.com/language/phrases/cherokee.php
    'chr': f"ᎤᎵᎮᎵᏍᏗ! {short_author} ᏓᏆᏙ.",
    # https://www.facebook.com/umndakhotaiapi/posts/10153132735022077/
    'dak': f"Háu! {short_author} emákiyapi do.",
    # http://akiuk.lksd.org/resources/yup_ik_phrases
    'ypk': f"Waqaa! Quyana tailuci!",
    # http://www.suduva.com/acoma_conversation.htm
    'kee': f"Guw'aadzi!",
    # https://www.omniglot.com/language/phrases/choctaw.htm
    'cho': f"Halito! Sa hohchifo ut {short_author}.",
    # http://www.suduva.com/zuni_conversation.htm
    'zun': f"Keshhi, hom a:kuwaye! Ho' {short_author} leshhina.",
    # https://www.omniglot.com/language/phrases/yucatec-maya.php
    'yua': f"Ba'ax ka wa'alik? Kíimak 'oolal. In k'aaba'e {short_author}. Xíiktech uutsil",
    # https://www.omniglot.com/writing/otomi.htm
    'oto': f"Zenjua Ki!",
    # http://talksauk.com/#/phrases/greetings_and_feelings
    # http://talksauk.com/#/dictionary/everyday_words
    'kic': f"Ho^",
}

site_title_translations['kjq'] = site_title_translations['kee']

phrases = [
  "Hello, dear guest! My name is Hugo Omar Rivera Calzadillas."
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
  # https://omniglot.com/language/phrases/lfn.php
  'lfn': [
      'Bonveni!',
      'Tu parla engles? Un lingua no sufisi.',
      'Joia! Sania!',
      'Bon viaje!',
  ],
  # https://omniglot.com/language/phrases/lojban.htm
  'jbo': [
      "fi'i",
      "xu do se bangu la .inglic.",
      ".a'o pluka litru le braxamsi.",
  ],
  'kr': [
    "반갑습니다, 친애하는 여러분.",
    "제 이름은 Hugo Omar Rivera Calzadillas입니다.",
    "저는 멕시코계 미국인이면서, 프로그래머겸 아티스트 입니다.",
    "저는 여러분의 언어를 말하거나 쓸 수는 없지만 배우고 싶습니다.",
    "저의 영어 또는 스페인어 버전의 웹사이트를 방문해 주세요.",
    "읽어주셔서 감사합니다.",
    "당신을 축복하고 당신이 온라인 여행을 하면서 많은 흥미로운 웹사이트 찾기를 희망합니다.",
  ]
}

for lang, t in site_title_translations.items():
    if lang not in phrases_translations:
        phrases_translations[lang] = [t]

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
    'cymru': 'Cymraeg gb-wls',
    'ro': 'limba_română',

    'scot': 'Gàidhlig_(Scots_Gaelic) gb-sct',

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

  'from the levant': {
    'il': 'עִבְרִית_(Ivrit)',
    'et': 'አማርኛ_(Amarəñña) et',
    'gr': 'ελληνικά_(elliniká)',
    'شبكة': 'اَلْعَرَبِيَّةُ_(al-ʿarabiyyah) ' + \
            'eg dz sd iq sa ye sy so tn jo ae ly lb ps om',
    'ir': 'فارسی_(fārsi)',
  },

  'african': {
    # NO DOMAIN NAME
    'za-xh': '[ˈǁʰɔsa]_(Xhosa_(have_fun)) za',
    # NO DOMAIN NAME
    'zulu': 'Zulu za',
    'so': 'Af-Soomaali',

    # TODO igbo, swahili, somali, sesotho, shona, hausa, chichewa
  },

  'austronesian languages and other pacific islands': {
    'ph': 'Filipino',
    # NO DOMAIN NAME
    'ph-ceb': 'Cebuano ph',
    'ws': 'Gagana_Sāmoa',
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

  'first nations': {
    'nhn': 'Nahuatl mx',
    'tar': "Rarámuri_ra'ícha_or_Ralámuli_ra'ícha_(Tarahumara) mx",

    'nv': 'Diné_bizaad_or_Naabeehó_bizaad_(Navajo) us',
    'chr': 'ᏣᎳᎩ_ᎦᏬᏂᎯᏍᏗ_Tsalagi_Gawonihisdi_(Cherokee) us',
    'haw': 'ʻŌlelo_Hawaiʻi us',

    # https://en.wikipedia.org/wiki/Dakota_language
    'dak': 'Dakhótiyapi_Dakȟótiyapi_(Dakota) us',

    # Alaska
    # https://en.wikipedia.org/wiki/Yupik_languages
    'ypk': 'Yupik us',

    # US and Canada, the Dakotas, Nebraska, Missouri, Montana
    # https://en.wikipedia.org/wiki/Lakota_language
    'lkt': "Lakȟótiyapi_(Lakota) us ca",

    # https://en.wikipedia.org/wiki/Southern_Athabaskan_languages
    'apa': 'Southern_Athabaskan_or_Apachean us mx',

    # New Mexico
    # language isolate
    # https://en.wikipedia.org/wiki/Keres_language
    'kee': 'Eastern_Keresan us',
    'kjq': 'Western_Keresan us',

    # Oklahoma
    # https://en.wikipedia.org/wiki/Choctaw_language
    'cho': 'Choctaw us',

    # NM and AZ
    # language isolate, possibly 7000 years old
    # https://en.wikipedia.org/wiki/Zuni_language
    'zun': "Shiwiʼma_or_Zuni us",

    # AZ
    # https://en.wikipedia.org/wiki/Hopi_language
    'hop': 'Hopílavayi_(Hopi) us',

    # Pueblo people in Rio Grande valley in NM, also in AZ
    # https://en.wikipedia.org/wiki/Tewa_language
    'tew': 'Tano_or_Tewa us',

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
