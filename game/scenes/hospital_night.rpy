default count = 0
default calling = True
default body = True

label hospital:
    play sound "audio/music/hospital_sound.mp3" loop fadein 1.5

    # Cena inicial (tela preta)
    scene black
    with dissolve
    $ renpy.pause(0.5)

    # Primeira piscada (rápida visão do hospital)
    scene hospital_day
    with dissolve
    $ renpy.pause(0.3)

    scene black
    with dissolve
    $ renpy.pause(0.4)

    # Segunda piscada (um pouco mais longa)
    scene hospital_day
    with dissolve
    $ renpy.pause(0.5)

    scene black
    with dissolve
    $ renpy.pause(0.3)

    # Visão final (olhos abrem completamente)
    scene hospital_day
    with fade
    
    voice "audio/narrador/hospital/01.wav"
    "You hear a repetitive  and subtle sound of equipment and machinery constantly beeping."

    voice "audio/narrador/hospital/02.wav"
    "The air is cold, and sterile. Cleaning products and other chemicals are mixed with a frail scent of metal."

    voice "audio/narrador/hospital/03.wav"
    "Now that you identified the odor of the metal, you can almost taste it, if you concentrate long enough."

    voice "audio/narrador/hospital/04.wav"
    "But concentration is hard. There is this non-stop beeping and hurried steps that echos on distant corridors."

    voice "audio/narrador/hospital/05.wav"
    "Deep inside you, anxiety grows. It started in the air, and now it is inside you too."

    voice "audio/narrador/hospital/06.wav"
    "It's not just anxiety actually. You have a bad feeling about everything in this place. You need to get out."

    

label choice:
    "What should I do?"
    menu:
        "Call a doctor." if calling:
            voice "audio/narrador/hospital/07.wav"
            "You try to call someone, nobody came. Screaming doesn't helped either. There must be another way out."
            $ calling = False
            jump choice
        
        "I need to focus on something again." if not calling:
            voice "audio/narrador/hospital/11.wav"
            "That is indeed a good idea, the last time you tried to remeber, you concentrated in the alarm. Try it with something else."
            jump way_out

        "Let's try to get up." if body:
            voice "audio/narrador/hospital/08.wav"
            "Once again you try to feel or control your limbs, but it's a waste of time. Seems like your conscience is free, but your body trapped."
            $ body = False
            jump choice

        "Close my eyes, let's try to sleep" if not body:
            jump voyage

        "Why am I here?":
            voice "audio/narrador/hospital/09.wav"
            "You try very hard to remember, why are you here. Nothing comes to mind, strange. Is your head empty?"
            voice "audio/narrador/hospital/10.wav"
            "Maybe think of something else, there must be a way out."
            jump way_out

label way_out:

    voice "audio/narrador/hospital/20.wav"
    "Concentrate! You can find a way out, what do you want to focus on?"

    menu:

        "The sound of the steps":
            jump plaza_day
        
        "The cold in the air":
            #jump park_night
            pass
        
        "The sound of the machines.":
            jump voyage
        
        "The smell of metal":
            #"city"
            pass

label voyage:
    voice "audio/narrador/hospital/12.wav"
    "The sounds of the hospital are not something strange anymore, they are becoming one with you."

    voice "audio/narrador/hospital/13.wav"
    "Closing your eyes is hard, but you can surely do it. Keep trying."

    scene hispital_day
    with dissolve
    $ renpy.pause(0.3)

    scene black
    with dissolve
    $ renpy.pause(0.4)

    jump bad_ending


label bad_ending:
    voice "audio/narrador/hospital/14.wav"
    "You are back where you were, at the void. But now you feel numb. The only thing that lingers is longing."

    voice "audio/narrador/hospital/15.wav"
    "There is nothing that you can do anymore. And there is no sign of this state that you find yourself is going to end anytime soon."

label limbo:
    
    menu:
        "Wake up" if count != 3:
            voice "audio/narrador/hospital/16.wav"
            "There is no use in that"
            $ count += 1
            jump limbo

        "Remember" if count != 3:
            voice "audio/narrador/hospital/17.wav"
            "This won't work anymore"
            $ count += 1
            jump limbo
        
        "Make it stop!" if count != 3:
            voice "audio/narrador/hospital/17.wav"
            "But you don't know how"
            $ count += 1
            jump limbo
        
        "Is there hope?" if count == 3:
            voice "audio/narrador/hospital/17.wav"
            "Now there is only eternity."
            return


    