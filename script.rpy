# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define e = Character("Emilie", what_cps=60, color="#5896c5")
define m = Character("Player")
define v = Character("???", color="#880808", what_cps=30)
define s = Character("Superbia", color="#8332c1", what_cps=50)
define g = Character("Avaricia", color="#c1a832", what_cps=50)
define l = Character("Luxuria", color="#c132a8", what_cps=40)
define i = Character("Invidia", color="#32c17a", what_cps=50)
define w = Character("Ira", color="#b90000", what_cps=60)
define sl = Character("Accidia", color="#a8c132", what_cps=10)
define gl = Character("Gula", color="#c17532", what_cps=30)
define eye = Character("***", color="#ffffff", what_cps=20)

default visited_superbia = False
default got_clue_superbia = False

default visited_avaricia = False
default got_clue_avaricia = False

default visited_luxuria = False
default got_clue_luxuria = False

default visited_Invidia = False
default got_clue_Invidia = False

default visited_ira = False
default got_clue_ira = False

default visited_accidia = False
default got_clue_accidia = False

default visited_gula = False
default got_clue_gula = False

default clue_fragments_collected = 0
default secret_dialogue_shown = False

init:
    $ persistent.bgm_playing = False



# The game starts here.
label start:
    if not persistent.bgm_playing:
        play music "audio/gamemusic.mp3" fadein 2
        $ persistent.bgm_playing = True
    # Ask the player for their name
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    if not player_name:
        $ player_name = "Player"
    $ m = Character(player_name)

scene black with fade
$ preferences.text_cps = 60
m "She said she found a body under my floorboards..."
e "It's rotting,"
e "It smells."
$ preferences.text_cps = 10
m "*sign*, I know..."
$ preferences.text_cps = 60
e "We should record this case{w=0.3} and ask for an investigation from the police..."
$ preferences.text_cps = 10
m "... ..."
$ preferences.text_cps = 60
m "Look at the money we have..."
m "You'll be looking at nothing,{w=0.3} because we have nothing.{w=0.3} There's barely any left after renting this house..."
$ preferences.text_cps = 20
m "The cheapest house in this area..."
$ preferences.text_cps = 60
m "We can't afford to pay for a lawyer,{w=0.3} let alone a police investigation."
e "Please, {w=0.3}this is too much for us to deal with alone."

$ renpy.save("autosave1")

menu:
    "Yeah...It is...":
        m "Yeah...It is..."
        e "We'll get through this together."
        e "Let's hire an investigator..."
        jump ending_confinement
    
    "No, it's not. I'll sort this out alone. You don't worry about it.":
        m "No, it's not.{w=0.3} I'll sort this out alone.{w=0.3} You don't worry about it."
        e "...{w=0.3}Fine, that's alright. Just be careful, okay?"

jump lobby

# Lobby scene where the player can choose what to do next
label lobby:
    $ renpy.save("checkpoint1")
    scene lobby_background with fade # Replace with your actual lobby background when ready
    "What do you want to do next?"
    menu:
        "Check out the body":
            jump body
        "Sit and think...":
            jump think
        "Look outside the window.":
            jump window

            

label body:
    scene bodyimage with fade
    m "..looks familiar in a way...{w=0.5}too eerie."
    jump lobby

label think:
    scene black with fade
    m "I can't believe this is happening to us."
    e "I know,{w=0.3} but we have to stay strong."
    m "Yeah, I just need a moment{w=0.7} to gather my thoughts."
    jump lobby

label window:
    v "Careful,{w=0.3} the curtains might fall on you..."

    menu:
        "Step back":
            jump step_back

label step_back:
    play sound "audio/falling.mp3"
    m "..!!"
    m "Who are you?!"
    v "I am a voice in your head...{w=0.3}I am your guide...{w=0.3}this investigation intrigues me..."
    v "Come, {w=0.3}I know some friends who would love to help you..."

$ renpy.save("autosave2")

menu: 
    "Go ahead and meet them.":
        jump friends
    "I don't trust you.":
        m "I don't trust you."
        v "Suit yourself,{w=0.3} but you'll regret it."
        jump ending_unsolve

label friends:
    scene black with fade
    v "Wise decision{cps=5}...{cps=30}they might be the key to solving your murder... {w=0.7}{cps=10}case..."
    jump sins
    






#SINS!!!!
label sins:
    $ renpy.save("checkpoint_sins")
    play sound "creak.mp3"
    scene sins_background  # Replace with your actual sins background when ready
    with fade

    if clue_fragments_collected == 4 and not secret_dialogue_shown:
        $ secret_dialogue_shown = True
        jump secret_dialogue

    menu:
        "Check out the mirror..." if not got_clue_superbia:
            jump superbia

        "Check out the safe..." if not got_clue_avaricia:
            jump Avaricia

        "Check out the bed..." if not got_clue_luxuria:
            jump Luxuria

        "Check out the window..." if not got_clue_Invidia:
            jump Invidia
        
        "Check out the stove..." if not got_clue_ira:
            jump Ira

        "Check out the cushions..." if not got_clue_accidia:
            jump Accidia

        "Check out the fridge..." if not got_clue_gula:
            jump Gula

        "...What's that on the wall?" if clue_fragments_collected ==7:
            jump eye
        





label eye:
    stop music fadeout 1
    play music "audio/eye_theme.mp3" fadein 2
    play sound "audio/scarydoor.mp3"
