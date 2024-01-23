import pygame
import time
import random

wait =  .4

pygame.init()

songs = []

class sounds:
    def play1():
        sound = pygame.mixer.Sound("beep.wav")
        pygame.mixer.Sound.play(sound)
    def play2():
        sound = pygame.mixer.Sound("beep (1).wav")
        pygame.mixer.Sound.play(sound)
    def play3():
        sound = pygame.mixer.Sound("beep (2).wav")
        pygame.mixer.Sound.play(sound)
    def play4():
        sound = pygame.mixer.Sound("beep (3).wav")
        pygame.mixer.Sound.play(sound)
    def play5():
        sound = pygame.mixer.Sound("beep (4).wav")
        pygame.mixer.Sound.play(sound)
    def play6():
        sound = pygame.mixer.Sound("beep (5).wav")
        pygame.mixer.Sound.play(sound)



def save_song(nums):
    songs.append(nums)
    
def play_song(numss):
    
    nums = songs[int(numss)]
    print(nums)
    for i in range(len(nums)):
        
        if nums[i] == 1:
            
            
            sound.play1()
            time.sleep(wait)
            
        if nums[i] == 2:
            
          
            sound.play2()
            time.sleep(wait)
            
        if nums[i] == 3:
            
            
            sound.play3()
            time.sleep(wait)
            
        if nums[i] == 4:
            
            
            sound.play4()
            time.sleep(wait)
            
        if nums[i] == 5:
            
           
            sound.play5()
            time.sleep(wait)
            
        if nums[i] == 6:
            
            
            sound.play6()
            time.sleep(wait)
            
    main(wait)

def main(wait):
    
    num = random.randrange(1,6)
    song = []
    inp = input("how many notes will the song last?: ")
    inp_min = int(inp)
    
    for i in range(int(inp)):
        inp_min -= 1
        
        if num == 1 and inp_min >= 1:
            
            song.append(num)
            num = random.choice([3, 2])
            sound.play1()
            time.sleep(wait)
            
        elif num == 2 and inp_min >= 1:
            
            song.append(num)
            num = random.choice([4, 5])
            sound.play2()
            time.sleep(wait)
            
        elif num == 3 and inp_min >= 1:
           
            song.append(num)
            num = random.choice([2, 6])
            sound.play3()
            time.sleep(wait)
            
        elif num == 4 and inp_min >= 1:
            
            song.append(num)
            num = random.choice([1, 5])
            sound.play4()
            time.sleep(wait)
            
        elif num == 5 and inp_min >= 1:
          
            song.append(num)
            num = random.choice([3, 6])
            sound.play5()
            time.sleep(wait)
            
        elif num == 6 and inp_min >= 1:
          
            song.append(num)
            num = random.choice([4,2])
            sound.play6()
            time.sleep(wait)

    print(song)
    
    print("song number is", len(songs))
    
    save = input("would you like to save that song end or play an old song?: ")
    
    if save == "save" or save == "yes" or save == "yes save"or save == "save song"or save == "yes save song":
        save_song(song)
        main(wait)
        
    elif save == "end":
        quit()
        
    elif save == "play old" or save == "play" or save == "old" or save == "play last song" or save == "yes play" or save == "play old song":
        num_s = input("what is the song number?: ")
        play_song(num_s)
        
    else:
        main(wait)
        
    

    
        
sound = sounds
main(wait)

