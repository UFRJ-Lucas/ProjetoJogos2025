label streets:
    play sound "audio/music/city_ambience.mp3" loop fadein 1.5 

    # Primeira piscada (rápida visão das ruas)
    scene streets #botar o arquivo
    with dissolve
    $ renpy.pause(0.3)

    
    voice "audio/narrador/streets/01.wav" 
    "From inside a car, you the streets of your city."
    voice "audio/narrador/streets/02.wav"
    "This is what keep people going to anywhere and then back again."
    voice "audio/narrador/streets/03.wav" 
    "Where are you planing to go?."


label drive:
    "where are you going?"
    menu:
        "To the church.":
            scene black
            with fade
            jump church
        
        "I wanna go home!":
            scene black
            with fade
            jump house

        "To my job.":
            scene black
            with fade
            jump office

        "This was the street of my old school!":
            scene black
            with fade
            jump school

        "There are some things I need to do in the city center.":
            scene black
            with fade
            jump city

        "I could use a walk at the plaza.":
            scene black
            with fade
            jump plaza

        "Somewhere away from the city.":
            scene black
            with fade
            jump cabana