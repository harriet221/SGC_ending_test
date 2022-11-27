import enum


class Sounds(enum.Enum):
    bird = "resource/sound/summer-by-lake-bird-chirping-01.mp3"


class Images(enum.Enum):
    background = 'resource/image/background.jpg'
    logo = 'resource/image/logo-silver.png'
    key_left = 'resource/image/arrowkey_left.png'
    key_right = 'resource/image/arrowkey_right.png'

    # chess
    black_knight = 'resource/image/chess_black_knight.png'
    white_king = 'resource/image/chess_white_king.png'
    # green
    bat = 'resource/image/green_bat.png'
    lizard = 'resource/image/green_lizard.png'
    # pirate
    pirate_ship = 'resource/image/pirate_ship.png'
    kraken = 'resource/image/pirate_kraken.png'
    # card
    card_jack = 'resource/image/card_jack.png'
    card_queen = 'resource/image/card_queen.png'
    # desert
    snake = 'resource/image/desert_snake.png'
    desert_scolpion = 'resource/image/desert_scolpion.png'

    # weapon
    bullets_256 = 'resource/image/bullets_256px.png'
    missile_256 = 'resource/image/missile_256px.png'
    missile2_256 = 'resource/image/missile2_256px.png'
    bomb_256 = 'resource/image/bomb_256px.png'


class Content(enum.Enum):
    # caption
    main = 'Next Dimension'

    # button name
    signin_btn = 'Sign in'
    signup_btn = 'Sign up'
    quit_btn = 'Quit'
    start_btn = 'Game Start'
    rank_btn = 'Rank'
    store_btn = "Store"
    help_btn = 'Help'
    about_btn = 'About'
    sound_btn = "Sound"
    back_btn = 'Back'
    submit_btn = 'Submit'
    reset_btn = "Reset Password"
    buyitem_btn = "Buy Item"
    applyitem_btn = "Apply Item in Game"
    givecoin_btn = "Give Coin as a gift"
    buy_btn = "Buy"
    apply_btn = 'Apply'

    # help page
    help_title = 'Story & Game Rule'
    story = 'In 2300 AD, you can no longer live on Earth\n'\
        'and received a mission to find a new dimension for live.\n'\
        'Now you must find a new dimension\nwhile avoiding enemy attacks.\n'\
        'Good Luck!\n'
    rule = 'Use left and right arrow key to move your character'
    ruletable_row1 = '  Press left key to go left'
    ruletable_row2 = '  Press right key to go right'
    hp = 'Enemies have different HPs'
    hptable_row1 = '  Attack 1 time to kill'
    hptable_row2 = '  Attack 2 time to kill'

    # about page
    about_title = 'License & Source'
    basecode1 = 'Kill-Console/PythonShootGame(The GPL License)'
    basecode2 = 'CSID-DGU/2021-2-OSSProj-PlusAlpha-9(The MIT License)'
    imagesource = 'pixabay'
    soundesource = 'soundeffectplus'
    creators = '\nCreated by\n'\
        'Dongguk University OSSProj\n'\
        'Seojeong Yun, Gaeun Lee, Seyeon Park'
    github = 'Click here to go to our github link'

    # sign in or up page
    pwref = '* Please set the password to at least 8 digits'
    signupmsg = 'Successfully signed up!'
    signup = 'Success'
    errormsg = 'Check your email or password again'
    error = 'Error'
    resetmsg = 'Please reset your password via email'
    reset = 'Reset'
    default_email = 'seyeon0627@gmail.com'

    # store page
    store_title = 'Store'
    category1 = 'Weapons'
    applied_item = "Current Applied item"
    coin = "You Current coin"
    item_category = 'Weapons'
    gift_info = "Enter the email of the friend you want to give"
    giveok_msg = '선물이 완료되었습니다'
    giveok_msgtitle = 'Give Coin'
    have_msg = '이미 구매한 아이템입니다.'
    have_msgtitle = 'Already have'

    # game end page
    end = 'Game End'

    # none
    none = ''


class Item(enum.Enum):
    coin_10k = 10000
    coin_50k = 50000
    coin_100k = 100000
    coin_500k = 500000


class Url(enum.Enum):
    basecode1 = 'https://github.com/Kill-Console/PythonShootGame'
    basecode2 = 'https://github.com/CSID-DGU/2021-2-OSSProj-PlusAlpha-9'
    pixabay = 'https://pixabay.com/ko/'
    soundeffectplus = 'https://www.soundeffectsplus.com/'
    ourgithub = 'https://github.com/CSID-DGU/2022-2-OSSProj-SGC-3'


class Color(enum.Enum):
    black = 'black'
    white = 'white'


class Display(enum.Enum):
    w_init = 1/3
    h_init = 8/9
    angle = 0

    # scale
    small_scale = (0.1, 0.1)
    medium_scale = (0.4, 0.4)
    large_scale = (1, 1)

    # padding
    padding_large = (50, 0, 50, 0)  # content title
    padding_small = (3, 1, 3, 1)  # content table

    # fontsize
    title_fontsize = 35
    description_fontsize = 20
    reference_fontsize = 16

    # margin
    large_margin = 100
    small_margin = 30


class Speed(enum.Enum):
    bg = 4
    zero = 0
    bullet = 10
    player = 8
    enemy1 = 2
    enemy2 = 1.7
    coin = 10
    blind = 5
    bomb = 20
    mode = 3
    meteor = 20


class Utilization(enum.Enum):
    x = 0
    y = 1


class Resize(enum.Enum):
    display = 500
    standard = 10
    shoot = 1
    enemy1 = 9
    enemy2 = 10
    # resizable에 따른 변화
    #  0  500 1000 1500 2000 이상
    #  8   9   10   11   12  플레이어 속도
    # 10   9    8    7    6  총알 발사 빈도
    # 90   81  72   63   54  적1 출현 빈도
    # 100  90  80   70   60  적2 출현 빈도


class Game(enum.Enum):
    d_weight = 3000
    d_height = 10000
    p_margin = 20
    dim = 40


class Plane(enum.Enum):
    p1 = 0, 99, 102, 126
    p2 = 165, 360, 102, 126
    p3 = 165, 234, 102, 126
    p4 = 330, 624, 102, 126
    p5 = 330, 498, 102, 126
    p6 = 432, 624, 102, 126
    bullet = 1004, 987, 9, 21
    e1 = 534, 612, 57, 43
    e2 = 267, 347, 57, 43


class Divide(enum.Enum):
    player = 16
    player_d = 8
    player_i = 47
    coin = 240
    coin_i = 40
    star_r = 70
    star = 210
    star_i = 30


class Font(enum.Enum):
    size = 36
    location = 128, 128, 128
    rect = 10, 10
