import random
import time
import sys
import os


def start():
    # story generated
    animate_text("Hello, you are in the future and are fighting a robot")
    time.sleep(3)
    animate_text("You don't know what to do, that's why I'm here")
    time.sleep(3)
    animate_text("I am a Simulated Artificial Machine but you can call me S.A.M.")
    smileyface()

def smileyface(color_code='#40E0D0'):
    # Convert hex color code to RGB
    r = int(color_code[1:3], 16)
    g = int(color_code[3:5], 16)
    b = int(color_code[5:], 16)
    # Calculate ANSI escape code for 8-bit color
    ansi_color_code = f'\033[38;2;{r};{g};{b}m'

    time.sleep(0.3)
    print(ansi_color_code + '__________________ ')
    time.sleep(0.3)
    print('|                |')
    time.sleep(0.3)
    print('|  @        @    |')
    time.sleep(0.3)
    print('|       !        |')
    time.sleep(0.3)
    print('|   \_______/    |')
    time.sleep(0.3)
    print('|________________|')
    print('\033[0m')  # Reset color


# def animate_text(text, sleep_duration=0.1):
#     for char in text:
#         print(char, end='', flush=True)
#         time.sleep(sleep_duration)
#     print()

def animate_text(text, sleep_duration=0.1, color_code='#40E0D0'):
    # Convert hex color code to RGB
    r = int(color_code[1:3], 16)
    g = int(color_code[3:5], 16)
    b = int(color_code[5:], 16)
    # Calculate ANSI escape code for 8-bit color
    ansi_color_code = f'\033[38;2;{r};{g};{b}m'

    for char in text:
        print(f'{ansi_color_code}{char}', end='', flush=True)
        time.sleep(sleep_duration)
    print('\033[0m')  # Reset color at the end of the text


def lose_select():
    time.sleep(3)
    animate_text('I have been given an option to show you')
    time.sleep(3)
    animate_text('Someone has injected a new option')
    time.sleep(3)
    animate_text('if you get it right then you can continue')
    time.sleep(3)
    animate_text('if you get it wrong then you will lose again')
    time.sleep(3)

    select_choose = ''
    while select_choose != 'blue pill' and select_choose != 'red pill':
        select_choose = input('What do you choose, the red pill or the blue pill: ')

        if select_choose == 'blue pill':
            animate_text('congrats you chose the correct option!!!')
        elif select_choose == 'red pill':
            animate_text('WRONGGGG !!!!')
            sys.exit()

# First obstacle
def level1():
    question_one = ''
    while question_one != 'run away' and question_one != 'shoot robot in head':
        question_one = input('You can currently do two things which is either run away or shoot robot in head, what do you choose: ')
        
        #if chosen option and outcome of option
        if question_one == 'run away':
            time.sleep(3)
            animate_text('Unfortunately you have now been hunted down by an army of robots and have been executed')    
            time.sleep(3)
            animate_text('too bad')
            
            lose_select()
            level1()
            path()
            again = choice()
            random_select(again)

            # restart for when user fails
            # restart = input('Do you wanna restart: ')
            # if restart == 'yes':
            #     start()
            #     level1()
            #     path()
            #     again = choice()
            #     random_select(again)
            # else:
            #     print('bye')
            #     sys.exit()       
        
        elif question_one == 'shoot robot in head':
            time.sleep(3)
            animate_text('Congratulations you shot the robot in the head and are not dead!!')
            

def path():
    # story generated
    time.sleep(3)
    animate_text('You are running away from the robots but...')
    time.sleep(3)
    animate_text('there is a dangerous path of an army of robots coming your way')
    time.sleep(3)
    animate_text('you have got two paths that you can go down')
    time.sleep(3)
    animate_text('but you have to decide which one is the correct one since one of them is a dead end')
    time.sleep(3)
    animate_text('choose wisely!!!!!!! ')
    print()

# Second obstacle
def choice():
    question_two = ''
    while question_two != '1' and question_two != '2':
        time.sleep(1)
        question_two = input('So which one do you want to go on, path 1 or 2: ')
    return question_two


# random path chosen for user to be right or wrong
def random_select(rightpath):
    select = random.randint(1,2)

    if rightpath == str(select):
        time.sleep(3)
        animate_text('good you went down the correct path and cheated death!!')  
        # level2()
        restart = new_level()
        random_key(restart)


    else:
        time.sleep(3)
        animate_text('oh no you have been spotted by the robots!!!')
        time.sleep(3)
        animate_text('and you have been shot multiple time and are now dead.')
        lose_select()
        path()
        again = choice()
        random_select(again)


