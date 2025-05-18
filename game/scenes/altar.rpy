label altar:
    play music "audio/music/altar_ambience.mp3"
    $ renpy.music.set_volume(0.07, channel="music")

    scene altar_priest
    with dissolve
    $ renpy.pause(0.3)

    voice "audio/narrador/altar/01.wav" 
    "You stepped into the hush of the chapel, and time folded around you, like a veil."

    voice "audio/narrador/altar/02.wav" 
    "The altar — yes, the altar was there, quiet and waiting, not grand but right."

    voice "audio/narrador/altar/03.wav"
    "No gold. No carvings. Just timber, dark and real. It stood like it remembered something. Something you have forgotten. Or never even knew."

    voice "audio/narrador/altar/04.wav"
    "You see a priest, clad in black, sleeves dusted with ash or age — you couldn't tell which"

    voice "audio/narrador/altar/05.wav"
    "His back was to me, his hands still. Not folded, not lifted — just… resting on the wood, fingers splayed as though feeling the heartbeat of the altar itself."

    menu:
        "Get closer and talk to him.":
            voice "audio/narrador/altar/06.wav"
            "You come closer to him"
            voice "audio/narrador/altar/07.wav"
            "He didnt' turn, not right away. The air around him felt somewhat oppressive."
            voice "audio/narrador/altar/08.wav"
            "You tried to reach out 'hello'. But he didn't seem to listen."
            voice "audio/narrador/altar/09.wav"
            "Maybe he is lost in his own thoughts, or maybe medita..."

            voice "audio/priest/altar/01.wav"
            d "This place listens. More than most"

            voice "audio/narrador/altar/11.wav"
            "The religious figure did not even turn to face you."

            voice "audio/priest/altar/03.wav"
            d "This place is never empty, even when we think we're alone."
            jump priest


        "Let him alone":
            voice "audio/narrador/altar/10.wav"
            "You think is best to leave him alone."

            voice "audio/priest/altar/02.wav"
            d "I feel you, did you know?"

            voice "audio/narrador/altar/11.wav"
            "The religious figure did not even turn to face you."
            voice "audio/priest/altar/03.wav"
            d "This place is never empty, even when we think we're alone."
            jump priest

label priest: 

    scene altar
    with dissolve
    $ renpy.pause(0.3)

    show dom_visconti at center:
        zoom 1.7
    voice "audio/narrador/altar/12.wav"
    "He slowy turns around, and when he does, he is a little afraid."
    voice "audio/narrador/altar/13.wav"
    "Why he is like this is uncertain, you can't imagine why he would have such a reaction."

    show dom_visconti talking at center:
        zoom 1.7
    voice "audio/priest/altar/04.wav"
    d "Is that a trick? Or are you really here?"
    show dom_visconti at center:
        zoom 1.7

    menu:
        "I am right here, don't you see?":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/05.wav"
            d "Are you? Show yourself! The power of Christ compels you!"
            show dom_visconti at center:
                zoom 1.7

        "Trick? What are you talking about?":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/06.wav"
            d "Spirits cling to shadows. Especially the bitter ones"
            show dom_visconti at center:
                zoom 1.7

        "You remind me of someone I knew":
            $ dom = True
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/07.wav"
            d "You do not belong here..."
            show dom_visconti at center:
                zoom 1.7

    menu:
        "What are you saying? Are you insane?":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/08.wav"
            d "Are you testing my faith wraith?"
            show dom_visconti at center:
                zoom 1.7

        "Am I dreaming about this?":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/09.wav"
            d "Do not play the fool creature!"
            show dom_visconti at center:
                zoom 1.7

        "What is wrong? I don't get it.":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/10.wav"
            d "This is the house of the living. The house of God. And you... are unwelcome."
            show dom_visconti at center:
                zoom 1.7

    menu:
        "You cannot treat me like this!":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/11.wav"
            d "I will give you this chance, leave this sanctuary at once!"
            show dom_visconti at center:
                zoom 1.7

        "This is making no sense.":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/12.wav"
            d "You wear a face that was once human, but your heart is long gone."
            show dom_visconti at center:
                zoom 1.7

        "You must be out of your mind, I'm not doing anything wrong.":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/13.wav"
            d "I do not fear you. I will not allow you to remain in this world."
            show dom_visconti at center:
                zoom 1.7

        "I know you! From Sunday School" if dom:
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/14.wav"
            d "None of your tricks can affect a man from God!"
            show dom_visconti at center:
                zoom 1.7

            voice "audio/narrador/altar/14.wav"
            "But you do remember him, Dom Visconti. He was your teacher during your First Communion."
            $ priest_name = True

    menu:
        "Dom Visconti, from Sunday School!" if priest_name:
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/15.wav"
            d "Heavens! You indeed know my name!"
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/narrador/altar/16.wav"
            "The memories from that time are very strong now."
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/16.wav"
            d "Wait! Don't go yet!"

            $ renpy.pause(1)

            show dom_visconti at center:
                zoom 1.7

            $ renpy.pause(1)

            hide dom_visconti
            window hide

            scene black
            with fade

            stop music
            
            jump school   

        "Stop it please, you are scarying me.":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/20.wav"
            d "You sought to be seen — now you are judged. In the name of the Father, begone!"

            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/21.wav"
            d "Be cast out by the name above all names. Leave this sanctuary. Now"
            show dom_visconti at center:
                zoom 1.7

            voice "audio/narrador/altar/15.wav"
            "He lifted the book. Opened it. Began to speak — not in anger, but with power."
            
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/17.wav"
            d "Deliver us from evil, oh father!"

            window hide
            $ renpy.pause(1)

            hide dom_visconti
            $ renpy.pause(1)

            scene black
            with fade

            play sound "audio/sfx/clue_sfx.wav"
            "{b}Ending 8 - Divine Purge{/b}"
            return

        "This is nonsense, I'm leaving.":
            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/18.wav"
            d "You are not 'leaving' this place."
            show dom_visconti at center:
                zoom 1.7

            show dom_visconti talking at center:
                zoom 1.7
            voice "audio/priest/altar/19.wav"
            d "Be banished from this world by the name above all names. Ashes to ashes, dust to dust. Return to the land of the lord now!"

            window hide
            $ renpy.pause(1)

            hide dom_visconti talking
            $ renpy.pause(1)

            scene white
            with fade

            play sound "audio/sfx/clue_sfx.wav"
            "{b}Ending 9 - Unshackled and Forgiven{/b}"
            return

        
    