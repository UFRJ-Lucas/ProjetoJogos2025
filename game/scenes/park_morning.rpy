label park_morning:
    play sound "audio/music/park_ambience.mp3" loop fadein 1.5

    # Primeira piscada (rápida visão do parque)
    scene park_mornigng
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/park/01.wav" #faltando
    "The gentle cool breeze from the morning shakes the leaves, and makes you feel cold."

    voice "audio/narrador/park/02.wav" #faltando
    "Bird singing, some from afar, but other very close, make this place a tranquil heaven"

    voice "audio/narrador/park/03.wav" #faltando
    "Sun is still weak, but standing in sunlight makes you feel a little more awake, and warm."

    voice "audio/narrador/park/04.wav" #faltando
    "A fresh open space that can slow down time itself, and put some worries away."

    voice "audio/narrador/park/05.wav" #faltando
    "A place that the greeks would call elysian."

    voice "audio/narrador/park/06.wav" #faltando

label peace:
    "Was there any other place that makes you feel good in this way?"
    menu:
        "I went to a lake once.":
            voice "audio/narrador/park/07.wav" #faltando
            "Of course, surrounded by nature, the golden sun."

            voice "audio/narrador/park/08.wav" #faltando
            "You can almost feel that you are in there."
            jump lake

        "I loved the plaza.":
            voice "audio/narrador/park/09.wav" #faltando
            "Heaven is other people."

            voice "audio/narrador/park/10.wav" #faltando
            "Solitude is great, but being able to share this moment with other is greater"

            voice "audio/narrador/park/11.wav" #faltando
            "You remember this plaza very vividly, what you used to do there?"
            jump road

        "I would go to some rooftops to get a breath.":
            voice "audio/narrador/park/12.wav" #faltando
            "Sometimes life wasn't easy and you needed a break."

            voice "audio/narrador/park/13.wav" #faltando
            "'Everyone is like this', you think. You can be certain, but it feels like it."

            voice "audio/narrador/park/14.wav" #faltando
            "A safe space, that you could put yourself aside of everything, see things from above."

            voice "audio/narrador/park/15.wav" #faltando
            "And see the great engine that is human society."
            jump rooftops
        
        
        


    