def new_level():
        time.sleep(3)
        animate_text('I have given u two keys but a virus has entered my system')
        time.sleep(3)
        animate_text('now I dont know which is the correct key but u have to select it')
        time.sleep(3)
        animate_text('if u choose the correct one then u can continue, but if wrong then you will die... ')

        question_three = ''
        while question_three != '4' and question_three != '5':
            time.sleep(1)
            question_three = input('Choose the correct key: 4 or 5: ')
        return question_three

def random_key(correct_path):
    # option_one = (444)
    # option_two = (555)
    select = random.randint(4, 5)

    if correct_path == str(select):
        time.sleep(3)
        animate_text('good you chose the correct option')
        item ()
        
    else:
        time.sleep(3)
        animate_text('You are now dead')
        time.sleep(3)

        lose_select()
        # path()
        # again = choice()
        # random_select(again)
        
        restart = new_level()
        random_key(restart)

def item ():

        # question_one = ''
    # while question_one != 'run away' and question_one != 'shoot robot in head':
    time.sleep(3)
    animate_text('oh no')
    time.sleep(3)
    animate_text('in my system I have been given a new object')
    time.sleep(3)
    animate_text('do you want to take the object or not')
    time.sleep(3)
    animate_text('Choose Wisely!!!!!')
    object = ''
    while object != 'yes' and object != 'no':
        object = input('yes or no: ')
        if object == 'yes':
            time.sleep(3)
            animate_text('great!!! you have chosen the healing potion which allows you to heal from any attacks')
            level2()
        elif object == 'no':
            time.sleep(3)
            animate_text('oh no')
            time.sleep(3)
            animate_text('you fool, you have missed out on an incredible item known as the healing potion.')
            level2()


def item ():

        # question_one = ''
    # while question_one != 'run away' and question_one != 'shoot robot in head':
    time.sleep(3)
    animate_text('oh no')
    time.sleep(3)
    animate_text('in my system I have been given a new object')
    time.sleep(3)
    animate_text('do you want to take the object or not')
    time.sleep(3)
    animate_text('Choose Wisely!!!!!')
    object = ''
    while object != 'yes' and object != 'no':
        object = input('yes or no: ')
        if object == 'yes':
            time.sleep(3)
            animate_text('great!!! you have chosen the healing potion which allows you to heal from any attacks')
            level2()
        elif object == 'no':
            time.sleep(3)
            animate_text('oh no')
            time.sleep(3)
            animate_text('you fool, you have missed out on an incredible item known as the healing potion.')
            time.sleep(3)
            animate_text('...')
            level2()

