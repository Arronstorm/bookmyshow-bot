START_MSG = " I am Theater.io for more info type /help"
HELP_MSG = """List of available commands:\n
/city - Name of the city without any bracktes and use '_' for '  '
    Eg: Trivandrum - /city trivandrum 
          Abu Road - /city abu_road
          Kota (AP) - /city kota_ap\n
/theaters - Name of the theater with no special characters and use '-' for '  '
    Eg: PVR - /theater pvr
          Aries Plex - /theaters aries-plex\n
/date - To give the datein yyyy-mm-dd
    Eg: for 29th of may 2022 - /date 2022-04-29
          for todays date - /date\n
/movies - To get the list of movies in the theater you have given"""
IF_NO_ARG_IS_GIVEN = "you have not given any arguements"
BETA = "Currently in Beta Testing"
IF_NO_ARG_IS_GIVEN_FOR_DATE = "The date is now set to "

monthslist = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}

city_list = {
    "alsisar_(rajasthan)": "alsisar-rajasthan",
    "ashoknagar_(west bengal)": "ashoknagar-west-bengal",
    "ashta_(maharashtra)": "ashta-maharashtra",
    "atmakur_(nellore)": "atmakur-nellore",
    "aurangabad_(bihar)": "aurangabad-bihar",
    "aurangabad_(west_bengal)": "aurangabad-west-bengal",
    "belagavi_(belgaum)": "belagavi-belgaum",
    "berhampore_(w.b.)": "berhampore-wb",
    "berhampur_(odisha)": "berhampur-odisha",
    "bilaspur_(himachal_pradesh)": "bilaspur-himachal-pradesh",
    "cumbum_(ap)": "cumbum-ap",
    "fatehpur_(rajasthan)": "fatehpur-rajasthan",
    "hamirpur_(hp)": "hamirpur-hp",
    "hubballi_(hubli)": "hubballi-hubli",
    "kalaburagi_(gulbarga)": "kalaburagi-gulbarga",
    "kalol_(gandhinagar)": "kalol-gandhinagar",
    "kalol_(panchmahal)": "kalol-kanchmahal",
    "kodagu_(coorg)": "kodagu-coorg",
    "kota_(ap)": "kota-ap",
    "kovur_(nellore)": "kovur-nellore",
    "krishnarajpete_(k.r.pete)": "krishnarajpete-krpete",
    "mangaluru_(mangalore)": "mangaluru-mangalore",
    "manikonda_(ap)": "manikonda-ap",
    "mysuru_(mysore)": "mysuru-mysore",
    "narsapur_(medak)": "narsapur-medak",
    "national_capital_region_(ncr)": "national-capital-region-ncr",
    "parigi_(telangana)": "parigi-telangana",
    "patan_(satara)": "patan-satara",
    "pratapgarh_(rajasthan)": "pratapgarh-rajasthan",
    "pratapgarh_(up)": "pratapgarh-up",
    "prayagraj_(allahabad)": "prayagraj-allahabad",
    "rajamahendravaram_(rajahmundry)": "rajamahendravaram-rajahmundry",
    "ratnagiri_(odisha)": "ratnagiri-odisha",
    "tumakuru_(tumkur)": "tumakuru-tumkur",
    "vijayapura_(bengaluru rural)": "vijayapura-bengaluru rural",
    "vijayapura_bijapur)": "vijayapura-bijapur",
    "vizag_visakhapatnam)": "vizag-visakhapatnam",
    "b._Kothakota": "b-kothakota",
    "g.mamidada": "gmamidada",
    "agar_malwa": "agar-malwa",
    "andaman_and_nicobar": "andaman-and-nicobar",
    "bihar_sharif": "bihar-sharif",
    "biswanath_charali": "biswanath-charali",
    "biswanath_chariali": "biswanath-chariali",
    "chandpur_siau": "chandpur-siau",
    "charkhi_dadri": "charkhi-dadri",
    "cooch_behar": "cooch-behar",
    "dakshin_barasat": "dakshin-barasat",
    "dalli_rajhara": "dalli-rajhara",
    "east_godavari": "east-godavari",
    "fatehgarh_sahib": "fatehgarh-sahib",
    "gola_bazar": "gola-bazar",
    "hanuman_junction": "hanuman-junction",
    "hindaun_city": "hindaun-city",
    "jajpur_road": "jajpur-road",
    "jangareddy_gudem": "jangareddy-gudem",
    "joynagar_majilpur": "joynagar-majilpur",
    "karanja_lad": "karanja-lad",
    "kargi_road": "kargi-road",
    "khariar_road": "khariar-road",
    "kuchaman_city": "kuchaman-city",
    "lakhimpur_kheri": "lakhimpur-kheri",
    "mandi_dabwali": "mandi-dabwali",
    "mandi_gobindgarh": "mandi-gobindgarh",
    "maraimalai_nagar": "maraimalai-nagar",
    "math_chandipur": "math-chandipur",
    "mulugu_ghanpur": "mulugu-ghanpur",
    "mungra_badshahpur": "mungra-badshahpur",
    "ner_parsopant": "ner-parsopant",
    "new_tehri": "new-tehri",
    "palia_kalan": "palia-kalan",
    "port_blair": "port-blair",
    "rabkavi_banhatti": "rabkavi-banhatti",
    "railway_koduru": "railway-koduru",
    "sawai_madhopur": "sawai-madhopur",
    "seoni_malwa": "seoni-malwa",
    "south_24_parganas": "south-24-parganas",
    "sri_ganganagar": "sri-ganganagar",
    "station_ghanpur": "station-ghanpur",
    "sulthan_bathery": "sulthan-bathery",
    "sundar_nagar": "sundar-nagar",
    "talwandi_bhai": "talwandi-bhai",
    "tilda_neora": "tilda-neora",
    "tirumakudalu_narasipura": "tirumakudalu-narasipura",
    "uttara_kannada": "uttara-kannada",
    "west_kameng": "west-kameng",
    "bagha_purana": "bagha-purana",
    "abu_road": "abu-road"
}
