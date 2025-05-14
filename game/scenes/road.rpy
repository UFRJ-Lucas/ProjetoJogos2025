label road:

    # Primeira piscada (rápida visão da estrada)
    scene road_night
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/road/01.wav" # faltando
    "You find yourself standing before a lonely road. You see no cars driving by. All you can hear is the wind and the rustling leaves."

    voice "audio/narrador/road/02.wav" # faltando
    "It's foggy but you feel like you recognize this road. Something draws you to it, beckoning your feet forward."

    menu:
        "The sight of the path covered by fog. It makes you feel..."

        "Dread":
            voice "audio/narrador/road/03.wav" # faltando
            "You can't explain why, but the foggy road brings you a feeling of dread. You're not sure you want to go forward."

        "Curiosity":
            voice "audio/narrador/road/04.wav" # faltando
            "You can't explain why, but the foggy road makes you curious. What could be hiding behind that white veil?"

        "Peace":
            $ road_peace = True

            voice "audio/narrador/road/05.wav" # faltando
            "You can't explain why, but the foggy road brings you some peace of mind. Perhaps it invokes a feeling of finality?"
    
label road_choice_1:
    menu:
        "What should you do?"

        "Move on." if road_peace:
            jump house
        
        "Wait a bit.":
            voice "audio/narrador/road/06.wav" # faltando
            "You decide to wait some more. Perhaps a car will drive by and you can ask for a ride."
            jump road_choice_2

label road_choice_2:
    menu:
        "What should you do?"

        "Move on." if road_peace:
            jump house
        
        "Wait some more.":
            voice "audio/narrador/road/07.wav" # faltando
            "You keep waiting. It's dangerous to walk around aimlessly."
            jump road_choice_3

label road_choice_3:
    menu:
        "What should you do?"

        "Move on." if road_peace:
            jump house
        
        "Wait even more.":
            jump bad_end_waiting

label bad_end_waiting:
    voice "audio/narrador/road/08.wav" # faltando
    "It's better to just wait. You are in no hurry after all."

    voice "audio/narrador/road/09.wav" # faltando
    "Whatever it is that you could find beyond the road. You have no desire to know. You will wait here until you're ready."

    voice "audio/narrador/road/10.wav" # faltando
    "You will wait. No matter how long that takes."

    show black
    with dissolve

    "{b}Ending 2 - Refusal{/b}"
