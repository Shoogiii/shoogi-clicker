#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Shoogi Clicker v2.0 - Professional Auto Clicker
Author: MiniMax Agent
Version: 2.0.0
"""

import tkinter as tk
import customtkinter as ctk
import pyautogui
import threading
import time
import json
import os
import sys
import random
from datetime import datetime
from pynput import mouse, keyboard
import pystray
from PIL import Image, ImageDraw, ImageTk
import numpy as np
import ctypes
from ctypes import wintypes

# ==============================================================================
# KONFİGÜRASYON VE SABİTLER
# ==============================================================================

VERSION = "2.0.0"
APP_NAME = "Shoogi Clicker"
CONFIG_FILE = "shoogi_settings.json"

# Tema Renkleri - Cyber Violet
COLORS = {
    "bg_dark": "#0D0D0D",
    "bg_surface": "#1A1A1A",
    "bg_card": "#252525",
    "primary": "#8B5CF6",
    "primary_hover": "#7C3AED",
    "secondary": "#06B6D4",
    "success": "#22C55E",
    "danger": "#EF4444",
    "warning": "#F59E0B",
    "text_primary": "#FFFFFF",
    "text_secondary": "#9CA3AF",
    "text_muted": "#6B7280",
    "border": "#374151"
}

# Çoklu Dil Desteği
LANGUAGES = {
    "tr": {
        "app_title": "Shoogi Clicker",
        "dashboard": "Kontrol Paneli",
        "settings": "Ayarlar",
        "profiles": "Profiller",
        "statistics": "İstatistikler",
        "start": "BAŞLAT",
        "stop": "DURDUR",
        "status_ready": "HAZIR",
        "status_running": "ÇALIŞIYOR",
        "status_paused": "DURAKLADI",
        "total_clicks": "Toplam Tıklama",
        "session_clicks": "Oturum Tıklaması",
        "current_cps": "Mevcut CPS",
        "click_type": "Tıklama Türü",
        "click_mode": "Tıklama Modu",
        "interval": "Aralık (ms)",
        "cps": "CPS",
        "left": "Sol",
        "right": "Sağ",
        "middle": "Orta",
        "single": "Tek",
        "double": "Çift",
        "infinite": "Sınırsız",
        "repeat_x": "X Kez Tekrarla",
        "random_jitter": "Rastgele Jitter",
        "always_on_top": "Her Zaman Üstte",
        "sound_feedback": "Sesli Geri Bildirim",
        "follow_cursor": "İmleci Takip Et",
        "fixed_location": "Sabit Konum",
        "hotkey": "Kısayol Tuşu",
        "press_key": "Tuşa basın...",
        "save_profile": "Profili Kaydet",
        "load_profile": "Profili Yükle",
        "delete_profile": "Profili Sil",
        "new_profile": "Yeni Profil",
        "profile_name": "Profil Adı",
        "language": "Dil",
        "theme": "Tema",
        "dark": "Koyu",
        "light": "Açık",
        "system": "Sistem",
        "click_limit": "Tıklama Limiti",
        "unlimited": "Sınırsız",
        "coordinates": "Koordinatlar",
        "x_coord": "X",
        "y_coord": "Y",
        "set_position": "Konum Belirle",
        "exit": "Çıkış",
        "show": "Göster",
        "hide": "Gizle",
        "minimize": "Küçült",
        "presets": "Ön Ayarlar",
        "roblox_clan": "Roblox Clan",
        "ultra_turbo": "Ultra Turbo",
        "safe_mode": "Güvenli Mod",
        "afk_mode": "AFK Modu",
        "game_pvp": "Oyun PVP",
        "cookie_clicker": "Cookie Clicker",
        "data_entry": "Veri Girişi",
        "time_running": "Çalışma Süresi",
        "avg_cps": "Ort. CPS",
        "max_cps": "Maks. CPS",
        "efficiency": "Verimlilik",
        "reset_stats": "İstatistikleri Sıfırla",
        "export_stats": "İstatistikleri Dışa Aktar",
        "enabled": "Etkin",
        "disabled": "Devre Dışı",
        "seconds": "saniye",
        "minutes": "dakika",
        "hours": "saat",
        "error_invalid_input": "Geçersiz giriş!",
        "error_profile_exists": "Bu profil adı zaten mevcut!",
        "success_saved": "Başarıyla kaydedildi!",
        "success_deleted": "Başarıyla silindi!",
        "confirm_delete": "Silmek istediğinize emin misiniz?",
        "no_profile_selected": "Lütfen bir profil seçin!",
        "profile_loaded": "Profil yüklendi:",
        "system_tray": "Sistem Tepsisi"
    },
    "en": {
        "app_title": "Shoogi Clicker",
        "dashboard": "Dashboard",
        "settings": "Settings",
        "profiles": "Profiles",
        "statistics": "Statistics",
        "start": "START",
        "stop": "STOP",
        "status_ready": "READY",
        "status_running": "RUNNING",
        "status_paused": "PAUSED",
        "total_clicks": "Total Clicks",
        "session_clicks": "Session Clicks",
        "current_cps": "Current CPS",
        "click_type": "Click Type",
        "click_mode": "Click Mode",
        "interval": "Interval (ms)",
        "cps": "CPS",
        "left": "Left",
        "right": "Right",
        "middle": "Middle",
        "single": "Single",
        "double": "Double",
        "infinite": "Infinite",
        "repeat_x": "Repeat X Times",
        "random_jitter": "Random Jitter",
        "always_on_top": "Always on Top",
        "sound_feedback": "Sound Feedback",
        "follow_cursor": "Follow Cursor",
        "fixed_location": "Fixed Location",
        "hotkey": "Hotkey",
        "press_key": "Press key...",
        "save_profile": "Save Profile",
        "load_profile": "Load Profile",
        "delete_profile": "Delete Profile",
        "new_profile": "New Profile",
        "profile_name": "Profile Name",
        "language": "Language",
        "theme": "Theme",
        "dark": "Dark",
        "light": "Light",
        "system": "System",
        "click_limit": "Click Limit",
        "unlimited": "Unlimited",
        "coordinates": "Coordinates",
        "x_coord": "X",
        "y_coord": "Y",
        "set_position": "Set Position",
        "exit": "Exit",
        "show": "Show",
        "hide": "Hide",
        "minimize": "Minimize",
        "presets": "Presets",
        "roblox_clan": "Roblox Clan",
        "ultra_turbo": "Ultra Turbo",
        "safe_mode": "Safe Mode",
        "afk_mode": "AFK Mode",
        "game_pvp": "Game PVP",
        "cookie_clicker": "Cookie Clicker",
        "data_entry": "Data Entry",
        "time_running": "Time Running",
        "avg_cps": "Avg. CPS",
        "max_cps": "Max. CPS",
        "efficiency": "Efficiency",
        "reset_stats": "Reset Statistics",
        "export_stats": "Export Statistics",
        "enabled": "Enabled",
        "disabled": "Disabled",
        "seconds": "seconds",
        "minutes": "minutes",
        "hours": "hours",
        "error_invalid_input": "Invalid input!",
        "error_profile_exists": "Profile name already exists!",
        "success_saved": "Successfully saved!",
        "success_deleted": "Successfully deleted!",
        "confirm_delete": "Are you sure you want to delete?",
        "no_profile_selected": "Please select a profile!",
        "profile_loaded": "Profil yüklendi:",
        "system_tray": "System Tray",
        "location_jitter": "Konum Jitter (Anti-Cheat)",
        "jitter_px": "px"
    }
}


# Ön Ayarlar
PRESETS = {
    "roblox_pvp_elite": {
        "name_tr": "Roblox PvP Elite",
        "name_en": "Roblox PvP Elite",
        "interval_ms": 75, # ~13 CPS (Safe for most)
        "click_type": "left",
        "click_mode": "double",
        "repeat_mode": "infinite",
        "repeat_count": 0,
        "random_jitter": True,
        "jitter_amount": 25,
        "location_jitter": True,
        "location_jitter_amount": 3,
        "follow_cursor": True,
        "fixed_x": 0,
        "fixed_y": 0
    },
    "roblox_simulator_turbo": {
        "name_tr": "Roblox Simulator Turbo",
        "name_en": "Roblox Simulator Turbo",
        "interval_ms": 15, # ~66 CPS
        "click_type": "left",
        "click_mode": "single",
        "repeat_mode": "infinite",
        "repeat_count": 0,
        "random_jitter": True,
        "jitter_amount": 10,
        "location_jitter": True,
        "location_jitter_amount": 2,
        "follow_cursor": True,
        "fixed_x": 0,
        "fixed_y": 0
    },
    "roblox_afk_legit": {
        "name_tr": "Roblox AFK Legit",
        "name_en": "Roblox AFK Legit",
        "interval_ms": 120000, # 2 minutes
        "click_type": "left",
        "click_mode": "single",
        "repeat_mode": "infinite",
        "repeat_count": 0,
        "random_jitter": True,
        "jitter_amount": 30,
        "location_jitter": True,
        "location_jitter_amount": 10,
        "follow_cursor": True,
        "fixed_x": 0,
        "fixed_y": 0
    },
    "ultra_turbo": {
        "name_tr": "Ultra Turbo",
        "name_en": "Ultra Turbo",
        "interval_ms": 1,
        "click_type": "left",
        "click_mode": "single",
        "repeat_mode": "infinite",
        "repeat_count": 0,
        "random_jitter": False,
        "jitter_amount": 0,
        "location_jitter": False,
        "location_jitter_amount": 0,
        "follow_cursor": True,
        "fixed_x": 0,
        "fixed_y": 0
    },
    "safe_mode": {
        "name_tr": "Güvenli Mod",
        "name_en": "Safe Mode",
        "interval_ms": 100,
        "click_type": "left",
        "click_mode": "single",
        "repeat_mode": "infinite",
        "repeat_count": 0,
        "random_jitter": True,
        "jitter_amount": 20,
        "location_jitter": True,
        "location_jitter_amount": 2,
        "follow_cursor": True,
        "fixed_x": 0,
        "fixed_y": 0
    }
}




# ==============================================================================
# TEMA BİLEŞENLERİ
# ==============================================================================

class CyberButton(ctk.CTkButton):
    """Özel Cyber-themed buton"""
    def __init__(self, master, **kwargs):
        kwargs.setdefault("fg_color", COLORS["primary"])
        kwargs.setdefault("hover_color", COLORS["primary_hover"])
        kwargs.setdefault("text_color", COLORS["text_primary"])
        kwargs.setdefault("border_width", 0)
        kwargs.setdefault("corner_radius", 8)
        super().__init__(master, **kwargs)

class CyberSwitch(ctk.CTkSwitch):
    """Özel Cyber-themed switch"""
    def __init__(self, master, **kwargs):
        kwargs.setdefault("progress_color", COLORS["primary"])
        kwargs.setdefault("button_color", COLORS["primary"])
        kwargs.setdefault("button_hover_color", COLORS["primary_hover"])
        kwargs.setdefault("fg_color", COLORS["border"])
        super().__init__(master, **kwargs)

class CyberCard(ctk.CTkFrame):
    """Özel Cyber-themed kart"""
    def __init__(self, master, **kwargs):
        kwargs.setdefault("fg_color", COLORS["bg_card"])
        kwargs.setdefault("border_color", COLORS["border"])
        kwargs.setdefault("border_width", 1)
        kwargs.setdefault("corner_radius", 12)
        super().__init__(master, **kwargs)

class CyberEntry(ctk.CTkEntry):
    """Özel Cyber-themed giriş alanı"""
    def __init__(self, master, **kwargs):
        kwargs.setdefault("fg_color", COLORS["bg_surface"])
        kwargs.setdefault("border_color", COLORS["primary"])
        kwargs.setdefault("text_color", COLORS["text_primary"])
        kwargs.setdefault("placeholder_text_color", COLORS["text_muted"])
        super().__init__(master, **kwargs)

class StatCard(ctk.CTkFrame):
    """İstatistik kartı bileşeni"""
    def __init__(self, master, title, value="0", icon=None, **kwargs):
        kwargs.setdefault("fg_color", COLORS["bg_card"])
        kwargs.setdefault("border_color", COLORS["border"])
        kwargs.setdefault("border_width", 1)
        kwargs.setdefault("corner_radius", 10)
        super().__init__(master, **kwargs)
        
        self.title_label = ctk.CTkLabel(
            self, 
            text=title,
            font=ctk.CTkFont(size=11, weight="normal"),
            text_color=COLORS["text_muted"]
        )
        self.title_label.pack(pady=(10, 0), padx=10, anchor="w")
        
        self.value_label = ctk.CTkLabel(
            self,
            text=value,
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=COLORS["primary"]
        )
        self.value_label.pack(pady=(5, 10), padx=10, anchor="w")
    
    def update_value(self, value):
        self.value_label.configure(text=str(value))

# ==============================================================================
# TIKLAMA MOTORU
# ==============================================================================

class ClickEngine:
    """Tıklama motoru - işlem mantığı"""
    
    def __init__(self):
        self.running = False
        self.paused = False
        self.click_thread = None
        self.stop_event = threading.Event()
        
        # Windows için ctypes API'leri
        if sys.platform == "win32":
            self.user32 = ctypes.windll.user32
        else:
            self.user32 = None

        
        # Ayarlar
        self.interval_ms = 50
        self.click_type = "left"  # left, right, middle
        self.click_mode = "single"  # single, double
        self.repeat_mode = "infinite"  # infinite, repeat_x
        self.repeat_count = 0
        self.random_jitter = True
        self.jitter_amount = 15
        self.location_jitter = False
        self.location_jitter_amount = 5
        self.follow_cursor = True
        self.fixed_x = 0
        self.fixed_y = 0

        
        # İstatistikler
        self.total_clicks = 0
        self.session_clicks = 0
        self.start_time = None
        self.cps_history = []
        self.max_cps = 0
        
        # Callback
        self.on_stats_update = None
    
    def configure(self, **kwargs):
        """Ayarları güncelle"""
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def start(self):
        """Tıklamayı başlat"""
        if self.running:
            return
        
        self.running = True
        self.paused = False
        self.stop_event.clear()
        self.start_time = time.time()
        self.session_clicks = 0
        self.cps_history = []
        
        self.click_thread = threading.Thread(target=self._click_loop, daemon=True)
        self.click_thread.start()
    
    def stop(self):
        """Tıklamayı durdur"""
        self.running = False
        self.paused = False
        self.stop_event.set()
        
        if self.click_thread and self.click_thread.is_alive():
            self.click_thread.join(timeout=0.1)

    
    def toggle(self):
        """Tıklamayı aç/kapat"""
        if self.running:
            self.stop()
        else:
            self.start()
    
    def _click_loop(self):
        """Ana tıklama döngüsü"""
        clicks_per_action = 2 if self.click_mode == "double" else 1
        local_clicks = 0
        last_cps_check = time.time()
        cps_count = 0
        
        while self.running and not self.stop_event.is_set():
            try:
                # Koordinat belirleme
                if self.follow_cursor:
                    base_x, base_y = pyautogui.position()
                else:
                    base_x, base_y = self.fixed_x, self.fixed_y
                
                # Koordinat jitter'ı ekle (Anti-Cheat koruması)
                if self.location_jitter and self.location_jitter_amount > 0:
                    x = base_x + random.randint(-self.location_jitter_amount, self.location_jitter_amount)
                    y = base_y + random.randint(-self.location_jitter_amount, self.location_jitter_amount)
                else:
                    x, y = base_x, base_y

                
                # Tıklama yap
                self._do_click(x, y, self.click_type, clicks_per_action)

                
                # İstatistik güncelleme
                self.total_clicks += 1
                self.session_clicks += 1
                local_clicks += 1
                cps_count += 1
                
                # CPS hesapla
                current_time = time.time()
                if current_time - last_cps_check >= 1.0:
                    cps = cps_count / (current_time - last_cps_check)
                    self.cps_history.append(cps)
                    if len(self.cps_history) > 60:
                        self.cps_history.pop(0)
                    if cps > self.max_cps:
                        self.max_cps = cps
                    cps_count = 0
                    last_cps_check = current_time
                    
                    # Callback çağır
                    if self.on_stats_update:
                        self.on_stats_update(self.get_stats())
                
                # Limit kontrolü
                if self.repeat_mode == "repeat_x" and local_clicks >= self.repeat_count:
                    self.running = False
                    break
                
                # Aralık hesapla
                interval = self.interval_ms / 1000.0
                
                # Jitter ekle
                if self.random_jitter and self.jitter_amount > 0:
                    jitter = np.random.normal(0, interval * (self.jitter_amount / 100))
                    interval = max(0.001, interval + jitter)
                
                # Hassas bekleme
                self._precise_sleep(interval)
                
            except pyautogui.FailSafeException:
                print("Fail-safe tetiklendi! Fareyi köşeye çektiniz.")
                self.running = False
                if self.on_stats_update:
                    self.on_stats_update({"error": "fail_safe"})
                break
            except Exception as e:
                print(f"Tıklama hatası: {e}")
                break
        
        self.running = False
    
    def _do_click(self, x, y, button, clicks):
        """Optimize edilmiş tıklama fonksiyonu"""
        try:
            if sys.platform == "win32" and self.user32:
                # Windows Direct Injection (Daha hızlı)
                self.user32.SetCursorPos(int(x), int(y))
                
                button_map = {
                    "left": (0x0002, 0x0004),   # MOUSEEVENTF_LEFTDOWN, LEFTUP
                    "right": (0x0008, 0x0010),  # MOUSEEVENTF_RIGHTDOWN, RIGHTUP
                    "middle": (0x0020, 0x0040)  # MOUSEEVENTF_MIDDLEDOWN, MIDDLEUP
                }
                
                down, up = button_map.get(button, (0x0002, 0x0004))
                
                for _ in range(clicks):
                    self.user32.mouse_event(down, 0, 0, 0, 0)
                    self.user32.mouse_event(up, 0, 0, 0, 0)
            else:
                # Standart pyautogui (Cross-platform)
                pyautogui.click(x, y, button=button, clicks=clicks)
        except Exception:
            # Herhangi bir hata durumunda pyautogui'ye geri dön
            pyautogui.click(x, y, button=button, clicks=clicks)

    
    def _precise_sleep(self, duration):
        """Hassas bekleme fonksiyonu"""
        start = time.perf_counter()
        while time.perf_counter() - start < duration:
            if self.stop_event.is_set():
                break
            time.sleep(0.001)
    
    def get_stats(self):
        """İstatistikleri getir"""
        elapsed = time.time() - self.start_time if self.start_time else 0
        avg_cps = self.session_clicks / elapsed if elapsed > 0 else 0
        
        return {
            "total_clicks": self.total_clicks,
            "session_clicks": self.session_clicks,
            "current_cps": self.cps_history[-1] if self.cps_history else 0,
            "avg_cps": avg_cps,
            "max_cps": self.max_cps,
            "elapsed_time": elapsed,
            "running": self.running
        }
    
    def reset_stats(self):
        """İstatistikleri sıfırla"""
        self.total_clicks = 0
        self.session_clicks = 0
        self.start_time = None
        self.cps_history = []
        self.max_cps = 0

# ==============================================================================
# AYAR YÖNETİCİSİ
# ==============================================================================

class ConfigManager:
    """Ayarları yönet"""
    
    def __init__(self):
        self.config_file = CONFIG_FILE
        self.config = self.load()
    
    def load(self):
        """Ayarları yükle"""
        default = {
            "language": "tr",
            "theme": "dark",
            "always_on_top": False,
            "sound_feedback": False,
            "hotkey": "f6",
            "current_profile": "default",
            "profiles": {
                "default": PRESETS["roblox_pvp_elite"]
            },
            "statistics": {
                "total_clicks_all_time": 0,
                "total_sessions": 0,
                "total_time": 0
            }
        }
        
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # Mevcut ayarları birleştir
                    for key in default:
                        if key not in config:
                            config[key] = default[key]
                    return config
        except Exception as e:
            print(f"Ayar yükleme hatası: {e}")
        
        return default
    
    def save(self):
        """Ayarları kaydet"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Ayar kaydetme hatası: {e}")
            return False
    
    def get(self, key, default=None):
        """Değer getir"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """Değer ayarla"""
        self.config[key] = value
    
    def update_profile(self, name, data):
        """Profil güncelle"""
        self.config["profiles"][name] = data
        self.save()
    
    def delete_profile(self, name):
        """Profil sil"""
        if name in self.config["profiles"]:
            del self.config["profiles"][name]
            self.save()

# ==============================================================================
# ANA UYGULAMA
# ==============================================================================

class ShoogiClickerApp(ctk.CTk):
    """Ana uygulama sınıfı"""
    
    def __init__(self):
        super().__init__()
        
        # Başlangıç ayarları
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")
        
        # Değişkenler
        self.config = ConfigManager()
        self.lang = self.config.get("language", "tr")
        self.texts = LANGUAGES[self.lang]
        self.click_engine = ClickEngine()
        self.click_engine.on_stats_update = self.on_stats_update
        self.hotkey = self.config.get("hotkey", "f6")
        self.recording_hotkey = False
        
        # İstatistikleri yükle
        stats_cfg = self.config.get("statistics", {})
        self.click_engine.total_clicks = stats_cfg.get("total_clicks_all_time", 0)

        
        # Pencere ayarları
        self.title(f"{APP_NAME} v{VERSION}")
        self.geometry("700x600")
        self.configure(fg_color=COLORS["bg_dark"])
        self.resizable(False, False)
        
        # Simge ayarla
        self.setup_icon()
        
        # UI oluştur
        self.setup_ui()
        
        # Dinleyicileri başlat
        self.setup_listeners()
        
        # Kapatma protokolü
        self.protocol('WM_DELETE_WINDOW', self.on_closing)
        
        # Ayarları yükle
        self.load_settings()
        
        # İlk istatistik güncellemesi
        self.update_stats_display()
    
    def setup_icon(self):
        """Simgeyi ayarla"""
        icon_path = "shoogi_icon.png"
        if os.path.exists(icon_path):
            try:
                img = Image.open(icon_path)
                img = img.resize((32, 32), Image.Resampling.LANCZOS)
                self.icon_image = ImageTk.PhotoImage(img)
                self.wm_iconphoto(True, self.icon_image)
            except Exception as e:
                print(f"Simge yükleme hatası: {e}")
    
    def t(self, key):
        """Dil metni getir"""
        return self.texts.get(key, key)
    
    def setup_ui(self):
        """UI oluştur"""
        # Ana çerçeve
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Sol panel - Navigasyon
        self.sidebar = ctk.CTkFrame(self.main_frame, width=180, fg_color=COLORS["bg_surface"], corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        
        # Logo/Header
        self.logo_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.logo_frame.pack(pady=20, padx=10)
        
        self.logo_label = ctk.CTkLabel(
            self.logo_frame,
            text="⚡",
            font=ctk.CTkFont(size=40),
            text_color=COLORS["primary"]
        )
        self.logo_label.pack()
        
        self.title_label = ctk.CTkLabel(
            self.logo_frame,
            text="SHOOGI",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=COLORS["primary"]
        )
        self.title_label.pack()
        
        self.subtitle_label = ctk.CTkLabel(
            self.logo_frame,
            text="CLICKER",
            font=ctk.CTkFont(size=14, weight="normal"),
            text_color=COLORS["text_secondary"]
        )
        self.subtitle_label.pack()
        
        # Navigasyon butonları
        self.nav_buttons = {}
        nav_items = [
            ("dashboard", "📊", self.t("dashboard")),
            ("settings", "⚙️", self.t("settings")),
            ("profiles", "👤", self.t("profiles")),
            ("statistics", "📈", self.t("statistics"))
        ]
        
        for i, (key, icon, text) in enumerate(nav_items):
            btn = ctk.CTkButton(
                self.sidebar,
                text=f"  {icon} {text}",
                command=lambda k=key: self.switch_tab(k),
                fg_color="transparent",
                hover_color=COLORS["primary"],
                text_color=COLORS["text_secondary"],
                anchor="w",
                height=40
            )
            btn.pack(pady=2, padx=10, fill="x")
            self.nav_buttons[key] = btn
        
        # Sağ panel - İçerik
        self.content_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.content_frame.pack(side="right", fill="both", expand=True, padx=10)
        
        # Sekmeleri oluştur
        self.create_dashboard_tab()
        self.create_settings_tab()
        self.create_profiles_tab()
        self.create_statistics_tab()
        
        # İlk sekmeyi göster
        self.current_tab = "dashboard"
        self.show_tab("dashboard")
    
    def create_dashboard_tab(self):
        """Kontrol paneli sekmesi"""
        self.dashboard_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        
        # Başlık
        self.dash_title = ctk.CTkLabel(
            self.dashboard_frame,
            text=self.t("dashboard"),
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=COLORS["text_primary"]
        )
        self.dash_title.pack(anchor="w", pady=(10, 20))
        
        # Durum kartı
        self.status_card = CyberCard(self.dashboard_frame)
        self.status_card.pack(fill="x", pady=(0, 15))
        
        self.status_indicator = ctk.CTkLabel(
            self.status_card,
            text="●",
            font=ctk.CTkFont(size=20),
            text_color=COLORS["success"]
        )
        self.status_indicator.pack(pady=(15, 0))
        
        self.status_label = ctk.CTkLabel(
            self.status_card,
            text=self.t("status_ready"),
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=COLORS["success"]
        )
        self.status_label.pack(pady=(5, 15))
        
        # İstatistik kartları
        self.stats_grid = ctk.CTkFrame(self.dashboard_frame, fg_color="transparent")
        self.stats_grid.pack(fill="x", pady=(0, 15))
        
        self.stat_total = StatCard(self.stats_grid, self.t("total_clicks"), "0")
        self.stat_total.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        self.stat_session = StatCard(self.stats_grid, self.t("session_clicks"), "0")
        self.stat_session.pack(side="left", fill="x", expand=True, padx=5)
        
        self.stat_cps = StatCard(self.stats_grid, self.t("current_cps"), "0.0")
        self.stat_cps.pack(side="left", fill="x", expand=True, padx=(5, 0))
        
        # Ayarlar kartı
        self.settings_card = CyberCard(self.dashboard_frame)
        self.settings_card.pack(fill="x", pady=(0, 15))
        
        # Aralık ayarı
        interval_frame = ctk.CTkFrame(self.settings_card, fg_color="transparent")
        interval_frame.pack(fill="x", padx=15, pady=10)
        
        ctk.CTkLabel(interval_frame, text=self.t("interval"), text_color=COLORS["text_secondary"]).pack(side="left")
        
        self.interval_entry = CyberEntry(interval_frame, width=100)
        self.interval_entry.insert(0, "50")
        self.interval_entry.pack(side="right")
        
        # CPS/ms seçimi
        self.mode_var = ctk.CTkOptionMenu(
            interval_frame,
            values=["ms", "CPS"],
            fg_color=COLORS["bg_surface"],
            button_color=COLORS["primary"],
            button_hover_color=COLORS["primary_hover"],
            width=80
        )
        self.mode_var.set("ms")
        self.mode_var.pack(side="right", padx=10)
        
        # Tıklama türü
        click_type_frame = ctk.CTkFrame(self.settings_card, fg_color="transparent")
        click_type_frame.pack(fill="x", padx=15, pady=5)
        
        ctk.CTkLabel(click_type_frame, text=self.t("click_type"), text_color=COLORS["text_secondary"]).pack(side="left")
        
        self.click_type_var = ctk.CTkOptionMenu(
            click_type_frame,
            values=[self.t("left"), self.t("right"), self.t("middle")],
            fg_color=COLORS["bg_surface"],
            button_color=COLORS["primary"],
            button_hover_color=COLORS["primary_hover"]
        )
        self.click_type_var.set(self.t("left"))
        self.click_type_var.pack(side="right")
        
        # Tıklame modu
        click_mode_frame = ctk.CTkFrame(self.settings_card, fg_color="transparent")
        click_mode_frame.pack(fill="x", padx=15, pady=5)
        
        ctk.CTkLabel(click_mode_frame, text=self.t("click_mode"), text_color=COLORS["text_secondary"]).pack(side="left")
        
        self.click_mode_var = ctk.CTkOptionMenu(
            click_mode_frame,
            values=[self.t("single"), self.t("double")],
            fg_color=COLORS["bg_surface"],
            button_color=COLORS["primary"],
            button_hover_color=COLORS["primary_hover"]
        )
        self.click_mode_var.set(self.t("single"))
        self.click_mode_var.pack(side="right")
        
        # İlerleme modu
        repeat_frame = ctk.CTkFrame(self.settings_card, fg_color="transparent")
        repeat_frame.pack(fill="x", padx=15, pady=5)
        
        ctk.CTkLabel(repeat_frame, text=self.t("repeat_x"), text_color=COLORS["text_secondary"]).pack(side="left")
        
        self.repeat_var = ctk.CTkOptionMenu(
            repeat_frame,
            values=[self.t("infinite"), self.t("repeat_x")],
            fg_color=COLORS["bg_surface"],
            button_color=COLORS["primary"],
            button_hover_color=COLORS["primary_hover"],
            command=self.on_repeat_mode_changed
        )
        self.repeat_var.set(self.t("infinite"))
        self.repeat_var.pack(side="right", padx=5)
        
        self.repeat_count_entry = CyberEntry(repeat_frame, width=80)
        self.repeat_count_entry.insert(0, "100")
        self.repeat_count_entry.pack(side="right")
        self.repeat_count_entry.configure(state="disabled")
        
        # Switchler
        self.sw_jitter = CyberSwitch(
            self.settings_card,
            text=self.t("random_jitter")
        )
        self.sw_jitter.select()
        self.sw_jitter.pack(pady=10, padx=15, anchor="w")
        
        self.sw_follow = CyberSwitch(
            self.settings_card,
            text=self.t("follow_cursor")
        )
        self.sw_follow.select()
        self.sw_follow.pack(pady=5, padx=15, anchor="w")
        
        # Konum Jitter Switch
        self.sw_loc_jitter = CyberSwitch(
            self.settings_card,
            text=self.t("location_jitter")
        )
        self.sw_loc_jitter.pack(pady=5, padx=15, anchor="w")

        
        # Kısayol butonu
        hotkey_frame = ctk.CTkFrame(self.settings_card, fg_color="transparent")
        hotkey_frame.pack(fill="x", padx=15, pady=10)
        
        ctk.CTkLabel(hotkey_frame, text=self.t("hotkey") + ":", text_color=COLORS["text_secondary"]).pack(side="left")
        
        self.hotkey_btn = ctk.CTkButton(
            hotkey_frame,
            text=self.config.get("hotkey", "f6").upper(),
            command=self.record_hotkey,
            fg_color=COLORS["bg_surface"],
            border_color=COLORS["primary"],
            border_width=1,
            width=100
        )
        self.hotkey_btn.pack(side="right")
        
        # Ana butonlar
        button_frame = ctk.CTkFrame(self.dashboard_frame, fg_color="transparent")
        button_frame.pack(fill="x", pady=10)
        
        self.btn_start = CyberButton(
            button_frame,
            text=self.t("start"),
            command=self.toggle_clicking,
            height=50,
            font=ctk.CTkFont(size=16, weight="bold"),
            fg_color=COLORS["success"]
        )
        self.btn_start.pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        self.btn_preset = ctk.CTkButton(
            button_frame,
            text=self.t("presets"),
            command=self.show_presets_menu,
            height=50,
            fg_color=COLORS["bg_surface"],
            border_color=COLORS["border"],
            border_width=1
        )
        self.btn_preset.pack(side="right", fill="x", expand=True, padx=(5, 0))
    
    def create_settings_tab(self):
        """Ayarlar sekmesi"""
        self.settings_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        
        self.settings_title = ctk.CTkLabel(
            self.settings_frame,
            text=self.t("settings"),
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=COLORS["text_primary"]
        )
        self.settings_title.pack(anchor="w", pady=(10, 20))
        
        # Genel ayarlar kartı
        general_card = CyberCard(self.settings_frame)
        general_card.pack(fill="x", pady=(0, 10))
        
        # Dil
        lang_frame = ctk.CTkFrame(general_card, fg_color="transparent")
        lang_frame.pack(fill="x", padx=15, pady=10)
        
        ctk.CTkLabel(lang_frame, text=self.t("language"), text_color=COLORS["text_secondary"]).pack(side="left")
        
        self.lang_var = ctk.CTkOptionMenu(
            lang_frame,
            values=["Türkçe", "English"],
            command=self.change_language,
            fg_color=COLORS["bg_surface"],
            button_color=COLORS["primary"],
            button_hover_color=COLORS["primary_hover"]
        )
        self.lang_var.set("Türkçe" if self.lang == "tr" else "English")
        self.lang_var.pack(side="right")
        
        # Tema
        theme_frame = ctk.CTkFrame(general_card, fg_color="transparent")
        theme_frame.pack(fill="x", padx=15, pady=5)
        
        ctk.CTkLabel(theme_frame, text=self.t("theme"), text_color=COLORS["text_secondary"]).pack(side="left")
        
        self.theme_var = ctk.CTkOptionMenu(
            theme_frame,
            values=[self.t("dark"), self.t("light"), self.t("system")],
            command=self.change_theme,
            fg_color=COLORS["bg_surface"],
            button_color=COLORS["primary"],
            button_hover_color=COLORS["primary_hover"]
        )
        self.theme_var.set(self.t("dark"))
        self.theme_var.pack(side="right")
        
        # Switchler
        self.sw_top = CyberSwitch(
            general_card,
            text=self.t("always_on_top"),
            command=self.toggle_always_on_top
        )
        self.sw_top.pack(pady=10, padx=15, anchor="w")
        
        self.sw_sound = CyberSwitch(
            general_card,
            text=self.t("sound_feedback")
        )
        self.sw_sound.pack(pady=5, padx=15, anchor="w")
        
        # Hakkında
        about_card = CyberCard(self.settings_frame)
        about_card.pack(fill="x", pady=(10, 0))
        
        ctk.CTkLabel(
            about_card,
            text=f"{APP_NAME} v{VERSION}",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=COLORS["primary"]
        ).pack(pady=(15, 5))
        
        ctk.CTkLabel(
            about_card,
            text="Professional Auto Clicker",
            text_color=COLORS["text_secondary"]
        ).pack()
        
        ctk.CTkLabel(
            about_card,
            text="Made with ❤️ by Berat",
            text_color=COLORS["text_muted"],
            font=ctk.CTkFont(size=10)
        ).pack(pady=(0, 15))
    
    def create_profiles_tab(self):
        """Profiller sekmesi"""
        self.profiles_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        
        self.profiles_title = ctk.CTkLabel(
            self.profiles_frame,
            text=self.t("profiles"),
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=COLORS["text_primary"]
        )
        self.profiles_title.pack(anchor="w", pady=(10, 20))
        
        # Profil listesi
        list_card = CyberCard(self.profiles_frame)
        list_card.pack(fill="both", expand=True, pady=(0, 10))
        
        self.profile_listbox = tk.Listbox(
            list_card,
            bg=COLORS["bg_surface"],
            fg=COLORS["text_primary"],
            selectbackground=COLORS["primary"],
            borderwidth=0,
            highlightthickness=0
        )
        self.profile_listbox.pack(fill="both", expand=True, padx=10, pady=10)
        self.profile_listbox.bind('<<ListboxSelect>>', self.on_profile_select)
        
        # Profil butonları
        btn_frame = ctk.CTkFrame(self.profiles_frame, fg_color="transparent")
        btn_frame.pack(fill="x")
        
        CyberButton(
            btn_frame,
            text=self.t("load_profile"),
            command=self.load_selected_profile,
            height=35
        ).pack(side="left", fill="x", expand=True, padx=(0, 5))
        
        CyberButton(
            btn_frame,
            text=self.t("save_profile"),
            command=self.save_current_as_profile,
            height=35,
            fg_color=COLORS["secondary"]
        ).pack(side="right", fill="x", expand=True, padx=(5, 0))
        
        CyberButton(
            btn_frame,
            text=self.t("delete_profile"),
            command=self.delete_selected_profile,
            height=35,
            fg_color=COLORS["danger"]
        ).pack(side="right", fill="x", expand=True, padx=(5, 0))
    
    def create_statistics_tab(self):
        """İstatistikler sekmesi"""
        self.statistics_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        
        self.statistics_title = ctk.CTkLabel(
            self.statistics_frame,
            text=self.t("statistics"),
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=COLORS["text_primary"]
        )
        self.statistics_title.pack(anchor="w", pady=(10, 20))
        
        # Detaylı istatistikler
        stats_card = CyberCard(self.statistics_frame)
        stats_card.pack(fill="both", expand=True)
        
        # İstatistik satırları
        stats_data = [
            ("total_clicks", self.t("total_clicks"), "0"),
            ("session_clicks", self.t("session_clicks"), "0"),
            ("avg_cps", self.t("avg_cps"), "0.0"),
            ("max_cps", self.t("max_cps"), "0.0"),
            ("time_running", self.t("time_running"), "0:00:00")
        ]
        
        self.stat_labels = {}
        for key, label, default in stats_data:
            row = ctk.CTkFrame(stats_card, fg_color="transparent")
            row.pack(fill="x", padx=15, pady=8)
            
            ctk.CTkLabel(
                row,
                text=label,
                text_color=COLORS["text_secondary"]
            ).pack(side="left")
            
            value_label = ctk.CTkLabel(
                row,
                text=default,
                font=ctk.CTkFont(size=16, weight="bold"),
                text_color=COLORS["primary"]
            )
            value_label.pack(side="right")
            self.stat_labels[key] = value_label
        
        # Sıfırla butonu
        CyberButton(
            stats_card,
            text=self.t("reset_stats"),
            command=self.reset_statistics,
            height=40,
            fg_color=COLORS["danger"]
        ).pack(pady=15, padx=15, fill="x")
    
    def switch_tab(self, tab_name):
        """Sekme değiştir"""
        self.show_tab(tab_name)
    
    def show_tab(self, tab_name):
        """Sekme göster"""
        # Tüm sekmeleri gizle
        for frame in [self.dashboard_frame, self.settings_frame, 
                     self.profiles_frame, self.statistics_frame]:
            if frame:
                frame.pack_forget()
        
        # Buton renklerini güncelle
        for key, btn in self.nav_buttons.items():
            if key == tab_name:
                btn.configure(fg_color=COLORS["primary"])
            else:
                btn.configure(fg_color="transparent")
        
        # Seçili sekmeyi göster
        tab_map = {
            "dashboard": self.dashboard_frame,
            "settings": self.settings_frame,
            "profiles": self.profiles_frame,
            "statistics": self.statistics_frame
        }
        
        frame = tab_map.get(tab_name)
        if frame:
            frame.pack(fill="both", expand=True)
            self.current_tab = tab_name
    
    def on_repeat_mode_changed(self, value):
        """Tekrar modu değişti"""
        if value == self.t("repeat_x"):
            self.repeat_count_entry.configure(state="normal")
        else:
            self.repeat_count_entry.configure(state="disabled")
    
    def toggle_clicking(self):
        """Tıklamayı aç/kapat"""
        if self.click_engine.running:
            self.click_engine.stop()
            self.btn_start.configure(text=self.t("start"), fg_color=COLORS["success"])
            self.status_label.configure(text=self.t("status_ready"), text_color=COLORS["success"])
            self.status_indicator.configure(text_color=COLORS["success"])
        else:
            # Ayarları oku
            try:
                interval = float(self.interval_entry.get())
                if self.mode_var.get() == "CPS":
                    interval = 1000.0 / interval if interval > 0 else 50
                
                click_type_map = {self.t("left"): "left", self.t("right"): "right", self.t("middle"): "middle"}
                click_type = click_type_map.get(self.click_type_var.get(), "left")
                
                click_mode_map = {self.t("single"): "single", self.t("double"): "double"}
                click_mode = click_mode_map.get(self.click_mode_var.get(), "single")
                
                repeat_mode = "repeat_x" if self.repeat_var.get() == self.t("repeat_x") else "infinite"
                repeat_count = int(self.repeat_count_entry.get()) if repeat_mode == "repeat_x" else 0
                
                self.click_engine.configure(
                    interval_ms=interval,
                    click_type=click_type,
                    click_mode=click_mode,
                    repeat_mode=repeat_mode,
                    repeat_count=repeat_count,
                    random_jitter=self.sw_jitter.get(),
                    location_jitter=self.sw_loc_jitter.get(),
                    location_jitter_amount=5 if "roblox" in (self.config.get("current_profile", "")).lower() else 3,
                    follow_cursor=self.sw_follow.get()
                )

                
                self.click_engine.start()
                self.btn_start.configure(text=self.t("stop"), fg_color=COLORS["danger"])
                self.status_label.configure(text=self.t("status_running"), text_color=COLORS["danger"])
                self.status_indicator.configure(text_color=COLORS["danger"])
                
            except ValueError:
                self._show_error(self.t("error_invalid_input"))
    
    def _show_error(self, message):
        """Hata mesajı göster"""
        if sys.platform == "win32":
            ctypes.windll.user32.MessageBoxW(0, message, "Hata", 0x10)
        else:
            print(f"HATA: {message}")

    
    def on_stats_update(self, stats):
        """İstatistik güncellemesi"""
        if "error" in stats and stats["error"] == "fail_safe":
            self.after(0, self.handle_fail_safe)
        else:
            self.after(0, lambda: self._update_stats(stats))
    
    def handle_fail_safe(self):
        """Fail-safe durumunu yönet"""
        if self.click_engine.running:
            self.click_engine.stop()
        
        self.btn_start.configure(text=self.t("start"), fg_color=COLORS["success"])
        self.status_label.configure(text=self.t("status_ready"), text_color=COLORS["success"])
        self.status_indicator.configure(text_color=COLORS["success"])
        self._show_error("Fail-safe tetiklendi! Fareyi köşeye çektiğiniz için tıklama durduruldu.")

    
    def _update_stats(self, stats):
        """İstatistikleri güncelle (UI thread)"""
        self.stat_total.update_value(f"{stats['total_clicks']:,}")
        self.stat_session.update_value(f"{stats['session_clicks']:,}")
        self.stat_cps.update_value(f"{stats['current_cps']:.1f}")
        
        # Dashboard sekmesindeysek istatistik sekmesini de güncelle
        if self.current_tab == "statistics":
            self.update_stats_display()
    
    def update_stats_display(self):
        """İstatistik ekranını güncelle"""
        stats = self.click_engine.get_stats()
        
        if "total_clicks" in self.stat_labels:
            self.stat_labels["total_clicks"].configure(text=f"{stats['total_clicks']:,}")
        if "session_clicks" in self.stat_labels:
            self.stat_labels["session_clicks"].configure(text=f"{stats['session_clicks']:,}")
        if "avg_cps" in self.stat_labels:
            self.stat_labels["avg_cps"].configure(text=f"{stats['avg_cps']:.1f}")
        if "max_cps" in self.stat_labels:
            self.stat_labels["max_cps"].configure(text=f"{stats['max_cps']:.1f}")
        if "time_running" in self.stat_labels:
            elapsed = int(stats['elapsed_time'])
            hours = elapsed // 3600
            minutes = (elapsed % 3600) // 60
            seconds = elapsed % 60
            self.stat_labels["time_running"].configure(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    
    def record_hotkey(self):
        """Kısayol tuşu kaydet"""
        self.hotkey_btn.configure(text=self.t("press_key"))
        self.recording_hotkey = True
    
    def setup_listeners(self):
        """Klavye ve mouse dinleyicileri"""
        self.keyboard_listener = keyboard.Listener(on_press=self.on_key_press)
        self.keyboard_listener.start()
        
        self.mouse_listener = mouse.Listener(on_click=self.on_mouse_click)
        self.mouse_listener.start()
        
        # Periyodik UI güncellemesi
        self.after(100, self.periodic_update)
    
    def on_key_press(self, key):
        """Tuşa basıldığında"""
        try:
            k = key.char.lower() if hasattr(key, 'char') else key.name.lower()
        except:
            k = str(key).lower()
        
        if self.recording_hotkey:
            self.hotkey = k
            self.config.set("hotkey", k)
            self.config.save()
            self.hotkey_btn.configure(text=k.upper())
            self.recording_hotkey = False
            return
        
        if k == self.config.get("hotkey", "f6"):
            self.after(0, self.toggle_clicking)

    
    def on_mouse_click(self, x, y, button, pressed):
        """Mouse tıklamasında"""
        if not pressed:
            return
        
        if self.recording_hotkey:
            b = str(button).split('.')[-1].lower()
            self.hotkey = b
            self.config.set("hotkey", b)
            self.config.save()
            self.after(0, lambda: self.hotkey_btn.configure(text=b.upper()))
            self.recording_hotkey = False

    
    def periodic_update(self):
        """Periyodik güncelleme"""
        if self.click_engine.running:
            self.update_stats_display()
        self.after(100, self.periodic_update)
    
    def show_presets_menu(self):
        """Ön ayar menüsü"""
        menu = tk.Menu(self, tearoff=0)
        
        for preset_key, preset_data in PRESETS.items():
            name = preset_data.get(f"name_{self.lang}", preset_data["name_en"])
            menu.add_command(label=name, command=lambda p=preset_key: self.apply_preset(p))
        
        menu.post(self.btn_preset.winfo_rootx(), self.btn_preset.winfo_rooty() + self.btn_preset.winfo_height())
    
    def apply_preset(self, preset_key):
        """Ön ayar uygula"""
        preset = PRESETS[preset_key]
        
        self.interval_entry.delete(0, tk.END)
        self.interval_entry.insert(0, str(preset["interval_ms"]))
        
        click_type_map = {"left": self.t("left"), "right": self.t("right"), "middle": self.t("middle")}
        self.click_type_var.set(click_type_map.get(preset["click_type"], self.t("left")))
        
        click_mode_map = {"single": self.t("single"), "double": self.t("double")}
        self.click_mode_var.set(click_mode_map.get(preset["click_mode"], self.t("single")))
        
        if preset["random_jitter"]:
            self.sw_jitter.select()
        else:
            self.sw_jitter.deselect()
        
        if preset["follow_cursor"]:
            self.sw_follow.select()
        else:
            self.sw_follow.deselect()
            
        if preset.get("location_jitter", False):
            self.sw_loc_jitter.select()
        else:
            self.sw_loc_jitter.deselect()

    
    def change_language(self, value):
        """Dil değiştir"""
        self.lang = "tr" if value == "Türkçe" else "en"
        self.texts = LANGUAGES[self.lang]
        self.config.set("language", self.lang)
        self.config.save()
        
        # UI'ı yeniden oluştur (basit yenileme)
        self.reload_ui()
    
    def change_theme(self, value):
        """Tema değiştir"""
        theme_map = {self.t("dark"): "Dark", self.t("light"): "Light", self.t("system"): "System"}
        ctk.set_appearance_mode(theme_map.get(value, "Dark"))
        self.config.set("theme", value)
        self.config.save()
    
    def toggle_always_on_top(self):
        """Her zaman üstte"""
        self.attributes("-topmost", self.sw_top.get())
        self.config.set("always_on_top", self.sw_top.get())
        self.config.save()
    
    def reload_ui(self):
        """UI'ı güvenli bir şekilde yeniden yükle"""
        # Mevcut çerçeveleri temizle
        if hasattr(self, 'main_frame'):
            self.main_frame.destroy()
        
        # UI'ı yeniden oluştur
        self.setup_ui()
        # Ayarları tekrar yükle
        self.load_settings()
    
    def load_settings(self):
        """Ayarları yükle"""
        # Kısayol
        hotkey = self.config.get("hotkey", "f6")
        self.hotkey_btn.configure(text=hotkey.upper())
        
        # Always on top
        if self.config.get("always_on_top", False):
            self.sw_top.select()
            self.attributes("-topmost", True)
        
        # Profil listesini güncelle
        self.refresh_profile_list()
    
    def refresh_profile_list(self):
        """Profil listesini güncelle"""
        self.profile_listbox.delete(0, tk.END)
        profiles = self.config.get("profiles", {})
        for name in profiles.keys():
            self.profile_listbox.insert(tk.END, name)
    
    def on_profile_select(self, event):
        """Profil seçildiğinde butonları güncelle"""
        selection = self.profile_listbox.curselection()
        if selection:
            # İsteğe bağlı olarak buraya profil önizleme vs. eklenebilir
            pass

    
    def load_selected_profile(self):
        """Seçili profili yükle"""
        selection = self.profile_listbox.curselection()
        if not selection:
            print(self.t("no_profile_selected"))
            return
        
        profile_name = self.profile_listbox.get(selection[0])
        profile = self.config.get("profiles", {}).get(profile_name)
        
        if profile:
            self.interval_entry.delete(0, tk.END)
            self.interval_entry.insert(0, str(profile.get("interval_ms", 50)))
            
            click_type_map = {"left": self.t("left"), "right": self.t("right"), "middle": self.t("middle")}
            self.click_type_var.set(click_type_map.get(profile.get("click_type", "left"), self.t("left")))
            
            click_mode_map = {"single": self.t("single"), "double": self.t("double")}
            self.click_mode_var.set(click_mode_map.get(profile.get("click_mode", "single"), self.t("single")))
            
            if profile.get("random_jitter", False):
                self.sw_jitter.select()
            else:
                self.sw_jitter.deselect()
            
            if profile.get("follow_cursor", True):
                self.sw_follow.select()
            else:
                self.sw_follow.deselect()
                
            if profile.get("location_jitter", False):
                self.sw_loc_jitter.select()
            else:
                self.sw_loc_jitter.deselect()

            
            self.config.set("current_profile", profile_name)
            self.config.save()
    
    def save_current_as_profile(self):
        """Mevcut ayarları profil olarak kaydet"""
        dialog = ctk.CTkInputDialog(
            title=self.t("save_profile"),
            text=self.t("profile_name") + ":"
        )
        profile_name = dialog.get_input()
        
        if profile_name:
            try:
                profile_data = {
                    "interval_ms": float(self.interval_entry.get()),
                    "click_type": ["left", "right", "middle"][[self.t("left"), self.t("right"), self.t("middle")].index(self.click_type_var.get())],
                    "click_mode": ["single", "double"][[self.t("single"), self.t("double")].index(self.click_mode_var.get())],
                    "random_jitter": self.sw_jitter.get(),
                    "location_jitter": self.sw_loc_jitter.get(),
                    "follow_cursor": self.sw_follow.get()
                }

                
                self.config.update_profile(profile_name, profile_data)
                self.refresh_profile_list()
            except Exception as e:
                print(f"Profil kaydetme hatası: {e}")
    
    def delete_selected_profile(self):
        """Seçili profili sil"""
        selection = self.profile_listbox.curselection()
        if not selection:
            print(self.t("no_profile_selected"))
            return
        
        profile_name = self.profile_listbox.get(selection[0])
        
        if profile_name != "default":
            self.config.delete_profile(profile_name)
            self.refresh_profile_list()
    
    def reset_statistics(self):
        """İstatistikleri sıfırla"""
        self.click_engine.reset_stats()
        self.update_stats_display()
    
    def hide_to_tray(self):
        """Sistem tepsisine gizle"""
        self.withdraw()
        
        # Tray ikonu oluştur
        tray_img = Image.new('RGB', (64, 64), color=COLORS["primary"])
        d = ImageDraw.Draw(tray_img)
        d.text((16, 20), "SC", fill=(255, 255, 255))
        
        menu = pystray.Menu(
            pystray.Item(self.t("show"), self.show_from_tray),
            pystray.Item(self.t("exit"), self.exit_app)
        )
        
        self.tray_icon = pystray.Icon(APP_NAME, tray_img, APP_NAME, menu)
        threading.Thread(target=self.tray_icon.run, daemon=True).start()
    
    def show_from_tray(self):
        """Tepsiden göster"""
        if hasattr(self, 'tray_icon'):
            self.tray_icon.stop()
        self.deiconify()
        self.lift()
        self.focus_force()
    
    def exit_app(self):
        """Uygulamadan çık"""
        self.click_engine.stop()
        
        if hasattr(self, 'keyboard_listener'):
            self.keyboard_listener.stop()
        if hasattr(self, 'mouse_listener'):
            self.mouse_listener.stop()
        if hasattr(self, 'tray_icon'):
            self.tray_icon.stop()
        
        self.quit()
        os._exit(0)
    
    def on_closing(self):
        """Kapatma olayı"""
        self.click_engine.stop()
        
        # İstatistikleri güncelle ve kaydet
        stats_cfg = self.config.get("statistics", {})
        stats_cfg["total_clicks_all_time"] = self.click_engine.total_clicks
        self.config.set("statistics", stats_cfg)
        
        self.config.save()
        self.hide_to_tray()



# ==============================================================================
# ANA PROGRAM
# ==============================================================================

if __name__ == "__main__":
    # pyautogui güvenlik ayarları
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0
    
    # Uygulamayı başlat
    app = ShoogiClickerApp()
    app.mainloop()
