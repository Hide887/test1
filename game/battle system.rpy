


label boss_fight:
    if persistent.hard_mode_unlocked:
        call screen confirm(message=_("Activate hard mode?"), yes_action=[Hide("confirm"),Jump("hard_mode")], no_action=[Hide("confirm"), Jump("boss_fight_2")])
    else:
        jump boss_fight_2

label hard_mode:
    $ php = 16
    $ pmaxhp = 16
    $ hard_mode = True

label boss_fight_2:
    stop music fadeout 1
    call battletext (0.5, 0.45, "#f33", "BATTLE START", 50)
    with None
    play music battle fadeout 1
    show expression im.Tile("images/particles/fire.png", size=(5760, 1080)) as fire_bg behind dianne:
        parallel:
            xalign 0.0
            linear 20 xalign 1.0
            repeat
        parallel:
            alpha 0.1
            ease 3.2 alpha 0.3
            ease 3.2 alpha 0.1
            repeat
    show expression im.Tile("images/particles/fire.png", size=(5760, 1080)) as fire_bg2 behind dianne:
        parallel:
            xalign 1.0
            linear 30 xalign 0.0
            repeat
        parallel:
            alpha 0.1
            ease 5.2 alpha 0.3
            ease 5.2 alpha 0.1
            repeat
    with dscene
    $ last2_eaction = "attack"
    $ last_eaction = "attack"
    $ last_paction = "attack"
    call battle_turn
    return



screen battle_menu():
    use stats_frame
    imagebutton auto "gui/battleicons/Attack_button_%s.png" alt "Attack" action [SetVariable("paction","attack"), Jump("dianne_decide"), SelectedIf(None)] xpos 0.32 focus_mask True at battle_button_move
    imagebutton auto "gui/battleicons/Counter_button_%s.png" alt "Counter" action [SetVariable("paction","counter"), Jump("dianne_decide"), SelectedIf(None)] xpos 0.44 focus_mask True at battle_button_move
    imagebutton auto "gui/battleicons/Heal_button_%s.png" alt "Heal" action [SetVariable("paction","heal"), Jump("dianne_decide"), SelectedIf(None)] xpos 0.56 focus_mask True at battle_button_move
    imagebutton auto "gui/battleicons/Charge_button_%s.png" alt "Charge" action [SetVariable("paction","charge"), Jump("dianne_decide"), SelectedIf(None)] xpos 0.68 focus_mask True at battle_button_move
    hbox:
        xalign 0.5
        yanchor 1.0 ypos 0.99
        spacing 20
        textbutton _("Save") text_font gui.name_font text_size 35 at NVL_buttons_move action ShowMenu('save') alt _("Save") text_outlines [(2, "#000c", 0, 0)]
        textbutton _("Load") text_font gui.name_font text_size 35 at NVL_buttons_move action ShowMenu('load') alt _("Load") text_outlines [(2, "#000c", 0, 0)]
        textbutton _("Settings") text_font gui.name_font text_size 35 at NVL_buttons_move action ShowMenu('preferences') alt _("Settings") text_outlines [(2, "#000c", 0, 0)]
        textbutton _("Auto") text_font gui.name_font text_size 35 at NVL_buttons_move action Preference("auto-forward", "toggle") alt _("Auto") text_outlines [(2, "#000c", 0, 0)]
        textbutton _("Skip") text_font gui.name_font text_size 35 at NVL_buttons_move action Skip() alt _("Skip") text_outlines [(2, "#000c", 0, 0)]
        textbutton _("Hide") text_font gui.name_font text_size 35 at NVL_buttons_move action HideInterface() alt _("Hide") text_outlines [(2, "#000c", 0, 0)]


init -2:
    transform battle_button_move:
        xanchor 0.5 yanchor 1.0 ypos 1.1 alpha 0.0 zoom 0.9
        on idle:
            easein 0.2 ypos .89 alpha 1.0 zoom 0.85
        on hover:
            easein 0.2 ypos .885 alpha 1.0 zoom 1.0
        on hide:
            easeout 0.2 ypos 1.1 alpha 0.0 zoom 0.85



label battle_turn:
    $ last2_eaction = last_eaction
    $ last_eaction = eaction
    $ last_paction = paction
    call dianne_natural
    window hide
    $ renpy.block_rollback()
    call screen battle_menu