def level2():
    time.sleep(3)
    animate_text('You are now running far away from the robots')

    time.sleep(3)
    # print(""" ──────────────────────██
    #             ▄───▄▀█▄▄▄▄
    #             ─ ▄▀─█▄▄
    #             ▄▄▄▀───▀▄
    #             ▀────────▀▀ """)

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_running_man(position):
        clear_screen()
        
        ascii_art = """ ──────────────────────────██
                    ▄───▄▀█▄▄▄▄
                    ─ ▄▀─█▄▄
                    ▄▄▄▀───▀▄
                    ▀────────▀▀ """

        for line in ascii_art.split('\n'):
            print(" " * position + line)

    def run_animation(iterations):
        position = 0
        for _ in range(iterations):
            draw_running_man(position)
            time.sleep(0.05)  # Adjust the sleep time to control the animation speed
            position += 1
            if position >= 40:  # Adjust the maximum position based on your console width
                position = 0

    if __name__ == "__main__":
        # Specify the number of iterations
        num_iterations = 40  # Change this to the desired number
        run_animation(num_iterations)



    time.sleep(3)
    animate_text('and all of a sudden you see a cyborg in the distance')
    time.sleep(2)
    print("""   _______                   ________    |
    |ooooooo|      ____       | __  __ |   |
    |[]+++[]|     [____]      |/  \/  \|   |
    |+ ___ +|     ]()()[      |\__/\__/|   |
    |:|   |:|   ___\__/___    |[][][][]|   |
    |:|___|:|  |__|    |__|   |++++++++|   |
    |[]===[]|   |_|_/\_|_|    | ______ |   |
    _ ||||||||| _ | | __ | | __ ||______|| __|
    |_______|   |_|[::]|_|    |________|   \
                \_|_||_|_/                  \
                    |_||_|                     \
                _|_||_|_                     \
        ____    |___||___|                     \
    """)
    time.sleep(3)
    animate_text('he has been sent to capture you and take you back to the robots!!!')

    time.sleep(3)
    animate_text('three items are infront of you ')

    time.sleep(3)
    animate_text("a mech suit")
    time.sleep(2)
    print("""           ___
          |_|_|
          |_|_|              _____
          |_|_|     ____    |*_*_*|
 _______   _\__\___/ __ \____|_|_   _______
/ ____  |=|      \  <_+>  /      |=|  ____ \
~|    |\|=|======\\______//======|=|/|    |~
 |_   |    \      |      |      /    |    |
  \==-|     \     |  2D  |     /     |----|~~/
  |   |      |    |      |    |      |____/~/
  |   |       \____\____/____/      /    / /
  |   |         {----------}       /____/ /
  |___|        /~~~~~~~~~~~~\     |_/~|_|/
   \_/        |/~~~~~||~~~~~\|     /__|\
   | |         |    ||||    |     (/|| \)
   | |        /     |  |     \       \\
   |_|        |     |  |     |
              |_____|  |_____|
              (_____)  (_____)
              |     |  |     |
              |     |  |     |
              |/~~~\|  |/~~~\|
              /|___|\  /|___|\
             <_______><_______>
""")

    time.sleep(3)
    animate_text("tank")
    time.sleep(2)
    print("""░░░░░░███████ ]▄▄▄▄▄▄▄▄
    ▂▄▅█████████▅▄▃▂
    I███████████████████].
    ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤...
    """)

    time.sleep(3)
    animate_text('bomb')

    time.sleep(2)
    print("""             . . .                         
              \|/                          
            `--+--'                        
              /|\                          
             ' | '                         
               |                           
               |                           
           ,--'#`--.                       
           |#######|                       
        _.-'#######`-._                    
     ,-'###############`-.                 
   ,'#####################`,               
  /#########################\              
 |###########################|             
|#############################|            
|#############################|            
|#############################|            
|#############################|            
 |###########################|             
  \#########################/              
   `.#####################,'               
     `._###############_,'                 
        `--..#####..--'
    """)
#     question_one = ''
    # while question_one != 'run away' and question_one != 'shoot robot in head':
    items = ''
    while items != 'tank' and items != 'bomb' and items != 'mech suit':
        items = input("which item do you choose - the mech suit, tank or bomb : ")

        if (items == 'tank'):
            time.sleep(3)
            animate_text('oh no the cyborg has ripped through the tank')
            time.sleep(3)
            animate_text('you are running away to find safety')
            time.sleep(3)
            animate_text('but the cyborg has seen you and captured you')
            lose_select()
            level2()

        elif (items == 'bomb'):
            time.sleep(3)
            animate_text('you throw the bomb and it exlodes')
            time.sleep(3)
            animate_text('but it doesnt even lay a scratch on him')
            time.sleep(3)
            animate_text('because he is made from vibranium')
            time.sleep(3)
            animate_text('you are instantly captured now')
            lose_select()
            level2()

        elif (items == "mech suit"):
            time.sleep(3)
            animate_text('you are now in the mech suit')
            time.sleep(3)
            animate_text('the cyborg is running towards you')
            time.sleep(3)
            animate_text('this suit is highly advanced and gives you a ton of diffrent options')
            suit_options()
#     question_one = ''
    # while question_one != 'run away' and question_one != 'shoot robot in head':
def combat_option():
    combat_moves = ''
    while combat_moves != 'right hook' and combat_moves != 'head butt':
        time.sleep(3)
        combat_moves = input("do you want to throw a right hook or head butt: ")
        if (combat_moves == 'right hook'):
            time.sleep(3)
            animate_text('wow your right hook to the cyborg was so DEVASTATING that it has killed him')
            level3()
        elif (combat_moves == 'head butt'):
            time.sleep(3)
            animate_text('incredible your head butt has KNOCKED OUT the cyborg')
            level3()

