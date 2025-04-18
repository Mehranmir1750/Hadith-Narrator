import random
game = True
point = 0

famous_narrators = [
    {"name": "Abu Hurairah", "hadith_count": 5374},
    {"name": "Abdullah ibn Umar", "hadith_count": 2630},
    {"name": "Anas ibn Malik", "hadith_count": 2286},
    {"name": "Aisha bint Abi Bakr", "hadith_count": 2210},
    {"name": "Abdullah ibn Abbas", "hadith_count": 1660},
    {"name": "Jabir ibn Abdullah", "hadith_count": 1540},
    {"name": "Abu Sa'id al-Khudri", "hadith_count": 1170},
    {"name": "Abdullah ibn Amr ibn al-As", "hadith_count": 700},
    {"name": "Umm Salama", "hadith_count": 378},
    {"name": "Ali ibn Abi Talib", "hadith_count": 536},
    {"name": "Abu Bakr as-Siddiq", "hadith_count": 142},
    {"name": "Umar ibn al-Khattab", "hadith_count": 537},
    {"name": "Uthman ibn Affan", "hadith_count": 146},
    {"name": "Bilal ibn Rabah", "hadith_count": 44},
    {"name": "Muadh ibn Jabal", "hadith_count": 157},
    {"name": "Abu Musa al-Ashari", "hadith_count": 360},
    {"name": "Zayd ibn Thabit", "hadith_count": 92},
    {"name": "Abu Dharr al-Ghifari", "hadith_count": 281},
    {"name": "Sa'd ibn Abi Waqqas", "hadith_count": 121},
    {"name": "Hudhayfah ibn al-Yaman", "hadith_count": 228},
    {"name": "Salman al-Farsi", "hadith_count": 60},
    {"name": "Ka’b ibn Ujrah", "hadith_count": 40},
    {"name": "Umm Ayman", "hadith_count": 20},
    {"name": "Fatimah bint Muhammad", "hadith_count": 18},
    {"name": "Hassan ibn Thabit", "hadith_count": 12},
    {"name": "Ibn Mas'ud", "hadith_count": 848},
    {"name": "Imran ibn Husayn", "hadith_count": 650},
    {"name": "Barra' ibn Azib", "hadith_count": 305},
    {"name": "Abu Ayub al-Ansari", "hadith_count": 150},
    {"name": "Abdullah ibn Mas'ud", "hadith_count": 848}
]

while game:
    narrator_1 = random.choice(famous_narrators)
    narrator_2 = random.choice(famous_narrators)

    # Ensure both narrators are different
    while narrator_1["name"] == narrator_2["name"]:
        narrator_2 = random.choice(famous_narrators)

    print("\n" * 2)
    print("Who has recited more hadith?")
    print("\n")
    print(f"Compare A: {narrator_1['name']}")
    print("vs")
    print(f"Against B: {narrator_2['name']}")

    answer = input("Who narrated more Hadiths? Type 'a' or 'b': ").lower()

    def extract_answer(narrator_1, narrator_2):
        return "a" if narrator_1["hadith_count"] > narrator_2["hadith_count"] else "b"

    def check_answer(answer, correct_answer):
        global point
        global game

        if answer == correct_answer:
            point += 1
            print(f"✅ Correct! Your current score is: {point}")
        else:
            print("❌ Incorrect!")
            print(f"The correct answer was: {correct_answer.upper()}")
            print(f"Your final score is: {point}")
            game = False

    correct_answer = extract_answer(narrator_1, narrator_2)
    check_answer(answer, correct_answer)
