def Welcome():
    print("*_* --------------------------------------------------------------- *_*")
    print("\tThis is my home work \t- While LOOP - \n\tWelcome to Ghamdan Al-Yamani Program ")
    print(":) --------------------------------------------------------------- :( \nLet\'s Go -> \n" )
def end_program():
    print("*_* --------------------------------------------------------------- *_*")
    print("\tThink You For Using My Program  \n\tDone By: Ghamdan Mohammed Al-Yamani  ")
    print(":) --------------------------------------------------------------- :( " )
#GHAMDAN MOHAMMED MOHAMMED AL-YAMANI - GO -
Welcome()

captlais = {'tirane': 'albania', 'algiers': 'algeria', 'andorra la vella': 'andorra', 'luanda': 'angola',
            'saint johns': 'antigua and barbuda', 'buenos aires': 'argentina', 'yerevan': 'armenia',
            'canberra': 'australia', 'vienna': 'austria', 'baku': 'azerbaijan', 'nassau': 'bahamas',
            'manama': 'bahrain', 'dhaka': 'bangladesh', 'bridgetown': 'barbados', 'minsk': 'belarus',
            'brussels': 'belgium', 'belmopan': 'belize', 'porto novo': 'benin', 'thimphu': 'bhutan',
            'la paz': 'bolivia', 'sarajevo': 'bosnia and herzegovina', 'gaborone': 'botswana',
            'brasilia': 'brazil', 'bandar seri begawan': 'brunei', 'sofia': 'bulgaria',
            'ouagadougou': 'burkina faso', 'gitega': 'burundi', 'phnom penh': 'cambodia', 'yaounde': 'cameroon',
            'ottawa': 'canada', 'praia': 'cape verde', 'bangui': 'central african republic', 'ndjamena': 'chad',
            'santiago': 'chile', 'beijing': 'china', 'bogota': 'colombia', 'moroni': 'comoros',
            'kinshasa': 'congo, democratic republic of the', 'brazzaville': 'congo, republic of the',
            'san jose': 'costa rica', 'yamoussoukro': 'côte d ivoire (ivory coast)', 'zagreb': 'croatia',
            'havana': 'cuba', 'nicosia': 'cyprus', 'prague': 'czech republic (czechia)',
            'copenhagen': 'denmark', 'djibouti': 'djibouti', 'roseau': 'dominica',
            'santo domingo': 'dominican republic', 'dili': 'east timor', 'quito': 'ecuador', 'cairo': 'egypt',
            'san salvador': 'el salvador', 'london': 'england', 'malabo': 'equatorial guinea',
            'asmara': 'eritrea', 'tallinn': 'estonia', 'mbabana': 'eswatini (swaziland)',
            'addis ababa': 'ethiopia', 'palikir': 'federated states of micronesia', 'suva': 'fiji',
            'helsinki': 'finland', 'paris': 'france', 'libreville': 'gabon', 'banjul': 'gambia',
            'tbilisi': 'georgia', 'berlin': 'germany', 'accra': 'ghana', 'athens': 'greece',
            'saint georges': 'grenada', 'guatemala': 'guatemala', 'conakry': 'guinea',
            'bissau': 'guinea-bissau', 'georgetown': 'guyana', 'port au prince': 'haiti',
            'tegucigalpa': 'honduras', 'budapest': 'hungary', 'reykjavik': 'iceland', 'new delhi': 'india',
            'jakarta': 'indonesia', 'tehran': 'iran', 'baghdad': 'iraq', 'dublin': 'ireland',
            'jerusalem': 'palastine', 'rome': 'italy', 'kingston': 'jamaica', 'tokyo': 'japan',
            'amman': 'jordan', 'nur sultan': 'kazakhstan', 'nairobi': 'kenya', 'tarawa atoll': 'kiribati',
            'pristina': 'kosovo', 'kuwait': 'kuwait', 'bishkek': 'kyrgyzstan', 'vientiane': 'laos',
            'riga': 'latvia', 'beirut': 'lebanon', 'maseru': 'lesotho', 'monrovia': 'liberia',
                    'tripoli': 'libya', 'vaduz': 'liechtenstein', 'vilnius': 'lithuania', 'luxembourg': 'luxembourg',
                    'antananarivo': 'madagascar', 'lilongwe': 'malawi', 'kuala lumpur': 'malaysia', 'male': 'maldives',
                    'bamako': 'mali', 'valletta': 'malta', 'majuro': 'marshall islands', 'nouakchott': 'mauritania',
                    'port louis': 'mauritius', 'mexico': 'mexico', 'chisinau': 'moldova', 'monaco': 'monaco',
                    'ulaanbaatar': 'mongolia', 'podgorica': 'montenegro', 'rabat': 'morocco', 'maputo': 'mozambique',
                    'nay pyi taw': 'myanmar (burma)', 'windhoek': 'namibia', 'kathmandu': 'nepal',
                    'amsterdam': 'netherlands', 'wellington': 'new zealand', 'managua': 'nicaragua', 'niamey': 'niger',
                    'abuja': 'nigeria', 'pyongyang': 'north korea', 'skopje': 'north macedonia (macedonia)',
                    'belfast': 'northern ireland', 'oslo': 'norway', 'muscat': 'oman', 'islamabad': 'pakistan',
                    'melekeok': 'palau', 'panama': 'panama', 'port moresby': 'papua new guinea', 'asuncion': 'paraguay',
                    'lima': 'peru', 'manila': 'philippines', 'warsaw': 'poland', 'lisbon': 'portugal', 'doha': 'qatar',
                    'bucharest': 'romania', 'moscow': 'russia', 'kigali': 'rwanda',
                    'basseterre': 'saint kitts and nevis', 'castries': 'saint lucia',
                    'kingstown': 'saint vincent and the grenadines', 'apia': 'samoa', 'san marino': 'san marino',
                    'sao tome': 'sao tome and principe', 'riyadh': 'saudi arabia', 'edinburgh': 'scotland',
                    'dakar': 'senegal', 'belgrade': 'serbia', 'victoria': 'seychelles', 'freetown': 'sierra leone',
                    'singapore': 'singapore', 'bratislava': 'slovakia', 'ljubljana': 'slovenia',
                    'honiara': 'solomon islands', 'mogadishu': 'somalia', 'seoul': 'south korea', 'juba': 'south sudan',
                    'madrid': 'spain', 'pretoria': 'south africa', 'sri jayawardenapura kotte': 'sri lanka',
                    'khartoum': 'sudan', 'paramaribo': 'suriname', 'stockholm': 'sweden', 'bern': 'switzerland',
                    'damascus': 'syria', 'taipei': 'taiwan', 'dushanbe': 'tajikistan', 'dodoma': 'tanzania',
                    'bangkok': 'thailand', 'lome': 'togo', 'nukualofa': 'tonga', 'tunis': 'tunisia',
                    'ankara': 'türkiye (turkey)', 'ashgabat': 'turkmenistan', 'funafuti': 'tuvalu', 'kampala': 'uganda',
                    'kyiv': 'ukraine', 'abu dhabi': 'united arab emirates', 'washington': 'united states',
                    'montevideo': 'uruguay', 'tashkent': 'uzbekistan', 'port vila': 'vanuatu',
                    'vatican': 'vatican city', 'caracas': 'venezuela', 'hanoi': 'vietnam', 'cardiff': 'wales',
                    'sanaa': 'yemen', 'lusaka': 'zambia', 'harare': 'zimbabwe'}

count = 0
while count == 0:
    from_user = input("Enter any capital city that you want : ").lower()
    if from_user in captlais:
        count = 1
    else :
        print(f"{from_user} is not a capital city, Try again Like (sanaa) ")

user_point = 1
count = 1
while count == 1:
    print(f"True, You get point Because '{from_user.title()}' is capital city of '{captlais[from_user].title()}' .")
    last_char = from_user[-1]
    from_user = input(f"You Have 1 Point, GO GAME To Get Points.\nWhat is the capital city in the world it first char equal : '{last_char}' ? ").lower()
    if from_user[0] == last_char and from_user in captlais:
        user_point += 1
    else:
        print("Game Over... Because you are input capital city, The first char is not equal the last char.")
        print(f"Okay Not Bed, You get : {user_point} Points.")
        break

end_program()