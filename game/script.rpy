


















define narrator = Character(None)
define nv = Character(None, kind=nvl, what_xalign=0.5, window_xalign=0.5, what_text_align=0.5, what_prefix="{cps=0}")
define Malos = Character("Malos", color="#f00", image="malos", voice_tag="Malos")
define Dianne = Character("Dianne", color="#dd0", image="dianne", voice_tag="Dianne")





image bg black = "#000"
image bg white = "#fff"
image bg red = "#FF1500"
image bg pink = "#FF5672"
image bg green = "#0f0"
image bg hall = "images/bg/hall.png"



image belgerum = "images/cg/belgerum.png"
image DKALogo = "images/cg/DKALogo.png"
image light_effect = "images/particles/light.png"




define audio.demon_king = "music/main_menu.ogg"
define audio.heroine = "music/heroine.ogg"
define audio.battle = "music/battle.ogg"
define audio.ritual = "music/ritual.ogg"
define audio.dungeon = "music/dungeon.ogg"
define audio.brainwashed = "music/brainwashed.ogg"




define audio.wet_touch = "sounds/wet_touch.ogg"
define audio.insert = "sounds/insert.ogg"
define audio.insert2 = "sounds/insert2.ogg"
define audio.insert3 = "sounds/insert3.ogg"
define audio.slow_sex = "sounds/slow_sex.ogg"
define audio.sex = "sounds/sex.ogg"
define audio.sex2 = "sounds/sex2.ogg"
define audio.fast_sex = "sounds/fast_sex.ogg"
define audio.cum = "sounds/cum.ogg"
define audio.cum2 = "sounds/cum2.ogg"
define audio.cum3 = "sounds/cum3.ogg"

define audio.footsteps = "sounds/footsteps.ogg"
define audio.chains = "sounds/chains.ogg"
define audio.circlet = "sounds/circlet.ogg"
define audio.block = "sounds/block.ogg"
define audio.heal = "sounds/heal.ogg"
define audio.charge = "sounds/charge.ogg"
define audio.hit = "sounds/hit.ogg"
define audio.hit2 = "sounds/hit2.ogg"
define audio.punch = "sounds/punch.ogg"
define audio.evil_magic = "sounds/evil_magic.ogg"
define audio.stab = "sounds/stab.mp3"
define audio.rip = "sounds/rip.ogg"
define audio.thud = "sounds/thud.ogg"





init python:
    import random
    from random import shuffle
    import math

default php = 50
default pmaxhp = 50
default ehp = 100
default emaxhp = 100
default battle_phase = 1
default battletextcount = 1
default paction = ""
default eaction = ""
default pcharged = False
default echarged = False
default hard_mode = False
default clothes_ripped = False

init python:
    eattack_number = itertools.cycle([1, 2, 3, 4, 0])
    ecounter_number = itertools.cycle([0, 1, 2, 3, 4])
    eheal_number = itertools.cycle([0, 1, 2, 3, 4])
    echarge_number = itertools.cycle([0, 1, 2, 3, 4])
    pattack_number = itertools.cycle([0, 1, 2, 3, 4])
    pcounter_number = itertools.cycle([0, 1, 2, 3, 4])
    pheal_number = itertools.cycle([0, 1, 2, 3, 4])
    pcharge_number = itertools.cycle([0, 1, 2, 3, 4])
    ehurt_list = itertools.cycle(["voice/dianne/battle/hurt1.ogg", "voice/dianne/battle/hurt2.ogg", "voice/dianne/battle/hurt3.ogg", "voice/dianne/battle/hurt4.ogg", "voice/dianne/battle/hurt5.ogg", "voice/dianne/battle/hurt6.ogg", "voice/dianne/battle/hurt7.ogg"])
    ehurtbig_list = itertools.cycle(["voice/dianne/battle/hurtbig1.ogg", "voice/dianne/battle/hurtbig2.ogg", "voice/dianne/battle/hurtbig3.ogg"])
    phurt_list = itertools.cycle(["voice/malos/battle/hurt1.ogg", "voice/malos/battle/hurt2.ogg", "voice/malos/battle/hurt3.ogg", "voice/malos/battle/hurt4.ogg", "voice/malos/battle/hurt5.ogg"])
    phurtbig_list = itertools.cycle(["voice/malos/battle/hurtbig1.ogg", "voice/malos/battle/hurtbig2.ogg", "voice/malos/battle/hurtbig3.ogg"])
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['hide_windows'].remove('mouseup_2')
    config.keymap['game_menu'].append('mouseup_2')
    config.keymap['game_menu'].remove('mouseup_3')
define save_name = "Save"
define _game_menu_screen = "save"
default persistent.show_battletext = True
default persistent.hard_mode_unlocked = False
default persistent.hard_mode_unlocked_message = False







transform center:
    xalign 0.5 ypos 0.25 yanchor 0.25 alpha 1
transform right:
    xpos 0.73 xanchor 0.5 ypos 0.25 yanchor 0.25 alpha 1
transform left:
    xpos 0.27 xanchor 0.5 ypos 0.25 yanchor 0.25 alpha 1



transform center_fade_in:
    xalign 0.5 ypos 0.25 yanchor 0.25 alpha 0
    easein 0.7 alpha 1
