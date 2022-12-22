import sys
import pygame

# ENGINE IMPORTS
from engine_JNeto_Productions.game_loop import GameLoop
from engine_JNeto_Productions.rendering_layer import RenderingLayer
from engine_JNeto_Productions.camera import Camera
from engine_JNeto_Productions.scene import Scene
from engine_JNeto_Productions.systems.scalable_game_screen_system import GameScreen
from game_object_score_scene.black_filte_game_object import BlackFilter
from game_object_score_scene.score_registration_floating_menu import ScoreRegistrationFloatingMenu
from game_object_score_scene.text_holder_game_object import TextHolder

# GAME OBJECTS IMPORTS
from game_objects_main_scene.game_object_cockpit import Cockpit
from game_objects_main_scene.game_object_left_shoot_ui import LeftShootUi
from game_objects_main_scene.game_object_map_limits import MapLimits
from game_objects_main_scene.game_object_map import Map
from game_objects_main_scene.game_object_meteor import Meteor
from game_objects_main_scene.game_object_meteor_manager import MeteorManager
from game_objects_main_scene.game_object_player import Player
from game_objects_main_scene.game_object_score import Score
from game_objects_main_scene.game_object_main_scene_reseter import MainSceneReseter
from game_objects_menu_scene.banner_game_object import MenuBanner
from game_objects_menu_scene.menu_background_game_object import MenuBackground
from game_object_button import Button

# GAME LOOP
game_loop = GameLoop()

# MENU SCENE
menu_layer1 = RenderingLayer("menu_layer1")
menu_layer2 = RenderingLayer("menu_layer2")
camera_menu = Camera(RenderingLayer("map_layer"), menu_layer1, menu_layer2)
menu_scene = Scene(camera_menu)
map0 = Map(menu_scene)
menu_background = MenuBackground(menu_scene, menu_layer1)
menu_banner = MenuBanner(menu_scene, menu_layer1)

# SCORE SCENE
score_layer1 = RenderingLayer("score_layer1")
score_layer2 = RenderingLayer("score_layer2")
score_layer3 = RenderingLayer("score_layer3")
score_layer4 = RenderingLayer("score_layer4")
score_sence_camara = Camera(RenderingLayer("map_layer"), score_layer1, score_layer2, score_layer3, score_layer4)
score_scene = Scene(score_sence_camara)
map1 = Map(score_scene)
black_filter = BlackFilter(score_scene, score_layer1)
text_holder = TextHolder(score_scene, score_layer1)
score_registration_menu = ScoreRegistrationFloatingMenu(score_scene, score_layer4)



# MAIN SCENE
# CAMERA AND RENDERING LAYERS
map_rendering_layer = RenderingLayer("map_layer")
player_rendering_layer = RenderingLayer("player_layer")
map_limits_layer = RenderingLayer("map_limits_layer")
over_player_layer = RenderingLayer("over_player_layer")
bars_layer = RenderingLayer("bars_layer")
cockpit_layer = RenderingLayer("cockpit_layer")
main_camera = Camera(map_rendering_layer, player_rendering_layer, over_player_layer, map_limits_layer, bars_layer,cockpit_layer)
# MAIN SCENE
main_scene = Scene(main_camera)
# GAME OBJECTS
map = Map(main_scene)
map_limits = MapLimits(main_scene)
player = Player(main_scene)
cockpit = Cockpit(main_scene, cockpit_layer)
left_shoot_ui = LeftShootUi(main_scene)
Meteor.Game_loop = game_loop
Meteor.Score_scene = score_scene
meteor_manager = MeteorManager(main_scene, map_rendering_layer)
score = Score(main_scene)


# SCENE loaders/transitions/buttons
main_scene_reseter = MainSceneReseter(main_scene)

def func_setinha_back_to_menu():
    main_scene_reseter.reset_phase()
    game_loop.set_current_scene(menu_scene)
    print("main scene => menu")
setinha_main_game_button = Button("game_res/setinha.png", "game_res/setinha_active.png",
                                   pygame.Vector2(40, 40), 1.5, func_setinha_back_to_menu, main_scene, cockpit_layer)

setinha_score_button = Button("game_res/setinha.png", "game_res/setinha_active.png",
                                   pygame.Vector2(40, 40), 1.5, func_setinha_back_to_menu, score_scene, score_layer4)

def func_start_button():
    main_scene_reseter.reset_phase()
    game_loop.set_current_scene(main_scene)
    print("menu => main scene")
menu_start_button = Button("game_res/menu/menu_start.png", "game_res/menu/menu_start_active.png",
                           pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfRealScreenHeight-40), 2,
                           func_start_button, menu_scene, menu_layer2)

def func_score_button():
    print("menu => scores")
    game_loop.set_current_scene(score_scene)
menu_scores_button = Button("game_res/menu/menu_score_button.png", "game_res/menu/menu_score_button_active.png",
                           pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfRealScreenHeight+50), 2,
                           func_score_button, menu_scene, menu_layer2)

def func_exit_button():
    pygame.quit()
    sys.exit()
menu_exit_button = Button("game_res/menu/menu_exit.png", "game_res/menu/menu_exit_active.png",
                           pygame.Vector2(GameScreen.HalfDummyScreenWidth, GameScreen.HalfRealScreenHeight+140), 2,
                           func_exit_button, menu_scene, menu_layer2)

# GAME LOOP
game_loop.set_current_scene(menu_scene)
game_loop.run_game_loop()