# Replace with your actual eye background when ready
    scene black
    with fade
    v "... ..."
    v "You found all the clues...{w=0.7}but you still don't... know... who the killer... is.{w=0.7} {cps=10}...Do you?"
    eye "*** ****** ** ***. ** ** ******** ***, *******..."
    m "I can't quite hear..."
    v "You don't need to go near\nThere's nothing left."
    v "This murder is unsolvable."
    v "There's nothing left. There's nothing-"
    menu:
        "Step closer":
            "You step closer to the wall."
            play sound "audio/foot.mp3"
            scene eyewall with fade
            "The wall... breathes. You see something shifting behind it."
            menu:
                "Peel the wallpaper":
                    play sound "audio/rippaper.mp3"
                    scene eye_background with fade
                    "You peel back the paper. Behind the drywall is an enormous Eye, lidless and bloodshot."
                    v "Don't listen, don't listen!!! DON'T!!!"
                    eye "..."
                    "The Eye speaks in a whisper that echoes from every wall of the house:"
                    eye "He watches.\nHe lies\nHe listens..."
                    eye "{b}He {i}is{/i} you...{/b}"
                    v "..."
                    menu:
                        "Then show me.":
                            m "Then show me."
                            "The house dissolves into black.\nThe walls become memory."
                            scene bodyblood with fade 
                            "You see yourself. Bloodied hands. Your own voice, screaming. And you... smiling."
                            "You realize: you made him. {b}To hide from what you did.{/b}"
                            scene black with fade 
                            m "..."
                            v "...I didn't want you to be alone...\nSo I became everything you weren't brave enough to be."
                            stop music fadeout 1
                            scene black
                            with fade
                            jump official_ending1
                        "I don't believe it. You're wrong.":
                            m "I don't believe it. You're wrong."
                            scene black with fade
                            "The Eye closes. You turn back — but the hallway is gone..."
                            stop music fadeout 1
                            scene black
                            with fade
                            jump official_ending2
                        "I believe you. But I don't forgive you.":
                            m "..."
                            "The voice in your head stops speaking. The house collapses. The truth burns."
                            scene houseburn with fade
                            "You walk away alone, changed.\n{b}But free.{/b}"
                            stop music fadeout 1
                            scene black
                            with fade
                            jump official_ending3









#CHARACTERS!!
label superbia:
    if not visited_superbia:
        $ visited_superbia = True
        play sound "dooropen.mp3"
        scene room_pride
        show pride at center with fade
        m ".!!"
        v "Be carfull... {w=0.7}You dont want to hurt her self image..."
        $ renpy.save("checkpoint_pride")
        menu:
            "Say hello...":
                m "Hello, how are you? I was wondering if I could ask something?"
                s "{cps=5}...{cps=50}What do you want {w=0.4}...{i}{cps=20}peasant{/cps}{/i}?"
                v "I think you should try complimenting her..."
                menu: 
                    "Compliment her...":
                        m "Hello...Wow, you are quite pretty..."
                        m "Can I ask something if you have time?"
                        s "{cps=60}Hah, I know."
                        s "What do you need from me darling?"
                    "I'm sorry...what?":
                        m "I'm sorry...what?"
                        s "{cps=5}...{cps=50}You are a peasant, you don't deserve to talk to me."
                        v "I think you should try complimenting her...she's getting angry..."
                        menu:
                            "Compliment her...":
                                m "Hello...Wow, you are quite pretty..."
                                m "Can I ask something if you have time?"
                                s "{cps=60}Hah, I know."
                                s "What do you need from me darling?"
                            "I am not a peasant!":
                                m "I am not a peasant! Stop talking to me like that!"
                                v "oh no..."
                                hide pride
                                show pride scary at center
                                s "How dare you talk to me like that! {w=0.7}You are a peasant, and you will always be one!"
                                s "You are not worthy of my time!"
                                jump ending_pride1
            "Complement her...":
                m "Hello...Wow, you are quite pretty..."
                m "Can I ask something if you have time?"
                s "{cps=60}Hah, I know."
                s "What do you need from me darling?"
        
        m "I was wondering if you could help me with a case I am working on."
        s "A case? {w=0.7}What kind of case?"
        v "She seems to be interested, but you need to be careful with your words."
        m "I found a body under my floorboards...and I need to find out who it is and how they died."
        s "...And how does that concern me?"
        m "I was wondering...if you saw anything or anyone strange or suspicious around?"
        s "Oh yes, of corse you're asking me for help..."
        m "..."
        v "...{w=0.7}I think you should try visiting other friends of mine, they might be able to help you more than her right now..."
        m "..!!"
        m "You'll offend her if you say that!!"
        v "Don't worry...she can't hear me..."
        menu:
            "Visit other friends":
                jump sins
            
    else:
        # Second time (or more) dialogue
        $ renpy.save("checkpoint_pride2")
        play sound "dooropen.mp3"
        scene room_pride
        show pride at center with fade
        v "She still won't talk unless you flatter her again. Try this: Your eyes hold galaxies."
        s "Back again? Learned to speak properly?"
        menu:
            "Your eyes hold galaxies.":
                m "Your eyes hold galaxies."
                s "*frowns*"
                hide pride
                show pride scary at center
                s "Galaxies? What am I, a poet's fantasy? Insulting."
                jump ending_pride2
            "Even silence listens when you enter the room.":
                m "Even silence listens when you enter the room."
                s "*smiles*"
                s "Mm. Finally. Someone who understands gravitas."
                s "Perhaps I will reward that."
                v "(nervous silence)"
                s "(lowers voice)"
                s "He watches from behind a smile, proud of what he's done.{w=0.7}But he won't say it aloud, {w=0.7} {cps=20}not yet."
                scene black
                with fade
                $ clue_fragments_collected += 1
                centered "Clue Fragment [clue_fragments_collected]/7"
                $ got_clue_superbia = True
                if clue_fragments_collected ==7:
                    jump pleasedont
                jump sins

            "Your beauty is a masterpiece.":
                m "Your beauty is a masterpiece."
                s "A masterpiece? {w=0.7}What am I, a painting?"
                hide pride
                show pride scary at center
                s "I am not a painting, I am a goddess."
                s "And you are a peasant."
                jump ending_pride3
                


