

label start:
    $ renpy.music.set_volume(0.2, 0, channel="music")
    stop voice fadeout 2
    window hide

    scene expression im.Tile("gui/settings/bg.png", size=(2020, 1080)) at bg_loop_move
    show expression (Fireflies().sm):
        xalign 0.5 yalign 0.5
    show expression im.Tile("gui/main_menu/fire.png", size=(1920, 1080)) at fire_loop_move
    show expression (Fog().sm) as fog:
        alpha 0.8 zoom 0.5
    with dlong

    stop sound fadeout 3
    $ renpy.pause(1, hard=True)

    call nvl_start (show_bg=False)
    nv "The strong will survive."
    nv "The weak will perish."
    nv "Those who cannot prove their worth deserve to die."
    nv "That is the philosophy of the Demon Realm."
    call nvl_clear
    nv "Powerful demons fight, breed, and pass on their superior blood."
    nv "Frail demons are killed to make way for their superiors."
    nv "Thus, our society grows stronger with each new generation."
    call nvl_clear
    nv "One demon always rises to be the strongest of all."
    nv "The highest authority, leading demonkind to greatness."
    nv "The Demon King."
    nv "Me."
    call nvl_clear
    nv "I, Malos, rule the Demon Realm."
    nv "Under me, our kind have become stronger than ever."
    nv "It won't be long before we conquer all other races."
    call nvl_clear
    window show
    voice "voice/malos/story/line_001.ogg"
    Malos "Ha ha ha ha..."
    window hide
    pause 0
    scene bg hall with dlong:
        zoom 0.7 xalign 0.5 yalign 0.5
        ease 8 zoom 0.5

    window show
    "I stand proudly in the great hall of my castle."
    "I have no guards by my side, even knowing that an intruder is quickly approaching."
    "I don't need them."
    "Nor do I want anyone to steal my moment of triumph."

    voice "voice/malos/story/line_002.ogg"
    Malos "Any minute now..."
    "I received word from scouts that she was heading this way."
    "She must have come intending to slay me."
    "How adorable..."
    "Humans have such strange values."
    show bg:
        ease 4 zoom 0.6

    $ renpy.music.set_volume(0.4, 0, 'sound')
    play sound footsteps
    stop music fadeout 2
    "..."
    "I hear footsteps."
    $ renpy.music.set_volume(1.0, 2, 'sound')
    play sound footsteps
    "They echo through the hall, steadily growing louder, until..."

    play music heroine fadein 1
    show dianne con stareneutral at center_right_in:
        zoom 0.61
    pause 0.4

    "She arrives."

    stop sound fadeout 1
    $ renpy.music.set_volume(1.0, 0, 'sound')
    show dianne con stareyell at center with dexp
    voice "voice/dianne/story/line_001.ogg"
    Dianne "Demon King Malos, your rule is over!"
    show dianne angryyell with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_002.ogg"
    Dianne "I am Princess Dianne, and I will be the one to end your life!"
    show dianne con angryfrown with dexp
    voice "voice/malos/story/line_003.ogg"
    Malos "Hah! Such a bold statement..."
    voice "voice/malos/story/line_004.ogg"
    Malos "But do you have the strength to back it up?"
    show dianne con staregrit with dexp:
        ease 0.5 zoom 0.61
    voice "voice/dianne/story/line_003.ogg"
    Dianne "Don't underestimate me! Your overconfidence will be your downfall!"
    "She must not know who she's talking to."
    "No human could hope to stand against a demon as powerful as me."
    show bg:
        parallel:
            ease 2 zoom 0.9
        parallel:
            easein 2 yalign 1.0
            ease 6 yalign 0.5
    show dianne:
        ease 2 zoom 0.95 yoffset -450
        ease 6 yoffset -100
    "Though I must admit, she's very attractive."
    "Even wearing that thick armor, her feminine figure shines through."
    "Her features are elegant, despite the harsh journey she took to get here."
    show bg:
        ease 4 yalign 0.5 zoom 0.6
    show dianne:
        ease 4 zoom 0.61 yoffset 0
    voice "voice/malos/story/line_005.ogg"
    Malos "Hmmmm..."
    voice "voice/malos/story/line_006.ogg"
    Malos "You have an attitude problem, Princess Dianne."
    voice "voice/malos/story/line_007.ogg"
    Malos "But still, you have potential."
    voice "voice/malos/story/line_008.ogg"
    Malos "I'll be happy to make you my slave."
    show bg:
        yalign 0.5 zoom 0.6
    show dianne angryyell:
        yoffset 0
        ease 0.5 zoom 0.68
    with dexp
    voice "voice/dianne/story/line_004.ogg"
    Dianne "Never!"
    show dianne closedfrown with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_005.ogg"
    Dianne "Your army invaded my kingdom and slaughtered my people."
    show dianne staregrit with dexp
    voice "voice/dianne/story/line_006.ogg"
    Dianne "And worst of all, you killed my father with your own hands!"
    show dianne angryyell with dexp
    voice "voice/dianne/story/line_007.ogg"
    Dianne "I'd rather die than become your slave!"
    show dianne angryfrown with dexp
    voice "voice/malos/story/line_009.ogg"
    Malos "Ha ha ha!"
    voice "voice/malos/story/line_010.ogg"
    Malos "You think you have a choice in the matter?"
    voice "voice/malos/story/line_011.ogg"
    Malos "I'll show you my true power, then."
    voice "voice/malos/story/line_012.ogg"
    Malos "Resist me, and I'll break you!"
    show dianne angryyell with dexp
    voice "voice/dianne/story/line_008.ogg"
    Dianne "I won't lose to you! I swear it!"
    show dianne standby with dpose:
        ease 0.5 zoom 0.61
    voice "voice/dianne/story/line_009.ogg"
    Dianne "Have at you, monster!"

    window hide
    call screen confirm(message=_("View battle tutorial?"), yes_action=[Hide("confirm"),Jump("tutorial")], no_action=[Hide("confirm"), Jump("boss_fight")])

label tutorial:
    "During each turn of battle, you will be given a choice between four moves: Attack, Counter, Heal, or Charge."
    "Dianne will also use these four moves, so in order to win, choose moves that are effective against hers."
    "Choosing Attack will deal 4 damage to the Dianne's health."
    "Choosing Counter will only deal 2 damage, but it will nullify Dianne's damage if she chooses Attack."
    "Choosing Heal will restore 2 health points. If Dianne chooses Charge, healing will restore an additional 3 points."
    "Choosing Charge will boost the effect of your next action."
    "After a Charge, Attack will deal 10 damage, Counter will deal 5 damage, and Heal will restore 5 health."
    "Use these moves to deplete Dianne's health and win the battle!"
    "Each time Dianne loses a certain amount of health, a story segment will show, and Dianne will use a different strategy to determine her move choices."
    "Be prepared to adapt your battle plan to her, as you try and figure out how to beat her!"
    "That's all for the tutorial, so get out there and enslave that princess! Good luck!"
    jump boss_fight







label phase_2_intro:
    call dianne_natural
    voice "voice/malos/story/line_013.ogg"
    Malos "Ha ha ha! Your efforts are futile, princess."
    voice "voice/malos/story/line_014.ogg"
    Malos "The difference in our strength is clear. Don't convince yourself that you can win."
    show dianne con closedfrown with dpose
    voice "voice/dianne/story/line_010.ogg"
    Dianne "Your words mean nothing to me, Malos!"
    show dianne con angrygrit with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_011.ogg"
    Dianne "I won't fall here, not when so many lives are at stake!"
    show dianne con stareyell with dexp:
        ease 0.5 zoom 0.63
    voice "voice/dianne/story/line_012.ogg"
    Dianne "You can't convince me to give up, so stop your prideful boasting!"
    show dianne con starefrown with dexp
    voice "voice/malos/story/line_015.ogg"
    Malos "Well, I suppose it makes no difference at this point."
    voice "voice/malos/story/line_016.ogg"
    Malos "Now that I've decided to make you my slave, it's inevitable that you will submit."
    voice "voice/malos/story/line_017.ogg"
    Malos "So go on, keep struggling in vain! It only serves to amuse me!"
    voice "voice/malos/story/line_018.ogg"
    Malos "Ha ha ha ha!"
    show dianne standby with dpose:
        ease 0.5 zoom 0.61
    voice "voice/dianne/story/line_013.ogg"
    Dianne "Laugh while you can, Malos! I'm going to end your life!"
    voice "voice/malos/story/line_019.ogg"
    Malos "Go ahead and try!"
    return



label phase_3_intro:
    show bg:
        xalign 0.5 yalign 0.5 xoffset 0 yoffset 0 zoom 0.6
    show dianne con closedfrown at center with dpose:
        alpha 1 zoom 0.61 xoffset 0 yoffset 0
    voice "voice/dianne/story/line_014.ogg"
    Dianne "Not bad, Demon King."
    voice "voice/dianne/story/line_015.ogg"
    Dianne "You're just as savage and brutal as I expected."
    voice "voice/malos/story/line_020.ogg"
    Malos "Hah! I'm glad you recognize my power."
    voice "voice/malos/story/line_021.ogg"
    Malos "You face Malos, the strongest of demons! Of course I'm no weakling!"
    show dianne con angryyell with dexp:
        ease 0.5 zoom 0.69
    voice "voice/dianne/story/line_016.ogg"
    Dianne "That wasn't a compliment, you fiend!"
    show dianne con angrygrit with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_017.ogg"
    Dianne "You may be a fierce opponent, but I {b}will{/b} defeat you!"
    voice "voice/malos/story/line_022.ogg"
    Malos "That strong will of yours is quite admirable."
    voice "voice/malos/story/line_023.ogg"
    Malos "What is the source of your strength, I wonder..."
    show dianne con stareneutral with dexp:
        ease 0.5 zoom 0.62
    voice "voice/dianne/story/line_018.ogg"
    Dianne "You'd never understand, Malos."
    show dianne con stareyell with dexp
    voice "voice/dianne/story/line_019.ogg"
    Dianne "My strength comes from hard work and effort!"
    show dianne con closedfrown with dexp
    voice "voice/dianne/story/line_020.ogg"
    Dianne "I've spent years honing my skills, and training my body..."
    show dianne con angryyell with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_022.ogg"
    Dianne "And with the power I've gained, I will slay you!"
    show dianne con angryneutral with dexp
    voice "voice/malos/story/line_024.ogg"
    Malos "Ha ha ha! What a speech!"
    voice "voice/malos/story/line_025.ogg"
    Malos "You would make a fine poet if you tried your hand."
    voice "voice/malos/story/line_026.ogg"
    Malos "But this is the real world, not fantasy."
    voice "voice/malos/story/line_027.ogg"
    Malos "No \"hard work and effort\" will be enough to kill me!"
    show dianne con angrygrit with dexp:
        ease 0.5 zoom 0.61
    voice "voice/dianne/story/line_023.ogg"
    Dianne "We'll see about that, Malos!"
    show dianne standby with dpose
    voice "voice/dianne/story/line_024.ogg"
    Dianne "I'll show you that my strength is real!"
    return



label phase_4_intro:
    show bg:
        xalign 0.5 yalign 0.5 xoffset 0 yoffset 0 zoom 0.6
    show dianne con tiredfrown at center with dpose:
        alpha 1 zoom 0.61 xoffset 0 yoffset 0
    voice "voice/dianne/story/line_025.ogg"
    Dianne "Ugh... hah... hah..."
    voice "voice/malos/story/line_028.ogg"
    Malos "You seem out of breath, Dianne..."
    voice "voice/malos/story/line_029.ogg"
    Malos "Shall I give you a moment to rest, so this is a fair fight?"
    show dianne con angrygrit with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_026.ogg"
    Dianne "I don't need your pity, Malos!"
    show dianne con angryyell with dexp:
        ease 0.5 zoom 0.68
    voice "voice/dianne/story/line_027.ogg"
    Dianne "For all the crimes you've committed, you must be slain!"
    voice "voice/malos/story/line_030.ogg"
    Malos "Crimes? Do tell."
    voice "voice/malos/story/line_031.ogg"
    Malos "What crimes have I committed?"
    show dianne con angrygrit with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_028.ogg"
    Dianne "Don't claim innocence! I've experienced your cruelty firsthand!"
    show dianne con closedyell with dexp
    voice "voice/dianne/story/line_029.ogg"
    Dianne "Because of you, my kingdom is in ruins!"
    show dianne con closedgrit with dexp
    voice "voice/dianne/story/line_030.ogg"
    Dianne "My people live in fear, knowing that demon invaders seek to kill them all!"
    show dianne con angryyell with dexp:
        ease 0.5 zoom 0.68
    voice "voice/dianne/story/line_031.ogg"
    Dianne "You killed my father, the king, right in front of me!"
    show dianne con angryfrown with dexp
    voice "voice/malos/story/line_032.ogg"
    Malos "I admit that I have done those things."
    voice "voice/malos/story/line_033.ogg"
    Malos "But tell me, how are any of them crimes?"
    voice "voice/malos/story/line_034.ogg"
    Malos "Everything I have done is allowed by the laws of the Demon Realm!"
    show dianne con widesmall with dexp:
        ease 0.5 zoom 0.63
    voice "voice/dianne/story/line_032.ogg"
    Dianne "Nonsense! That can't be true."
    show dianne con wideyell with dexp
    voice "voice/dianne/story/line_033.ogg"
    Dianne "Your laws would justify mindless slaughter?"
    show dianne con widefrown with dexp
    voice "voice/malos/story/line_035.ogg"
    Malos "But of course."
    voice "voice/malos/story/line_036.ogg"
    Malos "This world is plagued with weaklings. Only the strong deserve to survive."
    voice "voice/malos/story/line_037.ogg"
    Malos "The only way to make demonkind stronger is to eliminate any who would fall behind."
    show dianne con tiredfrown with dexp
    voice "voice/malos/story/line_038.ogg"
    Malos "You humans are too weak. You never cleanse yourself of the useless and feeble."
    voice "voice/malos/story/line_039.ogg"
    Malos "By letting them live, you bloat humankind with worthless people who could never contribute."
    voice "voice/malos/story/line_040.ogg"
    Malos "Your king was too weak to hold a sword and fight to defend his homeland."
    voice "voice/malos/story/line_041.ogg"
    Malos "By slaying him, I was doing you all a favor."
    show dianne con angrygrit with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_034.ogg"
    Dianne "Liar! My father was a kind, good man!"
    show dianne con angryyell with dexp
    voice "voice/dianne/story/line_035.ogg"
    Dianne "He couldn't fight because he spent all of his time organizing and leading our people!"
    show dianne con closedgrit with dexp
    voice "voice/dianne/story/line_036.ogg"
    Dianne "He wasn't a fighter, but he didn't deserve to die!"
    show dianne con angrygrit with dexp:
        ease 0.5 zoom 0.69
    voice "voice/dianne/story/line_037.ogg"
    Dianne "Instead, you are the one who should be killed!"
    show dianne con angryfrown with dexp
    voice "voice/dianne/story/line_038.ogg"
    Dianne "Your cruelty knows no bounds, but you see no fault in your actions."
    voice "voice/dianne/story/line_039.ogg"
    show dianne con staregrit with dexp:
        ease 0.5 zoom 0.65
    Dianne "You are a monster, and I'll never forgive you!"
    voice "voice/malos/story/line_042.ogg"
    Malos "Ha ha ha ha!"
    show dianne con angryyell with dexp
    voice "voice/dianne/story/line_040.ogg"
    Dianne "Stop laughing!"
    show dianne standby with dpose:
        ease 0.5 zoom 0.61
    voice "voice/dianne/story/line_041.ogg"
    Dianne "I'll kill you!"
    return



