label prologue_awakening:
    scene black

    voice "audio/narrador/awakening/01.wav"
    "There is nothing, only darkness, and cold."

    voice "audio/narrador/awakening/02.wav"
    "And now something new is born from it. Loneliness."

    voice "audio/narrador/awakening/03.wav"
    "You feel the cool air around and within you."

    voice "audio/narrador/awakening/04.wav"
    "Limbs, trying to feel or control them is a waste of time, it is like you are only your conscience."

    voice "audio/narrador/awakening/05.wav"
    "An urge to wake up emerges from within you."

    voice "audio/narrador/awakening/06.wav"
    "Exhaustion grows, no matter how hard you try, it feels like you are losing your consciousness. 
    Trying to wake up requires too much strength, and as you almost grasp the light that shines from outside, 
    you are pulled right back into the void."

    menu:
        p "What should I do?"

        "Let's keep trying!":
            scene black
            with fade
            jump room

        "Can I get help?":
            jump choice_help

        "There is no use in trying again.":
            window hide
            $ renpy.pause(1)
            play sound "audio/sfx/clue_sfx.wav"
            "{b}Ending 1 - Oblivion{/b}"

label choice_help:
    play sound "audio/sfx/alarm_clock.ogg" loop fadein 1.5

    voice "audio/narrador/awakening/07.wav"
    "An alarm is ringing, some may say it would be luck. But for you, it is like a memory. It reminds you of the sound of..."

    menu:

        "A bell.":
            scene black
            with fade
            jump church
        
        "My phone.":
            scene black
            with fade
            jump room
        
        "A heartbeat.":
            scene black
            with fade
            stop sound fadeout 1.0
            jump hospital