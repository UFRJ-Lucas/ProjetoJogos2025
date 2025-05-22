label rooftops:
    stop sound fadeout 0.5 # sem som para essa cena

    scene rooftops_day
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/rooftops/01.wav" 
    "You find yourself on some sort of terrace. Looking into the distance you can see houses and buildings."

    voice "audio/narrador/rooftops/02.wav"
    "You're pretty high up. At least the view is nice."

    menu:
        "The sight makes you feel..."

        "Powerful":
            voice "audio/narrador/rooftops/03.wav"
            "Looking down on the city makes you feel powerful."

        "A sense of belonging":
            voice "audio/narrador/rooftops/04.wav"
            "Looking down on the city gives you a feeling of belonging."

    voice "audio/narrador/rooftops/05.wav" 
    "You keep looking on when something catches your attention."

    menu:
        "You see..."

        "A white bird":
            voice "audio/narrador/rooftops/06.wav" 
            "You notice a beautiful white bird flying around. The sight lifts your spirit and all that purity reminds you of something."
            scene black
            with fade
            jump church

        "A familiar building":
            voice "audio/narrador/rooftops/07.wav" 
            "You notice a familiar building. You remember going there often to work."
            scene black
            with fade
            jump office