label phase_5_intro:
    show bg:
        xalign 0.5 yalign 0.5 xoffset 0 yoffset 0 zoom 0.6
    show dianne standby at center with dexp:
        alpha 1 zoom 0.61 xoffset 0 yoffset 0
    voice "voice/dianne/story/line_042.ogg"
    Dianne "Guh..."
    voice "voice/malos/story/line_043.ogg"
    Malos "Ha ha ha! Time for my secret move!"
    voice "voice/malos/story/line_044.ogg"
    Malos "Take this!"
    show bg:
        linear 0.1 zoom 0.68
        easeout 0.2 zoom 0.6
    show dianne:
        parallel:
            pause 0.1
            ease 0.05 xoffset 10
            ease 0.05 xoffset -10
            ease 0.05 xoffset 8
            ease 0.05 xoffset -8
            ease 0.05 xoffset 5
            ease 0.05 xoffset -5
            ease 0.05 xoffset 0
        parallel:
            linear 0.1 zoom 0.71 yoffset -40
            easeout 0.2 zoom 0.61 yoffset 0
    show dianne hurt with Dissolve(0.1)
    play sound hit2
    show bg white as whiteflash with Dissolve(0.3)
    $ clothes_ripped = True
    voice "voice/dianne/story/line_185.ogg"
    Dianne "Ugh!"
    play sound rip
    pause 0.8
    hide whiteflash with dscene
    pause 0.5
    voice "voice/dianne/story/line_044.ogg"
    Dianne "No way... not my..."
    show dianne conripped staregrit with dpose
    voice "voice/dianne/story/line_045.ogg"
    Dianne "Y-you dirty coward!"
    voice "voice/malos/story/line_045.ogg"
    Malos "Ha ha ha! What a lovely sight!"
    "As Dianne tries to maintain her fighting stance, she can't hide the fact that her breasts are exposed."
    show bg:
        parallel:
            ease 2 zoom 0.9
        parallel:
            easein 2 yalign 0.6
            ease 6 yalign 0.5
    show dianne:
        ease 2 zoom 0.95 yoffset -200
        ease 6 yoffset -100
    "Such a magnificent pair..."
    "They're quite large for a human, and completely unblemished."
    "Each time she moves, I see them bounce lightly, displaying their softness."
    show bg:
        ease 4 yalign 0.5 zoom 0.6
    show dianne:
        ease 4 zoom 0.61 yoffset 0
    voice "voice/malos/story/line_046.ogg"
    Malos "Such lewd breasts... They'll be perfect for serving me."
    voice "voice/malos/story/line_047.ogg"
    Malos "I'll have you expose everything else before we're done here."
    show dianne conripped angryyell with dexp
    voice "voice/dianne/story/line_046.ogg"
    Dianne "A-as if I'd just let you mock me!"
    show dianne conripped angryfrown with dexp
    voice "voice/dianne/story/line_047.ogg"
    Dianne "You've driven me into a corner, but I can still fight, so there's still hope!"
    voice "voice/malos/story/line_048.ogg"
    Malos "Oh my, how threatening..."
    voice "voice/malos/story/line_049.ogg"
    Malos "I'd be terrified if I couldn't plainly see your arms trembling."
    voice "voice/malos/story/line_050.ogg"
    Malos "Just admit it. There's no way you can win."
    show dianne conripped winkgrit with dexp
    voice "voice/dianne/story/line_048.ogg"
    Dianne "True, I may be losing now..."
    show dianne conripped winkyell with dexp
    voice "voice/dianne/story/line_049.ogg"
    Dianne "But I still have one more technique!"
    show dianne conripped closedfrown with dexp
    voice "voice/dianne/story/line_050.ogg"
    Dianne "I didn't want to use it, but you've given me no choice."
    show dianne charge2 with dpose
    voice "voice/dianne/story/line_051.ogg"
    Dianne "Holy sword, the bane of evil, grant me your strength!"

    $ renpy.music.set_volume(0.4, 0, 'sound')
    play sound charge
    show bg white as whiteflash with dpose
    hide whiteflash with dpose

    voice "voice/dianne/story/line_052.ogg"
    Dianne "In my hour of need, let the heavens answer my prayers, and aid me!"

    $ renpy.music.set_volume(0.7, .5, 'sound')
    play sound charge
    show bg white as whiteflash with dpose
    hide whiteflash with dpose

    voice "voice/dianne/story/line_053.ogg"
    Dianne "Awaken, and grant me the power to slay the Demon King!"

    $ renpy.music.set_volume(1.0, 0, 'sound')
    play sound charge
    show bg white as whiteflash with dscene
    show light_effect behind dianne:
        xalign 0.5 yalign 0.5 zoom 0.9
    hide whiteflash with dscene

    voice "voice/malos/story/line_051.ogg"
    Malos "What...?"
    "A white aura surrounds Dianne, casting an eerie glow that fills the room."
    "I can feel it... Her power has significantly increased."
    "Every move she makes after this will be as if she had charged it in advance."
    "Perhaps now, she'll pose more of a challenge..."
    show dianne standby with dpose
    voice "voice/dianne/story/line_054.ogg"
    Dianne "I'm done playing games now, Malos."
    voice "voice/dianne/story/line_055.ogg"
    Dianne "Die!"
    return