label turn_decide:
    show screen stats_frame
    $ renpy.block_rollback()
    hide screen battle_menu
    window show
    if (eaction == "counter" and paction == "attack") or (eaction == "charge" and paction == "heal"):
        call dianne_turn
        call player_turn
    else:
        call player_turn
        call dianne_turn

    if ehp <= 100 - (battle_phase*20):
        $ battle_phase += 1
        hide screen stats_frame
        $ jumptarget = 'phase_' + str(battle_phase) + '_intro'
        $ renpy.call(jumptarget)
        call battletext (0.5, 0.45, "#f33", "Phase "+str(battle_phase), 50)
        show screen stats_frame
    jump battle_turn



label player_turn:
    $ jumptarget = 'p' + paction
    $ renpy.call(jumptarget)
    $ renpy.block_rollback()
    if ehp <= 0:
        $ renpy.pop_call()
        jump ending_3
    return



label pattack:
    $ damage = 4
    if pcharged:
        $ damage = 10
    if eaction == "counter":
        $ damage = 0

    call battletext (0.2, 0.15, "#fff", "Attack")
    $ saylist = ["Take this!", "Ha ha ha!", "Feel my wrath!", "Graaaah!", "I'll destroy you!"]
    $ saynumber = pattack_number.next()
    $ say1 = saylist[saynumber]
    voice str("voice/malos/battle/attack"+str(saynumber+1)+".ogg")
    Malos "[say1]"
    $ renpy.block_rollback()

    call dianne_hurt

    call battletext (0.5, 0.45, "#f33", "-"+str(damage)+" HP")
    if pcharged and eaction == "counter":
        $ say1 = renpy.random.choice(["I use my charged energy for a massive attack, but Dianne blocks it!", "I unleash my furious aura in a powerful punch, but Dianne deflects it!", "I use my stored power to launch a giant strike, but Dianne parries!"])
    elif pcharged:
        $ say1 = renpy.random.choice(["I deal huge damage using my charged energy!", "I unleash a charged strike!", "I use all of my power in a huge punch!"])
    elif eaction == "counter":
        $ say1 = renpy.random.choice(["I try to land a savage blow, but Dianne blocks it!", "I rush to attack, but Dianne easily parries my strike!", "I try to punch Dianne, but she deflects the blow!"])
    else:
        $ say1 = renpy.random.choice(["I attack with a savage punch!", "I lunge forward, swinging my fists!", "I leap into range and lash out my claws!", "I rush into the fray, punching madly!", "I shout a battle cry and attack!"])
    $ say2 = renpy.random.choice(["Dianne takes "+str(damage)+" damage!", "I hit Dianne for "+str(damage)+" damage!", "The attack deals "+str(damage)+" damage!", "The blow inflicts "+str(damage)+" damage!"])
    "[say1]\n[say2]"

    $ pcharged = False
    return



label pcounter:
    $ damage = 2
    if pcharged:
        $ damage = 5

    call battletext (0.2, 0.15, "#fff", "Counter")
    $ saylist = ["Come at me, princess!", "I'll block all of your attacks!", "I'm invincible!", "Just try to hit me!", "You think you can damage me?"]
    $ saynumber = pcounter_number.next()
    $ say1 = saylist[saynumber]
    voice str("voice/malos/battle/counter"+str(saynumber+1)+".ogg")
    Malos "[say1]"
    $ renpy.block_rollback()

    call dianne_hurt

    call battletext (0.5, 0.45, "#f33", "-"+str(damage)+" HP")
    if pcharged:
        $ say1 = renpy.random.choice(["I spend my charged energy on a swift attack, then pull back to safety!", "I toss a charged punch while defending myself!", "I launch a strong attack from a safe distance!"])
    else:
        $ say1 = renpy.random.choice(["I make a light jab, and then fall back to a defensive stance!", "I send Dianne a light blow while holding back!", "I take a defensive pose, and attack cautiously!", "I stay a safe distance away from Dianne while making light punches!", "I strike at Dianne while defending myself!"])
    $ say2 = renpy.random.choice(["Dianne takes "+str(damage)+" damage!", "I hit Dianne for "+str(damage)+" damage!", "The attack deals "+str(damage)+" damage!", "The blow inflicts "+str(damage)+" damage!"])
    "[say1]\n[say2]"

    $ pcharged = False
    return