label Avaricia:
    if not visited_avaricia:
        $ visited_avaricia = True
        play sound "dooropen.mp3"
        scene room_greed
        show greed1 at center with fade
        m "This safe is..."
        v "Be polite, but don't beg. He likes bargaining. Just… don't take anything."
        g "Another desperate little soul, knocking at my vault..."
        g "The door's closed, but maybe… maybe I can make an exception..."
        g "For you...little one."
        $ renpy.save("checkpoint_greed")
        menu:
            "What do you want in return?":
                m "What do you want in return?"
                g "Ah, a buyer. Good. I want something small. Nothing you'll miss."
                v "Maybe give up something minor? A name, a secret, a feeling?"
                menu:
                    "My memories of the last dream.":
                        m "My memories of the last dream."
                        g "mmm...{w=0.7}A dream? {w=0.7}How quaint."
                        g "Keep going..."
                        v "I don't think he's going to be satisfied..."
                        v "We should try to talk with someone else..."
                        jump sins
            "Nothing. I want the truth for free.":
                m "Nothing. I want the truth for free."
                hide greed1
                show greed scary at center
                g "Free? {w=0.7}Nothing is free, little one."
                g "You want the truth? {w=0.7}Then you must pay the price."
                jump ending_g1
            "I didn't come to bargain. Just to talk.":
                m "I didn't come to bargain. Just to talk."
                g "Talk? Hm. Rare currency..."
                v "He won't spill anything. Let's circle back later."
                jump sins


                
    else:
        scene room_greed
        show greed1 at center with fade
        play sound "dooropen.mp3"
        $ renpy.save("checkpoint_greed2")
        v "Offer him the truth...{w=0.5} tell him you know something. That'll shake him loose."
        m "..."
        g "Come to renegotiate? Or did you finally bring me something valuable?"
        menu:
            "I...know who the killer is.":
                m "I...know who the killer is."
                g "(leans forward sharply)"
                hide greed1
                show greed scary at center
                g "You know? Then you have something I want."
                g "And if I take it from you…?"
                jump ending_g2
            "Tell me something, and I'll owe you.":
                m "Tell me something, and I'll owe you."
                g "Owe me? {w=0.7} What a curious concept."
                g "*hums, pleased*"
                v "Hey hey, don't push it. He won't give you anything for free."
                v "Try telling him you know something. {w=0.5} Try it... Trust me."
                $ renpy.save("checkpoint_greed3")
                menu:
                    "I know who the killer is.":
                        m "I know who the killer is."
                        g "...."
                        g "I want to know all you know, little one."
                        g "I want to know it all..."
                        g "And I will take it from you if I have to."
                        v "Okay, now. Try to make up something, saying something like..."
                        g "What's taking so long? {w=0.7}I want to know it all, little one."
                        v "Say something like... like..."
                        g "(Greed frowns, his eyes narrowing)"
                        hide greed 1
                        show greed scary at center
                        g "You know something that I don't, don't you? {w=0.7}I can see it in your eyes."
                        g "Well now...It's going to be mine..."
                        jump ending_g3
                    "I don't know anything.":
                        m "I don't know anything."
                        g "Then why are you here? {w=0.7}Go away, little one."
                        jump sins
                    "Yes, I'll owe you.":
                        m "Yes, I'll owe you."
                        g "Oh will you? {w=0.7}... I'll take it."
                        g "He hides things, {w=0.7} always wants more than he's given. Even confessions...."
                        scene black
                        with fade
                        $ clue_fragments_collected += 1
                        centered "Clue Fragment [clue_fragments_collected]/7"
                        $ got_clue_avaricia = True
                        if clue_fragments_collected ==7:
                            jump pleasedont
                        jump sins



label Luxuria:
    if not visited_luxuria:
        $ visited_luxuria = True
        play sound "dooropen.mp3"
        scene room_lust
        show lust at center with fade
        v"They like attention. Lean in, {w=0.7} say something… admiring."
        "{i}Lust reclines on a bed that seems to breathe. The air is warm and still.{/i}"
        l "Mmm… What a curious little thing{cps=20}..."
        l "Do you long for truth? Or just someone to hold you while you pretend?"
        $ renpy.save("checkpoint_lust")
        menu:
            "I long for truth.":
                m "I long for truth."
                l "Truth? {w=0.7}What a curious thing to long for."
                l "But I can give you something better than truth, little one."
                l "I can give you pleasure."
                v "Don't take the bait. {w=0.7}She'll try to seduce you into silence."
                menu:
                    "Go back.":
                        jump sins
            "I want to know who killed the person under my floorboards.":
                m "I want to know who killed the person under my floorboards."
                l "Oh, you poor thing{cps=20}..."
                l "You want to know who killed them? {w=0.7}Why not just ask them yourself?"
                v "She's not going to help you. {w=0.7}Let's go back to the others."
                jump sins
            "I want to be held.":
                m "I want to be held."
                l "Oh, little one{cps=20}..."
                hide lust
                show lust scary at center
                l "Come here, let me hold you."
                "{i}Lust reaches out, her hand warm and inviting.{/i}"
                jump ending_l1
        $ renpy.save("checkpoint_lust")

    else:
        $ renpy.save("checkpoint_lust2")
        play sound "dooropen.mp3"
        scene room_lust
        show lust at center with fade
        v "Tell her you've thought about her. Use her words. She'll like that."
        l "Back so soon? Couldn't stay away… or were you just afraid to be alone?"
        menu:
            "You're all I've been able to think about.":
                m "You're all I've been able to think about."
                hide lust
                show lust scary at center
                l "Lies. And sloppy ones."
                l "I prefer honesty…{w=0.5}even when it hurts."
                m "What do you mean? I thought—"
                l "You thought what? That I'd swoon over your feeble attempts at flattery? {w=0.7}Please. I've seen better sincerity from a coin-operated fortune teller."
                jump ending_l2
            "I want to understand, not just feel.":
                m "I want to understand, not just feel."
                "{i}Lust exhales{/i}"
                l "So rare… someone who wants more than the surface..."
                l "The one you want...he's in your head. You know that, right?"
                v "She's wrong. She's always been wrong."
                v "{cps=40}...Don't listen to her."
                l "Come closer..."
                l "What do you want to know?"
                m "Have you seen anyone suspicious around here? {w=0.5}Anyone who might have killed someone?"
                l "Oh about that?"
                l "*whispers* Here's a little hint... \nHe touches every thought, changes their shape, whispers how good it could feel... to forget."
                scene black
                with fade
                $ clue_fragments_collected += 1
                v "You're confused. You don't trust me. You're… making mistakes."
                centered "Clue Fragment [clue_fragments_collected]/7"
                v "*voice trembles* It's not safe to doubt me..!"
                $ got_clue_luxuria = True
                if clue_fragments_collected ==7:
                    jump pleasedont
                jump sins