label ending_1:
    if _in_replay:
        $ renpy.music.set_volume(0.2, 0, channel="music")
        play music battle
        scene bg hall:
            zoom 0.6 xalign 0.5 yalign 0.5
        show expression im.Tile("images/particles/fire.png", size=(5760, 1080)) as fire_bg:
            parallel:
                xalign 0.0
                linear 20 xalign 1.0
                repeat
            parallel:
                alpha 0.1
                ease 3.2 alpha 0.3
                ease 3.2 alpha 0.1
                repeat
        show expression im.Tile("images/particles/fire.png", size=(5760, 1080)) as fire_bg2:
            parallel:
                xalign 1.0
                linear 30 xalign 0.0
                repeat
            parallel:
                alpha 0.1
                ease 5.2 alpha 0.3
                ease 5.2 alpha 0.1
                repeat
        show dianne attack2 at center:
            zoom 0.61
        with dlong
        window show
    else:
        hide screen stats_frame
        show bg:
            xalign 0.5 yalign 0.5 xoffset 0 yoffset 0 zoom 0.6
        show dianne attack2:
            alpha 1 zoom 0.61 xoffset 0 yoffset 0
        hide light_effect
        with dexp

    voice "voice/dianne/story/line_056.ogg"
    Dianne "Hyah!"
    show dianne:
        zoom 0.61 yoffset 0
        linear 0.1 zoom 0.76 yoffset 0
        easeout 0.2 zoom 0.66 yoffset -40
    show bg:
        xoffset 0
        pause 0.1
        parallel:
            ease 0.05 xoffset 15
            ease 0.05 xoffset -15
            ease 0.05 xoffset 10
            ease 0.05 xoffset -10
            ease 0.05 xoffset 6
            ease 0.05 xoffset -6
            ease 0.05 xoffset 0
        parallel:
            ease 0.3 yoffset -100
    play sound stab
    voice "voice/malos/story/line_052.ogg"
    Malos "Oof!"
    stop music fadeout 3
    "Dianne hits me with her sword, knocking me over."
    voice "voice/malos/story/line_053.ogg"
    Malos "Impudent human... You'll pay for that..."
    show dianne con closedfrown with dpose:
        ease 0.5 zoom 0.69
    voice "voice/dianne/story/line_057.ogg"
    Dianne "You can stop your foolish posturing now, Malos."
    play music heroine fadein 1
    show dianne con starefrown with dexp
    voice "voice/dianne/story/line_058.ogg"
    Dianne "Admit it! I've won."
    hide fire_bg
    hide fire_bg2
    with dpose
    "Dianne stands over me, looking down haughtily."
    voice "voice/malos/story/line_054.ogg"
    Malos "Hah. You have guts, princess."
    voice "voice/malos/story/line_055.ogg"
    Malos "But even if you stab me a hundred times, you cannot kill me."
    voice "voice/malos/story/line_056.ogg"
    Malos "Surely you know that I have the power to regenerate any wound."
    voice "voice/malos/story/line_057.ogg"
    Malos "My invincible, immortal body cannot be killed by someone like you!"
    show dianne con closedsmall with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_059.ogg"
    Dianne "Hmph."
    "Slowly, Dianne steps back."
    voice "voice/dianne/story/line_060.ogg"
    Dianne "You're right. I cannot kill you by merely stabbing you."
    show dianne con starefrown with dexp
    voice "voice/dianne/story/line_061.ogg"
    Dianne "You wouldn't be worthy of the name \"Demon King\" if that was all it took."
    show dianne con angrygrit with dexp
    voice "voice/dianne/story/line_062.ogg"
    Dianne "However, I came prepared."
    voice "voice/malos/story/line_058.ogg"
    Malos "What? You can't possibly..."
    show dianne con staresmile with dexp:
        ease 0.5 zoom 0.69
    voice "voice/dianne/story/line_063.ogg"
    Dianne "You know of the \"Ritual of Absorbing,\" don't you, Malos?"
    voice "voice/malos/story/line_059.ogg"
    Malos "It can't be! Where did you hear that name?!"
    show dianne con closedneutral with dexp:
        ease 0.5 zoom 0.66
    voice "voice/dianne/story/line_064.ogg"
    Dianne "I defeated many of your subjects on my way here, Malos."
    voice "voice/dianne/story/line_065.ogg"
    Dianne "After defeating one of your captains, I interrogated him, and he told me of it."
    show dianne con stareneutral with dexp
    voice "voice/dianne/story/line_066.ogg"
    Dianne "If you were gone, then your throne would be available for him to claim."
    show dianne con winksmile with dexp
    voice "voice/dianne/story/line_067.ogg"
    Dianne "How fitting that the Demon King would be betrayed by his own men."
    voice "voice/malos/story/line_060.ogg"
    Malos "Grrr... Accursed weakling..."
    voice "voice/malos/story/line_061.ogg"
    Malos "That traitor deserves to die!"
    show dianne con starefrown with dexp:
        ease 0.5 zoom 0.71
    voice "voice/dianne/story/line_068.ogg"
    Dianne "You won't have the chance to do anything, Malos."
    show dianne con closedneutral with dexp
    voice "voice/dianne/story/line_069.ogg"
    Dianne "Once I perform the Ritual of Absorbing, your life force will be drained away."
    show dianne con stareyell with dexp:
        ease 0.5 zoom 0.74
    voice "voice/dianne/story/line_070.ogg"
    Dianne "You'll be dead forever, and I'll gain enough power to eliminate the entire demon race!"
    show dianne con starefrown with dexp
    "The Ritual of Absorbing..."
    "If she's come here, with the intent of performing it, then..."
    voice "voice/malos/story/line_062.ogg"
    Malos "Hah. You can't fool me, princess."
    voice "voice/malos/story/line_063.ogg"
    Malos "Even if you did learn of a demon ritual, you wouldn't dare perform it."
    show dianne con closedgrit with dexp
    voice "voice/dianne/story/line_071.ogg"
    Dianne "When I left home, I swore to my people that I would slay you, or die trying."
    show dianne con angryyell with dexp:
        ease 0.5 zoom 0.79
    voice "voice/dianne/story/line_072.ogg"
    Dianne "Now that I have you at my mercy, I won't hesitate!"
    show dianne con angrygrit with dexp
    voice "voice/dianne/story/line_073.ogg"
    Dianne "Let's begin!"
    stop music fadeout 2
    window hide
    scene bg black with dscene
    $ renpy.pause(0.1, hard=True)
    pause 1
    play music ritual
    scene bg ritual:
        xalign 0.8 yalign 0.0 zoom 0.625
    show cg ritual grindangryfrown:
        xalign 0.8 yalign 0.0 zoom 0.85
    with dscene
    window show
    "After completing her preparation, Dianne stands above me."
    show cg ritual grinddownopenblush with dexp
    voice "voice/dianne/story/line_074.ogg"
    Dianne "Ah... This is..."
    show bg:
        ease 5 zoom 0.5
    show cg:
        ease 5 zoom 0.5
    "Dianne pulls down my loincloth, finding my fully-erect member."
    "It stands firmly upright while she lowers herself to take a closer look."
    show cg ritual grinddownfrownblush with dexp
    voice "voice/dianne/story/line_075.ogg"
    Dianne "So this is what it looks like..."
    show cg ritual grindavertfrownblush with dexp
    voice "voice/dianne/story/line_076.ogg"
    Dianne "It's... bigger than I was expecting."
    voice "voice/malos/story/line_064.ogg"
    Malos "Stop! Don't you dare perform the ritual!"
    show cg ritual grindangryfrown with dexp
    voice "voice/dianne/story/line_077.ogg"
    Dianne "Your struggles are in vain, Malos."
    show cg ritual grindangrygrit with dexp
    voice "voice/dianne/story/line_078.ogg"
    Dianne "I {b}will{/b} perform the ritual, and you {b}will{/b} be destroyed!"
    show bg:
        xalign 0.7 yalign 0.8
        ease 3 zoom 0.575
    show cg:
        xalign 0.7 yalign 0.8
        ease 3 zoom 0.65
    "With determination in her eyes, Dianne presses my penis between her legs."
    "Her underwear touches the sensitive shaft, lightly stimulating it."
    "Behind it, I can feel the shape of her soft, delicate skin."
    show bg:
        ease 3 xalign 0.8 yalign 0.3 zoom 0.55
    show cg ritual grindangryopen with dexp:
        ease 3 xalign 0.8 yalign 0.3 zoom 0.6
    voice "voice/dianne/story/line_079.ogg"
    Dianne "All I have to do is take your essence inside me, and speak the magic phrase..."
    show cg ritual grindangryfrown with dexp
    voice "voice/dianne/story/line_080.ogg"
    Dianne "Then, your life will be over."
    voice "voice/malos/story/line_065.ogg"
    Malos "No way... You wouldn't!"
    voice "voice/malos/story/line_066.ogg"
    Malos "You're a princess, right? I bet you're still a virgin."
    show cg ritual grindangrygrit with dexp
    voice "voice/dianne/story/line_080b.ogg"
    Dianne "I am... So what?"
    voice "voice/malos/story/line_067.ogg"
    Malos "Princesses are supposed to marry royalty, right?"
    voice "voice/malos/story/line_068.ogg"
    Malos "Your virginity is priceless for your heritage!"
    voice "voice/malos/story/line_069.ogg"
    Malos "Wasting it on a ritual will mean you can't give it to your future beloved."
    voice "voice/malos/story/line_070.ogg"
    Malos "You don't really want to give your chastity to the Demon King, do you?"
    show bg:
        ease 5 xalign 0.8 yalign 0.1 zoom 0.6
    show cg ritual grindavertgrit with dexp:
        ease 5 xalign 0.8 yalign 0.1 zoom 0.7
    voice "voice/dianne/story/line_080c.ogg"
    Dianne "I... I..."
    show cg ritual grindavertfrownblush with dexp
    Dianne "..."
    "She pauses for a moment, considering the implications of my words."
    show cg ritual grindavertopenblush with dexp
    voice "voice/dianne/story/line_080d.ogg"
    Dianne "...You're right, Malos."
    show cg ritual grindavertfrownblush with dexp
    voice "voice/dianne/story/line_080e.ogg"
    Dianne "I wanted my first time to be with someone I love."
    show cg ritual grinddownfrownblush with dexp
    voice "voice/dianne/story/line_080f.ogg"
    Dianne "But I can't let you live..."
    show cg ritual grinddowngritblush with dexp
    voice "voice/dianne/story/line_080g.ogg"
    Dianne "I hate that I have to do this, but..."
    show cg ritual grinddownopenblush with dexp
    voice "voice/dianne/story/line_080h.ogg"
    Dianne "I'll gladly sacrifice my chastity if it saves my kingdom."
    show bg:
        ease 5 xalign 0.8 yalign 0.3 zoom 0.55
    show cg ritual grinddownfrownblush with dexp:
        ease 5 xalign 0.8 yalign 0.3 zoom 0.6
    "Despite her obvious reluctance and frustration, she continues."
    voice "voice/malos/story/line_071.ogg"
    Malos "Grrr... do you not care for your pride? Your purity?"
    voice "voice/malos/story/line_072.ogg"
    Malos "Absorbing my power will corrupt you! You won't be human anymore!"
    show cg ritual grindangrygrit with dexp
    voice "voice/dianne/story/line_081.ogg"
    Dianne "Did you think I'd come this far without steeling my resolve?"
    show cg ritual grindangryopen with dexp
    voice "voice/dianne/story/line_082.ogg"
    Dianne "I don't care how far I have to lower myself. You will die today!"
    show cg ritual grindangryfrown with dexp
    "Her precious womanhood rubs against my giant, hardened penis."
    "The mound of skin surrounding it is smooth, pink, and pristine."
    "It truly is fit for a prince. She must take good care of it."
    show bg:
        ease 5 yoffset 50 zoom 0.575
    show cg:
        ease 5 yoffset 100 zoom 0.65
    voice "voice/malos/story/line_073.ogg"
    Malos "Don't do it! I forbid you!"
    voice "voice/dianne/story/line_083.ogg"
    show cg ritual grindangryopen with dexp
    Dianne "Stop protesting! You can't stop me!"
    show cg ritual grindangrygrit with dexp
    voice "voice/dianne/story/line_084.ogg"
    Dianne "For my people, I must do it!"
    "Determined, she aligns her virgin slit against my large, throbbing member."
    "In a single motion, she pushes her hips down, taking the length inside of her."
    show bg:
        ease 0.6 yoffset 0 yalign 1.0 zoom 0.5325
    show cg:
        parallel:
            easeout 0.4 yoffset 0 yalign 1.0 zoom 0.575
        parallel:
            pause 0.4
            ease 0.04 xoffset 10
            ease 0.04 xoffset -10
            ease 0.04 xoffset 5
            ease 0.04 xoffset -5
            ease 0.04 xoffset 3
            ease 0.04 xoffset -3
            ease 0.04 xoffset 0
    show cg ritual midweakopenblush with dexp
    play sound [ "<silence 0.2>", insert]
    voice "voice/dianne/story/line_085.ogg"
    Dianne "Uaaaaaaagh!"
    "A throaty moan leaves her lips involuntarily as I penetrate her."
    "Her body trembles, and her insides tightly clench my invading phallus."
    "She winces in pain as my penis steals her virginity."
    show bg:
        ease 3 xalign 0.8 yalign 0.4
    show cg:
        ease 3 xalign 0.8 yalign 0.4
    show cg ritual midweakgritblush with dexp
    voice "voice/dianne/story/line_086.ogg"
    Dianne "So... Big... Aaagh..."
    voice "voice/dianne/story/line_087.ogg"
    Dianne "But... I can't stop now!"
    show cg ritual middowngritblush with dexp
    voice "voice/dianne/story/line_088.ogg"
    Dianne "Now I need... to say the phrase..."
    voice "voice/malos/story/line_074.ogg"
    Malos "No... I won't let you...!"
    play sound [ "<silence 0.3>", insert]
    show cg ritual midweakopenblush with dexp:
        pause 0.3
        ease 0.04 yoffset 10
        ease 0.04 yoffset -10
        ease 0.04 yoffset 5
        ease 0.04 yoffset -5
        ease 0.04 yoffset 3
        ease 0.04 yoffset -3
        ease 0.04 yoffset 0
    voice "voice/dianne/story/line_089.ogg"
    Dianne "Amare ser– Awaah~!"
    "She begins the magic phrase, but I interrupt her by raising my hips, forcing my penis deeper inside her."
    "The movement startles her, and her words dissolve into an involuntary moan."
    "It prevents her from completing the phrase, so I keep moving."
    call slow_sex_shaker ("v")
    show cg ritual midshockedopenblush with dexp
    voice "voice/dianne/story/line_090.ogg"
    Dianne "N-no! Ah... Ah! S-stop! Aaaaagh~!"
    "With a steady rhythm, I thrust upward into her."
    "Dianne reacts with a loud, erotic voice."
    voice "voice/malos/story/line_075.ogg"
    Malos "Ah, How pitiful... You can't say one little phrase, since you're too distracted by my cock."
    voice "voice/malos/story/line_076.ogg"
    Malos "You can't complete the ritual after all, ha ha ha!"
    call slow_sex_shaker ("v")
    show cg ritual midangryopenblush with dexp
    voice "voice/dianne/story/line_091.ogg"
    Dianne "Aaah... No... No!"
    "In a moment of determination, Dianne slams down her hips."
    show bg:
        ease 0.6 yoffset 0 yalign 1.0 zoom 0.5325
    show cg:
        parallel:
            easeout 0.3 yoffset 0 yalign 1.0 zoom 0.575
        parallel:
            pause 0.3
            ease 0.04 xoffset 10
            ease 0.04 xoffset -10
            ease 0.04 xoffset 5
            ease 0.04 xoffset -5
            ease 0.04 xoffset 3
            ease 0.04 xoffset -3
            ease 0.04 xoffset 0
    show cg ritual deepwideopenblush with dexp
    play sound [ "<silence 0.1>", insert]
    voice "voice/dianne/story/line_092.ogg"
    Dianne "Uwaaaaaah~!"
    "By pushing her torso to the floor, she pins me down, forcing my motions to stop."
    "However, by doing so, she foces my cock far inside her, pushing her limits."
    "She endures the agony, forcing herself to concentrate."
    show cg ritual deepweakgritblush with dexp
    voice "voice/dianne/story/line_093.ogg"
    Dianne "There... Hah... Now... you can't move..."
    voice "voice/dianne/story/line_094.ogg"
    Dianne "A-amare..."
    voice "voice/malos/story/line_077.ogg"
    Malos "Don't say it!"
    show cg ritual deepangryopenblush with dexp
    voice "voice/dianne/story/line_095.ogg"
    Dianne "Amare servum tuus sum!"
    play sound evil_magic
    scene bg white with dscene
    "A magic aura spreads over the two of us, shining brightly."
    "We're both blinded for a moment as the ritual is completed."
    scene bg ritual:
        xalign 0.5 yalign 1.0 zoom 0.5
    show cg ritual deepdowngritblush_crest:
        xalign 0.5 yalign 1.0 zoom 0.5
    with dscene
    voice "voice/dianne/story/line_096.ogg"
    Dianne "Aaah... Wh-what...?"
    show cg ritual deepdownfrownblush_crest with dexp
    voice "voice/dianne/story/line_097.ogg"
    Dianne "Huh? What happened?"
    voice "voice/dianne/story/line_098.ogg"
    Dianne "Why are you still here, Malos? Shouldn't you be..."
    show cg ritual deepshockedfrown_crest with dexp
    voice "voice/dianne/story/line_099.ogg"
    Dianne "Wait... I can't move...!"
    voice "voice/malos/story/line_079.ogg"
    Malos "Ha..."
    voice "voice/malos/story/line_080.ogg"
    Malos "Ha ha ha ha!"
    show cg ritual deepavertopen_crest with dexp
    voice "voice/dianne/story/line_100.ogg"
    Dianne "What are you laughing about? What's going on?!"
    show cg ritual deepangrygrit_crest with dexp
    voice "voice/dianne/story/line_101.ogg"
    Dianne "What did you do to me?!"
    voice "voice/malos/story/line_081.ogg"
    Malos "I haven't done anything to you, princess."
    voice "voice/malos/story/line_082.ogg"
    Malos "You fell into my trap all by yourself!"
    show cg ritual deepshockedopen_crest with dexp
    voice "voice/dianne/story/line_102.ogg"
    Dianne "Trap?! What do you mean?"
    voice "voice/malos/story/line_083.ogg"
    Malos "That ritual you just performed... It wasn't the Ritual of Absorbing."
    voice "voice/malos/story/line_084.ogg"
    Malos "It was the Ritual of Enslavement!"
    voice "voice/malos/story/line_085.ogg"
    Malos "I had my captain teach you the wrong ritual... and you believed him!"
    voice "voice/malos/story/line_086.ogg"
    Malos "What a gullible fool you are!"
    show cg ritual deepshockedgrit_crest with dexp
    voice "voice/dianne/story/line_103.ogg"
    Dianne "No... No way!"
    show bg ritual:
        ease 3 xalign 0.7 yalign 0.9 zoom 0.625
    show cg:
        ease 3 xalign 0.7 yalign 0.9 zoom 0.75
    voice "voice/malos/story/line_087.ogg"
    Malos "Just look at yourself, princess! The ritual has left it's brand on you!"
    voice "voice/malos/story/line_088.ogg"
    Malos "That chained heart permanently marks you as my property!"
    "The mark of a successful ritual, the brand of slavery..."
    "It shines brightly on her skin, a freshly cast spell."
    show bg ritual:
        ease 3 yalign 0.5 zoom 0.55
    show cg ritual deepshockedopenblush_crest:
        ease 3 yalign 0.5 zoom 0.6
    "Dianne looks down at herself with undisguised horror and disgust."
    "She tries to pull away from me, but the spell holds her in place."
    show cg ritual deepavertgritblush_crest with dexp
    voice "voice/dianne/story/line_104.ogg"
    Dianne "I have to... escape..."
    voice "voice/malos/story/line_089.ogg"
    Malos "Don't even try, princess. From now on, you can only obey me."
    voice "voice/malos/story/line_090.ogg"
    Malos "Here, let me show you..."
    voice "voice/malos/story/line_091.ogg"
    Malos "I command you to move your hips and pleasure me."
    play sound [ "<silence 0.7>", insert]
    show cg ritual deepweakopenblush_crest with dexp:
        pause 0.7
        ease 0.04 yoffset 10
        ease 0.04 yoffset -10
        ease 0.04 yoffset 5
        ease 0.04 yoffset -5
        ease 0.04 yoffset 3
        ease 0.04 yoffset -3
        ease 0.04 yoffset 0
    voice "voice/dianne/story/line_105.ogg"
    Dianne "No... Aaaah~!"
    "Despite her refusal, Dianne's body starts to move, sliding up the shaft of my cock."
    "After gaining some height, she descends, engulfing the thick meat in her tight, soft flesh."
    "Dianne winces in pain, but can't stop herself, and her body starts to repeat the motion."
    call slow_sex_shaker ("v")
    show cg ritual deepweakgritblush_crest with dexp
    voice "voice/dianne/story/line_106.ogg"
    Dianne "N-no... Ah... Why... Ah.... Why can't..."
    call slow_sex_shaker ("v")
    show cg ritual deepweakopenblush_crest with dexp
    voice "voice/dianne/story/line_107.ogg"
    Dianne "Wh-why can't I stop?!"
    voice "voice/malos/story/line_092.ogg"
    Malos "Ha ha ha! You can't disobey me!"
    voice "voice/malos/story/line_093.ogg"
    Malos "The Ritual of Enslavement has bound you to my will!"
    voice "voice/malos/story/line_094.ogg"
    Malos "No matter how hard you fight it, you'll be forced to do as I say!"
    call slow_sex_shaker ("v")
    show cg ritual deepavertgritblush_crest with dexp
    voice "voice/dianne/story/line_108.ogg"
    Dianne "No! I don't... ah... I don't want..."
    call slow_sex_shaker ("v")
    show cg ritual deeprollgritblush_crest with dexp
    voice "voice/dianne/story/line_109.ogg"
    Dianne "This... ah... this can't be..."
    "Dianne's anguished cries ring out, along with the obscene noises of intercourse."
    "Despite how unwilling she claims to be, her body works eagerly to satisfy my lust."
    "I feel a deep satisfaction, seeing her helpless, pained expression, while her movements become more and more lewd."
    call slow_sex_shaker ("v")
    voice "voice/malos/story/line_095.ogg"
    Malos "Ah, you have a delightful body..."
    voice "voice/malos/story/line_096.ogg"
    Malos "I'll have to thank my captain for fooling you so well."
    voice "voice/malos/story/line_097.ogg"
    Malos "Perhaps I should let him use you after I'm done..."
    call slow_sex_shaker ("v")
    show cg ritual deepangryfrownblush_crest with dexp
    voice "voice/dianne/story/line_110.ogg"
    Dianne "I won't... ah... let you... get away with this... ah..."
    call slow_sex_shaker ("v")
    show cg ritual deepavertopenblush_crest with dexp
    voice "voice/dianne/story/line_111.ogg"
    Dianne "I'll... ah... kill you... ah..."
    voice "voice/malos/story/line_098.ogg"
    Malos "Say what you like, but there's nothing you can do."
    voice "voice/malos/story/line_099.ogg"
    Malos "You're my slave now! I own you!"
    voice "voice/malos/story/line_100.ogg"
    Malos "The only thing you can do now is serve me!"
    call slow_sex_shaker ("v")
    show cg ritual deepdowngritblush_crest with dexp
    voice "voice/dianne/story/line_112.ogg"
    Dianne "I won't... ah... give up!"
    call slow_sex_shaker ("v")
    show cg ritual deepweakgritblush_crest with dexp
    voice "voice/dianne/story/line_113.ogg"
    Dianne "Ah... Aaaah~! S-stop it!"
    voice "voice/malos/story/line_101.ogg"
    Malos "I'm not doing anything, princess."
    voice "voice/malos/story/line_101b.ogg"
    Malos "You're the one who's frantically pleasuring herself with my dick."
    call slow_sex_shaker ("v")
    show cg ritual deeprollgritblush_crest with dexp
    voice "voice/dianne/story/line_114.ogg"
    Dianne "Y-you know what I mean! Aagh~!"
    call slow_sex_shaker ("v")
    show cg ritual deeprollopenblush_crest with dexp
    voice "voice/dianne/story/line_115.ogg"
    Dianne "O-order me to stop! Ah! I want to stop!"
    voice "voice/malos/story/line_102.ogg"
    Malos "Fine, then. If that's what you really want."
    voice "voice/malos/story/line_103.ogg"
    Malos "I order you to stop holding back. Do it harder."
    call sex_shaker ("v")
    show cg ritual deepwidegritblush_crest with dexp
    voice "voice/dianne/story/line_116.ogg"
    Dianne "N-no! That's not what I meaaaaaaaant~!"
    call sex_shaker ("v")
    show cg ritual deepwideopenblush_crest with dexp
    voice "voice/dianne/story/line_117.ogg"
    Dianne "Aaaaaaah~!"
    "Immediately, Dianne's body increases its pace, thrusting itself onto my cock quickly and forcefully."
    "The rough motion makes her inner walls rub forcefully against my penis, stimulating it."
    "The warm embrace of her womanhood is blissful, and I can feel my pleasure rise."
    voice "voice/malos/story/line_104.ogg"
    Malos "Oh... You're actually really good at this."
    call sex_shaker ("v")
    show cg ritual deepweakgritblush_crest with dexp
    voice "voice/dianne/story/line_118.ogg"
    Dianne "Aaaaah... Aaaaaaaah~!"
    voice "voice/malos/story/line_105.ogg"
    Malos "Ha ha! You can't even speak anymore, can you?"
    "The pleasure overtakes me, and I start moving my own body to match hers."
    "Each time she pushes down to envelop me in her depths, I rise to meet her."
    call sex_shaker ("v")
    "Our motions collide with loud slaps, and before a second has passed, we're preparing for another thrust."
    "Such a pleasurable feeling... Ahhh..."
    voice "voice/malos/story/line_106.ogg"
    Malos "Oh yes... I'm going to cum soon..."
    call sex_shaker ("v")
    show cg ritual deepshockedgritblush_crest with dexp
    voice "voice/dianne/story/line_119.ogg"
    Dianne "Huh? Aaagh~! Nooo~!"
    call sex_shaker ("v")
    show cg ritual deepshockedopenblush_crest with dexp
    voice "voice/dianne/story/line_120.ogg"
    Dianne "D-don't do it! I can't... Aaaaagh~!"
    voice "voice/malos/story/line_107.ogg"
    Malos "Go as fast as you can! Bring me to climax!"
    voice "voice/malos/story/line_108.ogg"
    Malos "I'm gonna pump it all inside you!"
    call fast_sex_shaker ("v")
    show cg ritual deepwidegritblush_crest with dexp
    voice "voice/dianne/story/line_121.ogg"
    Dianne "N-no! Stop! Aaah! I'll g-get..."
    call fast_sex_shaker ("v")
    show cg ritual deepwideopenblush_crest with dexp
    voice "voice/dianne/story/line_122.ogg"
    Dianne "I'll g-get pregnant! Aaaah!"
    voice "voice/malos/story/line_109.ogg"
    Malos "Ha ha ha! That's the whole point!"
    voice "voice/malos/story/line_111.ogg"
    Malos "I'll fill you up, and give you my babies!"
    voice "voice/malos/story/line_112.ogg"
    Malos "The children of the strongest demon, and the strongest human..."
    voice "voice/malos/story/line_113.ogg"
    Malos "I wonder what they'll be like!"
    call fast_sex_shaker ("v")
    show cg ritual deepwidegritblush_crest with dexp
    voice "voice/dianne/story/line_123.ogg"
    Dianne "No! Aaah! I don't want... a demon's baby..."
    call fast_sex_shaker ("v")
    show cg ritual deeprollgritblush_crest with dexp
    voice "voice/dianne/story/line_124.ogg"
    Dianne "Aaaah... Stop... Stop it now!"
    voice "voice/malos/story/line_114.ogg"
    Malos "Here it comes, princess!"
    call fast_sex_shaker ("v")
    voice "voice/malos/story/line_115.ogg"
    Malos "Graaaaaaaah!"
    window hide
    play sound cum
    scene bg white with dissolve
    pause 1
    play sound cum2

    scene bg ritual:
        xalign 0.7 yalign 0.5 zoom 0.55
        ease 0.5 zoom 0.5
    show cg ritual deepwidetongueblush_cum:
        xalign 0.7 yalign 0.5 zoom 0.6
        ease 0.5 zoom 0.5
    with dissolve
    pause 0.5
    window show
    voice "voice/dianne/story/line_125.ogg"
    Dianne "Aaaaaaaaaaaaaaagh~!"
    play sound cum3
    "A thick gush of semen flows out of my dick, shooting straight into Dianne's deepest crevices."
    "She screams out in despair, but she can't pull back, or release her vice grip on my spurting cock."
    "All she can do is feel the hot liquid enter her depths, and tremble as the unfamiliar feeling scars her mind."
    play sound cum
    show cg ritual deeprolltongueblush_cum with dexp
    voice "voice/dianne/story/line_126.ogg"
    Dianne "N-no! There's too much..."
    "I sigh blissfully and let out more of my seed as Dianne sinks into despair."
    "This load... It's the largest one I've let out in a long time."
    voice "voice/malos/story/line_116.ogg"
    Malos "Ah... So satisfying."
    show cg ritual deepweaktongueblush_cum with dexp
    voice "voice/dianne/story/line_127.ogg"
    Dianne "No... No way..."
    show cg ritual deepweakgritblush_cum with dexp
    voice "voice/dianne/story/line_128.ogg"
    Dianne "How did this happen? I..."
    voice "voice/malos/story/line_117.ogg"
    Malos "You never had a chance against me, princess."
    voice "voice/malos/story/line_118.ogg"
    Malos "I let you think you'd won, but I've only been playing with you this whole time."
    voice "voice/malos/story/line_119.ogg"
    Malos "Face the facts. You're mine now."
    show cg ritual deepavertfrownblush_cum with dexp
    voice "voice/dianne/story/line_129.ogg"
    Dianne "I... I'm sorry, father..."
    voice "voice/dianne/story/line_130.ogg"
    Dianne "I've let you down... I've let everyone down..."
    voice "voice/malos/story/line_120.ogg"
    Malos "Now then... Let's continue."
    voice "voice/malos/story/line_121.ogg"
    Malos "I want to make sure you bear my child, so just once won't be enough."
    voice "voice/malos/story/line_122.ogg"
    Malos "Start moving again. That's an order."
    call slow_sex_shaker ("v")
    show cg ritual deeprollfrownblush_cum with dexp
    voice "voice/dianne/story/line_131.ogg"
    Dianne "N-no way... So soon..."
    "Even with so much of my semen inside her, Dianne begins the motion again."
    call slow_sex_shaker ("v")
    show cg ritual deeprollgritblush_cum with dexp
    voice "voice/dianne/story/line_131b.ogg"
    Dianne "Aaaaah~!"
    "It's going to be a long night..."
    stop music fadeout 3
    window hide
    scene bg black with dscene
    call nvl_start (show_bg=False)
    nv "Ending 1: Bound by the Ritual"
    call nvl_end
    pause 1
    stop sound
    $ renpy.end_replay()
    return



