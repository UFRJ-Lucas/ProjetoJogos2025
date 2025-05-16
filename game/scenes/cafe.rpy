label cafe:
    play sound "audio/music/cafe_ambience.mp3" loop fadein 1.5 volume 0.5

    # Primeira piscada (rápida visão do cafe)
    scene cafe_day
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/cafe/01.wav" 
    "The warm feeling in the air, enriched by the sweet aroma of freshly baked bread and strong coffee. The soft clinking of cups being placed on saucers can be heard here and there."
    
    voice "audio/narrador/cafe/02.wav" 
    "There are muffled laughs and low-toned conversations, as if the atmosphere were simultaneously public and intimate."

    voice "audio/narrador/cafe/03.wav" 
    "You feel a strong sense of familiarity. A lot of time was spent in here."

    menu:
        "This was a place of..."

        "Bonding.":
            voice "audio/narrador/cafe/04.wav" 
            "You often came here to spend time with friends and family. The memories of this place are undoubtedly a precious treasure."

        "Struggle.":
            voice "audio/narrador/cafe/05.wav" 
            "You often came here when things didn't go as planned. All that stress washed away by copious amount of coffee."
        
        "Routine.":
            voice "audio/narrador/cafe/06.wav"
            "You often came here to eat. The food here did make for some nice lunch."

    voice "audio/narrador/cafe/07.wav"
    "Anyway, you consider ordering something, but you're not exactly hungry at the moment."

    menu:
        "You won't order anything, but perhaps you could stay a little?"

        "Rest":

            voice "audio/narrador/cafe/08.wav"
            "You go to sit on the table in the back, and notice a strange book on top of it. Maybe a guest forgot it here?"

            voice "audio/narrador/cafe/09.wav"
            "Your curiosity gets the better of you, and you decide to read it."
            scene black
            with fade
            jump theater
        
        "Go home":

            voice "audio/narrador/cafe/10.wav" 
            "There is no point in staying here anymore. It's better to just go home."
            scene black
            with fade
            jump house
