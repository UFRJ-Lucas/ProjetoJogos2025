label beach:
    play sound "audio/music/beach_ambience.mp3" loop fadein 1.5 
    $ renpy.sound.set_volume(0.5, channel="sound")

    scene beach 
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/beach/01.wav" 
    "The constant sound of waves sometimes makes you think of deep breaths."

    voice "audio/narrador/beach/02.wav" 
    "Salt air is carried by the wind. The smell of the ocean hits your lungs."

    voice "audio/narrador/beach/03.wav" 
    "Your feets sink into the sand. It is warm, what makes the ocean even more appealing."

    voice "audio/narrador/beach/04.wav" 
    "Looking at the horizon, you see the world converging into itself. The meeting of the sea and the sky."

    voice "audio/narrador/beach/05.wav" 
    "A day at the beach, how are you gonna spend it?"

    menu:
        "I will just lay down in the sand.":
            voice "audio/narrador/beach/06.wav" 
            "The sand is warm, the sun heat spread all over your body."
            voice "audio/narrador/beach/07.wav" 
            "The temperature is searing and you feel good, alive, energised and could sleep by how relaxed you feel."
            voice "audio/narrador/beach/09.wav" 
            "There was another place that you felt like this..."
            scene black
            with fade
            jump park_morning

        "If someone comes to the beach and do not go into the sea didn't come to the beach at all.":
            voice "audio/narrador/beach/10.wav" 
            "You are right, let's get closer."
            scene sea 
            $ renpy.sound.set_volume(1, channel="sound")
            voice "audio/narrador/beach/11.wav" 
            "Tiny droplets from the breaking waves can be felt in all your body."
            voice "audio/narrador/beach/12.wav" 
            "The heat dissipate, the water is cold, it is relaxing."
            voice "audio/narrador/beach/13.wav" 
            "So relaxing, that you feel a little tired."
            voice "audio/narrador/beach/08.wav"
            "Your eyes are feeling heavy, and you try to stay awake."
            window hide

            scene black
            with dissolve
            $ renpy.pause(0.5)

            scene beach
            with dissolve
            $ renpy.pause(0.3)

            scene black
            with dissolve
            $ renpy.pause(0.4)

            scene beach_night 
            with dissolve
            $ renpy.pause(0.6)

            scene black
            with dissolve
            $ renpy.pause(0.5)

            scene beach_night 
            with fade
            $ renpy.pause(0.3)

            window show
            voice "audio/narrador/beach/14.wav" 
            "Did you sleep? Or the time went a little too fast?."
            voice "audio/narrador/beach/23.wav" 
            "At the sea, at night. With the bright moon calling."
            voice "audio/narrador/beach/15.wav"
            "You let the flow of the water take you."
            voice "audio/narrador/beach/16.wav"
            "Feels like you're joining this landscape."
            voice "audio/narrador/beach/17.wav" 
            "Letting the ocean wash away your unfinished bussiness."
            window hide
            $ renpy.pause(1)
            play sound "audio/sfx/clue_sfx.wav"
            "{b}Ending 4 - Freedom brought by the sea{/b}"

        "I like to enjoy the view!":
            voice "audio/narrador/beach/18.wav" 
            "The vista is breathtaking."
            voice "audio/narrador/beach/19.wav" 
            "It triggers all memories from the summers of your life."
            voice "audio/narrador/beach/20.wav" 
            "Lots of mornings at the beach, and after that..."
            voice "audio/narrador/beach/21.wav" 
            "Aren't you feeling hungry?"
            scene black
            with fade
            jump cafe

        "I not that fan of the beach actually...":
            voice "audio/narrador/beach/22.wav" 
            "Lets get the road then."
            scene black
            with fade
            jump road
        