label cabana:
    play sound "audio/music/woods_ambience.mp3" loop fadein 1.5 #achar um arquivo

    # Primeira piscada (rápida visão do parque)
    scene cabana_day #botar o arquivo
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/cabana/01.wav" #faltando
    "A small hut, in the middle of the woods."

    voice "audio/narrador/cabana/02.wav" #faltando
    "The air is pure, wind, animals and the trees sing the song of the forest together."

    voice "audio/narrador/cabana/03.wav" #faltando
    "A few days outside of the world will be great."


label nature:
    menu:
        "I am an urban person":
            voice "audio/narrador/cabana/04.wav" #faltando
            "There is no place like home."
            jump home

        "Reconect with nature is something that I need":
            voice "audio/narrador/cabana/05.wav" #faltando
            "The gentle breeze, the green from the leaves, focus of golden light from the sun."
            voice "audio/narrador/cabana/06.wav" #faltando
            "You were really missing this, to feel like a simple human being."
            voice "audio/narrador/cabana/07.wav" #faltando
            "Commune with nature is great and makes you feel alive, and have a purpose."
            voice "audio/narrador/cabana/08.wav" #faltando
            "You really should spend some days here."
            window hide
        

            scene cabana_night #botar o arquivo
            with dissolve
            $ renpy.pause(0.3)


            window show
            voice "audio/narrador/cabana/09.wav" #faltando
            "The sun is gone. Is hard to see everything."
            voice "audio/narrador/cabana/10.wav" #faltando
            "The moonlight is too brittle and blue, this light isn't enough to cut through the deep darkness."
            voice "audio/narrador/cabana/11.wav" #faltando
            "Besides some owls, there isn't much noise this time of the day."
            jump nightacabana

label nightacabana:
    voice "audio/narrador/cabana/12.wav" #faltando
    "Nightfall didn't bring you any sign of sleep."
    voice "audio/narrador/cabana/13.wav" #faltando
    "What will you do now?"
    menu:
        "I will lay down and read some book":
            voice "audio/narrador/cabana/14.wav" #faltando
            "Time flies, before you realize, it is day again."
            jump wild

        "I will try to sleep anyway":
            voice "audio/narrador/cabana/14.wav" #faltando
            "Time flies, before you realize, it is day again."
            jump wild

        "I really wanna go outside":
            voice "audio/narrador/cabana/15.wav" #faltando
            "Going outside at night will be dangerous."
            voice "audio/narrador/cabana/16.wav" #faltando
            "But you notice, after opening the door, it is day again."
            jump wild

label wild:
    voice "audio/narrador/cabana/17.wav" #faltando
    "Strange, the sun rose so quickly."
    voice "audio/narrador/cabana/18.wav" #faltando
    "Maybe it was the calling of nature."
    voice "audio/narrador/cabana/19.wav" #faltando
    "You can't remember much, but you feel, it is time to be one with it."
    window hide
    $ renpy.pause(0.5)
    "{b}Ending 5 - Wild at heart{/b}"

    