label pheal:
    call battletext (0.2, 0.15, "#fff", "Heal")
    $ saylist = ["I can do this all day!", "Your attacks mean nothing when I can heal myself!", "Behold my power of regeneration!", "No damage can hold me down!", "You'll never defeat me!"]
    $ saynumber = pheal_number.next()
    $ say1 = saylist[saynumber]
    voice str("voice/malos/battle/heal"+str(saynumber+1)+".ogg")
    Malos "[say1]"
    voice sustain
    $ renpy.block_rollback()

    $ hpheal = 2
    if pcharged:
        $ hpheal = 5
    if eaction == "charge":
        $ hpheal += 3
    if hpheal + php > pmaxhp:
        $ hpheal = pmaxhp-php
    $ php += hpheal

    play sound heal
    show bg green as screenflash with dexp
    hide screenflash with dexp

    call battletext (0.2, 0.15, "#00C400", "+"+str(hpheal)+" HP")

    if pcharged and eaction == "charge":
        $ say1 = renpy.random.choice(["I use my charged energy and Dianne's aura to heal!", "I restore my health with magic, taking advantage of me and Dianne's charging!", "I unleash a massive healing spell using the energy around me!"])
    elif pcharged:
        $ say1 = renpy.random.choice(["I heal myself with my charged energy!", "I use my charge to recover my strength!", "I use magic and my charged aura to heal!"])
    elif eaction == "charge":
        $ say1 = renpy.random.choice(["I heal myself, taking advantage of Dianne's aura!", "I absorb some of Dianne's charge and use it to restore my strength!", "I sooth my pain with mag energy taken from Dianne!"])
    else:
        $ say1 = renpy.random.choice(["I cast a minor healing spell!", "I hold my hand over my wounds, mending them with magic!", "I weave magic energy through myself, soothing my pain!"])
    $ say2 = renpy.random.choice(["I recover "+str(hpheal)+" HP!", "I am healed for "+str(hpheal)+" HP!", str(hpheal)+" HP is restored!"])
    "[say1]\n[say2]"
    $ pcharged = False
    return



label pcharge:
    call battletext (0.2, 0.15, "#fff", "Charge")
    $ saylist = ["Prepare yourself, weakling!", "I'll show you my true power!", "This isn't even my final form!", "My strength only grows!", "Uuuuaaaaaaaah!"]
    $ saynumber = pcharge_number.next()
    $ say1 = saylist[saynumber]
    voice str("voice/malos/battle/charge"+str(saynumber+1)+".ogg")
    Malos "[say1]"
    voice sustain
    $ renpy.block_rollback()

    play sound charge
    show bg white as screenflash with dexp
    hide screenflash with dexp

    if pcharged:
        $ say1 = renpy.random.choice(["I keep charging my energy!", "I continue to intensify my fighting spirit!", "I gather more power, focusing myself!"])
    else:
        $ say1 = renpy.random.choice(["I start charging a powerful attack!", "I gather energy from around me, and get ready to unleash it!", "I focus my magic to empower my next move!", "I steel my nerves and focus my strength!", "I concentrate, and cast a spell to grant me a powerful aura!"])
    "[say1]"

    $ pcharged = True
    return



label player_hurt:
    $ php -= damage
    if php < 0:
        $ php = 0
    show dianne:
        zoom 0.61 yoffset 0
        linear 0.1 zoom 0.71 yoffset 40
        easeout 0.2 zoom 0.61 yoffset 0
    if battle_phase == 5:
        show light_effect:
            linear 0.1 zoom 1.0
            easeout 0.2 zoom 0.9
    show bg:
        xoffset 0
        pause 0.1
        ease 0.05 xoffset 15
        ease 0.05 xoffset -15
        ease 0.05 xoffset 10
        ease 0.05 xoffset -10
        ease 0.05 xoffset 6
        ease 0.05 xoffset -6
        ease 0.05 xoffset 0
    if damage >= 4:
        pass
        if echarged and eaction == "attack":
            $ voice(phurtbig_list.next(), tag="Malos")
        else:
            $ voice(phurt_list.next(), tag="Malos")
    else:
        voice sustain
    if damage == 0:
        play sound block
    else:
        play sound hit
    return










label dianne_turn:
    if eaction == "attack":
        call eattack
    elif eaction == "counter":
        call ecounter
    elif eaction == "heal":
        call eheal
    elif eaction == "charge":
        call echarge
    $ renpy.block_rollback()
    if php <= 0:
        $ renpy.pop_call()
        if battle_phase == 5:
            jump ending_2
        else:
            jump ending_1
    return



