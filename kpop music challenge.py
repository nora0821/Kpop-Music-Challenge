import random
import winsound

# Define the play_sound function
def play_sound(sound_path):
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)

def main():
    print("\n♥ Welcome to Game Kpop Challenge ♥ Kpop Music Challenge!음악도전 ♥")
    sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\04.wav'
    play_sound(sound_path)  # Play the sound if the game starts

    print("\n♡ This Game Has 3 different levels ♡")
    print("♡ Level 1: You will be given a genre and lyric sentences for you to guess the song title and the singer ♡")
    print("__________________________________________________________________________________________________")
    print("\n♥ ੈ✩‧₊˚⋆͛*͛ ͙͛ ⁑͛⋆͛*͛  MAY THE CHALLENGE BEGIN ! ♥ ੈ✩‧₊˚⋆͛*͛ ͙͛ ⁑͛⋆͛*͛ ͙͛")
#First Question
    song = ["TT by Twice",]  

    x = random.choice(song)
    print("\nLevel 1 - KPOP Challenge")
    print("Guess the song title by using given clue and state the singer's name")
    print("Please write the answer in this format example: 3D by Jungkook")
    print("__________________________________________________________________________________________________")
    print("\n♥ Question 1")

    guess = None

    while x != guess:
        guess = str(input("\n♥ Genre Pop ~ Just Like TT?"))

        if x == guess:
            print("\nYou guessed {}. 고생 많았어 ! Correct! \U0001F601".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\01.wav'
            play_sound(sound_path)  # Play the sound when the answer is correct
            break
        else:
            print("\nYou guessed {}. 아이구 ! Come On! !\U0001F612".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\03.wav'
            play_sound(sound_path)  # Play the sound when the answer is wrong

#Second Question           
    song = ["Butter by BTS",]  
    x = random.choice(song)  # Choose a new random song for the next question
    print("__________________________________________________________________________________________________")
    print("\n♥ Question 2")
    guess = None

    while x != guess:
        guess = str(input("\n♥ Genre Pop ~ Smooth Like Butter?"))

        if x == guess:
            print("\nYou guessed {}. 고생 많았어 ! Correct! \U0001F601".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\01.wav'
            play_sound(sound_path)  # Play the sound when the answer is correct
            break
        else:
            print("\nYou guessed {}. 아이구 ! Come On! !\U0001F612".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\03.wav'
            play_sound(sound_path)  # Play the sound when the answer is wrong

#Third Question           
    song = ["Bang Bang Bang by Big Bang",]  
    x = random.choice(song)  # Choose a new random song for the next question
    print("__________________________________________________________________________________________________")
    print("\n♥ ੈ✩‧₊˚⋆͛*͛ ͙͛ ⁑͛⋆͛*͛  Congratulation You in Medium Level ! ♥ ੈ✩‧₊˚⋆͛*͛ ͙͛ ⁑͛⋆͛*͛ ͙͛")
    sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\06.wav'
    play_sound(sound_path)  # Play the sound for next level
    print("\n♥ Question 3")
    guess = None

    while x != guess:
        guess = str(input("\n♥ Genre Pop ~ Bang Bang Bang?"))

        if x == guess:
            print("\nYou guessed {}. 고생 많았어 ! Correct! \U0001F601".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\01.wav'
            play_sound(sound_path)  # Play the sound when the answer is correct
            break
        else:
            print("\nYou guessed {}. 아이구 ! Come On! !\U0001F612".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\03.wav'
            play_sound(sound_path)  # Play the sound when the answer is wrong

#Fourth Question           
    song = ["Super Shy by New Jeans",]  
    x = random.choice(song)  # Choose a new random song for the next question
    print("__________________________________________________________________________________________________")
    print("\n♥ Question 4")
    guess = None

    while x != guess:
        guess = str(input("\n♥ Genre Pop ~ I'm a super shy?"))

        if x == guess:
            print("\nYou guessed {}. 고생 많았어 ! Correct! \U0001F601".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\01.wav'
            play_sound(sound_path)  # Play the sound when the answer is correct
            break
        else:
            print("\nYou guessed {}. 아이구 ! Come On! !\U0001F612".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\03.wav'
            play_sound(sound_path)  # Play the sound when the answer is wrong

#Fifth Question           
    song = ["Eve by Lesserafim",]  
    x = random.choice(song)  # Choose a new random song for the next question
    print("__________________________________________________________________________________________________")
    print("\n♥ ੈ✩‧₊˚⋆͛*͛ ͙͛ ⁑͛⋆͛*͛  Congratulation You in Final Level ! ♥ ੈ✩‧₊˚⋆͛*͛ ͙͛ ⁑͛⋆͛*͛ ͙͛")
    sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\06.wav'
    play_sound(sound_path)  # Play the sound for next level
    print("\n♥Question 5")
    guess = None

    while x != guess:
        guess = str(input("\n♥ Genre Pop ~ I'm mess, mess, mess?"))

        if x == guess:
            print("\nYou guessed {}. 고생 많았어 ! Correct! \U0001F601".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\01.wav'
            play_sound(sound_path)  # Play the sound when the answer is correct
            break
        else:
            print("\nYou guessed {}. 아이구 ! Come On! !\U0001F612".format(guess))
            sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\03.wav'
            play_sound(sound_path)  # Play the sound when the answer is wrong

    print("__________________________________________________________________________________________________")
    print("\n♥ ੈ✩‧₊˚⋆͛*͛ ͙͛ ⁑͛⋆͛*͛  Congratulation You WIN!축하해요! ♥ ੈ✩‧₊˚⋆͛*͛ ͙͛ ⁑͛⋆͛*͛ ͙͛")
    sound_path = r'C:\Users\Makerlab\Desktop\TUNG\winsound.PlaySound\05.wav'
    play_sound(sound_path)  # Play the sound if the game FINISH


if __name__ == '__main__':
    main()
