# Wybór kategorii hasła oraz losowanie hasła z wybranej kategorii

import random

categories = ["animals", "plants", "professions", "proverbs"]

animals = ["chimpanzee", "cockroach", "pigeon", "guinea pig", "herring", "sturgeon"]
# chimpanzee - szympans, cockroach - karaluch, pigeon - gołąb, guinea pig - świnka morska,
# herring - śledź, sturgeon - jesiotr (XD)
plants = ["almond tree", "cabbage", "buckeye", "clover", "hogweed", "sneezeweed"]
# almond tree - migdałowiec, cabbage - kapusta, buckeye - kasztanowiec, clover - koniczyna, hogeweed - barszcz,
# sneezeweed - dzielżan(taki kwiatek ładny)
professions = ["software engineer", "physiotherapist", "veterinarian", "maintenance man", "shipyard worker", "tax collector"]
# software engineer - inżynier oprogramowania, programista, physiotherapist - fizjoterapeura, veterinarian - weterynarz,
# maintenance man - konserwator, shipyard worker - pracownik stoczni, tax collector - poborca podatkowy
proverbs = ["An empty vessel makes much noise", "Barking dogs seldom bite", "The show must go on", "You cant unscramble a scrambled egg",
"All that glitters is not gold"]
# [0]foolish or stupid people are the most talkative, [1]people who appear threatening rarely do harm,
# [2]A performance, event, etc., must continue even though there are problems, [3]Some actions are irreversible,
# [4]Things that look good outwardly may not be as valuable or good


print("Categories:") # wyświetlenie kategorii z listy
print()

for i in range(len(categories)):
    print(categories[i])

print()

answer = input("Which category from list do you want to choose? \n") # możliwość wyboru kategorii z listy
word = ()

if answer == "animals":
    word = random.choice(animals)

elif answer == "plants":
    word = random.choice(plants)

elif answer == "professions":
    word = random.choice(professions)

elif answer == "proverbs":
    word = random.chocie(proverbs)

# powyższe ify podpinają poniekąd pule haseł dla każdej kategorii pod daną kategorię,
# bo w zależności od wyboru ma zostać wylosowane słowo z listy wybranej kategorii
