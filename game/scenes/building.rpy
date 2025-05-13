default count = 0
default calling = True
default body = True

label building:
    play sound "audio/music/building_ambience.mp3" loop fadein 1.5

    # Primeira piscada (rápida visão do parque)
    scene building_day
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/building/01.wav" #faltando
    "Artificial lights make the day resemble night."

    voice "audio/narrador/building/02.wav" #faltando
    "At the distance you hear those royalty free music that no one really care about."

    voice "audio/narrador/building/03.wav" #faltando
    "Rehearsed smiles, shiny corridors, and an artificial scent, like a building's perfume"

    voice "audio/narrador/building/04.wav" #faltando
    "You feel no familiarity with this place, nor its plastic-wrapped food."

    voice "audio/narrador/building/11.wav" #faltando
    "The time here goes by, the lure of those display window may catch your atention for a little while."

    scene building_night
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/building/05.wav" #faltando
    "Actually, it's like you seen places like this exact one several times."

    voice "audio/narrador/building/04.wav" #faltando
    "There are other places that makes you feel this one too, in other ways..."


label performance:
    "Which place was that?"
    menu:
        "A church.":
            voice "audio/narrador/building/05.wav" #faltando
            "The place that precedes this one."

            voice "audio/narrador/building/06.wav" #faltando
            "Once those were the highest buildings."

            voice "audio/narrador/building/07.wav" #faltando
            "Focus on the bell and the acoustics..."
            jump church

        "A theather.":
            voice "audio/narrador/building/08.wav" #faltando
            "People living other lives, pretending to be someone else."
            voice "audio/narrador/building/09.wav" #faltando
            "There are astonishing similarities, right?"
            voice "audio/narrador/building/10.wav" #faltando
            "When were the last time you were inside one of these?"
            jump theater
        
        
        


    