label dianne_decide:
    if battle_phase == 1:
        if last_eaction == "attack" and ehp < 100:
            $ eaction = "heal"
        else:
            $ eaction = "attack"
    elif battle_phase == 2:
        if echarged:
            $ eaction = "counter"
        elif last_eaction == "counter":
            $ eaction = "attack"
        else:
            $ eaction = "charge"
    elif battle_phase == 3:
        $ eaction = last_paction
    elif battle_phase == 4:
        if echarged:
            if last_paction == "attack":
                $ eaction = "counter"
            elif last_paction == "counter":
                $ eaction = "counter"
            elif last_paction == "heal":
                $ eaction = "attack"
            else:
                $ eaction = "counter"
        elif last_paction == "attack":
            $ eaction = "counter"
        elif last_paction == "counter":
            $ eaction = "charge"
        elif last_paction == "heal":
            $ eaction = "attack"
        else:
            $ eaction = "counter"
    else:
        $ echarged = True
        if last_eaction == "attack":
            $ eaction = "counter"
        elif last_eaction == "counter":
            $ eaction = "heal"
        else:
            $ eaction = "attack"
    jump turn_decide



label eattack:
    call battletext (0.5, 0.45, "#fff", "Attack")
    if battle_phase == 5 or echarged:
        show dianne attack2 with dexp
    else:
        show dianne attack with dexp
    $ saynumber = eattack_number.next()
    $ saylist = ["Take this, you monster!", "This is for my people!", "You can't escape from justice, Malos!", "I'll make you pay for your cruelty!", "My strength will prevail!"]
    $ say1 = saylist[saynumber]
    voice str("voice/dianne/battle/attack"+str(saynumber+1)+".ogg")
    Dianne "[say1]"
    $ renpy.block_rollback()

    $ damage = 4
    if echarged:
        $ damage = 10
    if paction == "counter":
        $ damage = 0

    call player_hurt

    call battletext (0.2, 0.15, "#f33", "-"+str(damage)+" HP")

    if echarged and paction == "counter":
        $ say1 = renpy.random.choice(["Dianne uses her charged energy for a massive blow, but I block it!", "Dianne unleashes her aura in a powerful attack, but I deflect it!", "Dianne uses her stored power to launch a giant strike, but I parry!"])
    elif echarged:
        $ say1 = renpy.random.choice(["Dianne deals massive damage using her charged energy!", "Dianne uses her aura to hit me with a huge attack!", "Dianne swings her sword, making good use of her charge!"])
    elif paction == "counter":
        $ say1 = renpy.random.choice(["Dianne attacks, but I block it!", "Dianne swings her sword at me, but I parry it!", "Dianne sends a flying attack, but I deflect it!"])
    else:
        $ say1 = renpy.random.choice(["Dianne lashes out with her sword!", "Dianne rushes forward, swinging her blade!", "Dianne swipes her sword at me!", "Dianne shouts a battle cry and attacks!", "Dianne lunges at me, slashing her sword!"])
    $ say2 = renpy.random.choice(["I take "+str(damage)+" damage!", "I suffer "+str(damage)+" damage!", "I am hit for "+str(damage)+" damage!", "The attack deals "+str(damage)+" damage!"])
    "[say1]\n[say2]"

    if battle_phase != 5 and echarged:
        hide light_effect with dpose
    $ echarged = False
    return



label ecounter:
    call battletext (0.5, 0.45, "#fff", "Counter")
    show dianne counter with dexp
    $ saynumber = ecounter_number.next()
    $ saylist = ["You won't defeat me, Malos!", "I won't let you win!", "For my kindom, I'll live on!", "I will be my people's shield!", "Nothing you do will break my spirit!"]
    $ say1 = saylist[saynumber]
    voice str("voice/dianne/battle/counter"+str(saynumber+1)+".ogg")
    Dianne "[say1]"
    $ renpy.block_rollback()

    $ damage = 2
    if echarged:
        $ damage = 5

    call player_hurt

    call battletext (0.2, 0.15, "#f33", "-"+str(damage)+" HP")
    if echarged:
        $ say1 = renpy.random.choice(["Dianne quickly attacks using her charged energy, then defends!", "Dianne uses her charged energy for a swift attack, and then protects herself!", "Dianne readies herself to parry while launching a weaker attack with her charge!"])
    else:
        $ say1 = renpy.random.choice(["Dianne makes a swift attack, then readies herself to parry!", "Dianne defends herself while making a weak attack!", "Dianne strikes, then holds up her blade to block my attacks!", "Dianne attacks quickly, then gets ready to defend!", "Dianne retreats to safety while making light attacks!"])
    $ say2 = renpy.random.choice(["I take "+str(damage)+" damage!", "I suffer "+str(damage)+" damage!", "I am hit for "+str(damage)+" damage!", "The attack deals "+str(damage)+" damage!"])
    "[say1]\n[say2]"

    if battle_phase != 5 and echarged:
        hide light_effect with dpose
    $ echarged = False
    return