def suit_options():
        time.sleep(3)
        select_option = ''
        while select_option != 'rocket fist' and select_option != 'missile' and select_option != 'body slam':
            select_option = input("what would you like to use: rocket fist, missile, body slam: ")

            if (select_option == "rocket fist"):
                time.sleep(3)
                animate_text('good the cyborg is extremely disorientated')
                combat_option()
                # def combat_option():
                #     combat_moves = ''
                #     while combat_moves != 'right hook' and combat_moves != 'head butt':
                #         time.sleep(3)
                #         combat_moves = input("do you want to throw a right hook or head butt: ")
                #         if (combat_moves == 'right hook'):
                #             time.sleep(3)
                #             print('wow your right hook to the cyborg was so DEVASTATING that it has killed him')
                #             level3()
                #         elif (combat_moves == 'head butt'):
                #             time.sleep(3)
                #             print('incredible your head butt has KNOCKED OUT the cyborg')
                #             level3()

            elif (select_option == 'missile'):
                time.sleep(3)
                animate_text('oh no the cyborg is made from vibranium')
                time.sleep(3)
                animate_text('the cyborg punches you and takes you back to the robots')
                
                lose_select()
                suit_options()
                # level2()

            elif (select_option == 'body slam'):
                time.sleep(3)
                animate_text('the cyborg has been knocked unconsious good job')
                time.sleep(3)
                animate_text('u have enough time to run')
                level3()

def level3():
    time.sleep(3)
    animate_text('after that battle you are completely drained and are trying to find safety')
    time.sleep(3)
    animate_text('after walking for hours you come across a strange looking object')
    time.sleep(3)
    animate_text('the strange looking object looks like a computer from the past')
    time.sleep(4)
    print("""
▐▓█▀▀▀▀▀▀▀▀▀█▓▌░▄▄▄▄▄░
▐▓█░░▀░░▀▄░░█▓▌░█▄▄▄█░
▐▓█░░▄░░▄▀░░█▓▌░█▄▄▄█░
▐▓█▄▄▄▄▄▄▄▄▄█▓▌░█████░
░░░░▄▄███▄▄░░░░░█████░
    """)
    time.sleep(3)
    animate_text('there is a video recording on it')
#     question_one = ''
    # while question_one != 'run away' and question_one != 'shoot robot in head':
    message = ''
    while message != 'yes' and message != 'no':
        message = input('Do you want to play the recording: ')
        if message == 'yes':
            time.sleep(2)
            print('...')
            time.sleep(2)
            print('..')
            time.sleep(2)
            print('.')
            time.sleep(3)
            animate_text('Computer: We have found a way to end the war')
            time.sleep(3)
            print('We have ...')
            time.sleep(5)
            animate_text("Computer: We have created an algorithm which can search and terminate all AI organisms")
            time.sleep(2)
            animate_text('Computer: OH NO')
            time.sleep(3)
            animate_text('Computer: the machines have invaded our base')
            time.sleep(3)
            print("/@)|¬!}{")
            algorithm()
        
        elif message == 'no':
            time.sleep(3)
            animate_text('incorrect option')
            time.sleep(3)
            animate_text('eventually ...')
            time.sleep(3)
            animate_text('you die')
            lose_select()
            level3()
            # suit_options()