transform center_fade_out:
    xalign 0.5 ypos 0.25 yanchor 0.25 alpha 1
    easeout 0.7 alpha 0

transform center_left_in:
    xalign 0.5 ypos 0.25 yanchor 0.25 xoffset -50 alpha 0
    easein 0.7 xoffset 0 alpha 1
transform center_right_in:
    xalign 0.5 ypos 0.25 yanchor 0.25 xoffset 50 alpha 0
    easein 0.7 xoffset 0 alpha 1
transform center_left_out:
    xalign 0.5 ypos 0.25 yanchor 0.25 xoffset 0 alpha 1
    easeout 0.7 xoffset -50 alpha 0
transform center_right_out:
    xalign 0.5 ypos 0.25 yanchor 0.25 xoffset 0 alpha 1
    easeout 0.7 xoffset 50 alpha 0



transform right_left_in:
    xpos 0.73 xanchor 0.5 ypos 0.25 yanchor 0.25 xoffset -50 alpha 0
    easein 0.7 xoffset 0 alpha 1
transform right_right_in:
    xpos 0.73 xanchor 0.5 ypos 0.25 yanchor 0.25 xoffset 50 alpha 0
    easein 0.7 xoffset 0 alpha 1
transform right_left_out:
    xpos 0.73 xanchor 0.5 ypos 0.25 yanchor 0.25 xoffset 0 alpha 1
    easeout 0.7 xoffset -50 alpha 0
transform right_right_out:
    xpos 0.73 xanchor 0.5 ypos 0.25 yanchor 0.25 xoffset 0 alpha 1
    easeout 0.7 xoffset 50 alpha 0



transform left_left_in:
    xpos 0.27 xanchor 0.5 ypos 0.25 yanchor 0.25 xoffset -50 alpha 0
    easein 0.7 xoffset 0 alpha 1
transform left_right_in:
    xpos 0.27 xanchor 0.5 ypos 0.25 yanchor 0.25 xoffset 50 alpha 0
    easein 0.7 xoffset 0 alpha 1
transform left_left_out:
    xpos 0.27 xanchor 0.5 ypos 0.25 yanchor 0.25 xoffset 0 alpha 1
    easeout 0.7 xoffset -50 alpha 0
transform left_right_out:
    xpos 0.27 xanchor 0.5 ypos 0.25 yanchor 0.25 xoffset 0 alpha 1
    easeout 0.7 xoffset 50 alpha 0







transform side_same_transform(old, new):
    old
    new with Dissolve(0.2, alpha=True)
define config.side_image_same_transform = side_same_transform

transform change_transform(old, new):
    contains:
        old
        yalign 1.0 xoffset 0 alpha 1
        easeout 0.2 xoffset -15 alpha 0
    contains:
        new
        yalign 1.0 xoffset -15 alpha 0
        easein 0.2 xoffset 0 alpha 1
define config.side_image_change_transform = change_transform



define dexp = Dissolve(0.15)
define pexp = Pause(0.15)
define dpose = Dissolve(0.3)
define ppose = Pause(0.3)
define dlong = Dissolve(1)
define dscene = Dissolve(1.4)

transform sex_shake(shake_count=8, pause_length=0.1):
    ease 0.04 xoffset 10
    ease 0.04 xoffset -10
    ease 0.04 xoffset 5
    ease 0.04 xoffset -5
    ease 0.04 xoffset 3
    ease 0.04 xoffset -3
    ease 0.04 xoffset 0
    pause pause_length
    repeat shake_count

transform vsex_shake(shake_count=8, pause_length=0.1):
    ease 0.04 yoffset 10
    ease 0.04 yoffset -10
    ease 0.04 yoffset 5
    ease 0.04 yoffset -5
    ease 0.04 yoffset 3
    ease 0.04 yoffset -3
    ease 0.04 yoffset 0
    pause pause_length
    repeat shake_count

label fast_sex_shaker(dir="h"):
    play sound fast_sex
    if dir=="h":
        show cg at sex_shake(16, 0)
    else:
        show cg at vsex_shake(16, 0)
    return

label slow_sex_shaker(dir="h"):
    play sound slow_sex
    if dir=="h":
        show cg at sex_shake(7, 0.52)
    else:
        show cg at vsex_shake(7, 0.52)
    return

label sex_shaker(dir="h"):
    play sound sex
    if dir=="h":
        show cg at sex_shake(8, 0.162)
    else:
        show cg at vsex_shake(8, 0.162)
    return

label nvl_clear:
    nvl clear
    with dexp
    return

label nvl_start(show_bg=True):
    $ nvl_show(None)
    $ default_transition = dexp
    if show_bg:
        $ show_nvl_bg = True
    else:
        $ show_nvl_bg = False
    window show
    return

label nvl_end:
    window hide
    nvl clear
    $ nvl_hide(None)
    $ default_transition = None
    return


label splashscreen:
    $ renpy.music.set_volume(0.2, 0, channel="music")
    scene bg black
    pause 0.5
    voice "voice/malos/belgerum.ogg"
    show belgerum:
        xalign 0.5 yalign 0.5
    with dissolve
    $ renpy.pause(0.1, hard=True)
    pause 2
    hide belgerum
    with dissolve
    pause 0.8
    return



label before_main_menu:
    $ renpy.music.set_volume(0.2, 0, channel="music")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