label eheal:
    call battletext (0.5, 0.45, "#fff", "Heal")
    show dianne charge with dexp
    $ saynumber = eheal_number.next()
    $ saylist = ["Oh holy light, heal me!", "May light shine upon me!", "Bless me, spirits of virtue!", "May the gods restore my strength!", "I call upon the goddess of healing!"]
    $ say1 = saylist[saynumber]
    voice str("voice/dianne/battle/heal"+str(saynumber+1)+".ogg")
    Dianne "[say1]"
    voice sustain
    $ renpy.block_rollback()

    $ hpheal = 2
    if echarged:
        $ hpheal = 5
    if paction == "charge":
        $ hpheal += 3
    if hpheal + ehp > emaxhp:
        $ hpheal = emaxhp-ehp
    $ ehp += hpheal

    play sound heal
    show bg green as screenflash with dexp
    hide screenflash with dexp

    call battletext (0.5, 0.45, "#00C400", "+"+str(hpheal)+" HP")
    if echarged and paction == "charge":
        $ say1 = renpy.random.choice(["Dianne heals herself using her charged energy, and my own aura!", "Dianne casts a magic healing spell, taking advantage of potent magic from around her!"])
    elif echarged:
        $ say1 = renpy.random.choice(["Dianne uses her charged energy to heal herself!", "Dianne restores her fighting spirit with her magic aura!"])
    elif paction == "charge":
        $ say1 = renpy.random.choice(["Dianne drains some of my charged energy for healing!", "Dianne takes advantage of my charging to cast a powerful healing spell!", "Dianne soothes her pain using magic from my aura!"])
    else:
        $ say1 = renpy.random.choice(["Dianne casts a healing spell!", "Dianne mends her wounds with magic!", "Dianne uses magic energy to soothe her pain!", "Dianne recieves healing from the heavens!", "Dianne restores her strength with holy light!"])
    $ say2 = renpy.random.choice(["She recovers "+str(hpheal)+" HP!", "She is healed for "+str(hpheal)+" HP!", str(hpheal)+" HP is restored!"])
    "[say1]\n[say2]"
    if battle_phase != 5 and echarged:
        hide light_effect with dpose
    $ echarged = False
    return



label echarge:
    call battletext (0.5, 0.45, "#fff", "Charge")
    show dianne charge with dexp
    $ saynumber = echarge_number.next()
    $ saylist = ["Gods, grant me the power I need!", "Come, spirits! Give me your power!", "I call upon the strength of my ancestors!", "May the heavens side with me!", "The light will help me claim victory!"]
    $ say1 = saylist[saynumber]
    voice str("voice/dianne/battle/charge"+str(saynumber+1)+".ogg")
    Dianne "[say1]"
    voice sustain
    $ renpy.block_rollback()
    play sound charge
    show bg white as screenflash with dexp
    show light_effect behind dianne:
        xalign 0.5 yalign 0.5 zoom 0.9
    hide screenflash with dexp
    if echarged:
        $ say1 = renpy.random.choice(["Dianne continues to charge!", "Dianne keeps charging her energy!", "Dianne is still gathering her power!"])
    else:
        $ say1 = renpy.random.choice(["Dianne is charging her strength!", "Dianne uses magic to amplify her power!", "Dianne calls upon the gods to aid her!", "Dianne gathers a magic aura around herself!", "Dianne is gathering power from her surroundings!"])
    "[say1]"
    if paction == "heal":
        call dianne_natural
    $ echarged = True
    return



label dianne_hurt:
    $ ehp -= damage
    if ehp < 0:
        $ ehp = 0
    show bg:
        linear 0.1 zoom 0.68
        easeout 0.2 zoom 0.6
    if battle_phase == 5 or echarged:
        show light_effect:
            linear 0.1 zoom 1.0
            easeout 0.2 zoom 0.9
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
    if damage >= 4:
        show dianne hurt with Dissolve(0.1)
        if pcharged and paction == "attack":
            $ voice(ehurtbig_list.next(), tag="Dianne")
        else:
            $ voice(ehurt_list.next(), tag="Dianne")
    else:
        voice sustain
    if damage == 0:
        play sound block
    else:
        play sound punch
    return



