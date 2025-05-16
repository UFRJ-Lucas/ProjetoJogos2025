label school:
    play sound "audio/music/school_ambience.mp3" loop fadein 1.5 #achar um arquivo

    # Primeira piscada (rápida visão da escola)
    scene school #botar o arquivo
    with dissolve
    $ renpy.pause(0.3)

    
    voice "audio/narrador/school/01.wav" 
    "Sounds of laughter, screaming, and quick steps."

    voice "audio/narrador/school/02.wav"
    "Drawings, decorations, and a variety of colors are spread across the walls."

    voice "audio/narrador/school/03.wav"
    "The smell is of freshly sharpened pencils, paper, and snacks."

    voice "audio/narrador/school/04.wav"
    "The atmosphere holds an intense yet restrained energy."

    voice "audio/narrador/school/05.wav" 
    "You feel a great flow of youthful life, waiting for recess to break free like a bursting dam."

    voice "audio/narrador/school/06.wav"
    "Those kids are really eager to go home."

    voice "audio/narrador/school/07.wav" 
    "Home..."

    scene black
    with fade
    jump house


    