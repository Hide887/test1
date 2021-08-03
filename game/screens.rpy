init offset = -1





init python:
    renpy.start_predict("gui/*.*")
    renpy.start_predict("images/particles/*.*")






style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True


style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size

style bar:
    ysize gui.bar_size
    left_bar Frame("gui/defaults/bar/bar_full.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/defaults/bar/bar_empty.png", gui.bar_borders, tile=gui.bar_tile)
    hover_left_bar Frame("gui/defaults/bar/bar_full_hover.png", gui.bar_borders, tile=gui.bar_tile)
    hover_right_bar Frame("gui/defaults/bar/bar_empty_hover.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    left_bar Frame("gui/defaults/bar/vbar_full.png", gui.vbar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/defaults/bar/vbar_empty.png", gui.vbar_borders, tile=gui.bar_tile)
    hover_left_bar Frame("gui/defaults/bar/vbar_full_hover.png", gui.vbar_borders, tile=gui.bar_tile)
    hover_right_bar Frame("gui/defaults/bar/vbar_empty_hover.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/defaults/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/defaults/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/defaults/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/defaults/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/defaults/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/defaults/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/defaults/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/defaults/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/objects/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what, who_window_style="namebox"):
    style_prefix "say"

    window:
        id "window"

        text what id "what" color "#fff" line_spacing 10

        if who is not None:

            window:
                style "namebox"
                text who id "who" outlines [(3, "#000", 0, 1)]



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

        use quick_menu

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    ypos gui.name_ypos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ysize gui.namebox_height
    background Frame("gui/button/choice_idle_background.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding


style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")











screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xpos gui.text_xpos
            xanchor gui.text_xalign
            ypos gui.text_ypos

        text prompt style "input_prompt" color "#381E01"
        input id "input"

    use quick_menu


style input_prompt is default

style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

style input:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign













transform choice_button_move(t):
    alpha 0.0 zoom 0.95 xalign 0.5 yoffset 20
    t*0.25
    parallel:
        easein 0.3 alpha 1.0 yoffset 0
    parallel:
        on idle:
            ease 0.1 zoom 0.95
        on hover:
            ease 0.1 zoom 1.0
        on selected_idle:
            ease 0.1 zoom 1.0
        on selected_hover:
            ease 0.1 zoom 1.0
    on hide:
        easeout 0.3 zoom 0.8

transform choice_vbox_move:
    on hide:
        easeout 0.2 alpha 0.0 yoffset 20


screen choice(items):
    style_prefix "choice"
    vbox:
        at choice_vbox_move

        for t, (caption, action, chosen) in enumerate(items):
            if action:
                if " (disabled)" in caption:
                    textbutton caption.replace(" (disabled)", "") action None at choice_button_move(t) text_font gui.name_font
                else:
                    textbutton caption action [action, Hide("choice")] at choice_button_move(t) text_font gui.name_font
            else:
                textbutton caption action None at choice_button_move(t) text_font gui.name_font





define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing gui.choice_spacing

style choice_button is default:
    bottom_margin -5 bottom_padding 15
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    outlines [(2, "#000", 0, 0)]








screen quick_menu():
    zorder 100
    textbutton _("  Save  ") xpos 0.368 action [Hide("quick_tooltip"), ShowMenu('save')] hovered [ Show("quick_tooltip", my_tt_text=_("Save Game")) ] unhovered [Hide("quick_tooltip")] style "quick_textbutton" at QuickSettingButton
    textbutton _("  Load  ") xpos 0.457 action [Hide("quick_tooltip"), ShowMenu('load')] hovered [ Show("quick_tooltip", my_tt_text=_("Load Game")) ] unhovered [Hide("quick_tooltip")] style "quick_textbutton" at QuickSettingButton
    textbutton _("Settings") xpos 0.545 action [Hide("quick_tooltip"), ShowMenu('preferences')] hovered [ Show("quick_tooltip", my_tt_text=_("Adjust Settings")) ] unhovered [Hide("quick_tooltip")] style "quick_textbutton" at QuickSettingButton
    textbutton _("  Auto  ") xpos 0.635 action [Hide("quick_tooltip"), Preference("auto-forward", "toggle")] hovered [ Show("quick_tooltip", my_tt_text=_("Toggle Auto-forward")) ] unhovered [Hide("quick_tooltip")] style "quick_textbutton" at QuickSettingButton
    textbutton _("  Skip  ") xpos 0.720 action [Hide("quick_tooltip"), Skip()] hovered [ Show("quick_tooltip", my_tt_text=_("Toggle Skipping")) ] unhovered [Hide("quick_tooltip")] style "quick_textbutton" at QuickSettingButton
    textbutton _("  Hide  ") xpos 0.805 action [Hide("quick_tooltip"), HideInterface()] hovered [ Show("quick_tooltip", my_tt_text=_("Hide Textbox")) ] unhovered [Hide("quick_tooltip")] style "quick_textbutton" at QuickSettingButton

style quick_textbutton:
    yanchor 0.5 xanchor 0.5 selected_background Frame("gui/button/choice_hover_background.png", 20, 20) insensitive_background Frame("gui/button/choice_insensitive_background.png", 20, 20) ypos 0.97 background Frame("gui/button/choice_idle_background.png", 20, 20) xpadding 20 hover_background Frame("gui/button/choice_hover_background.png", 20, 20) bottom_padding 18
style quick_textbutton_text:
    color "#fff" yoffset 6 font gui.name_font outlines [(2, "#000", 0, 0)] size 32


transform QuickSettingButton:
    zoom 0.9
    on idle:
        ease 0.05 zoom 0.9
    on hover:
        ease 0.05 zoom 1.0
    on selected_idle:
        ease 0.05 zoom 1.0
    on selected_hover:
        ease 0.05 zoom 1.0

transform Quick_TT_MoveUp:
    ypos 0.912 xpos 0.83 xanchor 1.0 alpha 0
    linear 0.3 alpha 1.0
    pause 3.0
    linear 0.3 alpha 0

screen quick_tooltip(my_tt_text):
    text str(my_tt_text) color "#fff" size 20 at Quick_TT_MoveUp


style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")









screen main_menu():
    tag menu



    add im.Tile("gui/settings/bg.png", size=(2020, 1080)) at bg_loop_move
    add Fireflies().sm alpha 1 xalign 0.5 yalign 0.5
    add im.Tile("gui/main_menu/fire.png", size=(1920, 1080)) at fire_loop_move
    add Fog().sm alpha 0.8 zoom 0.5
    if renpy.seen_label("ending_3"):
        add "gui/main_menu/covergirl3.png" at mainmenu_char_move
        timer 0.0000000000001 action PlayCharacterVoice("Dianne", "voice/dianne/DKD2.ogg")
    elif renpy.seen_label("ending_1") or renpy.seen_label("ending_2"):
        add "gui/main_menu/covergirl2.png" at mainmenu_char_move
        timer 0.0000000000001 action PlayCharacterVoice("Dianne", "voice/dianne/DKD.ogg")
    else:
        add "gui/main_menu/covergirl.png" at mainmenu_char_move
        timer 0.0000000000001 action PlayCharacterVoice("Dianne", "voice/dianne/DKD.ogg")
    add "gui/main_menu/logo.png" at mainmenu_logo_move

    textbutton _("New Game") ypos 0.48 action [Play("sound", "sounds/depression.ogg"), Start()] style "main_menu_textbutton" text_style "main_menu_text" at mainmenu_button_move
    textbutton _("Load Game") ypos 0.58 action ShowMenu("load") style "main_menu_textbutton" text_style "main_menu_text" at mainmenu_button_move
    textbutton _("Settings") ypos 0.68 action ShowMenu("preferences") style "main_menu_textbutton" text_style "main_menu_text" at mainmenu_button_move
    textbutton _("Extras") ypos 0.78 action ShowMenu("cg_gallery") style "main_menu_textbutton" text_style "main_menu_text" at mainmenu_button_move
    textbutton _("Quit") ypos 0.88 action Quit(confirm=True) style "main_menu_textbutton" text_style "main_menu_text" at mainmenu_button_move

    if renpy.music.get_playing()!="music/main_menu.ogg":
        on "replace" action Play("music", "music/main_menu.ogg")


style main_menu_textbutton:
    hover_background Frame(im.Twocolor("gui/objects/fade_bg.png","#ff5","#ff5"), 1, 1) bottom_margin -60 background None xpadding 100
style main_menu_text:
    color "#fff" font gui.name_font outlines [ (2, "#000", 0, 0), (2, "#000", 0, 1) ] size 70

transform bg_loop_move:
    xoffset 0
    linear 2 xoffset -100
    repeat

transform fire_loop_move:
    alpha 0.4
    ease 2.3 alpha 0.6
    ease 2.3 alpha 0.4
    repeat

transform bg_loop_move2:
    xoffset 0 alpha 0
    parallel:
        linear 2 xoffset -100
        xoffset 0
        repeat
    parallel:
        pause 1.0
        linear 1 alpha 1

transform mainmenu_logo_move:
    yalign 0.1 xanchor 0.5 xpos 0.3 alpha 0 yoffset 20
    pause 0.5
    ease 0.5 alpha 1 yoffset 0

transform mainmenu_char_move:
    xoffset 50 alpha 0
    ease 1 alpha 1 xoffset 0

transform mainmenu_button_move:
    xanchor 0.0 xpos 0.05 yanchor 0.5 zoom 0.93
    yoffset 50 alpha 0.0
    pause 0.75
    ease 1 yoffset 0 alpha 1.0
    on idle:
        ease 0.15 zoom 0.93
    on hover:
        ease 0.15 zoom 1.0
    on selected_idle:
        ease 0.15 zoom 0.93
    on selected_hover:
        ease 0.15 zoom 0.93














define config.thumbnail_width = 150
define config.thumbnail_height = 84

screen load_save_slot(number, x, y):

    if FileSaveName(number):
        frame:
            xpos x+21 ypos y+25 background Frame("gui/save_load/alphamask.png", 20, 20)
            xsize 154 ysize 88 xpadding 0 ypadding 0
            add AlphaMask(FileScreenshot(number), "gui/save_load/alphamask.png") size (150,84) xpos 2 ypos 2
        text (FileTime(number, empty="")) xpos x+98 xanchor 0.5 text_align 0.5 ypos y+125 size 22 color "#fff" font gui.name_font outlines [ (1, "#000", 0, 0) ]

        textbutton _("Delete") xpos x+98 xanchor 0.5 text_align 0.5 ypos y+152 text_size 19 text_color "#fff" background Frame("gui/save_load/deletebg.png", 25, 0) hover_background Frame("gui/save_load/deletebg_hover.png", 25, 0) top_margin 6 bottom_margin 10 xpadding 18 action [Hide("menu_tooltip"), FileDelete(number)] hovered [ Show("menu_tooltip", my_tt_text=_("Delete the save in slot ")+str(number+1)) ] unhovered [Hide("menu_tooltip")] alt (_("Delete Save Slot ")+str(number+1)) text_font gui.default_font text_outlines [ (1, "#0009", 0, 0) ]
    else:
        text _("No Data") xpos x+98 xanchor 0.5 text_align 0.5 ypos y+130 size 32 color "#fff" font gui.name_font outlines [ (1, "#000b", 0, 0) ]



screen menu_nav():

    if main_menu:
        textbutton _("Return") ypos 0.31 alt _("Return") action [Hide("menu_tooltip"), Return()] hovered [ Show("menu_tooltip", my_tt_text=_("Return to main menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
        textbutton _("Load") ypos 0.4 alt _("Load") action [Hide("menu_tooltip"), ShowMenu("load")] hovered [ Show("menu_tooltip", my_tt_text=_("Continue a saved game")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
        textbutton _("Settings") ypos 0.49 alt _("Settings") action [Hide("menu_tooltip"), ShowMenu("preferences")] hovered [ Show("menu_tooltip", my_tt_text=_("Open settings menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
        textbutton _("Display") ypos 0.55 alt _("Display Settings") action [Hide("menu_tooltip"), ShowMenu("preferences"), Function(settings_menu_page_display), SelectedIf(persistent.display_select and persistent.settings_open)] hovered [ Show("menu_tooltip", my_tt_text=_("Open display settings menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_subtextbutton" text_style "menu_nav_subtext" at menu_nav_move2
        textbutton _("Audio") ypos 0.6 alt _("Audio Settings") action [Hide("menu_tooltip"), ShowMenu("preferences"), Function(settings_menu_page_audio), SelectedIf(persistent.audio_select and persistent.settings_open)] hovered [ Show("menu_tooltip", my_tt_text=_("Open audio settings menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_subtextbutton" text_style "menu_nav_subtext" at menu_nav_move2
        textbutton _("Gameplay") ypos 0.65 alt _("Gameplay Settings") action [Hide("menu_tooltip"), ShowMenu("preferences"), Function(settings_menu_page_gameplay), SelectedIf(persistent.gameplay_select and persistent.settings_open)] hovered [ Show("menu_tooltip", my_tt_text=_("Open gameplay settings menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_subtextbutton" text_style "menu_nav_subtext" at menu_nav_move2
        textbutton _("Quit Game") ypos 0.74 alt _("Quit Game") action [Hide("menu_tooltip"), Quit(confirm=True)] hovered [ Show("menu_tooltip", my_tt_text=_("Quit the game")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
    else:
        textbutton _("Return") ypos 0.22 alt _("Return") action [Hide("menu_tooltip"), Return()] hovered [ Show("menu_tooltip", my_tt_text=_("Resume gameplay")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
        textbutton _("Save") ypos 0.31 alt _("Save") action [Hide("menu_tooltip"), ShowMenu("save")] hovered [ Show("menu_tooltip", my_tt_text=_("Record your progress")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
        textbutton _("Load") ypos 0.4 alt _("Load") action [Hide("menu_tooltip"), ShowMenu("load")] hovered [ Show("menu_tooltip", my_tt_text=_("Continue a saved game")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
        textbutton _("Settings") ypos 0.49 alt _("Settings") action [Hide("menu_tooltip"), ShowMenu("preferences")] hovered [ Show("menu_tooltip", my_tt_text=_("Open settings menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
        textbutton _("Display") ypos 0.55 alt _("Display Settings") action [Hide("menu_tooltip"), ShowMenu("preferences"), Function(settings_menu_page_display), SelectedIf(persistent.display_select and persistent.settings_open)] hovered [ Show("menu_tooltip", my_tt_text=_("Open display settings menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_subtextbutton" text_style "menu_nav_subtext" at menu_nav_move2
        textbutton _("Audio") ypos 0.6 alt _("Audio Settings") action [Hide("menu_tooltip"), ShowMenu("preferences"), Function(settings_menu_page_audio), SelectedIf(persistent.audio_select and persistent.settings_open)] hovered [ Show("menu_tooltip", my_tt_text=_("Open audio settings menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_subtextbutton" text_style "menu_nav_subtext" at menu_nav_move2
        textbutton _("Gameplay") ypos 0.65 alt _("Gameplay Settings") action [Hide("menu_tooltip"), ShowMenu("preferences"), Function(settings_menu_page_gameplay), SelectedIf(persistent.gameplay_select and persistent.settings_open)] hovered [ Show("menu_tooltip", my_tt_text=_("Open gameplay settings menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_subtextbutton" text_style "menu_nav_subtext" at menu_nav_move2
        textbutton _("Main Menu") ypos 0.74 alt _("Main Menu") action [Hide("menu_tooltip"), MainMenu()] hovered [ Show("menu_tooltip", my_tt_text=_("Return to the main menu")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move
        textbutton _("Quit Game") ypos 0.83 alt _("Quit Game") action [Hide("menu_tooltip"), Quit(confirm=True)] hovered [ Show("menu_tooltip", my_tt_text=_("Quit the game")) ] unhovered [Hide("menu_tooltip")] style "menu_nav_textbutton" text_style "menu_nav_text" at menu_nav_move


style menu_nav_textbutton:
    yanchor 0.5 xpos 0.18 xanchor 1.0
    background None hover_background Frame("gui/objects/fade_bg.png", 1, 1)
style menu_nav_text:
    color "#fff" text_align 1.0 hover_color "#ffa" selected_color "#ff4" font gui.name_font outlines [ (2, "#000b", 0, 0) ] size 54

style menu_nav_subtextbutton:
    yanchor 0.5 xpos 0.18 xanchor 1.0
style menu_nav_subtext:
    color "#fff" text_align 1.0 hover_color "#fff" selected_color "#ffa" font gui.name_font size 36


transform menu_nav_move:
    zoom 0.88 yanchor 0.5
    on idle:
        ease 0.15 zoom 0.88
    on hover:
        ease 0.15 zoom 1.0
    on selected_idle:
        ease 0.1 zoom 1.0
    on selected_hover:
        ease 0.1 zoom 1.0


transform menu_nav_move2:
    zoom 0.9 xpos 0.18 yanchor 0.5
    on idle:
        alpha 0.4
        ease 0.15 zoom 0.9
    on hover:
        alpha 0.6
        ease 0.15 zoom 1.0
    on selected_idle:
        alpha 0.6
        ease 0.1 zoom 1.0
    on selected_hover:
        alpha 0.6
        ease 0.1 zoom 1.0


screen menu_tooltip(my_tt_text):
    text my_tt_text size 36 at Menu_TT_MoveUp

transform Menu_TT_MoveUp:
    ypos 0.875 xpos 0.38 xanchor 0.0 alpha 0
    on show:
        alpha 0
        linear 0.2 alpha 1.0
    on hide:
        linear 0.2 alpha 0


screen save_pages():
    use save_page(1)
    use save_page(2)
    use save_page(3)
    use save_page(4)
    use save_page(5)
    use save_page(6)
    use save_page(7)
    use save_page(8)
    use save_page(9)

screen save_page(page_number):
    textbutton _("Page "+str(page_number)) text_font gui.name_font text_size 30 text_outlines [ (2, "#000c", 0, 0) ] at SaveLoad_Pages_move ypos 0.78 xpos (0.305+page_number*0.06) action [Hide("menu_tooltip"), FilePage(page_number), With(Dissolve(0.15))] hovered [ Show("menu_tooltip", my_tt_text=_("Open Page "+str(page_number))) ] unhovered [Hide("menu_tooltip")] background None hover_background Frame("gui/objects/fade_bg.png", 1, 1) text_color "#fff" text_hover_color "#ffa" text_selected_color "#ff4"


transform SaveLoad_Pages_move:
    zoom 0.8 xanchor 0.5
    on idle:
        ease 0.15 zoom 0.8 yoffset 0
    on hover:
        ease 0.15 zoom 1.0 yoffset -5
    on selected_idle:
        zoom 1.0
        ease 0.1 yoffset -7
    on selected_hover:
        ease 0.1 zoom 1.0 yoffset -7
    on hide:
        ease 0.15 zoom 0.8 yoffset 0

transform return_button_move:
    zoom 0.9 xanchor 0.5 xpos 0.93 yanchor 0.5 ypos 0.08
    on idle:
        ease 0.15 zoom 0.9
    on hover:
        ease 0.15 zoom 1.0
    on hide:
        ease 0.15 zoom 0.9



screen save():
    $ persistent.settings_open = False
    tag menu
    use menu_background(_("Save Game"))
    use menu_nav
    use save_pages
    for i in range(0, 10):
        if i<=4:
            $ y=310
        else:
            $ y=570
        if (i==0) or (i==5):
            $ x=625
        elif (i==1) or (i==6):
            $ x=845
        elif (i==2) or (i==7):
            $ x=1065
        elif (i==3) or (i==8):
            $ x=1285
        else:
            $ x=1505
        imagebutton auto "gui/save_load/load_slot_%s.png" xpos x ypos y focus_mask True action [Hide("menu_tooltip"), FileAction(i), With(Dissolve(0.15))] hovered [ Show("menu_tooltip", my_tt_text=_("Save slot ")+str(i+1)) ] unhovered [Hide("menu_tooltip")] alt (_("Save Slot ")+str(i+1))
        use load_save_slot(number=i, x=x, y=y)

screen load():
    $ persistent.settings_open = False
    tag menu
    use menu_background(_("Load Game"))
    use menu_nav
    use save_pages
    for i in range(0, 10):
        if i<=4:
            $ y=310
        else:
            $ y=570
        if (i==0) or (i==5):
            $ x=625
        elif (i==1) or (i==6):
            $ x=845
        elif (i==2) or (i==7):
            $ x=1065
        elif (i==3) or (i==8):
            $ x=1285
        else:
            $ x=1505
        imagebutton auto "gui/save_load/load_slot_%s.png" xpos x ypos y focus_mask True action [Hide("menu_tooltip"), FileAction(i)] hovered [ Show("menu_tooltip", my_tt_text=_("Save slot ")+str(i+1)) ] unhovered [Hide("menu_tooltip")] alt (_("Save Slot ")+str(i+1))
        use load_save_slot(number=i, x=x, y=y)









style boolean_button:
    bottom_margin -15 selected_background Frame("gui/button/choice_hover_background.png", 50, 1) ypadding 50 background Frame("gui/button/choice_idle_background.png", 50, 1) xpadding 30 hover_background Frame("gui/button/choice_hover_background.png", 50, 1)

style boolean_button_text:
    size 30 font gui.name_font text_align 0.5 outlines [ (2, "#000a", 0, 0) ]

screen menu_background(caption):
    add im.Tile("gui/settings/bg.png", size=(2020, 1080)) at bg_loop_move
    add "gui/settings/frames.png"
    text caption font gui.name_font size 100 outlines [ (3, "#0007", -2, 6), (3, "#880", 0, 1) ] yalign 0.1 xpos 0.605 xanchor 0.5

screen preferences():
    $ persistent.settings_open = True
    tag menu
    use menu_background("")

    use menu_nav
    if persistent.settings_page == "display":
        text _("Display Settings") font gui.name_font size 100 outlines [ (3, "#0007", -2, 6), (3, "#880", 0, 1) ] yalign 0.1 xpos 0.605 xanchor 0.5
        text _("Display Mode") font gui.name_font size 50 text_align 0.5 xanchor 0.5 xpos 0.605 ypos 0.32 color "#fff" outlines [(2, "#000", 0, 0)]
        hbox:
            xanchor 0.5 xpos 0.605
            yanchor 0.5 ypos 0.44
            spacing 40
            textbutton _("Fullscreen Mode") action [Hide("menu_tooltip"), Preference('display', 'fullscreen'), SelectedIf(_preferences.fullscreen)] hovered [ Show("menu_tooltip", my_tt_text=_("Set game to fullscreen mode")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move
            textbutton _("Windowed Mode") action [Hide("menu_tooltip"), Preference('display', 'any window'), SelectedIf(not _preferences.fullscreen)] hovered [ Show("menu_tooltip", my_tt_text=_("Set game to windowed mode")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move
        text _("Window Size") font gui.name_font size 50 text_align 0.5 xanchor 0.5 xpos 0.605 ypos 0.58 color "#fff" outlines [(2, "#000", 0, 0)]
        hbox:
            xanchor 0.5 xpos 0.39 yanchor 0.5 ypos 0.7
            textbutton _("1920 x 1080") alt _("1920 by 1080 resolution") action [Hide("menu_tooltip"), Preference("display", 1.0)] hovered [ Show("menu_tooltip", my_tt_text=_("Set game window to 1920 x 1080 resolution")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move
        hbox:
            xanchor 0.5 xpos 0.53 yanchor 0.5 ypos 0.7
            textbutton _("1600 x 900") alt _("1600 by 900 resolution") action [Hide("menu_tooltip"), Preference("display", 0.83333333333)] hovered [ Show("menu_tooltip", my_tt_text=_("Set game window to 1600 x 900 resolution")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move
        hbox:
            xanchor 0.5 xpos 0.67 yanchor 0.5 ypos 0.7
            textbutton _("1280 x 720 ") alt _("1280 by 720 resolution") action [Hide("menu_tooltip"), Preference("display", 0.666666666667)] hovered [ Show("menu_tooltip", my_tt_text=_("Set game window to 1280 x 720 resolution")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move

        hbox:
            xanchor 0.5 xpos 0.81 yanchor 0.5 ypos 0.7
            textbutton _(" 960 x 540 ") alt _("960 by 540 resolution") action [Hide("menu_tooltip"), Preference("display", 0.5)] hovered [ Show("menu_tooltip", my_tt_text=_("Set game window to 960 x 540 resolution")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move

    if persistent.settings_page == "audio":
        text _("Audio Settings") font gui.name_font size 100 outlines [ (3, "#0007", -2, 6), (3, "#880", 0, 1) ] yalign 0.1 xpos 0.605 xanchor 0.5
        frame:
            style_group "pref"


            text _("Music") font gui.name_font size 50 text_align 0.5 xanchor 0.5 xpos 0.605 ypos 0.275 color "#fff" outlines [(2, "#000", 0, 0)]
            bar value Preference("music volume") xanchor 0.5 xpos 0.605 ypos 0.37 yanchor 0.5 hovered [ Show("menu_tooltip", my_tt_text=_("Set volume of music")) ] unhovered [Hide("menu_tooltip")] alt _("Music Volume") xsize 500 left_gutter 10 right_gutter 10 at setting_bar_move

            hbox:
                xanchor 0.5 xpos 0.605 ypos 0.4525 spacing 20
                text _("Sounds") font gui.name_font size 50 text_align 0.5 color "#fff" outlines [(2, "#000", 0, 0)]
                imagebutton auto "gui/settings/sound_test_%s.png" yalign 0.5 yoffset 5 action [Hide("menu_tooltip"), Play("sound", system_sound_preview.next())] hovered [ Show("menu_tooltip", my_tt_text=_("Preview sounds")) ] unhovered [Hide("menu_tooltip")] alt _("Preview sounds")
            bar value Preference("sound volume") xanchor 0.5 xpos 0.605 ypos 0.5475 yanchor 0.5 hovered [ Show("menu_tooltip", my_tt_text=_("Set volume of sounds")) ] unhovered [Hide("menu_tooltip")] alt _("Sound Volume") xsize 500 left_gutter 10 right_gutter 10 at setting_bar_move

            hbox:
                xanchor 0.5 xpos 0.455 ypos 0.63 spacing 20
                text _("Malos") font gui.name_font size 50 text_align 0.5 color "#fff" outlines [(2, "#000", 0, 0)]
                imagebutton auto "gui/settings/sound_test_%s.png" yalign 0.5 yoffset 5 action [Hide("menu_tooltip"), PlayCharacterVoice("Malos", malos_voice_preview.next())] hovered [ Show("menu_tooltip", my_tt_text=_("Preview Malos' voice")) ] unhovered [Hide("menu_tooltip")] alt _("Preview Malos' voice")
            bar value SetCharacterVolume("Malos") xanchor 0.5 xpos 0.455 ypos 0.725 yanchor 0.5 hovered [ Show("menu_tooltip", my_tt_text=_("Set volume of Malos' voice")) ] unhovered [Hide("menu_tooltip")] alt _("Malos Voice Volume") xsize 500 left_gutter 10 right_gutter 10 at setting_bar_move

            hbox:
                xanchor 0.5 xpos 0.755 ypos 0.63 spacing 20
                text _("Dianne") font gui.name_font size 50 text_align 0.5 color "#fff" outlines [(2, "#000", 0, 0)]
                imagebutton auto "gui/settings/sound_test_%s.png" yalign 0.5 yoffset 5 action [Hide("menu_tooltip"), PlayCharacterVoice("Dianne", dianne_voice_preview.next())] hovered [ Show("menu_tooltip", my_tt_text=_("Preview Dianne's voice")) ] unhovered [Hide("menu_tooltip")] alt _("Preview Dianne's voice")
            bar value SetCharacterVolume("Dianne") xanchor 0.5 xpos 0.755 ypos 0.725 yanchor 0.5 hovered [ Show("menu_tooltip", my_tt_text=_("Set volume of Dianne's voice")) ] unhovered [Hide("menu_tooltip")] alt _("Dianne Voice Volume") xsize 500 left_gutter 10 right_gutter 10 at setting_bar_move


    if persistent.settings_page == "gameplay":
        text _("Gameplay Settings") font gui.name_font size 100 outlines [ (3, "#0007", -2, 6), (3, "#880", 0, 1) ] yalign 0.1 xpos 0.605 xanchor 0.5
        hbox:
            xanchor 0.5 xpos 0.605
            yanchor 0.5 ypos 0.52
            spacing 20
            vbox:
                xalign 0.5 spacing 70 style_group "pref"
                vbox:
                    xalign 0.5 yalign 0.0 spacing 20
                    text _("        Text Speed        ") font gui.name_font size 50 text_align 0.5 xanchor 0.5 xpos 0.5 color "#fff" outlines [(2, "#000", 0, 0)]
                    hbox:
                        xalign 0.5 yalign 0.5
                        null height 44
                        bar value Preference("text speed") xalign 0.5 yalign 0.5 hovered [ Show("menu_tooltip", my_tt_text=_("Set text speed")) ] unhovered [Hide("menu_tooltip")] alt _("Text speed") xsize 450 left_gutter 10 right_gutter 10 at setting_bar_move
                vbox:
                    xalign 0.5 yalign 0.5 spacing 20
                    text _("          Skip          ") font gui.name_font size 50 text_align 0.5 xanchor 0.5 xpos 0.5 color "#fff" outlines [(2, "#000", 0, 0)]
                    hbox:
                        xalign 0.5 yalign 0.5 spacing 20
                        textbutton _("Seen Text") alt _("Skip only seen text") action [Hide("menu_tooltip"), Preference('skip', 'seen')] hovered [ Show("menu_tooltip", my_tt_text=_("Skip only seen text")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move
                        textbutton _("All Text") alt _("Skip all text") action [Hide("menu_tooltip"), Preference('skip', 'all')] hovered [ Show("menu_tooltip", my_tt_text=_("Skip all text")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move
                vbox:
                    xalign 0.5 yalign 0.5 spacing 20
                    text _("        Battle Text         ") font gui.name_font size 50 text_align 0.5 xanchor 0.5 xpos 0.5 color "#fff" outlines [(2, "#000", 0, 0)]
                    hbox:
                        xalign 0.5 yalign 0.5 spacing 20
                        textbutton _("Show") alt _("Show floating text during battle") action [Hide("menu_tooltip"), SetField(persistent, 'show_battletext', True)] hovered [ Show("menu_tooltip", my_tt_text=_("Show floating text during battle")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move
                        textbutton _("Hide") alt _("Hide floating text during battle") action [Hide("menu_tooltip"), SetField(persistent, 'show_battletext', False)] hovered [ Show("menu_tooltip", my_tt_text=_("Hide floating text during battle")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move

            vbox:
                xalign 0.5 spacing 70 style_group "pref"
                vbox:
                    xalign 0.5 yalign 0.0 spacing 20
                    text _("           Auto Speed           ") font gui.name_font size 50 text_align 0.5 xanchor 0.5 xpos 0.5 color "#fff" outlines [(2, "#000", 0, 0)]
                    hbox:
                        xalign 0.5 yalign 0.5
                        null height 44
                        bar value Preference("auto-forward time") xalign 0.5 yalign 0.5 hovered [ Show("menu_tooltip", my_tt_text=_("Set auto-forward speed")) ] unhovered [Hide("menu_tooltip")] bar_invert True alt _("Auto-forward Speed") xsize 450 left_gutter 10 right_gutter 10 at setting_bar_move
                vbox:
                    xalign 0.5 yalign 0.5 spacing 20
                    text _("        After Choices        ") font gui.name_font size 50 text_align 0.5 xanchor 0.5 xpos 0.5 color "#fff" outlines [(2, "#000", 0, 0)]
                    hbox:
                        xalign 0.5 yalign 0.5 spacing 20
                        textbutton _("Stop Skipping") alt _("Stop SKipping after choices") action [Hide("menu_tooltip"), Preference('after choices', 'stop')] hovered [ Show("menu_tooltip", my_tt_text=_("Stop skipping after choices")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move
                        textbutton _("Keep Skipping") alt _("Keep Skipping after choices") action [Hide("menu_tooltip"), Preference('after choices', 'skip')] hovered [ Show("menu_tooltip", my_tt_text=_("Keep skipping after choices")) ] unhovered [Hide("menu_tooltip")] style "boolean_button" text_style "boolean_button_text" at boolean_buttons_move


transform boolean_buttons_move:
    zoom 0.85 xalign 0.5 yalign 0.5
    on idle:
        ease 0.15 zoom 0.85
    on hover:
        ease 0.15 zoom 0.98
    on selected_idle:
        zoom 1.0
    on selected_hover:
        zoom 1.0
    on hide:
        ease 0.15 zoom 0.85

transform setting_bar_move:
    zoom 0.94
    on idle:
        ease 0.15 zoom 0.94
    on hover:
        ease 0.15 zoom 1.0
    on selected_idle:
        zoom 1.0
    on selected_hover:
        zoom 1.0
    on hide:
        ease 0.15 zoom 0.94

init 1 python:
    def settings_menu_page_display():
        persistent.settings_page = "display"
        persistent.display_select = True
        persistent.audio_select = False
        persistent.gameplay_select = False
    def settings_menu_page_audio():
        persistent.settings_page = "audio"
        persistent.display_select = False
        persistent.audio_select = True
        persistent.gameplay_select = False
    def settings_menu_page_gameplay():
        persistent.settings_page = "gameplay"
        persistent.display_select = False
        persistent.audio_select = False
        persistent.gameplay_select = True
    if not persistent.settings_page:
        persistent.settings_page = "display"

    import itertools
    system_sound_preview = itertools.cycle(["sounds/hit.ogg", "sounds/punch.ogg", "sounds/charge.ogg", "sounds/heal.ogg"])
    malos_voice_preview = itertools.cycle(["voice/malos/story/line_080.ogg", "voice/malos/story/line_123.ogg", "voice/malos/story/line_167.ogg"])
    dianne_voice_preview = itertools.cycle(["voice/dianne/story/line_056.ogg", "voice/dianne/battle/counter2.ogg", "voice/dianne/story/line_105.ogg"])

    style.pref_frame.background = None
    style.pref_slider.ysize = gui.bar_size
    style.pref_slider.left_bar = Frame("gui/defaults/bar/bar_full.png", gui.bar_borders, tile=gui.bar_tile)
    style.pref_slider.right_bar = Frame("gui/defaults/bar/bar_empty.png", gui.bar_borders, tile=gui.bar_tile)
    style.pref_slider.hover_left_bar = Frame("gui/defaults/bar/bar_full_hover.png", gui.bar_borders, tile=gui.bar_tile)
    style.pref_slider.hover_right_bar = Frame("gui/defaults/bar/bar_empty_hover.png", gui.bar_borders, tile=gui.bar_tile)
    style.pref_slider.xmaximum = 345
    style.pref_slider.thumb = None















screen confirm(message, yes_action, no_action):


    modal True
    zorder 200
    add "#000" alpha 0.5

    frame:
        at Confirm_screen_trans
        background Frame("gui/objects/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
        xanchor 0.5 xpos 0.5 yalign 0.55 ypadding 30 xsize 1039 ysize 414

        if message == layout.ARE_YOU_SURE:
            label _("Are you sure?") style "confirm_prompt"
        elif message == layout.QUIT:
            label _("Are you sure you want to quit?") style "confirm_prompt"
        elif message == layout.DELETE_SAVE:
            label _("Are you sure you want to delete this save?") style "confirm_prompt"
        elif message == layout.OVERWRITE_SAVE:
            label _("Are you sure you want to overwrite your save?") style "confirm_prompt"
        elif message == layout.LOADING:
            label _("Are you sure you want to load? Unsaved progress will be lost.") style "confirm_prompt"
        elif message == layout.MAIN_MENU:
            label _("Are you sure you want to return to the main menu? Unsaved progress will be lost.") style "confirm_prompt"
        else:
            label _(message) style "confirm_prompt"

        textbutton _("Yes") xoffset -150 xanchor 0.5 yoffset 100 yanchor 0.5 action [yes_action, SelectedIf(False)] text_font gui.name_font text_size 60 at Confirm_YN_move text_align 0.5 background Frame("gui/button/choice_idle_background.png", 50, 1) hover_background Frame("gui/button/choice_hover_background.png", 50, 1) selected_background Frame("gui/button/choice_hover_background.png", 50, 1) ypadding 120 bottom_margin -40 xpadding 60 text_outlines [ (2, "#000a", 0, 0) ]
        textbutton _("No") xoffset 150 xanchor 0.5 yoffset 100 yanchor 0.5 action [no_action, SelectedIf(False)] text_font gui.name_font text_size 60 at Confirm_YN_move text_align 0.5 background Frame("gui/button/choice_idle_background.png", 50, 1) hover_background Frame("gui/button/choice_hover_background.png", 50, 1) selected_background Frame("gui/button/choice_hover_background.png", 50, 1) ypadding 120 bottom_margin -40 xpadding 60 text_outlines [ (2, "#000a", 0, 0) ]

        key "game_menu" action no_action

style confirm_prompt:
    xalign 0.5 xpadding 50 ypos 0.35 yanchor 0.55

style confirm_prompt_text:
    line_spacing 10 text_align 0.5 font gui.default_font size 46
    color "#fff"
    layout "subtitle"

transform Confirm_YN_move:
    zoom 0.85 xalign 0.5 yalign 0.5
    on idle:
        ease 0.15 zoom 0.85
    on hover:
        ease 0.15 zoom 1.0
    on selected_idle:
        zoom 1.0
    on selected_hover:
        zoom 1.0
    on hide:
        ease 0.15 zoom 0.85

transform Confirm_screen_trans:
    alpha 0.0
    easein 0.2 alpha 1.0
    on hide:
        easeout 0.15 alpha 0.0


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")









screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    xalign 1.0
    background Frame("gui/objects/frame.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size
    outlines [(2, "#000", 0, 0)]

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):
    zorder 500
    style_prefix "notify"
    frame at notify_appear:
        text message
    timer 3.25 action Hide('notify')

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    xalign 1.0
    background Frame("gui/objects/frame.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size
    font gui.default_font
    outlines [(2, "#000", 0, 0)]








init:
    $ show_nvl_bg = True

screen nvl(dialogue, items=None):
    if show_nvl_bg:
        add "#000" alpha 0.75
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


    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

transform NVL_buttons_move:
    zoom 0.82 yalign 1.0
    on idle:
        ease 0.15 zoom 0.82
    on hover:
        ease 0.15 zoom 1.0
    on selected_idle:
        zoom 1.0
    on selected_hover:
        zoom 1.0
    on hide:
        ease 0.15 zoom 0.82


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who xalign 0.5 text_align 0.5 id d.who_id

            text d.what xalign 0.5 text_align 0.5 id d.what_id line_spacing 10




define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")
    outlines [(2, "#000c", 0, 0)]

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")
    outlines [(2, "#000c", 0, 0)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
