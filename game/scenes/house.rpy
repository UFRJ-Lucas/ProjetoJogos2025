label house:
    stop sound fadeout 0.5 # sem som para essa cena

    # Primeira piscada (rápida visão da casa)
    scene house_front
    with fade
    $ renpy.pause(0.3)

    voice "audio/narrador/house/01.wav" # faltando
    "After a long walk, you finally reach the place you've been meaning to reach. The comfort of your own lair."

    if "FOGGY_ROAD" in memories_visited:
        voice "audio/narrador/house/02.wav" # faltando
        "The same sense of quietude you felt on that foggy road washes over you. The sun is serene. The breeze is pleasant."

        voice "audio/narrador/house/03.wav" # faltando
        "You could stand here all day, but you know now that you must keep moving on."

    "<SCENE CONTINUES>"

    if "PLAZA_NOTEBOOK" in memories_visited:
        "<RECALL SKETCHBOOK MEMORY>"