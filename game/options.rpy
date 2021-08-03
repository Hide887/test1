













define config.name = _("Demon King Domination")

define config.screen_width = 1920
define config.screen_height = 1080
define config.has_quicksave = False
define config.has_autosave = False
define config.autosave_frequency = None
define config.autosave_slots = 1
define config.image_cache_size = 32
define config.predict_statements = 20


define config.developer = True


define config.version = ""



define gui.about = _("")




define build.name = "Demon_King_Domination"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True


define config.default_music_volume = 1.0
define config.default_sfx_volume = 1.0
define config.default_voice_volume = 1.0





define config.main_menu_music = "music/main_menu.ogg"









define config.enter_transition = Dissolve (0.3)
define config.exit_transition = Dissolve (0.3)
define config.intra_transition = Dissolve(0.3)


define config.main_game_transition = Dissolve(0.3)


define config.window_show_transition = Dissolve (0.3)
define config.window_hide_transition = Dissolve (0.3)


define config.after_load_transition = Dissolve (0.8)


define config.end_game_transition = Dissolve (0.8)
define config.end_splash_transition = Dissolve(0.8)
define config.game_main_transition = Dissolve(0.8)


define config.after_load_transition = Dissolve(0.3)


define config.enter_replay_transition = Dissolve(0.8)
define config.exit_replay_transition = Dissolve(0.8)


define config.enter_yesno_transition = Dissolve(0.3)
define config.exit_yesno_transition = Dissolve(0.3)












define config.window = "auto"
define config.default_fullscreen = False







default preferences.text_cps = 150





default preferences.afm_time = 7
















define config.save_directory = "Demon_King_Domination_Save_Game"







define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('game/cache/**.**', None)
    build.classify('game/images/bg/unused/**.**', None)
    build.classify('game/music/unused/**.**', None)
    build.classify('game/sounds/unused/**.**', None)
    build.classify('game/**.ini', None)
    build.classify('game/**.rpy', None)




    build.archive("scripts", "all")
    build.archive("gui", "all")
    build.archive("bg", "all")
    build.archive("cg", "all")
    build.archive("particles", "all")
    build.archive("sprites", "all")
    build.archive("images", "all")
    build.archive("movies", "all")
    build.archive("music", "all")
    build.archive("VA", "all")
    build.archive("sounds", "all")
    build.archive("H-patch", "all")

    build.classify('game/H-patch/**.**', 'H-patch')

    build.classify('game/**.rpyc', 'scripts')
    build.classify('game/**.rpyb', 'scripts')
    build.classify('game/**.ttf', 'scripts')
    build.classify('game/**.txt', 'scripts')

    build.classify('game/gui/**.**', 'gui')
    build.classify('game/images/bg/**.**', 'bg')
    build.classify('game/images/cg/**.**', 'cg')
    build.classify('game/images/particles/**.**', 'particles')
    build.classify('game/images/sprite/**.**', 'sprites')
    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.mkv', 'movies')

    build.classify('game/music/**.**', 'music')
    build.classify('game/**.ogg', 'sounds')
    build.classify('game/**.mp3', 'sounds')
    build.classify('game/**.wav', 'sounds')




    build.documentation('*.html')
    build.documentation('*.txt')





define build.itch_project = "belgerum/demon-king-domination"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
