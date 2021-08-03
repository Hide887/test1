screen extras_nav() style_prefix :

    textbutton _("CG Gallery") ypos 0.305 action [Hide("menu_tooltip"), ShowMenu("cg_gallery")] hovered [ Show("menu_tooltip", my_tt_text=_("Open CG Gallery")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
    textbutton _("Scene Replay") ypos 0.395 action [Hide("menu_tooltip"), ShowMenu("scene_gallery")] hovered [ Show("menu_tooltip", my_tt_text=_("Open Scene Replay Gallery")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
    textbutton _("Music Room") ypos 0.485 action [Hide("menu_tooltip"), ShowMenu("music_room")] hovered [ Show("menu_tooltip", my_tt_text=_("Open Music Room")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
    textbutton _("Credits") ypos 0.575 action [Hide("menu_tooltip"), ShowMenu("credits")] hovered [ Show("menu_tooltip", my_tt_text=_("View Credits")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
    textbutton _("Main Menu") ypos 0.665 action [Hide("menu_tooltip"), Return()] hovered [ Show("menu_tooltip", my_tt_text=_("Return to Main Menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move



screen cg_gallery():
    tag menu
    use menu_background(_("CG Gallery"))
    use extras_nav

    use cg_gallery_slot("ritual", "Ending 1", "ending_1", -1, 0)
    use cg_gallery_slot("dungeon", "Ending 2", "ending_2", 1, 0)
    use cg_gallery_slot("brainwashed", "Ending 3", "ending_3", 0, 1)

screen cg_gallery_slot(cg_name, formal_cg_name, cg_label, x_number, y_number):
    frame:
        background None xsize 416 ysize 248 xanchor 0.5 yanchor 0.5 xpos (0.605+((x_number)*0.12)) ypos (0.40+((y_number)*0.25))
        if renpy.seen_label(cg_label):
            imagebutton idle "gui/extras/thumbs/slot_idle.png" hover "gui/extras/thumbs/slot_hover.png" action [Hide("menu_tooltip"), Show(("cg_gallery_"+cg_name), transition=Dissolve(0.3))] hovered [ Show("menu_tooltip", my_tt_text=("Show "+formal_cg_name+" CG")) ] unhovered [Hide("menu_tooltip")] alt (formal_cg_name+" CG") foreground AlphaMask("gui/extras/thumbs/"+cg_name+".png", "gui/extras/thumbs/alphamask.png") at cg_slot_move
        else:
            imagebutton idle "gui/extras/thumbs/slot_idle.png" action None at cg_slot_move


transform cg_slot_move:
    zoom 0.95 xalign 0.5 yalign 0.5
    on idle:
        ease 0.1 zoom 0.95
    on hover:
        ease 0.1 zoom 1.0


screen cg_gallery_controls(current_screen, next_screen="cg_gallery"):
    key "dismiss" action [Hide(current_screen), Show(next_screen, transition=Dissolve(0.3))]
    key "game_menu" action [Hide(current_screen), Show("cg_gallery", transition=Dissolve(0.3))]
    key "hide_windows" action [Hide(current_screen), Show("cg_gallery", transition=Dissolve(0.3))]


screen cg_gallery_ritual():
    tag menu
    add "bg ritual":
        zoom 0.5
    add "cg ritual grindavertfrownblush":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_ritual", "cg_gallery_ritual2")
screen cg_gallery_ritual2():
    tag menu
    add "bg ritual":
        zoom 0.5
    add "cg ritual grindangrygrit":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_ritual2", "cg_gallery_ritual3")
screen cg_gallery_ritual3():
    tag menu
    add "bg ritual":
        zoom 0.5
    add "cg ritual midweakopenblush":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_ritual3", "cg_gallery_ritual4")
screen cg_gallery_ritual4():
    tag menu
    add "bg ritual":
        zoom 0.5
    add "cg ritual deepshockedopenblush":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_ritual4", "cg_gallery_ritual5")
screen cg_gallery_ritual5():
    tag menu
    add "bg ritual":
        zoom 0.5
    add "cg ritual deepshockedfrown_crest":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_ritual5", "cg_gallery_ritual6")
screen cg_gallery_ritual6():
    tag menu
    add "bg ritual":
        zoom 0.5
    add "cg ritual deeprollopenblush_crest":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_ritual6", "cg_gallery_ritual7")
screen cg_gallery_ritual7():
    tag menu
    add "bg ritual":
        zoom 0.5
    add "cg ritual deepwidetongueblush_cum":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_ritual7", "cg_gallery_ritual8")
screen cg_gallery_ritual8():
    tag menu
    add "bg ritual":
        zoom 0.5
    add "cg ritual deeprollgritblush_cum":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_ritual8")


screen cg_gallery_dungeon():
    tag menu
    add "cg dungeon closedgape":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_dungeon", "cg_gallery_dungeon2")
screen cg_gallery_dungeon2():
    tag menu
    add "cg dungeon angryyell":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_dungeon2", "cg_gallery_dungeon3")
screen cg_gallery_dungeon3():
    tag menu
    add "cg dungeon shockedblushopen grind":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_dungeon3", "cg_gallery_dungeon4")
screen cg_gallery_dungeon4():
    tag menu
    add "cg dungeon avertblushwavy grindwet":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_dungeon4", "cg_gallery_dungeon5")
screen cg_gallery_dungeon5():
    tag menu
    add "cg dungeon rollblushyell deep":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_dungeon5", "cg_gallery_dungeon6")
screen cg_gallery_dungeon6():
    tag menu
    add "cg dungeon calmblushgape inside":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_dungeon6", "cg_gallery_dungeon7")
screen cg_gallery_dungeon7():
    tag menu
    add "cg dungeon winceblushgrit deep":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_dungeon7", "cg_gallery_dungeon8")
screen cg_gallery_dungeon8():
    tag menu
    add "cg dungeon dazedblushtongue deepcum":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_dungeon8", "cg_gallery_dungeon9")
screen cg_gallery_dungeon9():
    tag menu
    add "cg dungeon rollblushtonguedrool insidecum":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_dungeon9")





screen cg_gallery_brainwashed():
    tag menu
    add "cg brainwashed squintopenmasturbate":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_brainwashed", "cg_gallery_brainwashed2")
screen cg_gallery_brainwashed2():
    tag menu
    add "cg brainwashed puppybitemasturbate":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_brainwashed2", "cg_gallery_brainwashed3")
screen cg_gallery_brainwashed3():
    tag menu
    add "cg brainwashed staretonguespread":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_brainwashed3", "cg_gallery_brainwashed4")
screen cg_gallery_brainwashed4():
    tag menu
    add "cg brainwashed squintlickgrind":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_brainwashed4", "cg_gallery_brainwashed5")
screen cg_gallery_brainwashed5():
    tag menu
    add "cg brainwashed closedwideinside":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_brainwashed5", "cg_gallery_brainwashed6")
screen cg_gallery_brainwashed6():
    tag menu
    add "cg brainwashed staretongueinside":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_brainwashed6", "cg_gallery_brainwashed7")
screen cg_gallery_brainwashed7():
    tag menu
    add "cg brainwashed rollahegaocum":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_brainwashed7", "cg_gallery_brainwashed8")
screen cg_gallery_brainwashed8():
    tag menu
    add "cg brainwashed puppylickcum":
        zoom 0.5
    use cg_gallery_controls("cg_gallery_brainwashed8")







screen scene_gallery():
    tag menu
    use menu_background(_("Scene Replay"))
    use extras_nav

    use scene_gallery_slot("ritual", "Ending 1", "ending_1", -1, 0)
    use scene_gallery_slot("dungeon", "Ending 2", "ending_2", 1, 0)
    use scene_gallery_slot("brainwashed", "Ending 3", "ending_3", 0, 1)

screen scene_gallery_slot(cg_name, formal_cg_name, cg_label, x_number, y_number):
    frame:
        background None xsize 416 ysize 248 xanchor 0.5 yanchor 0.5 xpos (0.605+((x_number)*0.12)) ypos (0.40+((y_number)*0.25))

        if renpy.seen_label(cg_label):
            imagebutton idle "gui/extras/thumbs/slot_idle.png" hover "gui/extras/thumbs/slot_hover.png" action [Hide("menu_tooltip"), Replay(cg_label)] hovered [ Show("menu_tooltip", my_tt_text=("Replay "+formal_cg_name)) ] unhovered [Hide("menu_tooltip")] alt (formal_cg_name+" CG") foreground AlphaMask("gui/extras/thumbs/"+cg_name+".png", "gui/extras/thumbs/alphamask.png") at cg_slot_move
        else:
            imagebutton idle "gui/extras/thumbs/slot_idle.png" action None at cg_slot_move







init python:
    mr = MusicRoom(single_track=True)
    mr.add("music/main_menu.ogg", always_unlocked=True)
    mr.add("music/heroine.ogg", always_unlocked=False)
    mr.add("music/battle.ogg", always_unlocked=False)
    mr.add("music/ritual.ogg", always_unlocked=False)
    mr.add("music/dungeon.ogg", always_unlocked=False)
    mr.add("music/brainwashed.ogg", always_unlocked=False)
    track_hover = None

screen music_room():
    tag menu
    use menu_background(_("Music Room"))
    use extras_nav

    frame:
        xanchor 0.5 xpos 0.605 yalign 0.55
        background None
        has hbox:
            spacing 50
        vbox:
            spacing 20
            use music_room_button("The Demon King", "music/main_menu.ogg")
            use music_room_button("The Heroine", "music/heroine.ogg")
            use music_room_button("Clash of Champions", "music/battle.ogg")
            use music_room_button("Ritual of Enslavement", "music/ritual.ogg")
            use music_room_button("Dark Dungeon", "music/dungeon.ogg")
            use music_room_button("Puppet Princess", "music/brainwashed.ogg")



screen music_room_button(formal_title, track_filename):
    if renpy.seen_audio(track_filename):
        textbutton formal_title action [Hide("menu_tooltip"), mr.Play(track_filename)] hovered [ Show("menu_tooltip", my_tt_text="Play track \""+formal_title+"\"") ] unhovered [Hide("menu_tooltip")] xalign 0.0 yalign 0.5 ymargin -5 xpadding 30 left_padding 75 text_style "music_room_text" background "gui/extras/play_idle.png" hover_background "gui/extras/play_hover.png" selected_background "gui/extras/play_hover.png"
    else:
        textbutton "? ? ? ? ? ? ?" action None xalign 0.0 yalign 0.5 ymargin -5 xpadding 30 left_padding 75 text_style "music_room_text" background "gui/extras/play_insensitive.png"


style music_room_text:
    text_align 0.5 ypos -5 font gui.name_font size 42
    color "#fff"
    hover_color "#ff4"
    selected_color "#ff0"
    selected_hover_color "#ff0"
    insensitive_color "#aaa"
    outlines [ (1, "#000", 0, 0) ]



screen credits():
    tag menu
    use menu_background(_("Credits"))
    use extras_nav

    vbox:
        xanchor 0.5 xpos 0.605 yalign 0.55 spacing 10 style_prefix "credits"

        text "{u}{b}Writer, Programmer, Musician, Sound Artist, Voice of Malos{/b}{/u}"
        use credits_link("Belgerum", "https://www.youtube.com/user/belgerum")
        null height 32
        text "{u}{b}Artist{/b}{/u}"
        use credits_link("Kronifer", "http://fkineror.tumblr.com/")
        null height 32
        text "{u}{b}Voice of Dianne{/b}{/u}"
        use credits_link("Trina", "https://www.youtube.com/channel/UCvUCST8Of2QzqMJ71fhYNig/")
        null height 32
        text "{u}{b}Special Thanks{/b}{/u}"
        use credits_link("Renpytom", "https://www.renpy.org/")

style credits_text:
    xalign 0.5 color "#fff" text_align 0.5 font gui.default_font outlines [ (1, "#000", 0, 0) ] size 38

screen credits_link(credit_name, credit_link):
    textbutton credit_name action [Hide("menu_tooltip"), OpenURL(credit_link)] hovered [ Show("menu_tooltip", my_tt_text="Visit "+credit_name+"'s Website") ] text_font gui.name_font unhovered [Hide("menu_tooltip")] xalign 0.5 text_align 0.5 text_size 42 background None hover_background Frame(im.Twocolor("gui/objects/fade_bg.png", "#000", "#000"), 1, 1) text_color "#ff0" text_outlines [ (1, "#000", 0, 0) ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
