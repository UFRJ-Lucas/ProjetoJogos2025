label prologue_awakening:
    scene black

    "There is nothing, only darkness, and cold."

    "And now something new is born from it. Loneliness."

    "You feel the cool air around and within you."

    "Limbs, trying to feel or control them is a waste of time, it is like you are only your conscience."

    "An urge to wake up emerges from within you."

    "Exhaustion grows, no matter how hard you try, it feels like you are losing your consciousness. 
    Trying to wake up requires too much strength, and as you almost grasp the light that shines from outside, 
    you are pulled right back into the void."

    menu:
        p "What should I do?"

        "Let's keep trying!":
            "Room"

        "Can I get help?":
            play sound "audio/sfx/alarm_clock.ogg" loop fadein 1.5

            "Alarm"

        "There is no use in trying again.":
            "Oblivion - Ending"
