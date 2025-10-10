# ================================================
#  Five Nights at Glackus`s Education Edition API
#  Author: Gleb Ustimenko (nogai3, glackus)
#  Version: 1.0.0
#  Date: 2025-10-08
#  Copyright: (C) LighSync Games. 2023-2025
# ================================================

import random
from config import write_at_config, read_at_config

# ---- [ === Power System === ] ----

class Power:
    def __init__(self):
        self.value = read_at_config("EducationEdition", "power")
        self.enabled = read_at_config("Dev", "-disable_lights")
    
    def get_power(self):
        return read_at_config("EducationEdition", "power")
    
    def set_power(self, points: int):
        self.value = points
        write_at_config("EducationEdition", "power", points)
    
    def disable_power(self):
        self.enabled = False
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_energy", 1)
        print("[POWER]: Энергия отключена.")
    
    def enable_power(self):
        self.enabled = True
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_energy", 0)
        print("[POWER]: Энергия включена.")
power = Power()

# ---- [ === MusicBox === ] ----

class MusicBox:
    def __init__(self):
        self.enabled = read_at_config("Dev", "-disable_musicbox")
        self.level = read_at_config("EducationEdition", "musicbox_level")
    
    def get_level(self):
        return read_at_config("EducationEdition", "musicbox_level")
    
    def set_level(self, level: int):
        if 1 <= level:
            self.level = level
            write_at_config("EducationEdition", "musicbox_level", level)
        else:
            print(f"[MUSICBOX]: Уровень должен быть между 1 и 8.")
    
    def disable(self):
        self.enabled = False
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_musicbox", 1)
        print("[MUSICBOX]: Музыкальная шкатулка отключена.")
    
    def enable(self):
        self.enabled = True
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_musicbox", 0)
        print("[MUSICBOX]: Музыкальная шкатулка включена.")
musicbox = MusicBox()

# ---- [ === Camera === ] ----

class Camera:
    def __init__ (self):
        self.current_camera = read_at_config("EducationEdition", "current_camera")
        self.is_camera_open_var = read_at_config("EducationEdition", "is_camera_open")

    def open_camera(self):
        write_at_config("EducationEdition", "is_camera_open", 1)
        self.is_camera_open_var = 1
        print("[CAMERA]: Камера открыта")

    def close_camera(self):
        write_at_config("EducationEdition", "is_camera_open", 0)
        self.is_camera_open_var = 0
        print("[CAMERA]: Камера закрыта")
    
    def is_camera_open(self):
        return read_at_config("EducationEdition", "is_camera_open")

    def change_camera(self, cam_id: int):
        self.current_camera = cam_id
        write_at_config("EducationEdition", "current_camera", cam_id)
        print(f"[CAMERA]: Переключение на камеру {cam_id}")

    def get_current_camera(self):
        return read_at_config("EducationEdition", "current_camera")
    
    def prohibit_camera(self):
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_cams", 1)
        print("[CAMERA]: Камеры запрещены")

    def allow_camera(self):
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_cams", 0)
        print("[CAMERA]: Камеры разрешены")
camera = Camera()

# ---- [ === Flashlight === ] ----

class Flashlight:
    def __init__(self):
        self.enabled = read_at_config("Dev", "-disable_lights")
        self.power = read_at_config("EducationEdition", "flashlight_power")    

    def flashlight_power(self, power: bool):
        self.power = power
        write_at_config("EducationEdition", "flashlight_power", int(power))
        state = "включен" if power else "выключен"
        print(f"[FLASHLIGHT]: Фонарик {state}.")
    
    def flashlight_disable(self):
        self.enabled = False
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_lights", 1)
        print("[FLASHLIGHT]: Фонарик отключен.")
    
    def flashlight_enable(self):
        self.enabled = True
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_lights", 0)
        print("[FLASHLIGHT]: Фонарик включен.")
flashlight = Flashlight()

# ---- [ === Entities and AI === ] ----

