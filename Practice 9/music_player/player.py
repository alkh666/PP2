import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.load_playlist()

    def load_playlist(self):
        music_dir = "music"
        if os.path.exists(music_dir):
            for file in sorted(os.listdir(music_dir)):
                if file.endswith((".mp3", ".wav")):
                    self.playlist.append(os.path.join(music_dir, file))

    def play(self):
        if not self.playlist:
            return
        pygame.mixer.music.load(self.playlist[self.current_index])
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_track_name(self):
        if not self.playlist:
            return "No tracks found"
        return os.path.basename(self.playlist[self.current_index])

    def get_position(self):
        if self.is_playing:
            return pygame.mixer.music.get_pos() // 1000  # в секундах
        return 0

    def get_status(self):
        return "▶ Playing" if self.is_playing else "■ Stopped"