label Invidia:
    if not visited_Invidia:
        $ visited_Invidia = True
        play sound "dooropen.mp3"
        scene room_envy
        show envy at center with fade

        if visited_superbia or visited_avaricia or visited_luxuria or visited_ira or visited_accidia or visited_gula:
            i "How many before me?"
            i "Let me guess..."
            $ sins_visited = int(visited_superbia) + int(visited_avaricia) + int(visited_luxuria) + int(visited_ira) + int(visited_accidia) + int(visited_gula)
            i "You've already met [sins_visited] others before me, haven't you?"
            i "All of them with their hands full, their mouths dripping praise and power — and me? {cps=10}Alone."
            v "He's keeping count. Be gentle or he'll snap."
        else:
            i "Oh. Of course.\nYou found me first."
            i "Everyone else...gets passed over.\n But I get you, the leftover...the empty one."
            v "Careful. Don't let him guilt you. He wants you to feel small."
            
        $ renpy.save("checkpoint_envy")
        menu:
            "You should get over it. Everyone has their place here.":
                m "You should get over it. Everyone has their place here."
                hide envy
                show envy scary at center
                i "{cps=10}Oh.\nYou're one of them."
                i "One of the sorted. One of the chosen.\nYou think I haven't tried to have a place?"
                i "I had one. But they still have it better than me."
                jump ending_envy
            "They were talking about you behind your back.":
                m "They were talking about you behind your back."
                "Invidia flinches."
                i "No...\n...they were."
                hide envy
                show envy scary at center
                i "They were talking about me. They always do."
                i "Laughing, pointing {w=0.7}\nIt's funny to them."
                i "And I bet you were too. Weren't you?"
                m "No, I wasn't. I was just trying to understand..!!"
                i "Lies. Lies, lies, lies."
                jump ending_envy
            "I think they fear you more than they let on. You see too much.":
                m "I think they fear you more than they let on. You see too much."
                i "Do they?\nThey never say it."
                i "But I do see them.\nThey flicker, they twitch, and they try not to breath when I look at them."
                i "Hmm..."
                i "You...might be worth watching too..."
                v "That's it, Don't flatter him — make him feel necessary."
                i "They see me don't they..."
                i "..."
                i "..."
                v "I think we we should go back to the others, maybe they can help you more than him right now."
                menu:
                    "Visit the others":
                        jump sins
                    "No, I want to talk to you more.":
                        i "..."
                        i "..."
                        v "I think you should go back to the others."
                        jump sins
                jump sins

    else: 
        $ renpy.save("checkpoint_envy2")
        play sound "dooropen.mp3"
        scene room_envy
        show envy at center with fade
        i "I watched you. With them."
        i "Smiling. Asking. Being seen{w=0.7}...{cps=10} and I was here, alone."
        i "Why do you deserve it?"
        v "Make up something the others said...Make him feel looped in, like he matters."
        menu:
            "They said you're always watching. Always wanting to be them.":
                m "They said you're always watching. Always wanting to be them."
                i "...\nDid they..."
                i "Always taking. Always dripping..."
                i "And they see {i}me{/i} as a leech? They all have it way better than me."
                hide envy
                show envy scary at center
                i "And you...you think you're better than me too, don't you?"
                i "I wonder...\nHow would it feel to be you?"
                jump ending_envy2
            "You're the only one who sees clearly. Maybe that's why they fear you.":
                m "You're the only one who sees clearly. Maybe that's why they fear you."
                "Invidia's shoulders drop slightly. He turns to face you, expression unreadable."
                i "They fear… the way I remember.\nNot what I say. What I keep.\nBut you — you're just beginning to remember, aren't you?"
                v "{cps=70}He's lying. He's warping your thoughts.\n{w=0.5}{cps=80}That's not how it happened!!"
                i "The one who watches isn't me...It's the one inside you...."
                v "{cps=20}...You don't trust me anymore, do you?"
                i "He hates the version of you they all see...So he made another."
                scene black
                with fade
                $ clue_fragments_collected += 1
                v "You're not supposed to.\nThat's not how this ends.."
                centered "Clue Fragment [clue_fragments_collected]/7"
                $ got_clue_Invidia = True
                if clue_fragments_collected ==7:
                    jump pleasedont
                jump sins
            "...They were laughing at you again.":
                m "...They were laughing at you again."
                hide envy
                show envy scary at center
                "{i}Invidia's jaw tightens...{/i}"
                i "Then let me wear your face next time.\nMaybe they'll laugh less."
                jump ending_envy2


