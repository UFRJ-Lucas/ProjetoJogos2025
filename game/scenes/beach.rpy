label beach:
    play sound "audio/music/beach_ambience.mp3" loop fadein 1.5 #achar um arquivo
    $ renpy.sound.set_volume(0.5, channel="music")

    scene beach #faltando
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/beach/01.wav" # faltando
    "The constant sound of waves sometimes makes you think of deep breaths."

    voice "audio/narrador/beach/02.wav" # faltando
    "Salt air is carried by the wind. The smell of the ocean hits your lungs."

    voice "audio/narrador/beach/03.wav" # faltando
    "Your feets sink into the sand. It is warm, what makes the ocean even more appealing."

    voice "audio/narrador/beach/04.wav" # faltando
    "Looking at the horizon, you see the world converging into itself. The meeting of the sea and the sky."

    voice "audio/narrador/beach/05.wav" # faltando
    "A day at the beach, how are you gonna spend it?"

    menu:
        "I will just lay down in the sand.":
            voice "audio/narrador/beach/06.wav" # faltando
            "The sand is warm, the sun heat spread all over your body."
            voice "audio/narrador/beach/07.wav" # faltando
            "The temperature is searing and you feel good, alive, energised and could sleep on how relaxed you feel."
            voice "audio/narrador/beach/09.wav" # faltando
            "There was another place that you felt like this..."
            jump park_morning

        "If someone comes to the beach and do not go into the sea didn't come to the beach at all.":
            voice "audio/narrador/beach/10.wav" # faltando
            "You are right, let's get closer."
            scene sea #faltando
            $ renpy.sound.set_volume(1, channel="music")
            voice "audio/narrador/beach/11.wav" # faltando
            "Tiny droplets from the breaking waves can be felt in all your body."
            voice "audio/narrador/beach/12.wav" # faltando
            "The heat dissipate, the water is cold, it is relaxing."
            voice "audio/narrador/beach/13.wav" # faltando
            "So relaxing, that you feel a little sleepy."
            window hide

            scene beach_night #faltando
            with dissolve
            $ renpy.pause(0.6)

            window show
            voice "audio/narrador/beach/14.wav" # faltando
            "Did you sleep? Or the time went a little too fast?."
            voice "audio/narrador/beach/17.wav" # faltando
            "At the sea, at night. With the bright moon calling."
            voice "audio/narrador/beach/15.wav" # faltando
            "You let the flow of the water take you."
            voice "audio/narrador/beach/16.wav" # faltando
            "Feels like you're joining this landscape."
            voice "audio/narrador/beach/17.wav" # faltando
            "Letting the ocean wash away your unfinished bussiness."
            "{b}Ending 4 - Freedom broght by the sea{/b}"

        "I like to enjoy the view!":
            voice "audio/narrador/beach/18.wav" # faltando
            "The vista is breathtaking."
            voice "audio/narrador/beach/19.wav" # faltando
            "It triggers all memories from the summers of your life."
            voice "audio/narrador/beach/20.wav" # faltando
            "Lots of mornings at the beach, and after that..."
            voice "audio/narrador/beach/21.wav" # faltando
            "Aren't you feeling hungry?"
            jump cafe

        "I not that fan of the beach actually...":
            voice "audio/narrador/beach/22.wav" # faltando
            "Lets get the road then."
            jump road
        