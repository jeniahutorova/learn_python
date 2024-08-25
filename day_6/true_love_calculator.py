def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    
    total1 = 0
    total2 = 0
    
    letters1 = "true"
    for letter in letters1:
        total1 += name1.count(letter) + name2.count(letter)
    
    letters2 = "love"
    for letter in letters2:
        total2 += name1.count(letter) + name2.count(letter)
    
    love_score = int(f"{total1}{total2}")
    
    print(love_score)

calculate_love_score("Kanye West", "Kim Kardashian")