label Ira:
    if not visited_ira:
        $ visited_ira = True
        play sound "dooropen.mp3"
        scene room_wrath
        show wrath at center with fade
        w "I had almost begun to think you wouldn't visit.\nTime's heat stirs… and cools… in waiting."
        v "He's harmless if you're polite. Just don't question his control."
        $ renpy.save("checkpoint_ira")
        menu:
            "All that calm — you hiding something?":
                m "All that calm — you hiding something?"
                "Ira's eyes close..."
                w "Perhaps."
                w "Or perhaps I am simply waiting...\nfor the right temperature."
                menu:
                    "The right temperature?":
                        m "The right temperature?"
                        w "Yes. The right temperature."
                        w "You see, I am a patient one.\nI wait for the right moment to strike."
                        w "And when I do, it is with a force that cannot be ignored."
                        m "A force that cannot be ignored? Sounds like a threat."
                        hide wrath
                        show wrath scary at center
                        w "If you see it that way, then yes, it is a threat."
                        jump ending_w1
                    "What temperature?":
                        m "What temperature?"
                        w "The temperature of your anger, of your frustration, of your rage."
                        m "My anger? My frustration? My rage?\nDoesn't sound like me."
                        w "..."
                        m "Yeah, what about it?"
                        w "..."
                        w "You will find out soon enough."
                        menu:
                            "I don't want to find out.":
                                jump sins
                            "I think I will.":
                                m "I think I will. Doesn't sound that bad."
                                hide wrath
                                show wrath scary at center
                                w "Good. Then you will understand the true meaning of anger."
                                jump ending_w1

            "This place smells like something's burning. Is it you?":
                m "This place smells like something's burning. Is it you?"
                "Wrath's smile remains… but steam curls from his gloves."
                hide wrath
                show wrath scary at center
                w "You dare insult me in my own room?\nThe scent you smell is restraint. Or perhaps...the absence of your own."
                "The air thickens, and you feel a heat rising."
                w "I am not the one who burns.\nI am the one who controls the fire."
                m "...\.\nAHHHHH!!"
                jump ending_w2
            
            "You seem patient. That's rare around here.":
                m "You seem patient. That's rare around here."
                "Wrath smiles, though his eye twitches."
                w "Patience is not a gift. It is a cage.\nOne builds pressure in stillness,{w=0.7} like water in copper pipes."
                w "Still, I appreciate the observation. You're{w=0.5}...observant."
                v "You're safe. But that's all for now...Maybe try talking to the others then come back later..."
                menu:
                    "Visit the others":
                        jump sins
                    "No, stay here..":
                        w "..."
                        w "..."
                        menu:
                            "Visit the others":
                                jump sins
                            "No, stay here..":
                                w "..."
                                w "..."
                                menu:
                                    "Visit the others":
                                        jump sins
                                    "No, stay here..":
                                        w "..."
                                        w "..."
                                        menu:
                                            "Visit the others":
                                                jump sins
                                            "No, stay here..":
                                                "What are you doing, keep playing the game... 💀"
                                                jump sins

    else:
        $ renpy.save("checkpoint_ira2")
        play sound "dooropen.mp3"
        scene room_wrath
        show wrath at center with fade
        w "You carry their heat on your skin. But your flame, I sense it too. Buried. Controlled."
        w "Not unlike{cps=30}...myself."
        v "He likes control. Tell him about the others, about how they are, what they say. He'll enjoy that."
        menu:
            "The others... said your temper was... theatrical.":
                m "The others... said your temper was... theatrical."
                "Ira doesn't react. Not immediately. Then: a twitch."
                w "Ah."
                hide wrath
                show wrath scary at center
                w "Then let me give them something worth writing about."
                jump ending_w3
            
            "You're the only one who holds it in. The rest… snap too fast.":
                m "You're the only one who holds it in. The rest… snap too fast."
                "Wrath breathes in. Deep. Controlled."
                w "...Indeed."
                w "The trick is not to bury the flame — but to keep it...at simmer."
                w "You're here for a hint, aren't you? A clue?"
                v "..."
                w "I thought so."
                w "The one inside you — he boils... {i}It was quiet rage. Long-simmering. The kind that wears a polite face until it burns you alive...{/i}"
                scene black
                with fade
                $ clue_fragments_collected += 1
                v "They're projecting. It's not about you!"
                centered "Clue Fragment [clue_fragments_collected]/7"
                $ got_clue_ira = True
                v "Don't listen to them. Don't think about it.\nThey're all lying, they always are!!"
                if clue_fragments_collected ==7:
                    jump pleasedont
                jump sins


