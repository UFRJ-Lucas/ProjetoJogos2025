label house:
    stop sound fadeout 0.5 # sem som para essa cena

    scene house_front
    with Fade(0.5, 1.0, 0.5)

    voice "audio/narrador/house/01.wav" # faltando
    "After a long walk, you finally reach the place you've been meaning to reach. The comfort of your own lair."

    if len(memories_visited) <= 0: # Final Ruim se não coletou nenhuma memória significativa
        jump bad_end_locked

    if "FOGGY_ROAD" in memories_visited:
        voice "audio/narrador/house/02.wav" # faltando
        "The same sense of quietude you felt on that foggy road washes over you. The sun is serene. The breeze is pleasant."

        voice "audio/narrador/house/03.wav" # faltando
        "You could stand here all day, but you know now that you must keep moving on."

    if "THEATER_PLAY" in memories_visited:
        voice "audio/narrador/house/04.wav" # faltando
        "The protagonist from that play found their true purpose at their journey's end."

        voice "audio/narrador/house/05.wav" # faltando
        "Will you find yours?"

    voice "audio/narrador/house/06.wav" # faltando
    "You try opening the front door. It's unlocked."

    voice "audio/narrador/house/07.wav" # faltando
    "After a deep breath, you step inside."

    scene room_day
    with Fade(0.5, 1.0, 0.5)

    voice "audio/narrador/house/08.wav" # faltando
    "You search around the house. Memories flowing back like a torrent. Finally, you reach your bedroom."

    voice "audio/narrador/house/09.wav" # faltando
    "A figure lies in your bed, with their back facing you. The light coming from the outside is strong and you have trouble seeing who it is."

    if "PLAZA_NOTEBOOK" in memories_visited:
        voice "audio/narrador/house/10.wav" # faltando
        "Then a jolt runs through your brain. This person was drawn in that sketchbook you found in the plaza."

        voice "audio/narrador/house/11.wav" # faltando
        "You remember clearly now the hours you spent together sketching. It was one of your favorite pastimes."

    if "CHURCH_VISITED" in memories_visited:
        voice "audio/narrador/house/12.wav" # faltando
        "Your heart aches, the air is heavy and you feel a hint of sadness in the room."

        voice "audio/narrador/house/13.wav" # faltando
        "You're not sure why, but you feel like this person's spirit has a wound that is yet to heal."
    
    voice "audio/narrador/house/14.wav" # faltando
    "A mirror on the wall close by catches your attention."

    if len(memories_visited) >= 3:
        jump good_end
    else:
        jump normal_end

label bad_end_locked:
    voice "audio/narrador/house/15.wav" # faltando
    "You try opening the door. It's locked. You see no way in."

    voice "audio/narrador/house/16.wav" # faltando
    "Suddenly, your eyes get heavy. Your start fainting."

    scene black
    with fade

    voice "audio/narrador/house/17.wav" # faltando
    "That which was calling for you is no more. You find yourself back into the void, waiting for another chance."

    voice "audio/narrador/house/18.wav" # faltando
    "You can't remember your face. You can't remember your name. You can't remember your life."

    "{b}Ending 10 - Locked Away{/b}"
    return

label normal_end:
    scene mirror_broken
    with dissolve

    voice "audio/narrador/house/19.wav" # faltando
    "It's broken. Only a faint silhoutte can be seen in the reflection."

    voice "audio/narrador/house/20.wav" # faltando
    "Something within you is still missing. But that's okay."

    voice "audio/narrador/house/21.wav" # faltando
    "You're home, and very tired. Everything will make sense after some rest."

    if "CAFE_BONDING" in memories_visited:
        voice "audio/narrador/house/22.wav" # faltando
        "You could try calling your parents later. Perhaps they could help."

    voice "audio/narrador/house/23.wav" # faltando
    "For now you lay in bed, the person besides you not budging, and rest your eyes."

    scene black
    with fade

    "{b}Ending - House of Sweet Dreams{/b}"
    return

label good_end:
    scene mirror_clear
    with dissolve

    voice "audio/narrador/house/24.wav" # faltando
    "You see nothing. There is no reflection."

    voice "audio/narrador/house/25.wav" # faltando
    "It makes sense, you're not here anymore. This is a memory from ahead of your time."

    voice "audio/narrador/house/26.wav" # faltando
    "A moment in time that you couldn't reach."

    voice "audio/narrador/house/27.wav" # faltando
    "But you don't mind. You remember it all too clear now. Every single moment."

    if "CAFE_BONDING" in memories_visited:
        voice "audio/narrador/house/28.wav" # faltando
        "You remember the faces of your family, all your friends. So many different people in your life"

    voice "audio/narrador/house/29.wav" # faltando
    "You had a wonderful life, and you wish for nothing more."

    voice "audio/narrador/house/30.wav" # faltando
    "Now the time has come, you lay in bed and sleep. A peaceful smile across your face."

    scene black
    with fade

    "{b}Good Ending - Rest{/b}"
    return