label ending_2:
    if _in_replay:
        $ renpy.music.set_volume(0.2, 0, channel="music")
        $ clothes_ripped = True
        play music battle
        scene bg hall:
            zoom 0.6 xalign 0.5 yalign 0.5
        show expression im.Tile("images/particles/fire.png", size=(5760, 1080)) as fire_bg:
            parallel:
                xalign 0.0
                linear 20 xalign 1.0
                repeat
            parallel:
                alpha 0.1
                ease 3.2 alpha 0.3
                ease 3.2 alpha 0.1
                repeat
        show expression im.Tile("images/particles/fire.png", size=(5760, 1080)) as fire_bg2:
            parallel:
                xalign 1.0
                linear 30 xalign 0.0
                repeat
            parallel:
                alpha 0.1
                ease 5.2 alpha 0.3
                ease 5.2 alpha 0.1
                repeat
        show light_effect:
            xalign 0.5 yalign 0.5 zoom 0.9
        show dianne attack2 at center:
            zoom 0.61
        with dlong
        window show
    else:
        hide screen stats_frame
        show bg:
            xalign 0.5 yalign 0.5 xoffset 0 yoffset 0 zoom 0.6
        show light_effect:
            xalign 0.5 yalign 0.5 zoom 0.9
        show dianne attack2:
            alpha 1 zoom 0.61 xoffset 0 yoffset 0
        with dexp

    voice "voice/dianne/story/line_132.ogg"
    Dianne "Yah!"
    show dianne:
        zoom 0.61 yoffset 0
        linear 0.1 zoom 0.76 yoffset 0
        easeout 0.2 zoom 0.66 yoffset -40
    show light_effect:
        linear 0.1 zoom 1.0
        easeout 0.2 zoom 0.9
    show bg:
        xoffset 0
        pause 0.1
        parallel:
            ease 0.05 xoffset 15
            ease 0.05 xoffset -15
            ease 0.05 xoffset 10
            ease 0.05 xoffset -10
            ease 0.05 xoffset 6
            ease 0.05 xoffset -6
            ease 0.05 xoffset 0
        parallel:
            ease 0.3 yoffset -50
    play sound stab
    voice "voice/malos/story/line_123.ogg"
    Malos "Gah!"
    "Knocking me back with a barrage of powerful strikes, Dianne lands a final blow."
    "As I stagger backwards, her sword plunges into my chest, splitting my flesh."
    voice "voice/malos/story/line_124.ogg"
    Malos "Gaaaah!"
    "A searing pain spreads through me, and I fall to my knees."
    "Dianne twists the sword in the wound, tearing through my guts."
    show dianne standby with dpose
    voice "voice/dianne/story/line_133.ogg"
    Dianne "For my father... For my people..."
    voice "voice/dianne/story/line_134.ogg"
    Dianne "For all the crimes you've committed..."
    show dianne charge2 with dpose
    voice "voice/dianne/story/line_135.ogg"
    Dianne "I sentence you to death, Malos."
    stop music fadeout 3
    voice "voice/malos/story/line_125.ogg"
    Malos "No... This can't be..."
    show bg:
        ease 1 yoffset -100
    show dianne:
        ease 1 yoffset -80
    show light_effect:
        ease 1 yoffset -40
    "I fall to my knees, my strength leaving my body."
    "I collapse at Dianne's feet in a pool of blood."
    show dianne conripped tiredopen with dpose
    voice "voice/dianne/story/line_136.ogg"
    Dianne "I... I did it."
    show dianne conripped tiredsmile
    hide light_effect
    hide fire_bg
    hide fire_bg2
    with dlong
    voice "voice/dianne/story/line_137.ogg"
    Dianne "I won..."
    pause 0.2
    show dianne:
        transform_anchor True
        easeout_cubic 1.5 yanchor 0.0 ypos 1.5 rotate 20 xoffset 400
    pause 1
    hide dianne
    hide light_effect
    with dpose
    play sound thud
    "I hear a thud next to me."
    "Slowly, I turn my head, and in the corner of my vision, I see Dianne lying on the floor, unconscious."
    "After using such intense power, Dianne must have fainted from exhaustion..."
    play music demon_king
    voice "voice/malos/story/line_126.ogg"
    Malos "Ha..."
    voice "voice/malos/story/line_127.ogg"
    Malos "Ha ha ha..."
    voice "voice/malos/story/line_128.ogg"
    Malos "Ha ha ha ha ha!"
    "I laugh in triumph."
    "I can feel my magic healing my wound, regenerating my strength."
    "Foolish princess... Stabbing me through the chest isn't enough to kill me."
    "You're very strong if you can break through my defences, but now, you've made a fatal mistake."
    "You didn't finish the job, and the backlash from your awakening has left you helpless."
    show bg:
        ease 2 yoffset 0 yalign 0.5 xalign 0.5
    "My regeneration magic finishes its work, and I stand up, looking down at her limp form."
    "She's defenseless now, even though she was so strong just a moment ago."
    "Carefully, I hoist her body over my shoulder."
    "She doesn't awaken, still unconscious."
    voice "voice/malos/story/line_129.ogg"
    Malos "Ha ha ha..."
    voice "voice/malos/story/line_130.ogg"
    Malos "I have special plans for you, princess Dianne..."
    show bg:
        ease 8 yoffset 0 yalign 0.5 xalign 0.5 zoom 0.9
    "I carry her away, taking her to a more suitable part of the castle..."
    stop music fadeout 2
    window hide
    scene bg black with dscene
    window show
    play music dungeon
    "..."
    voice "voice/dianne/story/line_138.ogg"
    Dianne "Mmmmm..."
    "Oh, she's waking up now!"
    window hide
    scene cg dungeon closedgape with dscene:
        zoom 1 xalign 1.0 yalign 0.5
        ease 3 zoom 0.9
    window show
    voice "voice/dianne/story/line_139.ogg"
    Dianne "Mmmm... Huh?"
    show cg dungeon calmgape with dexp
    voice "voice/dianne/story/line_140.ogg"
    Dianne "Where am I..."
    voice "voice/malos/story/line_131.ogg"
    Malos "Glad to see you're awake, princess."
    show cg:
        ease 0.5 zoom 0.8
    show cg dungeon angryyell with dexp
    voice "voice/dianne/story/line_141.ogg"
    Dianne "Malos! How are you–"
    play sound chains
    show cg dungeon avertopen with dexp
    voice "voice/dianne/story/line_142.ogg"
    Dianne "Huh? I can't move... and..."
    play sound chains
    show cg:
        ease 2 zoom 0.65 xalign 0.5
    show cg dungeon angryblushgrit with dexp
    voice "voice/dianne/story/line_143.ogg"
    Dianne "Wh-where's my armor?! How dare you!"
    "Dianne looks around her in panic, realizing her situation."
    "I've taken her to my dungeon and restrained her."
    "I've also stripped her of what remained of her clothes."
    "Her naked body is exposed, along with her cute, virgin womanhood."
    show cg:
        ease 1 zoom 0.6
    voice "voice/malos/story/line_132.ogg"
    Malos "Don't worry, princess. You won't need that armor anymore."
    voice "voice/malos/story/line_133.ogg"
    Malos "No good slave would wear such a modest outfit. You're better off naked."
    show cg:
        ease 1 zoom 0.65 xalign 0.8
    show cg dungeon angryyell with dexp
    voice "voice/dianne/story/line_144.ogg"
    Dianne "C-coward! I'll kill you!"
    show cg dungeon avertgrit with dexp
    play sound chains
    voice "voice/dianne/story/line_145.ogg"
    Dianne "Ugh... grr..."
    "Dianne spends a few moments struggling against her bonds, but is unable to escape them."
    "There's no way she can break those chains. I enchanted them myself."
    "Still, it's amusing to watch her squirm."
    play sound chains
    show cg dungeon angrygrit with dexp
    voice "voice/dianne/story/line_146.ogg"
    Dianne "Gah... Release me!"
    voice "voice/malos/story/line_134.ogg"
    Malos "Why should I? You stabbed me in the chest!"
    voice "voice/malos/story/line_135.ogg"
    Malos "That hurts a lot, you know? You should apologise."
    show cg dungeon angryyell with dexp
    voice "voice/dianne/story/line_147.ogg"
    Dianne "Never! A coward like you doesn't deserve my respect."
    voice "voice/malos/story/line_136.ogg"
    Malos "Well, I suppose it doesn't matter."
    voice "voice/malos/story/line_137.ogg"
    Malos "You're mine now, princess, and you'll repent with your body."
    show cg:
        ease 3 zoom 0.6 xalign 0.5
    show cg dungeon angrygape with dexp
    "I approach Dianne's helpless form, admiring her exposed backside."
    show cg dungeon angrygape grind with dpose
    "I lightly touch her with the tip of my member, showing my intent clearly."
    show cg dungeon shockedyell grind with dexp
    voice "voice/dianne/story/line_148.ogg"
    Dianne "W-wait! Stop!"
    "Her struggles grow more frantic as she feels the weight and heat against her sensitive skin."
    show cg dungeon shockedblushgrit grind with dexp
    voice "voice/dianne/story/line_149.ogg"
    Dianne "G-get that filthy thing away from me!"
    voice "voice/malos/story/line_138.ogg"
    Malos "Say what you like, princess, but I won't listen."
    voice "voice/malos/story/line_139.ogg"
    Malos "You're just a slave now, and I'll use you however I want."
    show cg dungeon avertblushwavy grind with dexp
    voice "voice/dianne/story/line_150.ogg"
    Dianne "I'm not your slave! I'll get out of this... somehow..."
    voice "voice/malos/story/line_140.ogg"
    Malos "There's no way for you to escape, princess. This dungeon is your home now."
    voice "voice/malos/story/line_141.ogg"
    Malos "Don't worry, I'll be here to keep you company..."
    play sound wet_touch
    "Enjoying how uncomfortable it makes her, I rub my penis on Dianne's soft buttocks."
    "She shivers at the touch, surely knowing what fate awaits her."
    play sound wet_touch
    show cg dungeon avertblushopen grind with dexp
    "She draws back as far as her restraints will allow, but it's not enough to escape from me."
    "My thick rod of flesh slides over her slit, and she flinches at the sensation."
    show cg dungeon closedblushopen grind with dexp
    voice "voice/dianne/story/line_151.ogg"
    Dianne "S-stop it... You won't get way with this..."
    show cg dungeon angryblushwavy grind with dexp
    voice "voice/dianne/story/line_152.ogg"
    Dianne "There's no way you can keep me here forever..."
    voice "voice/malos/story/line_142.ogg"
    Malos "Hah! Before long, you'll be begging for me to ravish you."
    show cg dungeon angryblushgrit grind with dexp
    voice "voice/dianne/story/line_153.ogg"
    Dianne "N-no way... Like I'd ever beg for that."
    show cg dungeon angryblushyell grind with dexp
    voice "voice/dianne/story/line_154.ogg"
    Dianne "You can't break me... I'll never give in!"
    show cg dungeon angryblushwavy grind with dexp
    "Even in such a pitiful situation, she's still defiant..."
    "How amusing."
    show cg:
        ease 3 zoom 0.6 xalign 0.25
    "I angle my hips so that my hardened dick lines up with her hole, ready to penetrate it."
    voice "voice/malos/story/line_143.ogg"
    Malos "Ha ha ha! Keep that spirit up, princess."
    voice "voice/malos/story/line_144.ogg"
    Malos "It'll be fun to see how long it lasts!"
    show cg dungeon shockedblushyell grind with dexp
    voice "voice/dianne/story/line_155.ogg"
    Dianne "N-no... Nooooo!"
    play sound insert
    show cg:
        parallel:
            easein 0.35 zoom 0.65 xalign 0.5
        parallel:
            pause 0.3
            ease 0.05 xoffset 8
            ease 0.05 xoffset -8
            ease 0.05 xoffset 5
            ease 0.05 xoffset -5
            ease 0.05 xoffset 3
            ease 0.05 xoffset -3
            ease 0.05 xoffset 0
    show cg dungeon rollblushyell deep with dpose
    voice "voice/dianne/story/line_155b.ogg"
    Dianne "Aaaaaaaagh~!"
    "With a forceful thrust, I plunge my cock inside her."
    "I stretch her tight hole wider than any human would, pushing it past any normal limits."
    show cg dungeon closedblushgrit deep with dexp
    voice "voice/dianne/story/line_156.ogg"
    Dianne "Ah... No... Stop!"
    show cg dungeon rollblushgrit deep with dexp
    voice "voice/dianne/story/line_157.ogg"
    Dianne "I can't... ah..."
    "Her words fall apart as she trembles, unable to process what is happening."
    "Lodged deep inside her, I can feel her inner walls clench tight around my invading member."
    "I sigh happily as I feel her womanhood's grip on me, and see her strong will falter."
    voice "voice/malos/story/line_145.ogg"
    Malos "Ooh... Your hole is incredible, Dianne..."
    voice "voice/malos/story/line_146.ogg"
    Malos "You'll make a wonderful slave!"
    show cg dungeon avertblushgrit deep with dexp
    voice "voice/dianne/story/line_158.ogg"
    Dianne "No... I won't let you... treat me like this..."
    voice "voice/malos/story/line_147.ogg"
    Malos "I'll treat you as I like!"
    voice "voice/malos/story/line_148.ogg"
    Malos "You're mine now, so stop struggling and accept your fate!"
    show cg dungeon angryblushgrit deep with dexp
    voice "voice/dianne/story/line_159.ogg"
    Dianne "I won't... I won't!"
    "Slowly recovering from the impact, I can see the fire return to her eyes..."
    "That must mean that she's ready to continue."
    show cg:
        ease 3 zoom 0.6 xalign 0.25
    "I pull back my hips, getting ready for another thrust."
    play sound wet_touch
    show cg dungeon angryblushgrit inside with dpose
    "My member rubs against her sensitive walls as it exits her narrow passage."
    show cg dungeon shockedblushgape inside with dexp
    voice "voice/dianne/story/line_160.ogg"
    Dianne "W-wait! I-I'm not..."
    voice "voice/malos/story/line_149.ogg"
    Malos "I don't care! Take this!"
    play sound insert
    show cg:
        parallel:
            easein 0.35 zoom 0.65 xalign 0.5
        parallel:
            pause 0.3
            ease 0.05 xoffset 8
            ease 0.05 xoffset -8
            ease 0.05 xoffset 5
            ease 0.05 xoffset -5
            ease 0.05 xoffset 3
            ease 0.05 xoffset -3
            ease 0.05 xoffset 0
    show cg dazedblushopen deep with dpose
    voice "voice/dianne/story/line_161.ogg"
    Dianne "Ah... Uuuaaaaah~!"
    "With another unforgiving push, I fill Dianne's insides again."
    "I feel the deepest parts of her, and push up against them."
    "Her muscles grow tense as her sensitive spots are hit roughly."
    show cg rollblushwavy deep with dexp
    voice "voice/dianne/story/line_162.ogg"
    Dianne "This is... ah... too much! Ah..."
    voice "voice/malos/story/line_150.ogg"
    Malos "Hah! So much for your feeble pride."
    voice "voice/malos/story/line_151.ogg"
    Malos "I'll force that attitude out of you! Ha ha ha ha!"
    "I don't give Dianne any time to rest, and start to move again."
    call slow_sex_shaker
    show cg closedblushgrit deep with dexp
    voice "voice/dianne/story/line_163.ogg"
    Dianne "No... no! Ah... Aaaaaah~!"
    call slow_sex_shaker
    show cg rollblushyell deep with dexp
    voice "voice/dianne/story/line_164.ogg"
    Dianne "Stop iiiiiit~!"
    "Repeatedly, I piston my throbbing member into her, sliding in and out at a good pace."
    "She groans in protest, but can do nothing to stop me."
    "The dull slap of my hips colliding with her backside accents each thrust."
    call slow_sex_shaker
    show cg rollblushopen deep with dexp
    voice "voice/dianne/story/line_165.ogg"
    Dianne "Ah... Aaaah..."
    voice "voice/malos/story/line_152.ogg"
    Malos "How are you feeling now, princess?"
    voice "voice/malos/story/line_153.ogg"
    Malos "Still think you can hold out against me?"
    call slow_sex_shaker
    show cg calmblushyell deep with dexp
    voice "voice/dianne/story/line_166.ogg"
    Dianne "Ah... I will... Ah..."
    voice "voice/malos/story/line_154.ogg"
    Malos "Hah! Your voice is so weak compared to a minute ago."
    voice "voice/malos/story/line_155.ogg"
    Malos "You'll definitely submit to me in time."
    call slow_sex_shaker
    show cg calmblushgrit deep with dexp
    voice "voice/dianne/story/line_167.ogg"
    Dianne "You can't... ah... make me..."
    voice "voice/malos/story/line_156.ogg"
    Malos "We'll see about that."
    "As I keep ravaging her body, it slowly seems to grow used to my brutality."
    "Her muscles start to lose their tension, no longer trying to break the chains that bind her."
    "Her insides grow moist, coating my dick with juices, and allowing me to move faster."
    call sex_shaker
    show cg avertblushwavy deep with dexp
    voice "voice/dianne/story/line_168.ogg"
    Dianne "Ah... Aaaah..."
    voice "voice/malos/story/line_157.ogg"
    Malos "Hmm... You're good at this, princess."
    voice "voice/malos/story/line_158.ogg"
    Malos "It won't be long before I cum..."
    call sex_shaker
    show cg calmblushgape with dexp
    voice "voice/dianne/story/line_169.ogg"
    Dianne "Ah... cum?"
    show cg shockedblushgape with dexp
    "Her eyes flash open as she has a realization."
    call sex_shaker
    show cg shockedblushyell with dexp
    voice "voice/dianne/story/line_170.ogg"
    Dianne "N-no! S-stop! You can't!"
    "Despite her protest, I move my hips with renewed vigor."
    call sex_shaker
    show cg rollblushopen with dexp
    voice "voice/dianne/story/line_171.ogg"
    Dianne "D-don't cum inside! Ah..."
    voice "voice/malos/story/line_159.ogg"
    Malos "Ha ha ha!"
    voice "voice/malos/story/line_160.ogg"
    Malos "Of course I will! Why wouldn't I?"
    call sex_shaker
    show cg rollblushgrit with dexp
    voice "voice/dianne/story/line_172.ogg"
    Dianne "D-don't... I might get... ah..."
    voice "voice/malos/story/line_161.ogg"
    Malos "Of course, getting you pregnant was my plan from the start!"
    voice "voice/malos/story/line_162.ogg"
    Malos "It would be such a waste if some weakling gave you their baby."
    voice "voice/malos/story/line_163.ogg"
    Malos "Instead, rejoice! Your children will bear the bloodline of the Demon King!"
    "I thrust into her with increasing intensity, growing closer and closer to climax."
    call fast_sex_shaker
    show cg shockedblushgape with dexp
    voice "voice/dianne/story/line_173.ogg"
    Dianne "N-no! Ah... I can't...!"
    call fast_sex_shaker
    show cg closedblushgrit with dexp
    voice "voice/dianne/story/line_174.ogg"
    Dianne "P-pull it out! I... I... Ah!"
    call fast_sex_shaker
    show cg dazedblushyell with dexp
    voice "voice/dianne/story/line_175.ogg"
    Dianne "Please! Ah! I don't want your baby!"
    voice "voice/malos/story/line_164.ogg"
    Malos "You're my slave now! It doesn't matter what you want!"
    voice "voice/malos/story/line_165.ogg"
    Malos "If I say you'll bear my children, then you cannot refuse!"
    call fast_sex_shaker
    show cg winceblushopen with dexp
    voice "voice/dianne/story/line_176.ogg"
    Dianne "No... No!"
    voice "voice/malos/story/line_166.ogg"
    Malos "It's time! Get pregnant, slave!"
    call fast_sex_shaker
    show cg rollblushyell with dexp
    voice "voice/dianne/story/line_177.ogg"
    Dianne "Ah! Noooo! Ah!"
    play sound cum
    show bg white with dissolve
    pause 1
    hide bg white
    play sound cum2
    show cg dazedblushtongue deepcum:
        parallel:
            easein 0.35 zoom 0.68 xalign 0.65
        parallel:
            pause 0.3
            ease 0.05 xoffset 8
            ease 0.05 xoffset -8
            ease 0.05 xoffset 5
            ease 0.05 xoffset -5
            ease 0.05 xoffset 3
            ease 0.05 xoffset -3
            ease 0.05 xoffset 0
    with dissolve
    voice "voice/dianne/story/line_178.ogg"
    Dianne "Aaaaaaaaaaaaah~!"
    "With one final swing of my hips, I plunge as far as possible inside Dianne, and release my load."
    play sound cum3
    "My semen oozes into her, thick strands pumping directly into her womb."
    show cg winceblushtongue with dexp
    voice "voice/dianne/story/line_179.ogg"
    Dianne "Aaaah~! So much..."
    voice "voice/malos/story/line_167.ogg"
    Malos "Take it all!"
    play sound cum
    "The white fluids spray inside of Dianne, overflowing from her narrow passage."
    "My mind is filled with a amazing feeling of conquest as I make Dianne cry out in despair."
    show cg calmblushgapedrool with dexp
    voice "voice/dianne/story/line_180.ogg"
    Dianne "No... I couldn't stop it..."
    play sound wet_touch
    show cg:
        ease 3 zoom 0.6 xalign 0.25
    show cg calmblushgapedrool insidecum with dpose
    "As my semen fills her, I pull back slightly, making room within her for the excessive amount."
    "By the time my ejaculation ends, she's stopped resisting at all."
    show cg calmblushgritdrool with dpose
    voice "voice/dianne/story/line_181.ogg"
    Dianne "Why did this happen...?"
    voice "voice/malos/story/line_168.ogg"
    Malos "This happened because it is my will, princess."
    voice "voice/malos/story/line_169.ogg"
    Malos "You're mine now. All that matters is what I want from you."
    show cg avertblushwavydrool with dexp
    voice "voice/dianne/story/line_182.ogg"
    Dianne "...Do what you will."
    show cg closedblushwavydrool with dexp
    voice "voice/dianne/story/line_183.ogg"
    Dianne "I've failed... My people are doomed now..."
    voice "voice/dianne/story/line_184.ogg"
    Dianne "They trusted me... but their hope was in vain."
    voice "voice/malos/story/line_170.ogg"
    Malos "That's right. Your people had no chance to begin with."
    voice "voice/malos/story/line_171.ogg"
    Malos "Soon, my army will conquer your entire realm, and demons will rule over humankind."
    voice "voice/malos/story/line_172.ogg"
    Malos "You were their last hope, but now, I'm going to make you a symbol of their demise."
    voice "voice/malos/story/line_173.ogg"
    Malos "I hope you're ready. I have so much more planned for tonight, my little slave..."
    stop music fadeout 3
    window hide
    scene bg black with dscene
    call nvl_start (show_bg=False)
    nv "Ending 2: Captured Princess"
    call nvl_end
    pause 1
    stop sound
    $ renpy.end_replay()
    return