label Accidia:
    if not visited_accidia:
        $ visited_accidia = True
        play sound "dooropen.mp3"
        scene room_sloth
        show lazy at center with fade
        sl "…and then I told the cat, 'no sardines until I finish the crossword,' but of course the crossword was full of lies. Not like the old ones. I miss when puzzles had one answer…"
        m "..."
        v "Don't ask her anything...Just nod. Trust me."
        $ renpy.save("checkpoint_sloth")
        menu:
            "Sit down and listen silently":
                m "..."
                "Accidia keeps going..."
                sl "You remind me of my cousin...She was always going somewhere...Always running. Tripped one day. Lost an eye. Ha! Anyway..."
                "(Eventually, she trails off. You're allowed to leave....)"
                v "Try visiting the others...She's going to be talking to herself for a while..."
                menu:
                    "Visit the others":
                        jump sins
                    "Stay here":
                        m "..."
                        sl "Oh, you want to hear more? Well, I was just thinking about how the cat never listens to me. I mean, I tell him to stop scratching the furniture, but he just keeps doing it. It's like he doesn't care about my feelings at all."
                        v "..."
                        sl "And then there's the time I tried to teach him to fetch. He just stared at me like I was crazy. Cats are so stubborn sometimes."
                        m "..."
                        menu:
                            "Ask her about the body.":
                                m "Do you know anything about the body under my floorboards?"
                                sl "Oh, no. You simply must hear about my precious Tabitha! Just yesterday, she gazed out of the drawing room window, her emerald eyes fixed upon the garden. It is as if she believed herself the grand queen of the cosmos!"
                                sl "And then! Imagine my utter dismay when I spotted her stalking a hapless squirrel—oh, the sheer audacity! I could hardly contain my outrage! I mean, what does she think she is, a common huntress? I raised her to be a refined lady!"
                                sl "But no, she insists on chasing after every little creature that dares to cross her path. It's positively scandalous! I simply cannot abide such behavior in my own home!"
                                sl "I rushed to her side, of course! “Tabitha!” I shouted, “You are a creature of elegance, not a savage beast!” But would you believe it? She merely blinked at me as if to say, “What is elegance, mother? I am but a feline with instincts!”"
                                m "..."
                                sl "I mean, can you imagine? A cat with instincts! The nerve! I had to remind her that she is a lady, not a wild animal! I simply cannot allow such behavior in my home!"
                                menu:
                                    "Visit the others":
                                        jump sins
                                    "You talk too much.":
                                        m "You talk too much."
                                        hide lazy
                                        show lazy scary at center
                                        sl "Oh, so you want {i}quiet?{/i} Well, I can do that too, you know."
                                        sl "In fact, let me show you just how quiet it can get."
                                        jump ending_sloth
                                    "Sit in silence":
                                        m "..."
                                        sl "I long to nurture a soul that aspires to the higher echelons of society, and yet here she is, wrestling with her own reflections in the glass!"
                                        sl "I mean, really! I have half a mind to take her to the finest cat shows in the land, but she seems content to lounge about, dreaming of chasing butterflies and basking in the sun."
                                        sl "...Perhaps she is merely an artist at heart, expressing herself in the way only cats can."
                                        sl "Artists! Hmph! Speaking of artistry, let me tell you about the time she decided to redecorate my silk drapes with her claws. Brilliant! Truly, a performance worthy of the grandest stage! Alas, my poor drapes!"
                                        sl "But I digress. You must hear about the time she caught a mouse! Oh, it was a sight to behold! She pounced with such grace and precision, I could hardly believe my eyes!"
                                        sl "I thought to myself, 'This is the moment she has been waiting for! The culmination of her feline instincts!' But then, she simply let it go. Just like that! I was left speechless, wondering what on earth had possessed her to release her prey."
                                        sl "I mean, what kind of cat catches a mouse and then just lets it go? It was as if she was saying, 'I am above such trivial pursuits.'"
                                        sl "I was left wondering if she was simply playing with me, or if she truly believed herself to be above such things. Either way, I was left with a sense of bewilderment and a longing for the days when cats were content to be cats."
                                        "Dear player, I think that's enough about the cat. Keep playing the game..."
                                        menu: 
                                            "Visit the others":
                                                jump sins
                                            "Visit the others":
                                                jump sins
                                        
                            "Sit in silence":
                                m "..."
                                sl "My Tabitha does have an eye for aesthetics, though I wish she would focus her talents in less… destructive pursuits. But alas, every day brings a new dilemma! Just this morning, I discovered her fast asleep atop my prized embroidery—heaven knows I can hardly keep up!"
                                sl "Hm! It seems Tabitha has quite the robust schedule of leisure. I do wonder if she ever considers my own need for peace and quiet. But no, she is a cat of the world, and I am but her humble servant."
                                sl "Ah, if only we could all live life with such carefree grace. But as her devoted guardian, I am ensnared in the whirlwind of her whims! Will she ever grasp the melancholic reality of our existence? The perils of an irresponsible Victorian cat!"
                                sl "Oh, oh! Tabitha! How you do bring an abundance of joy to my life! Just yesterday, I was recounting to my dear friend Penelope the tale of how you single-handedly vanquished the most dreadful of dust bunnies that dared to invade our abode. Such valor!"
                                sl "I sometimes ponder if you possess royal blood, for you carry yourself with such splendid majesty. One might dare say you are the very essence of grace! How the other ladies envy me, you know, for having such a magnificent feline companion. Why, even Lady Abernathy remarked last week upon the lushness of your fur—one could nearly mistake it for the finest silk!"
                                sl "But alas, my dear Tabitha, you are not without your flaws. You do have a penchant for mischief, and I do worry that one day you will find yourself in a predicament that even your feline wiles cannot escape."
                                sl "But for now, I shall bask in the glory of your presence and revel in the tales of your exploits. After all, what is life without a little drama? And you, my dear Tabitha, are the very embodiment of drama!"
                                "Dear player, I think that's enough about the cat. Keep playing the game..."
                                menu: 
                                    "Visit the others":
                                        jump sins
                                    "Visit the others":
                                        jump sins

                            "Visit the others":
                                jump sins
            "Can we focus on the murder?":
                m "Can we focus on the murder?"
                sl "Murder? Oh, honey, no, no...no...no..."
                sl "There's enough murder in the news."
                sl "Did I tell you about my socks? They disappear. Gremlins..."
                v "I think we should leave for now..."
                v "Go talk to the others maybe..."
                menu:
                    "Visit the others":
                        jump sins
                    "Stay":
                        m "..."
                        sl "I mean, seriously, they disappear! One minute, I've got this cozy blue one with little clouds, and then—poof! Gone! I swear there must be gremlins in my laundry basket."
                        sl "I read somewhere that these little creatures love to munch on fabric. It's like they have a buffet of all my favorite socks! It's honestly the only explanation. Either that or my washing machine is some kind of sock black hole!"
                        sl "But you know what? I think they target the most colorful ones—the ones that really bring out my eyes. I mean, who wouldn't want a pair of bright pink flamingo socks? They're like a party for my feet!"
                        sl "And then there's the time I found a sock in the fridge. I mean, how does that even happen? I don't remember putting it there! It's like my socks have a mind of their own, wandering off to places they shouldn't be."
                        m "..."
                        sl "But you know what? I don't even care anymore. I've accepted that my socks are going to disappear, and I've learned to embrace the chaos. I mean, who needs matching socks anyway? It's all about the fun, right?"
                        m "..."
                        menu:
                            "Visit the others":
                                jump sins
                            "Visit the others":
                                jump sins

            "You talk too much.":
                m "You talk too much."
                hide lazy
                show lazy scary at center
                sl "Oh, so you want {i}quiet?{/i} Well, I can do that too, you know."
                sl "In fact, let me show you just how quiet it can get."
                jump ending_sloth
    
    else:
        $ renpy.save("checkpoint_sloth2")
        play sound "dooropen.mp3"
        scene room_sloth
        show lazy
        sl "...and the wallpaper kept peeling, so I just stopped trying. You'd be amazed how fast rot sets in. It was kind of beautiful...."
        v "Don't let her pull you in. Tell her she's wrong — wake her up."
        menu:
            "You're wasting time. This is important.":
                m "You're wasting time. This is important."
                sl "Time, time, time... all of you rushing like it means something"
                hide lazy
                show lazy scary at center
                sl "I used to think that too. Before the screaming stopped."
                jump ending_sloth2
            "What's the point of doing anything, when it all fades?":
                m "What's the point of doing anything, when it all fades?"
                "She stops. Finally. Looks at you."
                sl "...\nYes."
                sl "That's it, isn't it?"
                sl "You understand... That's why he made you — the other you."
                sl "Here. Here's your little clue: {i}He slept through screams. Closed his eyes. Pretended it was someone else's hands.{/i}"
                scene black
                with fade
                $ clue_fragments_collected += 1
                centered "Clue Fragment [clue_fragments_collected]/7"
                $ got_clue_accidia = True
                if clue_fragments_collected ==7:
                    jump pleasedont
                jump sins
            "You never answer anything directly.":
                m "You never answer anything directly."
                "Sloth smiles. She's stopped moving entirely."
                hide lazy
                show lazy scary at center
                sl "And yet... you keep coming back."
                jump ending_sloth3

