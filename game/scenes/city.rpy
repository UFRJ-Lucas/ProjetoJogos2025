label city:
    $ visit_city = True
    play sound "audio/music/city_ambience.mp3" loop fadein 1.5 #achar um arquivo

    scene city_day #botar o arquivo
    with dissolve
    $ renpy.pause(0.3)
    
    voice "audio/narrador/city/01.wav" #faltando
    "Mirror-covered buildings reflect the sky and stand close to classical architecture."

    voice "audio/narrador/city/02.wav" #faltando
    "It is clear that in this place, the ages have stacked up chaotically."

    voice "audio/narrador/city/03.wav" #faltando
    "A place that, at the same time, holds a great deal of history and seems to have none at all."

    voice "audio/narrador/city/04.wav" #faltando
    "The sound of hurried footsteps, honking horns, and loud advertisements competes with the scent of hot asphalt and smoke mixed with perfume."

    voice "audio/narrador/city/05.wav" #faltando
    "In other words, a delight for those who loves pure chaos in every way, shape or form."

    voice "audio/narrador/city/06.wav" #faltando
    "Everything moves intensely, yet nothing seems to enchant anyone."

    voice "audio/narrador/city/07.wav" #faltando
    "You have the feeling that most of these people are like you."

    voice "audio/narrador/city/08.wav" #faltando
    "They are not really here."

    voice "audio/narrador/city/09.wav" #faltando
    "But it must be something something that you enjoy here, right?"

label center:
    menu:
        "I really like all these people wandering about, minding their bussiness.":
            voice "audio/narrador/city/10.wav" #faltando
            "Social life is of the upmost importance of the society."
            voice "audio/narrador/city/12.wav" #faltando
            "And you know a great place with this quality, that happens to be more relaxing."
            jump plaza

        "Culture, what the city was and what it is now, they rhyme in the streets!":
            voice "audio/narrador/city/11.wav" #faltando
            "Every building is tells multiple stories."
            voice "audio/narrador/city/13.wav" #faltando
            "Each visit to the city center is a class on history."
            voice "audio/narrador/city/14.wav" #faltando
            "And it invites us to think about society, power, people."
            voice "audio/narrador/city/15.wav" #faltando
            "There must be an interesting building around here..."
            jump building

        "I just like it. The city is alive, this is it's pulsing heart.":
            voice "audio/narrador/city/12.wav" #faltando
            "And the streets are its veins."
            jump streets
        
        
label city_night:

    scene city_night #botar o arquivo
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/city/16.wav" #faltando
    "And here you are again."

    voice "audio/narrador/city/17.wav" #faltando
    "But this time is very different. The city is dead."

    voice "audio/narrador/city/18.wav" #faltando
    "Obviously it will be reborn again in the morning."

    voice "audio/narrador/city/19.wav" #faltando
    "Yet, it is hard to believe that is the same place."

    voice "audio/narrador/city/20.wav" #faltando
    "There is an oneiric quality to this, there is fear and worries, those are present for sure."

    voice "audio/narrador/city/21.wav" #faltando
    "What was the last time a good story came from the city center at night?"

label midnight:
    menu:
        "I really can't recall, this is dangerous.":
            voice "audio/narrador/city/22.wav" #faltando
            "Ironically, to get out of there, you need to skulk through those slumbering streets."
            jump streets_night
        "I was waiting an bus here. Those ones, that can not enter the terminal.":
            jump beach
        "I was leaving the theater.":
            jump theater



    