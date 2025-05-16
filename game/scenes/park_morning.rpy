label park_morning:
    play sound "audio/music/woods_ambience.mp3" loop fadein 1.5 

    # Primeira piscada (rápida visão do parque)
    scene park_morning
    with dissolve
    $ renpy.pause(0.3)

    
    
    voice "audio/narrador/park/01.wav"
    "The gentle cool breeze from the morning shakes the leaves, and makes you feel cold."

    voice "audio/narrador/park/02.wav" 
    "Bird singing, some from afar, but other very close, make this place a tranquil heaven"

    voice "audio/narrador/park/03.wav"
    "Sun is still weak, but standing in sunlight makes you feel a little more awake, and warm."

    voice "audio/narrador/park/04.wav" 
    "A fresh open space that can slow down time itself, and put some worries away."

    voice "audio/narrador/park/05.wav"
    "A place that the greeks would call elysian."

    voice "audio/narrador/park/06.wav"
    "Was there any other place that makes you feel good in this way?"

    menu:
        "I went to a lake once.":
            voice "audio/narrador/park/07.wav"
            "Of course, surrounded by nature, the golden sun."

            voice "audio/narrador/park/08.wav"
            "You can almost feel that you are in there."
            scene black
            with fade
            jump lake

        "I loved the plaza.":
            voice "audio/narrador/park/09.wav"
            "Heaven is other people."

            voice "audio/narrador/park/10.wav" 
            "Solitude is great, but being able to share this moment with other is greater"

            voice "audio/narrador/park/11.wav"
            "You remember this plaza very vividly, what you used to do there?"
            scene black
            with fade
            jump plaza_day

        "I would go to some rooftops to get a breath.":
            voice "audio/narrador/park/12.wav" 
            "Sometimes life wasn't easy and you needed a break."

            voice "audio/narrador/park/13.wav"
            "'Everyone is like this', you think. You can be certain, but it feels like it."

            voice "audio/narrador/park/14.wav" 
            "A safe space, that you could put yourself aside of everything, see things from above."

            voice "audio/narrador/park/15.wav"
            "And see the great engine that is human society."
            scene black
            with fade
            jump rooftops
        
        
        


    