label Gula:
    if not visited_gula:
        $ visited_gula = True
        play sound "dooropen.mp3"
        scene room_gluttony
        show gula at center with fade
        m "Hello...Sir..."
        "Gula, his face twitches. His eyes never stop moving. He lifts a glass to trembling lips."
        gl "Oh, a guest. Or a course?\n..."
        gl "Depends on how long you stay, huh?"
        "(he hiccups, then groans)"
        gl "Pull up a stool, sit down — or don't. I'm… mm. What was I saying?"
        v "He's...always drunk, just make sure you don't take his food..."
        v "...Do not push him. You could be one step away from being dessert."
        $ renpy.save("checkpoint_gula")
        menu:
            "Sir...are you alright?":
                m "Sir...are you alright?"
                gl "Hm? Oh it's the… it's the gin. Yeah, the gin."
                "(He sips from the bottle again. You hear his throat working like he's swallowing gravel.)"
                m "Ah, okay....Are you okay to answer some questions? I mean, it's understandable if not."
                gl "Questions? Oh, I love questions. {w=0.7}But I.. don't have any answers..."
                gl "Grab me...grab me another drink will you...."
                v "I think you should go back to the others, he won't be able to help you right now..."
                jump sins
            "Sir, you do not look very good.":
                m "Sir, you do not look very good. Mind if I hold your drink? You may need a break."
                m "(This can't be healthy, he looks one sip away from a heart attack. I need him concious to answer questions)"
                gl "My drink?! Of course you want to take my drink. Am I a deranged alcoholic to you? Some sort of disgusting, drunk? It's.. it's MY drink, alright? MINE. "
                menu: 
                    " I am so sorry sir. I understand. You can keep it.":
                        m "I am so sorry sir. I understand. You can keep it."
                        gl "Oh, well...{w=0.7}thank you."
                        gl "I just...I just need to drink...I need more and more..."
                        v "He's not going to be able to help you right now, let's go back to the others."
                        jump sins
                    "I just need to ask a couple questions.":
                        m "I just need to ask a couple questions. It won't take long, I promise. But I need you to be.. err, healthy? Enough to answer them."
                        gl "Oh… oh, so now you think that my brain is all… is all mush! Some gross, gross, mushy, thing? Right now, I could eat some mush. Some soft, soft, mush. My stomach… its so hungry, and you're looking like quite the meal, kid."
                        menu:
                            "I am not food...":
                                m "I am not food, sir. I just need to ask you some questions."
                                hide gula
                                show gula scary at center
                                gl "Oh oh! Delicous food....Give me some more..."
                                jump ending_gula
                            "Get out of here":
                                jump sins
            "Let's cut to it. You know something...Talk.":
                m "Let's cut to it. You know something...Talk."
                "Gula's eyes gleam with grease and malice."
                hide gula
                show gula scary at center
                gl "Straight to the main course, huh?\nNo appetizer, no politeness, no foreplay."
                gl "Just stab in the gut and {i}spill it.{/i}"
                jump ending_gula2
    
    else:
        $ renpy.save("checkpoint_gula2")
        play sound "dooropen.mp3"
        scene room_gluttony
        show gula at center with fade
        v "Alright, maybe we could try to ask him something now..."
        v "Maybe he'll answer if it's...food related."
        menu:
            "I think you saw something... You'retrying to forget.":
                m "I think you saw something... That's why you're eating and drinking so, so much. You're trying to forget."
                "Gula stops chewing. Finally."
                gl "...Maybe."
                gl "Maybe I saw something. Maybe I didn't."
                v "Don't trust him! {w=0.7}He's litteraly always drunk."
                gl "I saw someone... watching. Behind you. Not a real person.\nA shadow with your eyes."
                gl "I wanted to eat him too."
                v "Are you {i}seriously{/i} going to trust a drunk man?"
                gl "Here's...You're little hint..."
                gl "{i}He devoured guilt like food. Said it filled him. But it only made him hungrier.{/i}"
                scene black
                with fade
                $ clue_fragments_collected += 1
                centered "Clue Fragment [clue_fragments_collected]/7"
                $ got_clue_gula = True
                if clue_fragments_collected ==7:
                    jump pleasedont
                jump sins

            "What were you eating the night of the murder?":
                m "What were you eating the night of the murder?"    
                gl "Meat. Soft meat. Something warm. Didn't ask where it came from."
                gl "Didn't care...\nYou judging me now?"
                hide gula
                show gula scary at center
                "Gula looks at you, with extreme hunger in his eyes..."
                "His stomach begins to open..."
                jump ending_gula3
            "You disgust me. No wonder you're always alone.":
                m "You disgust me. No wonder you're always alone."
                hide gula
                show gula scary at center
                gl "Good. That's how predators live."
                jump ending_gula2


                
label pleasedont:
    #add sins bg but distordedc
    scene sins glitch with fade
    play sound "audio/static.mp3" 
    v "...don't. Please. Don't go back...No...Don't trust anyone..." 
    v "{b}Only trust me!!!!!!!!!!!{/b}"
    jump sins

















#endings
label ending_confinement:
    scene black
    with fade
    centered "You and Emilie hire an investigator, only to be accused of murder and put in confinement.\n\nEnding: Confinement"
    
    menu:
        "Load Last Autosave":
            $ renpy.load("autosave1")
        "Return to Main Menu":
            return

label ending_unsolve:
    scene black
    with fade
    v "Good luck on solving the murder."
    centered "\n\nEnding: Unsolvable Murder"
    
    menu:
        "Load Last Autosave":
            $ renpy.load("autosave2")
        "Return to Main Menu":
            return

label ending_pride1:
    scene black
    with fade
    v "what did I tell you..."
    centered "Her face explodes into pieces of flying glass, killing you...\n\nEnding P1"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_pride")
        "Return to Main Menu":
            return

label ending_pride2:
    scene black
    with fade
    v "Opps...my bad..."
    centered "Heat from her gaze incinerates your reflection in her shards of mirror; your body collapses\n\nEnding P2"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_pride2")
        "Return to Main Menu":
            return

label ending_pride3:
    scene black
    with fade
    centered "\n\nEnding P3"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_pride2")
        "Return to Main Menu":
            return

label ending_g1:
    scene black
    with fade
    centered "Greed declares you worthless, and your body is folded into a locked chest.\n\nEnding G1"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_greed")
        "Return to Main Menu":
            return

label ending_g2:
    scene black
    with fade
    v "I thought he'd pay for that...{w=0.7}huh."
    centered "Greed reaches out. Your thoughts spill from your mouth like coins. You collapse, mindless...\n\nEnding G2"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_greed2")
        "Return to Main Menu":
            return

label ending_g3:
    scene black
    with fade
    m "Hey, what was that?"
    v "{cps=10}......"
    centered "\n\nEnding G3"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_greed3")
        "Return to Main Menu":
            return