label dianne_natural:
    show bg:
        xalign 0.5 yalign 0.5 xoffset 0 yoffset 0 zoom 0.6
    if battle_phase == 5:
        show light_effect:
            zoom 0.9
    show dianne standby at center with dexp:
        alpha 1 zoom 0.61 xoffset 0 yoffset 0
    return












transform battletexttrans:
    alpha 0.0 xpos battlexpos xanchor 0.5 ypos battleypos yanchor 0.5
    parallel:
        linear 0.2 alpha 1.0
        pause 0.3
        linear 1.5 alpha -1.0
    parallel:
        linear 2 ypos (battleypos-0.2)



screen battletext1():
    zorder 10
    text "{b}{size=[battletextsize1]}{color=[battletextcolor1]}[battledisptext1]{/color}{/size}{/b}" outlines [(2, "#000c", 0, 0)] at battletexttrans
    timer 2 action Hide("battletext1")
screen battletext2():
    zorder 10
    text "{b}{size=[battletextsize2]}{color=[battletextcolor2]}[battledisptext2]{/color}{/size}{/b}" outlines [(2, "#000c", 0, 0)] at battletexttrans
    timer 2 action Hide("battletext2")
screen battletext3():
    zorder 10
    text "{b}{size=[battletextsize3]}{color=[battletextcolor3]}[battledisptext3]{/color}{/size}{/b}" outlines [(2, "#000c", 0, 0)] at battletexttrans
    timer 2 action Hide("battletext3")
screen battletext4():
    zorder 10
    text "{b}{size=[battletextsize4]}{color=[battletextcolor4]}[battledisptext4]{/color}{/size}{/b}" outlines [(2, "#000c", 0, 0)] at battletexttrans
    timer 2 action Hide("battletext4")
screen battletext5():
    zorder 10
    text "{b}{size=[battletextsize5]}{color=[battletextcolor5]}[battledisptext5]{/color}{/size}{/b}" outlines [(2, "#000c", 0, 0)] at battletexttrans
    timer 2 action Hide("battletext5")
screen battletext6():
    zorder 10
    text "{b}{size=[battletextsize6]}{color=[battletextcolor6]}[battledisptext6]{/color}{/size}{/b}" outlines [(2, "#000c", 0, 0)] at battletexttrans
    timer 2 action Hide("battletext6")



label battletext(batxpos=0.5, batypos=0.5, battextcolor="#fff", batdisptext="sample text", battextsize="39"):
    if persistent.show_battletext:
        $ battlexpos = batxpos
        $ battleypos = batypos
        if battletextcount == 1:
            $ battletextcolor1 = battextcolor
            $ battledisptext1 = batdisptext
            $ battletextsize1 = battextsize
            hide screen battletext1
            show screen battletext1
        elif battletextcount == 2:
            $ battletextcolor2 = battextcolor
            $ battledisptext2 = batdisptext
            $ battletextsize2 = battextsize
            hide screen battletext2
            show screen battletext2
        elif battletextcount == 3:
            $ battletextcolor3 = battextcolor
            $ battledisptext3 = batdisptext
            $ battletextsize3 = battextsize
            hide screen battletext3
            show screen battletext3
        elif battletextcount == 4:
            $ battletextcolor4 = battextcolor
            $ battledisptext4 = batdisptext
            $ battletextsize4 = battextsize
            hide screen battletext4
            show screen battletext4
        elif battletextcount == 5:
            $ battletextcolor5 = battextcolor
            $ battledisptext5 = batdisptext
            $ battletextsize5 = battextsize
            hide screen battletext5
            show screen battletext5
        elif battletextcount == 6:
            $ battletextcolor6 = battextcolor
            $ battledisptext6 = batdisptext
            $ battletextsize6 = battextsize
            hide screen battletext6
            show screen battletext6
        $ battletextcount += 1
        if battletextcount == 7:
            $ battletextcount = 1
    return



init -2:


    style gm_nav_button:
        size_group "gm_nav"



screen stats_frame():
    frame:
        xpadding 36 ypadding 36 xsize 600 ysize 170 xanchor 0.0 xpos 0.0 yalign 0.0
        text "Malos" alt "" size 60 ypos -20 color "#f00" font gui.name_font outlines [ (2, "#000", 0, 0)]
        hbox:
            text "HP " alt "" size 35 ypos 61 xmaximum 200
            bar value AnimatedValue(php, pmaxhp, 0.1) xmaximum 350 ysize 45 ypos 55 left_gutter 10 right_gutter 10
        text "[php]/[pmaxhp]" alt "" size 35 xalign 1.0 ypos 61
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