label ending_3:
    if _in_replay:
        $ renpy.music.set_volume(0.2, 0, channel="music")
        $ clothes_ripped = True
        play music battle
        scene bg hall:
            zoom 0.6 xalign 0.5 yalign 0.5
        show expression im.Tile("images/particles/fire.png", size=(5760, 1080)) as fire_bg:
            parallel:
                xalign 0.0
                linear 20 xalign 1.0
                repeat
            parallel:
                alpha 0.1
                ease 3.2 alpha 0.3
                ease 3.2 alpha 0.1
                repeat
        show expression im.Tile("images/particles/fire.png", size=(5760, 1080)) as fire_bg2:
            parallel:
                xalign 1.0
                linear 30 xalign 0.0
                repeat
            parallel:
                alpha 0.1
                ease 5.2 alpha 0.3
                ease 5.2 alpha 0.1
                repeat
        show light_effect:
            xalign 0.5 yalign 0.5 zoom 0.9
        show dianne standby at center:
            zoom 0.61
        with dlong
        window show
    else:
        hide screen stats_frame
        $ persistent.hard_mode_unlocked = True

    voice "voice/malos/story/line_174.ogg"
    Malos "You're finished, princess!"
    voice "voice/malos/story/line_175.ogg"
    Malos "Time for the final blow! Graaaah!"
    stop music fadeout 1
    show bg:
        linear 0.1 zoom 0.73
    show light_effect:
        linear 0.1 zoom 1.0
    show dianne:
        parallel:
            pause 0.1
            ease 0.05 xoffset 10
            ease 0.05 xoffset -10
            ease 0.05 xoffset 8
            ease 0.05 xoffset -8
            ease 0.05 xoffset 5
            ease 0.05 xoffset -5
            ease 0.05 xoffset 0
        parallel:
            linear 0.1 zoom 0.76 yoffset -40
    show dianne hurt with Dissolve(0.1)
    play sound hit2
    show bg white as whiteflash with Dissolve(0.1)
    voice "voice/dianne/story/line_043.ogg"
    Dianne "Aaaagh!"
    play sound rip
    "I strike, blowing past Dianne's defences."
    show dianne con2 weakopen:
        zoom 0.82
    hide fire_bg
    hide fire_bg2
    hide whiteflash with dscene
    hide light_effect with dlong
    "Losing her strength, the powerful aura surrounding her fades away."
    play music demon_king
    "Barely able to continue standing, she trembles, glaring back at me."
    show dianne con2 worriedclench with dexp
    voice "voice/dianne/story/line_186.ogg"
    Dianne "No... I'm running out of time..."
    voice "voice/dianne/story/line_187.ogg"
    Dianne "But... I can't lose here!"
    voice "voice/malos/story/line_176.ogg"
    Malos "You can't win, princess. You're not strong enough."
    show dianne con2 weakclench with dexp:
        pause 0.4
        ease 1 xoffset -200 zoom 0.63
    voice "voice/dianne/story/line_188.ogg"
    Dianne "Grrr... Hah!"
    "On shaky legs, Dianne turns and flees."
    voice "voice/malos/story/line_177.ogg"
    Malos "How cute. You think you can escape me?"
    show bg:
        ease 0.7 zoom 0.9 xoffset 200
    show dianne:
        ease 0.7 xoffset 0 zoom 0.9
    "In only a few bounds across the hall, I catch up to her."
    "I grab one of her arms, stopping her in her tracks."
    show dianne con2 worriedopen with dexp:
        ease 0.4 zoom 0.85
        easeout 0.2 zoom 0.94
    voice "voice/dianne/story/line_189.ogg"
    Dianne "No... Let go of me!"
    voice "voice/malos/story/line_178.ogg"
    Malos "You won't get away so easily."
    voice "voice/malos/story/line_179.ogg"
    Malos "You've lost this fight, and now, I'll make you my slave!"
    show dianne con2 weakclench with dexp
    voice "voice/dianne/story/line_190.ogg"
    Dianne "S-stop saying that! I'm not your property!"
    show dianne:
        ease 0.4 zoom 0.9
        easeout 0.2 zoom 0.98
    "She pulls away from me, trying to break free, but there's nothing she can do now that I've caught her."
    "In a desperate gambit, she swings her fist at me, but it isn't nearly enough to hurt me."
    voice "voice/malos/story/line_180.ogg"
    Malos "Your struggles are in vain, princess! You can't break free, so just give up!"
    show dianne con2 weakopen with dexp
    voice "voice/dianne/story/line_191.ogg"
    Dianne "Never! I won't let you win!"
    show dianne con2 worriedclench with dexp
    voice "voice/dianne/story/line_192.ogg"
    Dianne "As long as I have my will, I won't submit to you!"
    voice "voice/malos/story/line_181.ogg"
    Malos "As long as you have your will, you say..."
    voice "voice/malos/story/line_182.ogg"
    Malos "Well then, all I have to do is strip you of your free will!"
    show dianne con2 agonyclench with dexp
    "Dianne's expression turns to shock, and she redoubles her effort to escape."
    voice "voice/dianne/story/line_193.ogg"
    Dianne "No... No!"
    show dianne con2 agonyopen with dexp
    voice "voice/dianne/story/line_194.ogg"
    Dianne "You can't do that! It's not possible!"
    voice "voice/malos/story/line_183.ogg"
    Malos "We'll see about that!"
    show dianne:
        ease 0.5 zoom 1
    "I pull Dianne close to me, and press the palm of my hand against her forehead."
    play sound evil_magic
    show bg red as redflash with Dissolve(0.1)
    show dianne:
        ease 0.05 xoffset 10
        ease 0.05 xoffset -10
        ease 0.05 xoffset 8
        ease 0.05 xoffset -8
        ease 0.05 xoffset 5
        ease 0.05 xoffset -5
        ease 0.05 xoffset 0
    hide redflash with dpose
    "As I begin a potent magic spell, my hand glows with dark power."
    voice "voice/malos/story/line_184.ogg"
    Malos "Let us seal the contract, princess!"
    voice "voice/malos/story/line_185.ogg"
    Malos "From this moment on, you are mine!"
    play sound evil_magic
    show bg red as redflash with Dissolve(0.1)
    show dianne con2 agonyshriek:
        ease 0.05 xoffset 10
        ease 0.05 xoffset -10
        ease 0.05 xoffset 8
        ease 0.05 xoffset -8
        ease 0.05 xoffset 5
        ease 0.05 xoffset -5
        ease 0.05 xoffset 0
    hide redflash with dpose
    voice "voice/dianne/story/line_195.ogg"
    Dianne "Aaaaaaaaah! Nooooo!"
    "The princess shrieks in pain as I forcefully probe into her mind."
    "My soul slips through her mental defences, flowing into her thoughts and destroying all resistance."
    play sound evil_magic
    show bg red as redflash with Dissolve(0.1)
    show dianne con2 worriedshriek:
        ease 0.05 xoffset 10
        ease 0.05 xoffset -10
        ease 0.05 xoffset 8
        ease 0.05 xoffset -8
        ease 0.05 xoffset 5
        ease 0.05 xoffset -5
        ease 0.05 xoffset 0
    hide redflash with dpose
    voice "voice/dianne/story/line_196.ogg"
    Dianne "No ... It hurts..."
    "Slowly, her reaction fades away, her eyes grow clouded, and her body falls limp."
    "No matter how much she hates it, she can't defend herself against this."
    play sound evil_magic
    show bg red as redflash with Dissolve(0.1)
    show dianne con2 worriedopen:
        ease 0.05 xoffset 10
        ease 0.05 xoffset -10
        ease 0.05 xoffset 8
        ease 0.05 xoffset -8
        ease 0.05 xoffset 5
        ease 0.05 xoffset -5
        ease 0.05 xoffset 0
    hide redflash with dpose
    "My spell is burrowing into her head, erasing her thoughts and feelings."
    "Her mind is being emptied... and she is becoming my puppet."
    play sound evil_magic
    show bg red as redflash with Dissolve(0.1)
    show dianne con2 worriedgape:
        ease 0.05 xoffset 10
        ease 0.05 xoffset -10
        ease 0.05 xoffset 8
        ease 0.05 xoffset -8
        ease 0.05 xoffset 5
        ease 0.05 xoffset -5
        ease 0.05 xoffset 0
    hide redflash with dpose
    voice "voice/malos/story/line_186.ogg"
    Malos "How does it feel, Dianne? What is it like to be completely dominated by your worst enemy?"
    voice "voice/dianne/story/line_197.ogg"
    Dianne "..."
    "No response."
    voice "voice/malos/story/line_187.ogg"
    Malos "Hah! I suppose you aren't in a situation to speak your mind anymore."
    voice "voice/malos/story/line_188.ogg"
    Malos "Well, then, let's fix you up, my little slave."
    $ renpy.music.set_volume(0.4, 0, 'sound')
    play sound charge
    show bg white as whiteflash with dpose
    show dianne con2 emptygape
    hide whiteflash with dissolve
    "After draining her willpower, I replace it with a new desire."
    "A powerful desire to serve and please me, as her master."
    play sound charge
    show bg white as whiteflash with dpose
    hide whiteflash with dissolve
    "I will be the only one she cares about... the only being in the world that matters to her."
    "Making me happy is her only purpose."
    play sound charge
    show bg white as whiteflash with dpose
    hide whiteflash with dissolve
    "She will be filled with an insatiable lust for me."
    "Only I will be able to satisfy her intense carnal desires."
    $ renpy.music.set_volume(0.7, 0, 'sound')
    play sound charge
    show bg white as whiteflash with dlong
    hide whiteflash with dscene
    "As I finish placing these thoughts into her, the magic energy begins to fade away."
    show bg:
        ease 0.5 zoom 0.8
    show dianne:
        ease 0.5 zoom 0.8
    "Cautiously, I release her from my grip, and she stands motionless."
    voice "voice/malos/story/line_189.ogg"
    Malos "It is done."
    voice "voice/malos/story/line_190.ogg"
    Malos "Who are you now?"
    show dianne con2 worriedgape with dexp
    voice "voice/dianne/story/line_198.ogg"
    Dianne "I... I am..."
    voice "voice/dianne/story/line_199.ogg"
    Dianne "I am your slave, master."
    show dianne con2 heartgape with dexp
    voice "voice/dianne/story/line_200.ogg"
    Dianne "I want... to be used by you..."
    show dianne con2 heartopenleak with dexp
    voice "voice/dianne/story/line_201.ogg"
    Dianne "I need your love... I need to feel you inside me..."
    show dianne con2 heartdroolleak with dexp:
        ease 0.5 zoom 0.85
    voice "voice/dianne/story/line_202.ogg"
    Dianne "I'll make you feel good, master... Please let me serve you!"
    "Dianne acts like a completely different person."
    "Her face flushes red with desire as her breathing grows heavy."
    show bg:
        ease 4 yoffset -200
    show dianne:
        ease 4 yoffset -300
    "Such a lewd expression... and such a lewd body."
    "It's painfully obvious to see the clear liquid dampening her underwear and dripping down her thighs."
    "Now, and forever after, she will belong to me."
    show bg:
        ease 4 yoffset 0
    show dianne:
        ease 4 yoffset 0
    voice "voice/malos/story/line_191.ogg"
    Malos "Very well, slave. I'll let you serve me."
    voice "voice/malos/story/line_192.ogg"
    Malos "But first, why don't you prove your new loyalty..."
    voice "voice/malos/story/line_193.ogg"
    Malos "Show me just how much you want my love."
    show dianne:
        ease 0.5 zoom 0.92 yoffset 0
    voice "voice/dianne/story/line_203.ogg"
    Dianne "Of course! Anything for you, master!"
    stop music fadeout 2

    $ renpy.music.set_volume(1.0, 0, 'sound')
    window hide
    scene bg black with dscene
    play music brainwashed
    window show

    "Quickly, Dianne removes what remains of her armor, exposing her naked body."
    "She hastily yanks her off her gem-studded circlet with one hand."
    "A priceless accessory, proof of her royal lineage, and the adoration of her subjects..."
    play sound circlet
    window hide
    pause 0.7
    scene cg brainwashed stareopenmasturbate with dscene:
        xalign 1.0 yalign 0.5 zoom 1
        ease 8 zoom 0.5
    window show

    "She tosses it aside like trash in her eagerness to obey me."
    voice "voice/dianne/story/extra_01.ogg"
    Dianne "Oooh... Master..."
    play sound wet_touch
    show cg brainwashed squintlickmasturbate with dexp
    voice "voice/dianne/story/extra_02.ogg"
    Dianne "I want you... ah... I need you so badly..."
    show cg:
        xalign 0.1 yalign 0.45 zoom 0.5
        ease 5 zoom 0.7
    "Unable to contain herself, Dianne's hands immediately grasp at her sensitive body."
    "With one hand squeezing her breast, and the other frantically rubbing her slit, she looks at me with seductive eyes."
    play sound [wet_touch, "<silence 1.5>", wet_touch, "<silence 1.5>", wet_touch, "<silence 1.5>", wet_touch]
    show cg brainwashed closedmoanmasturbate with dexp
    voice "voice/dianne/story/extra_03.ogg"
    Dianne "Ngah... Ah... haa... oooh..."
    play sound [wet_touch, "<silence 1.5>", wet_touch, "<silence 1.5>", wet_touch, "<silence 1.5>", wet_touch]
    show cg brainwashed puppymoanmasturbate with dexp
    voice "voice/dianne/story/extra_04.ogg"
    Dianne "I've never... felt like this before... Aah..."
    show cg:
        parallel:
            ease 5 zoom 0.9
        parallel:
            easein 5 xalign 0.4
    "Her crotch is soaked... It's overflowing with her love."
    "She strokes the surface with her fingers, making lewd, wet noises."
    show cg:
        ease 3 xalign 0.25 zoom 0.9
    play sound [wet_touch, "<silence 1.5>", wet_touch, "<silence 1.5>", wet_touch, "<silence 1.5>", wet_touch]
    show cg brainwashed squintopenmasturbate with dexp
    voice "voice/dianne/story/extra_05.ogg"
    Dianne "Everything feels so good... Ah... So amazing..."
    show cg brainwashed squintbitemasturbate with dexp
    voice "voice/dianne/story/extra_06.ogg"
    Dianne "But... It's not enough!"
    show cg brainwashed puppybitemasturbate with dexp
    "She stares into my eyes, pleading for me to use her."
    play sound [wet_touch, "<silence 1.5>", wet_touch, "<silence 1.5>", wet_touch, "<silence 1.5>", wet_touch]
    voice "voice/dianne/story/extra_07.ogg"
    Dianne "Only you can make me better, master..."
    show cg brainwashed squintmoanmasturbate with dexp
    voice "voice/dianne/story/extra_08.ogg"
    Dianne "My slutty wet hole wants your demon cock..."
    show cg brainwashed puppylickmasturbate with dexp
    voice "voice/dianne/story/extra_09.ogg"
    Dianne "If you don't fill me up quickly, I'll lose my mind..."
    "Hah! As if she hasn't already lost her mind."
    show cg:
        ease 5 xalign 0.15 zoom 0.75
    "Her fingers move quickly as she spreads her legs wide, showing me everything."
    play sound [wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch]
    show cg brainwashed closedbitemasturbate with dexp
    voice "voice/dianne/story/extra_10.ogg"
    Dianne "No way... I can't... Uh..."
    play sound [wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch]
    show cg brainwashed rollbitemasturbate with dexp
    voice "voice/dianne/story/extra_11.ogg"
    Dianne "This isn't... enough...!"
    "Her movements are frantic as she tries to satisfy herself."
    "However, she's only making it worse."
    "The magic has affected her mind and body. She won't be able to cum this way."
    "The only time she will be allowed to cum is when I'm inside her."
    play sound [wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch]
    show cg brainwashed puppybitemasturbate with dexp
    voice "voice/dianne/story/extra_12.ogg"
    Dianne "Please, master! I can't take this any longer!"
    play sound [wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch]
    show cg brainwashed puppywidemasturbate with dexp
    voice "voice/dianne/story/extra_13.ogg"
    Dianne "I want your cock! I need your dick!"
    play sound [wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch]
    show cg brainwashed squintopenmasturbate with dexp
    voice "voice/dianne/story/extra_14.ogg"
    Dianne "I'll die if you don't ram it into me!"
    play sound [wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch, "<silence 0.8>", wet_touch]
    show cg brainwashed closedwidemasturbate with dexp
    voice "voice/dianne/story/extra_15.ogg"
    Dianne "Please! Pound me hard! Make me yours!"
    show cg brainwashed closedbitemasturbate with dexp
    "She begs for me without a hint of shame or remorse."
    voice "voice/malos/story/line_194.ogg"
    Malos "Ha ha ha! You've fallen quite far, princess."
    voice "voice/malos/story/line_195.ogg"
    Malos "I suppose I'll grant your request."
    show cg:
        ease 5 xalign 0.15 zoom 0.6
    show cg brainwashed stareahegaomasturbate with dexp
    voice "voice/dianne/story/extra_16.ogg"
    Dianne "Oh, yes! Yees~!"
    "As she sees me relent, she quickly stops rubbing herself."
    show cg brainwashed squintlickspread with dpose
    voice "voice/dianne/story/line_204.ogg"
    Dianne "Here, master... I'm ready for your love."
    "She places her hands on her buttocks, stretching her moist slit."
    "Moisture drips from her, showing just how eager she is."
    voice "voice/malos/story/line_196.ogg"
    Malos "What an obedient little slave."
    voice "voice/malos/story/line_197.ogg"
    Malos "I won't go easy on your precious little hole."
    show cg brainwashed puppylickspread with dexp
    voice "voice/dianne/story/line_205.ogg"
    Dianne "Oh, yes... I can't wait!"
    play sound wet_touch
    show cg brainwashed downlickgrind with dpose
    "I grab hold of her hips, and press my dick against her stretched opening."
    "My cock rubs her sensitive womanhood, making her shiver at the sensation."
    show cg brainwashed downmoangrind with dexp
    voice "voice/dianne/story/line_206.ogg"
    Dianne "Your cock is so hard and hot... It's going to drive me crazy!"
    show cg brainwashed puppyopengrind with dexp
    voice "voice/dianne/story/line_207.ogg"
    Dianne "I want it so badly, master... I want you to mess me up..."
    voice "voice/malos/story/line_198.ogg"
    Malos "Hah! You're so eager!"
    voice "voice/malos/story/line_199.ogg"
    Malos "Just a few minutes ago, you wanted to kill me, but now you're begging for me to use you!"
    voice "voice/malos/story/line_200.ogg"
    Malos "What delicious irony..."
    show cg brainwashed puppybitegrind with dexp
    voice "voice/dianne/story/line_208.ogg"
    Dianne "I'm so sorry for fighting you, master! I don't know what I was thinking."
    show cg brainwashed squintbitegrind with dexp
    voice "voice/dianne/story/line_209.ogg"
    Dianne "If I killed you, I'd have nothing left to live for..."
    show cg brainwashed puppymoangrind with dexp
    voice "voice/dianne/story/line_210.ogg"
    Dianne "I'll never attack you again, so please forgive me!"
    "As Dianne begs for my forgiveness, her slit grows more and more wet."
    "She pushes her hips up as far as she can, greedily craving my touch."
    voice "voice/malos/story/line_201.ogg"
    Malos "Fine, I'll let it slide."
    voice "voice/malos/story/line_202.ogg"
    Malos "But I need to punish you for your disobedience..."
    show cg brainwashed starewidegrind with dexp
    voice "voice/dianne/story/line_211.ogg"
    Dianne "Oh yes! Please punish me, master!"
    show cg brainwashed downtonguegrind with dexp
    voice "voice/dianne/story/line_212.ogg"
    Dianne "Punish my hole with your big fat dick!"
    voice "voice/malos/story/line_203.ogg"
    Malos "Hah! How could I refuse a request like that?!"
    "I've left her waiting for long enough."
    show cg:
        ease 3 xalign 0.15 zoom 0.55
    "I pull back my hips, letting the tip of my cock reach her entrance."
    voice "voice/malos/story/line_204.ogg"
    Malos "Here you go!"
    play sound insert
    show cg:
        parallel:
            easein 0.35 zoom 0.725 xalign 0.05
        parallel:
            pause 0.3
            ease 0.05 xoffset 8
            ease 0.05 xoffset -8
            ease 0.05 xoffset 5
            ease 0.05 xoffset -5
            ease 0.05 xoffset 3
            ease 0.05 xoffset -3
            ease 0.05 xoffset 0
    show cg brainwashed closedahegaoinside with dpose
    voice "voice/dianne/story/line_213.ogg"
    Dianne "Aaaaaaaaah~! Master!"
    "I thrust my length into her love tunnel, shoving it all the way to her deepest places."
    "She receives it with joy, her moist walls helping to ease the insertion."
    "Gripping my cock like a vice, she pulls me further inside and holds me there, not wanting to let go."
    show cg brainwashed rolltongueinside with dexp
    voice "voice/dianne/story/line_214.ogg"
    Dianne "Aaaaaah~! It's so good!"
    show cg brainwashed squintlickinside with dexp
    voice "voice/dianne/story/line_215.ogg"
    Dianne "I can feel you, master! Ah... You're inside me!"
    voice "voice/malos/story/line_205.ogg"
    Malos "Ah... How lovely..."
    "I take in the sensation as Dianne moans lustfully, clearly enjoying herself."
    show cg brainwashed rollmoaninside with dexp
    voice "voice/dianne/story/line_216.ogg"
    Dianne " Ah... Amazing... I need more!"
    show cg brainwashed puppywideinside with dexp
    voice "voice/dianne/story/line_217.ogg"
    Dianne "Punish me more, master! I'm begging you!"
    voice "voice/malos/story/line_206.ogg"
    Malos "Ha ha ha! What a lewd slave, begging for her master's cock!"
    voice "voice/malos/story/line_207.ogg"
    Malos "I'll gladly grant your wish!"
    "I pull back my hips, and thrust into her again, forcing her hole to stretch around me."
    play sound insert
    show cg at sex_shake(1, 0)
    show cg brainwashed closedtongueinside with dexp
    voice "voice/dianne/battle/hurt6.ogg"
    Dianne "Uh!"
    "An obscene, wet squish sounds out, and Dianne gasps in pleasure."
    "Slowly, I build up my rhythm, and our bodies move like one."
    call slow_sex_shaker
    show cg brainwashed squintmoaninside with dexp
    voice "voice/dianne/story/line_218.ogg"
    Dianne "Aaaaaah~! I love this!"
    call slow_sex_shaker
    show cg brainwashed rolllickinside with dexp
    voice "voice/dianne/story/line_219.ogg"
    Dianne "I love your cock, master! Ah! It feels too good!"
    voice "voice/malos/story/line_208.ogg"
    Malos "Hah! I'm starting to think this is a reward for you, not a punishment."
    voice "voice/malos/story/line_209.ogg"
    Malos "Not that it matters... You live to serve me now, so this is your only purpose!"
    call slow_sex_shaker
    show cg brainwashed squintwideinside with dexp
    voice "voice/dianne/story/line_220.ogg"
    Dianne "Oh, yes! You're right, master! Ah!"
    call slow_sex_shaker
    show cg brainwashed squintahegaoinside with dexp
    voice "voice/dianne/story/line_221.ogg"
    Dianne "I'm worthless... I'm just a hole to put your penis in!"
    call slow_sex_shaker
    show cg brainwashed rolltongueinside with dexp
    voice "voice/dianne/story/line_222.ogg"
    Dianne "So use me! Violate me! Ravish me!"
    voice "voice/malos/story/line_210.ogg"
    Malos "As you wish, you perverted slave!"
    call sex_shaker
    "I push my hips forward again and again, slamming my thick meat into her repeatedly."
    "Each thrust uses more force than the last, but it only increases Dianne's arousal."
    call sex_shaker
    show cg brainwashed puppymoaninside with dexp
    voice "voice/dianne/story/line_223.ogg"
    Dianne "Ah... hah... Ooh..."
    "She looks up at me with lusty eyes, pleading for me to be even rougher."
    "Her breasts bounce lewdly, and her breathing is shallow and quick."
    call sex_shaker
    show cg brainwashed puppyahegaoinside with dexp
    voice "voice/dianne/story/line_224.ogg"
    Dianne "Aaaah~! I love you, master!"
    "Her voice is filled with ecstasy as I abuse her body."
    "She tightens her womanhood around my cock, and massages it with her inner walls."
    "It feels amazing. Princesses truly are superior to commoners..."
    call sex_shaker
    voice "voice/malos/story/line_211.ogg"
    Malos "Ah... You're a good hole, slave."
    voice "voice/malos/story/line_212.ogg"
    Malos "I'm going to grant you the honor of taking my seed."
    call fast_sex_shaker
    show cg brainwashed downtongueinside with dexp
    voice "voice/dianne/story/line_225.ogg"
    Dianne "Oh! Oh, Yes! I want it!"
    call fast_sex_shaker
    show cg brainwashed squintwideinside with dexp
    voice "voice/dianne/story/line_226.ogg"
    Dianne "Give me all of it! Ah! Yes!"
    "Eagerly, she spreads herself wider, and I pound into her like a beast."
    "She cries out in ecstasy as I speed frantically towards climax."
    call fast_sex_shaker
    show cg brainwashed rolllickinside with dexp
    voice "voice/dianne/story/line_227.ogg"
    Dianne "Ah! Ah! Do it!"
    call fast_sex_shaker
    show cg brainwashed squintmoaninside with dexp
    voice "voice/dianne/story/line_228.ogg"
    Dianne "Fill me up with your semen! Make me pregnant!"
    call fast_sex_shaker
    show cg brainwashed squintahegaoinside with dexp
    voice "voice/dianne/story/line_229.ogg"
    Dianne "I want your baby, master!"
    "As she begs for my cum, I roughly slam my dick inside her faster and faster."
    call fast_sex_shaker
    voice "voice/malos/story/line_213.ogg"
    Malos "Graaaaaah! Here it is!"
    call fast_sex_shaker
    voice "voice/malos/story/line_214.ogg"
    Malos "Take all of it! Every last drop!"
    call fast_sex_shaker
    show cg brainwashed downtongueinside with dexp
    voice "voice/dianne/story/line_230.ogg"
    Dianne "Ah! Yes! It's here! Ah!"
    play sound cum
    show bg white with dissolve
    pause 1
    play sound cum2
    show cg brainwashed rollahegaocum:
        ease 0.5 zoom 0.83 xalign 0.1
    hide bg white with dissolve
    voice "voice/dianne/story/line_231.ogg"
    Dianne "Aaaaaaaaaaaaaaaah~!"
    play sound cum3
    voice "voice/dianne/story/line_231b.ogg"
    Dianne "Masteeeeeeeer~!"
    "With one final thrust, I plunge to her depths and explode inside her."
    play sound cum
    "My penis throbs as it releases an unbelievable amount of thick semen."
    "Shot after shot of the white seed flows inside her, trying to fit, but failing."
    "Strands drip down her inner thighs, making way for more."
    play sound cum3
    show cg brainwashed squintlickcum with dexp
    voice "voice/dianne/story/line_232.ogg"
    Dianne "Oh, yes... There's so much inside me..."
    show cg brainwashed puppytonguecum with dexp
    voice "voice/dianne/story/line_233.ogg"
    Dianne "Ah... Thank you so much, master!"
    voice "voice/malos/story/line_215.ogg"
    Malos "I'm not done yet...!"
    play sound cum
    show cg brainwashed closedmoancum with dexp
    "My semen oozes into her, flowing into every corner of her love tunnel."
    "It's surely made its way to her womb by now."
    show cg brainwashed squintahegaocum with dexp
    voice "voice/dianne/story/line_234.ogg"
    Dianne "I did it... I got master's baby..."
    show cg brainwashed rollahegaocum with dexp
    voice "voice/dianne/story/line_235.ogg"
    Dianne "It feels so good..."
    show cg brainwashed squintlickcum with dexp
    voice "voice/dianne/story/line_236.ogg"
    Dianne "But... now I want more..."
    "She can't go back, now."
    show cg:
        ease 8 xalign 0.0 zoom 0.6
    "Her mind has been altered beyond repair, and I've poured my essense inside her."
    "She'll be my loyal slave forever, and bear many children for me."
    "Even as I invade her homeland and destroy her kingdom, she'll beg for my cock."
    voice "voice/malos/story/line_216.ogg"
    Malos "So this is the last hope of humanity..."
    voice "voice/malos/story/line_217.ogg"
    Malos "How pathetic! Even your strongest warrior is helpless against me!"
    voice "voice/malos/story/line_218.ogg"
    Malos "I'll make all of you humans into slaves!"
    show cg brainwashed rolltonguecum with dexp
    voice "voice/dianne/story/line_237.ogg"
    Dianne "Ah... Yes."
    show cg brainwashed rolllickcum with dexp
    voice "voice/dianne/story/line_238.ogg"
    Dianne "We all exist to serve you, master."
    show cg brainwashed puppyahegaocum with dexp
    voice "voice/dianne/story/line_239.ogg"
    Dianne "I can't wait any longer... I want you to use me again..."
    voice "voice/malos/story/line_219.ogg"
    Malos "Of course, my little slave."
    voice "voice/malos/story/line_220.ogg"
    Malos "I'll use you as much as you want..."
    "As I get ready to make love to her again, I laugh maniacally."
    "Soon, the world will be mine!"
    stop music fadeout 3
    window hide
    scene bg black with dscene
    call nvl_start (show_bg=False)
    nv "Ending 3: Master's loyal slave"
    call nvl_end
    pause 1
    play music demon_king
    window show
    "..."
    "... ..."
    "... ... ..."
    "The human kingdom is doomed."
    "Their heroine has fallen, and there is nobody left to stand against the demon army."
    "How pathetic..."
    "As the Demon Realms expand, I set my sights on future conquests."
    "Let's see..."
    "The elven kingdoms look like a good target for my next assault..."
    "Ha ha ha!"
    "I can't wait!"
    window hide

    show DKALogo with dscene:
        xalign 0.5 yalign 0.4
    pause 5
    $ renpy.pause(0.1, hard=True)
    hide DKALogo with dscene
    hide text with dscene
    pause 1

    call nvl_start (show_bg=False)
    if not persistent.hard_mode_unlocked_message:
        $ persistent.hard_mode_unlocked_message = True
        call nvl_clear
        nv "Hard mode has been unlocked!"
        nv "Play the game again, and test your skill!"
    if hard_mode:
        call nvl_clear
        nv "Wow! You beat hard mode! What a dedicated player!"
        nv "You must have spent a lot of time playing to get this far."
        nv "All I can do is say thanks for playing, from the bottom of my heart!"
    call nvl_clear
    nv "Thanks for playing our game!"
    nv "If you want to see more games like this,\nconsider {a=https://www.patreon.com/Belgerum}supporting our future games on Patreon!{/a}"
    nv "You can also {a=https://belgerum.bandcamp.com/album/demon-king-domination-soundtrack}download the soundtrack{/a} if you like the game's music."
    call nvl_clear
    nv "Stay happy, stay healthy, stay horny!"
    nv "~ Belgerum ~"
    call nvl_end
    pause 1
    stop sound
    $ renpy.end_replay()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