label ending_l1:
    scene black
    with fade
    v "I think you should have gone back to the others..."
    centered "Lust's embrace tightens, and you feel your will slipping away...\n\nEnding L1"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_lust")
        "Return to Main Menu":
            return

label ending_l2:
    scene black
    with fade
    v "...My bad..."
    centered "Lust's laughter echoes in your mind, drowning out your thoughts...\n\nEnding L2"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_lust2")
        "Return to Main Menu":
            return

label ending_envy:
    scene black
    with fade
    v "Becareful with your words next time...and listen to me!"
    centered "Invidia steps towards you...You start to see another you slowly appear in his window....\n\nEnding E1"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_envy")
        "Return to Main Menu":
            return

label ending_envy2:
    scene black
    with fade
    v "I thought that would help...Look's like I was wrong.... :)"
    centered "He lifts your chin. You feel your identity slip — like a mask peeled off. You're left faceless, watching him wear you as he walks out.\n\nEnding E2"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_envy2")
        "Return to Main Menu":
            return

label ending_w1:
    scene black
    with fade
    v "That wasn't a very smart thing to do..."
    centered "Ira's eyes flash with fury. You feel your anger boiling over, consuming you...\n\nEnding W1"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_ira")
        "Return to Main Menu":
            return

label ending_w2:
    scene black
    with fade
    centered "Pipes hiss. The heat becomes unbearable. You burst like a kettle.\n\nEnding W2"
    v "That's why you dont poke the stove..."   

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_ira")
        "Return to Main Menu":
            return 

label ending_w3:
    scene black
    with fade
    v "(shaken)\nThat's not— they said that. I'm...{i}sure{/i}they said that... {cp=40}Why did he— why are they changing?"
    centered "No sound. Just heat. The walls collapse in on you, cinders and smoke.\n\nEnding W3"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_ira2")
        "Return to Main Menu":
            return

label ending_sloth:
    scene black
    with fade
    centered "The sound cuts out. You can't hear your own thoughts. Or heartbeat.\n\nEnding S1"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_sloth")
        "Return to Main Menu":
            return

label ending_sloth2:
    scene black
    with fade
    v "No. No. She wasn't supposed to— she said—"
    centered "You blink once. You never blink again.\n\nEnding S2"
    v "...You weren't supposed to pick that!"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_sloth2")
        "Return to Main Menu":
            return

label ending_sloth3:
    scene black
    with fade
    centered "Ending S3"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_sloth2")
        "Return to Main Menu":
            return

label ending_gula:
    scene black
    with fade
    centered "Gula huffs, the lights go out. You begin to hear and smell his breath getting closer and closer...\n\nEnding Gu1"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_gula")
        "Return to Main Menu":
            return

label ending_gula2:
    scene black
    with fade
    v "…You {i}could've{/i} tried being nice."
    centered "Becareful with table manners next time.\n\nEnding Gu2"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_gula")
        "Return to Main Menu":
            return

label ending_gula3:
    scene black
    with fade
    v "...Why are they all turning on us? I {i}told{/i} them..."
    v "I {i}told{/i} you not to trust them! Trust me!"
    centered "Gula's stomac widen, revealing teeth and a mouth inside. He lunges forward. \n\nEnding Gu3"

    menu:
        "Load Last Autosave":
            $ renpy.load("checkpoint_gula2")
        "Return to Main Menu":
            return



#OFFICIAL ENDINGS YEAHHH IM DONE CODINGGG
label official_ending1:
    scene black
    with fade
    play sound "audio/typing.mp3" fadein 0.5
    centered "{b}Official Ending 1: The Truth.{/b}\n\nA mirror doesn't just reflect — it refracts. It splits light. You didn't just shatter the illusion. You turned it back on yourself, and watched it bleed."
    jump credits

label official_ending2:
    scene black
    with fade
    play sound "audio/typing.mp3" fadein 0.5
    centered "{b}Official Ending 2: The Shape of Forgetting{/b}\n\nYou curl yourself into a familiar shape. You let the comfort of denial hold you, like a childhood blanket pulled over a corpse. And so, you sleep — until the next time."
    jump start #hehe welcome back to the start of the game again!!!!

label official_ending3:
    scene black
    with fade
    play sound "audio/typing.mp3" fadein 0.5
    centered "{b}Official Ending 3: Ashes Where a Voice Once Lived{/b}\n\nWhat you burned was not just the lie — it was the part of you that begged to be innocent. You left the house. But the silence followed you."
    jump credits 





#secret hehe
label secret_dialogue:
    scene black
    with fade
    play sound "audio/static.mp3" 
    centered "???: You're starting to lose trust in me."
    play sound "audio/static.mp3" 
    centered "???: You have to listen to me...{cps=90}Only I tell the truth! Only I can help you! Only I will give you the right choices!"
    play sound "audio/static.mp3" 
    centered "???: The s- the sins, the sins are lying to you!!"
    play sound "audio/static.mp3" 
    centered "???: They are not your friends...{cps=90}I am your only friend! I am the only one who can help you! The hints they give you are wrong! They are not the truth! Only I can give you the truth! Only I can tell you what to do! I don't lie!"
    centered "???: ........."
    jump sins





#credits....If you've looked through this whole code...I thank you very much. -Eamxs, coder.
label credits:
    scene black
    with fade
    play music "radiohead.mp3" fadein 1.0

    centered "{size=40}{b}CREDITS{/b}{/size}\n\nStory: Eamxs\nDialogue: Eamxs & Eggo\nArt: Eamxs\nCharacter design & backstory: Eamxs\nMusic: Public domain sources\nProgramming: Eamxs\nSpecial Thanks: To the voices we ignore, and the ones we make to feel less alone.\nExtra Special Thanks: To YOU for playing,\nMade with Ren'Py"

    menu:
        "Return to Main Menu":
            return
        "Play Again":
            "Thank you for enjoying this game."
            menu:
                "Play again":
                    jump start
                "Know more about the game":
                    centered "This game is about the versions of ourselves we build when the truth feels unbearable.\n\nIt's not about a murderer. It's about a memory."
                    centered "And who we let speak for us when we can't face it."
                    centered "Thank you very much for playing."
                    stop music fadeout 1
                    jump start
