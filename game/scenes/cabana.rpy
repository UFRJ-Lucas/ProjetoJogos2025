label cabana:
    play sound "audio/music/woods_ambience.mp3" loop fadein 1.5 

    # Primeira piscada (rápida visão da cabana)
    scene cabana_day 
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/cabana/01.wav" 
    "A small hut, in the middle of the woods."

    voice "audio/narrador/cabana/02.wav" 
    "The air is pure, wind, animals and the trees sing the song of the forest together."

    voice "audio/narrador/cabana/03.wav" 
    "A few days outside of the world would be great."


label nature:
    menu:
        "I am an urban person":
            voice "audio/narrador/cabana/04.wav"
            "There is no place like home."
            jump home

        "Reconect with nature is something that I need":
            voice "audio/narrador/cabana/05.wav" 
            "The gentle breeze, the green from the leaves, focus of golden light from the sun."
            voice "audio/narrador/cabana/06.wav" 
            "You were really missing this, to feel like a simple human being without all of this affairs."
            voice "audio/narrador/cabana/07.wav"
            "Commune with nature is great and makes you feel alive, and have a purpose. As oppose to the modern world..."
            voice "audio/narrador/cabana/08.wav" 
            "You really should spend some days here."
            window hide
            play sound "audio/music/night_woods_ambience.mp3" loop fadein 1.5
            $ renpy.sound.set_volume(0.5, channel="sound")

            $ renpy.pause(0.5)

            scene cabana_night
            with dissolve
            $ renpy.pause(0.3)


            window show
            voice "audio/narrador/cabana/09.wav" 
            "The sun is gone. Is hard to see anything."
            voice "audio/narrador/cabana/10.wav" 
            "The moonlight is too brittle and blue, this light isn't enough to cut through the deep darkness."
            voice "audio/narrador/cabana/11.wav" 
            "Besides some owls and crickets, there isn't much noise this time of the day."
            jump nightacabana

label nightacabana:
    voice "audio/narrador/cabana/12.wav" 
    "Nightfall didn't bring you any sign of sleep."
    voice "audio/narrador/cabana/13.wav" 
    "What will you do now?"
    menu:
        "I will lay down and read some book":
            voice "audio/narrador/cabana/14.wav" 
            "Time flies, before you realize, it is day again."
            jump wild

        "I will try to sleep anyway":
            voice "audio/narrador/cabana/14.wav" 
            "Time flies, before you realize, it is day again."
            jump wild

        "I really wanna go outside":
            voice "audio/narrador/cabana/15.wav" 
            "Going outside at night will be dangerous."
            voice "audio/narrador/cabana/16.wav" 
            "But you notice, after opening the door, it is day again." 
            #colocar barulho de porta?
            jump wild

label wild:
    play sound "audio/music/woods_ambience.mp3" loop fadein 1.5 
    $ renpy.sound.set_volume(1.0, channel="sound")
    scene cabana_day 
    with dissolve
    $ renpy.pause(0.3)
    voice "audio/narrador/cabana/17.wav" 
    "Strange, the sun rose so quickly."
    voice "audio/narrador/cabana/18.wav" 
    "Maybe all of this was the calling of nature."
    voice "audio/narrador/cabana/19.wav"
    "You can't remember much, but you feel, it is time to be one with it."
    window hide
    $ renpy.pause(1)
    play sound "audio/sfx/clue_sfx.wav"
    "{b}Ending 7 - Wild at heart{/b}"

    