class Entity:
    def __init__(self):
        self.ai_enabled = read_at_config("Dev", "-disable_animatronics")
        self.ignored_list = []
    
    def add_entity(self, entity_id: int):
        if entity_id <= 4:
            if entity_id == 4:
                write_at_config("EducationEdition", "office_entity_2", entity_id)
            else:
                write_at_config("EducationEdition", "office_entity_1", entity_id)
        else:
            print(f"[ENTITY]: Неизвестная сущность: {entity_id}")
        print(f"[ENTITY]: Сущность {entity_id} добавлена")
    
    def remove_entity(self, entity_id: int):
        if entity_id <= 3:
            write_at_config("EducationEdition", "office_entity_1", 0)
        elif entity_id == 4:
            write_at_config("EducationEdition", "office_entity_2", 0)
        else:
            print(f"[ENTITY]: Неизвестная сущность: {entity_id}")
        print(f"[ENTITY]: Сущность {entity_id} удалена")
    
    def remove_all_entites(self, player_enabled: bool):
        if player_enabled:
            write_at_config("EducationEdition", "power", -1)
        write_at_config("EducationEdition", "office_entity_1", 0)
        write_at_config("EducationEdition", "office_entity_2", 0)
        state = "включая игрока" if player_enabled else ""
        print(f"[ENTITY]: Все сущности удалены {state}")
    
    def ai_set_movement(self, entity_id: int, needed_points: int):
        match entity_id:
            case 1:
                write_at_config("EducationEdition", "glackus_movement_points", needed_points)
            case 2:
                write_at_config("EducationEdition", "wandarmo_movement_points", needed_points)
            case 3:
                write_at_config("EducationEdition", "fster_movement_points", needed_points)
            case 4:
                write_at_config("EducationEdition", "biggie_movement_points", needed_points)
            case _:
                print(f"[AI]: Неизвестная сущность: {entity_id}")
        print(f"[AI]: Сущность {entity_id} движется на {needed_points} точек")
    
    def ai_ignore(self, entity_id: int):
        write_at_config("Dev", "-dev_mode", 1)
        match entity_id:
            case 1:
                write_at_config("Dev", "-disable_glackus", 1)
            case 2:
                write_at_config("Dev", "-disable_wandarmo", 1)
            case 3:
                write_at_config("Dev", "-disable_fster", 1)
            case 4:
                write_at_config("Dev", "-disable_biggie", 1)
            case _:
                print("[AI]: Неизвестная сущность")
        self.ignored_list.append(entity_id)
        print(f"[AI]: Сущность {entity_id} игнорирует игрока") 
    
    def ai_unignore(self, entity_id: int):
        write_at_config("Dev", "-dev_mode", 1)
        match entity_id:
            case 1:
                write_at_config("Dev", "-disable_glackus", 0)
            case 2:
                write_at_config("Dev", "-disable_wandarmo", 0)
            case 3:
                write_at_config("Dev", "-disable_fster", 0)
            case 4:
                write_at_config("Dev", "-disable_biggie", 0)
            case _:
                print("[AI]: Неизвестная сущность")
        if entity_id in self.ignored_list:
            self.ignored_list.remove(entity_id)
        print(f"[AI]: Сущность {entity_id} больше не игнорирует игрока")
    
    def ai_disable(self):
        self.ai_enabled = False
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_animatronics", 1)
        print("[AI]: ИИ отключен")
    
    def ai_enable(self):
        self.ai_enabled = True
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_animatronics", 0)
        print("[AI]: ИИ включен")
    
    def get_ai_ignored_list(self):
        return self.ignored_list
entity = Entity()

# ---- [ === Time === ] ----

class Time:
    def __init__(self):
        self.current_time = read_at_config("EducationEdition", "time")
        self.enable = read_at_config("Dev", "-disable_time")
    
    def get_time(self):
        return read_at_config("EducationEdition", "time")
    
    def set_time(self, time: int):
        write_at_config("EducationEdition", "time", time)
        self.current_time = time
    
    def disable_time(self):
        self.enable = False
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_time", 1)
        print("[TIME]: Время отключено.")
    
    def enable_time(self):
        self.enable = True
        write_at_config("Dev", "-dev_mode", 1)
        write_at_config("Dev", "-disable_time", 0)
        print("[TIME]: Время включено.")   
time = Time()

# ---- [ === Session === ] ----

class Sesssion:
    def __init__(self):
        self.fullscreen = read_at_config("EducationEdition", "screen_mode")
        self.running = read_at_config("EducationEdition", "is_running")
        self.account_name = f"Player{random.randint(0,9999)}"
        self.account_uuid = "0000-0000-0000-0000"
        self.session_id = 1
        self.level = read_at_config("fnag1", "level")
        self.version = read_at_config("EducationEdition", "version")
    
    def get_fps(self):
        return read_at_config("EducationEdition", "fps")

    def get_window_mode(self):
        return read_at_config("EducationEdition", "screen_mode")

    def set_window_mode(self, fullscreen: bool):
        self.fullscreen = fullscreen
        write_at_config("EducationEdition", "screen_mode", fullscreen)
        mode = "полноэкранный" if fullscreen else "оконный"
        print(f"[SESSION]: Режим окна установлен на {mode}")
    
    def is_running(self):
        return read_at_config("EducationEdition", "is_running")
    
    def get_session_id(self):
        return read_at_config("Session", "sessionid") or self.session_id
    
    def get_account_uuid(self): 
        return read_at_config("Session", "uuid") or self.account_uuid

    def get_account_name(self):
        return read_at_config("Session", "username") or self.account_name
    
    def set_game_scene(self, scene_id: int):
        write_at_config("EducationEdition", "current_screen_id", scene_id)
        print(f"[SESSION]: Смена игровой сцены на {scene_id}")
    
    def set_level(self, level: int):
        self.level = level
        write_at_config("fnag1", "level", level)
        print(f"[SESSION]: Уровень установлен на {level}")

    def get_game_version(self):
        return read_at_config("EducationEdition", "version")
session = Sesssion()