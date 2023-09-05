import os
import pygame

class MusicPlayer:
    def __init__(self):
        pygame.init()
        self.playlist = []
        self.current_track = 0
        self.load_playlist()

    def load_playlist(self):
        music_folder = "path/to/your/music/folder"
        self.playlist = [os.path.join(music_folder, filename) for filename in os.listdir(music_folder) if filename.endswith(".mp3")]

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_track])
            pygame.mixer.music.play()

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.play()

    def print_playlist(self):
        for i, track in enumerate(self.playlist):
            print(f"{i + 1}. {os.path.basename(track)}")

def main():
    player = MusicPlayer()

    while True:
        print("\nMusic Player Menu:")
        print("1. Play")
        print("2. Pause")
        print("3. Resume")
        print("4. Stop")
        print("5. Next Track")
        print("6. Previous Track")
        print("7. Print Playlist")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            player.play()
        elif choice == "2":
            player.pause()
        elif choice == "3":
            player.resume()
        elif choice == "4":
            player.stop()
        elif choice == "5":
            player.next_track()
        elif choice == "6":
            player.prev_track()
        elif choice == "7":
            player.print_playlist()
        elif choice == "8":
            print("Goodbye!")
            pygame.quit()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
