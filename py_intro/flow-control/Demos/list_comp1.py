def main():
    words = ['Woodstock', 'Gary', 'Tucker', 'Gopher', 'Spike', 'Ed',
             'Faline', 'Willy', 'Rex', 'Rhino', 'Roo', 'Littlefoot',
             'Bagheera', 'remy', 'Pongo', 'Kaa', 'Rudolph', 'Banzai',
             'Courage', 'Nemo', 'Nala', 'Alvin', 'Sebastian', 'Iago']
    three_letter_words = [w for w in words if len(w) == 3]
    print(three_letter_words)
    
main()

%reset


[word for word in words if word[0] == "R"]

[word for word in words if word[0].upper() == "R"]


