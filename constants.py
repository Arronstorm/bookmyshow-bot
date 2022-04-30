START_MSG = " I am Theater.io for more info type /help"
HELP_MSG = """List of available commands:\n
/city - Name of the city without any bracktes and use '-' for '  '
    Eg: Trivandrum - /city trivandrum 
          Abu Road - /city abu-road
          Kota (AP) - /city kota-ap\n
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
    "alsisar-(rajasthan)": "alsisar-rajasthan",
    "ashoknagar-(west bengal)": "ashoknagar-west-bengal",
    "ashta-(maharashtra)": "ashta-maharashtra",
    "atmakur-(nellore)": "atmakur-nellore",
    "aurangabad-(bihar)": "aurangabad-bihar",
    "aurangabad-(west-bengal)": "aurangabad-west-bengal",
    "belagavi-(belgaum)": "belagavi-belgaum",
    "berhampore-(w.b.)": "berhampore-wb",
    "berhampur-(odisha)": "berhampur-odisha",
    "bilaspur-(himachal-pradesh)": "bilaspur-himachal-pradesh",
    "cumbum-(ap)": "cumbum-ap",
    "fatehpur-(rajasthan)": "fatehpur-rajasthan",
    "hamirpur-(hp)": "hamirpur-hp",
    "hubballi-(hubli)": "hubballi-hubli",
    "kalaburagi-(gulbarga)": "kalaburagi-gulbarga",
    "kalol-(gandhinagar)": "kalol-gandhinagar",
    "kalol-(panchmahal)": "kalol-kanchmahal",
    "kodagu-(coorg)": "kodagu-coorg",
    "kota-(ap)": "kota-ap",
    "kovur-(nellore)": "kovur-nellore",
    "krishnarajpete-(k.r.pete)": "krishnarajpete-krpete",
    "mangaluru-(mangalore)": "mangaluru-mangalore",
    "manikonda-(ap)": "manikonda-ap",
    "mysuru-(mysore)": "mysuru-mysore",
    "narsapur-(medak)": "narsapur-medak",
    "national-capital-region-(ncr)": "national-capital-region-ncr",
    "parigi-(telangana)": "parigi-telangana",
    "patan-(satara)": "patan-satara",
    "pratapgarh-(rajasthan)": "pratapgarh-rajasthan",
    "pratapgarh-(up)": "pratapgarh-up",
    "prayagraj-(allahabad)": "prayagraj-allahabad",
    "rajamahendravaram-(rajahmundry)": "rajamahendravaram-rajahmundry",
    "ratnagiri-(odisha)": "ratnagiri-odisha",
    "tumakuru-(tumkur)": "tumakuru-tumkur",
    "vijayapura-(bengaluru rural)": "vijayapura-bengaluru rural",
    "vijayapura-bijapur)": "vijayapura-bijapur",
    "vizag-visakhapatnam)": "vizag-visakhapatnam",
    "b.-Kothakota": "b-kothakota",
    "g.mamidada": "gmamidada",
    "agar-malwa": "agar-malwa",
    "andaman-and-nicobar": "andaman-and-nicobar",
    "bihar-sharif": "bihar-sharif",
    "biswanath-charali": "biswanath-charali",
    "biswanath-chariali": "biswanath-chariali",
    "chandpur-siau": "chandpur-siau",
    "charkhi-dadri": "charkhi-dadri",
    "cooch-behar": "cooch-behar",
    "dakshin-barasat": "dakshin-barasat",
    "dalli-rajhara": "dalli-rajhara",
    "east-godavari": "east-godavari",
    "fatehgarh-sahib": "fatehgarh-sahib",
    "gola-bazar": "gola-bazar",
    "hanuman-junction": "hanuman-junction",
    "hindaun-city": "hindaun-city",
    "jajpur-road": "jajpur-road",
    "jangareddy-gudem": "jangareddy-gudem",
    "joynagar-majilpur": "joynagar-majilpur",
    "karanja-lad": "karanja-lad",
    "kargi-road": "kargi-road",
    "khariar-road": "khariar-road",
    "kuchaman-city": "kuchaman-city",
    "lakhimpur-kheri": "lakhimpur-kheri",
    "mandi-dabwali": "mandi-dabwali",
    "mandi-gobindgarh": "mandi-gobindgarh",
    "maraimalai-nagar": "maraimalai-nagar",
    "math-chandipur": "math-chandipur",
    "mulugu-ghanpur": "mulugu-ghanpur",
    "mungra-badshahpur": "mungra-badshahpur",
    "ner-parsopant": "ner-parsopant",
    "new-tehri": "new-tehri",
    "palia-kalan": "palia-kalan",
    "port-blair": "port-blair",
    "rabkavi-banhatti": "rabkavi-banhatti",
    "railway-koduru": "railway-koduru",
    "sawai-madhopur": "sawai-madhopur",
    "seoni-malwa": "seoni-malwa",
    "south-24-parganas": "south-24-parganas",
    "sri-ganganagar": "sri-ganganagar",
    "station-ghanpur": "station-ghanpur",
    "sulthan-bathery": "sulthan-bathery",
    "sundar-nagar": "sundar-nagar",
    "talwandi-bhai": "talwandi-bhai",
    "tilda-neora": "tilda-neora",
    "tirumakudalu-narasipura": "tirumakudalu-narasipura",
    "uttara-kannada": "uttara-kannada",
    "west-kameng": "west-kameng",
    "bagha-purana": "bagha-purana",
    "abu-road": "abu-road"
}