def algorithm():
            time.sleep(3)
            initiate = ''
            while initiate != 'start' and initiate != 'terminate':
                initiate = input('If you wish to initiate this algorithm please type start or if you wish to terminate the algorithm please type terminate: ')
                if (initiate == 'start'):
                    time.sleep(3)
                    print('....')
                    time.sleep(3)
                    print('beep')
                    time.sleep(3)
                    print('boop')
                    time.sleep(3)
                    print('boop')
                    time.sleep(3)
                    print('beep')
                    time.sleep(3)
                    animate_text('Congratulations you have sucessfully killed all of the robots in this timeline !!!!!!')
                    print("""
 '\|/'                                  *
-- * -----
  /|\      ____
 ' | '    {_   o^>       *
   :        -_  /)
   :         (   (        .-''`'.
   .          \   \      /       \
   .           \    \   /         \
                \    `-'           `'.
                 \    . '        /    `.
                  \  ( \  )     (     .')
   ,,   t          '. |  /       |     (
  '|``_/^\___        '|  |`'-..-'|   ( ()
_~~|~/_|_|__/|~~~~~~~ |  / ~~~~~ |   | ~~~~~~~~
 -_  |L[|]L|/         | |\       )   )
                      ( |(       /  /|
   ~~ ~  ~ ~~~~       | /\\     / /| |
                      ||  \\  _/ / | |
             ~ ~ ~~~ _|| (_/ (___)_| |
                    (__)         (____)
""")
                elif (initiate == 'terminate'):
                    time.sleep(3)
                    animate_text('WTF !!!!')

                    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣄⠀⣠⠤⡄⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⣤⣭⣋⠉⠙⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⢷⡵⠋⠙⣠⡧⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡺⣍⡈⠙⠢⣄⠈⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠖⠉⠀⡠⠞⠉⢁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠙⢦⡀⠀⢱⡀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣯⠏⢀⡴⠋⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡻⠧⣄⣱⡀⠀⢣⡸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⢠⠎⠀⠀⣴⣿⠿⢿⢻⣿⡟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠈⠁⠀⠀⠑⠿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⡴⠋⠀⣀⠼⠋⠁⢀⣬⣾⡿⣇⠀⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠳⡄⠀⠀⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠞⠁⠀⢠⣴⣿⣿⠟⠀⠈⢰⣦⣄⣀⣀⢿⠟⡟⢿⣟⣇⣈⣽⢹⣿⣿⣿⡇⠿⡄⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠃⠀⢀⠆⠉⣩⢽⠛⠣⣟⢤⣧⠜⢛⣽⣟⣭⢀⢹⣿⣿⡇⠓⣇⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⡇⠀⠀⠊⠀⠸⢛⣻⣟⠆⣸⠆⠸⣌⠫⣟⣛⠛⠸⢸⣿⡿⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⢀⡰⠋⠀⠀⠀⠀⠀⠀⢀⡎⢹⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⣀⡠⢆⡀⠀⠀⢨⢦⡀⠀⠀⠀⢸⣿⠇⠀⠀⠀⠱⣄⡀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠈⣿⠉⠙⣧⠀⠀⠀⠀⠀⠀⠁⢀⡴⠗⠀⠀⠘⣦⡅⠀⠀⠀⢸⣻⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⡾⣫⡟⠀⠀⠀⠀⠀⠀⢀⡠⠖⠋⠀⠀⠀⠸⡎⠲⠇⠀⠀⠀⠀⠀⠀⠀⠛⠓⠚⠳⠴⠛⠚⣇⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠙⠄⠀⠀⡄⠀
                ⠀⠀⠘⠀⢸⠏⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⢻⣤⣠⡄⠀⠀⠀⠀⠀⠀⣴⠃⣠⣤⣤⣄⡀⠙⠆⠀⠀⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⣀⣀⣀⣤⣤⣤⡤⠴⠒⠀⠀⠀
                ⠤⠀⠀⠀⢸⡀⠀⠀⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⠟⡇⠀⠀⠀⠀⠀⠀⠁⠺⣗⡒⠓⣚⡇⠀⠀⠀⡼⠙⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱
                ⠀⠀⠀⠀⠀⠉⠑⠲⠶⢶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢤⡞⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⢉⣉⠁⠀⠀⢀⣼⠁⠀⠈⠳⣄⢀⡴⠚⠲⢄⡀⢀⣀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⢄⣀⡤⠶⠤⣴⠒⠒⠒⠋⠁⣼⠁⠀⠙⠦⣀⠀⠀⠀⠀⠀⠚⠉⠈⠙⠂⢀⠞⢹⠀⠀⠀⠀⡼⠉⠀⠀⠀⠀⠈⠉⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⢹⡄⠀⠀⠀⠈⠻⡗⠦⠤⢄⣀⣀⣀⣀⠔⠉⢀⡼⢦⡀⠀⣰⠁⠀⠀⠀⠀⠸⡀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⢱⡀⠀⠀⠀⡀⣀⣀⣠⠴⢋⠇⠀⠙⠲⠧⣤⠀⠀⠀⠀⠀⢣⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢤⣀⣸⡉⠉⠉⠉⠉⠉⠉⠀⠀⡼⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")




# option to play again at completion of game
play_again = "yes"

while play_again == "yes" or play_again == "y":
    start()
    level1()
    path()
    again = choice()
    random_select(again)
    
    # restart = new_level()
    # random_key(restart)


    time.sleep(1)

    play_again = input("""Do you want to play again? 
    Type yes or y to play again and no or n if you want to stop: """)

stop_game = "no"
while stop_game == "no" or stop_game == "n":
        animate_text('bye')
        break
