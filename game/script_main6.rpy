label main6:
    jump main6_A

label main6_A:
    
    #*plo6|６月２５日（ＭＯＮ）：日常の賛歌
    #@day nowday='６月２５日（ＭＯＮ）'
    
    play music "sound/bgm/bgm_001.ogg" fadeout 2.0
    
    scene bg bg_b00
    with Fade(1, 0, 1)
    
    "朝はいつも通りの時間に起き、登校の支度をし…………たつもりが、１時間早かった。"
    
    "道理で目覚ましが鳴らんわけだ。"
    
    scene bg bg_b02
    with Fade(1, 0, 1)
    
    "早めにリビングへ行ったが、しとねはもう朝食と弁当の支度を並行して行っていた。"
    
    show sitone si_2_05
    with dissolve
    
    si "「あれ、おはよう。おにいちゃん、今日は早いね」"
    
    "驚いたような顔をしながらも、手を休めずに朝の挨拶。"
    
    so "「おはよう。何でこんなに早く起きたんだろうな？」"
    
    "それは俺自身が一番驚いていることである。"
    
    "普段は目覚ましが鳴らん限り起きないくせに……。"
    
    so "「まぁ、早く起きたといっても、殆どやること無いんだがな……」"
    
    "大きな独り言を呟くと、しとねが一つ提案を寄越す。"
    
    show sitone si_2_01
    
    si "「じゃぁ、折角起きたんだから、一緒にお弁当でも作ってみる？やること無いなら、一緒にやろ？」"
    
    so "「いや、でも殆ど料理なんて出来んぞ？いつもお前に任せっきりなのは、お前が一番知ってるだろうに」"
    
    show sitone si_2_02
    
    si "「うん、だから教えてあげる。一緒に作ってみない？」"
    
    "しとねは心なしか目を輝かせているように見える。"
    
    "ど、どうしようか……"
    
    #*plo6_s|
    
    menu:
        "一緒に作る":
            $ loveSi += 1
            jump sitone4_A # si_6.ks - si_6a
            
        "しとねに任せる":
            jump main6_A_1 # plo6_2

#;---------------しとねに-------------------
label main6_A_1:
    #*plo6_2|
    
    so "「いや、今日は遠慮しておく」"
    
    show sitone si_2_04
    
    si "「今日はって……いつもでしょ？」"
    
    so "「だってさ、俺が作るよりお前が作ったほうが安心じゃないか」"
    
    "正論だ。反論は出来まい。"
    
    show sitone si_2_07
    
    si "「そ、それはそうかもしれないけど……」"
    
    "しとねは少し残念そうにそう呟く。"
    
    so "「かもしれない、じゃなくて確実にそうだな。ということでよろしく頼む。教えてもらうのはまた今度で良いよ」"
    
    si "「うん」"
    
    "少し悪いことをしたなぁとは思いながらも、昼ご飯がまずいのは嫌なのでそのまましとねに任せることにした。"
    
    "そして、しとねが弁当を作り終えるのを待ち、今日は少し早めに学校へ行ってみることにした。"
    
    jump main6_B # plo6_3
    
#;-----------------しとねに任せる終了-----------------
label main6_B:
    #*plo6_3|６月２５日（ＭＯＮ）：日常の賛歌（２）
    
    play music "sound/bgm/bgm_002.ogg" fadeout 2.0
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    show akira aki_1_05
    with dissolve
    
    ak "「…………！！！！？」"
    
    "俺より後に登校してきた明良が、俺を見て絶句する。"
    
    "失礼なヤツだな。"
    
    so "「なぁ、俺はどういうリアクションをとったらいいんだ？」"
    
    "硬直する明良を見かね、問う。"
    
    ak "「今日は熱があるのかはたまた何かの予兆か！？こんなことになるなら、もっと親孝行すべきだった！！！畜生ッ！！」"
    
    so "「あのなぁ、俺だってたまには早く起きることだってあるってんだよ」"
    
    "それをこいつは……"
    
    show akira aki_1_07
    
    ak "「そんなこと言ってもなぁ。中学からの付き合いでこんなこと殆ど無かったろうが」"
    
    so "「ま、まぁそうかもしれんが」"
    
    ak "「嗚呼、祈る他に術なし。万事休す、か」"
    
    so "「…………」"
    
    "明良が目の前で跪き、両手を合わせて天に祈っている。"
    
    "……放っておこう。"
    
    hide akira aki_1_07
    with dissolve
    
    "そこそこ付き合いを重ねてきたクラスメイトも、登校するなり奇異の目を向けてくる。"
    
    "俺は珍獣か何かの気分を初めて味わった。"
    
    "そのうち、みそぎが登校してきた。"
    
    show misogi mi_1_01
    with dissolve
    
    mi "「おはよう、聡介くん」"
    
    "そして、俺の元へ。"
    
    so "「あ、ああ、おはよう」"
    
    mi "「ねぇ、進藤くんどうしたの？」"
    
    "先ほどからずっと祈り続けている明良を見て、みそぎが不思議そうに訊ねる。"
    
    so "「いや、気にするな。後で粗大ごみにでも捨てておく」"
    
    show misogi mi_1_02
    
    mi "「そう？捨てに行くの手伝おうか？」"
    
    so "「！！？」"
    
    "みそぎが微笑しながら、大真面目にそんなことを言う。"
    
    "というか、みそぎがこんな冗談を受け入れるということ自体が意外だ。"
    
    show akira aki_1_09 at left
    show misogi mi_1_02 at right
    with dissolve
    
    ak "「な！？それはないよみそぎちゃーんおはようッ！！」"
    
    "みそぎの言葉を耳にし、固まっていた明良が唐突に覚醒する。"
    
    show misogi mi_1_01 #[tr sto=mi_1_01]
    with dissolve
    
    mi "「……あ、うん、おはよう」"
    
    "挨拶は忘れず、しかし何事も無かったかのように動じないみそぎ。"
    
    "それどころか、追撃まで開始する始末。"
    
    show misogi mi_1_01 #[tr sto=mi_1_02]
    with dissolve
    
    mi "「それで、いつ捨てに行くのかな？」"
    
    "何故だッ！！？笑顔が眩しい！！"
    
    ak "「がっびーん！！」"
    
    "追撃がクリティカルヒットし、その場に崩れ落ちる明良。"
    
    so "「な、なぁ、みそぎ。それくらいにしておいてやれ」"
    
    mi "「うん、聡介くんがそう言うならやめるね」"
    
    "といって、自分の席に戻っていった。"
    
    show akira aki_1_09
    with dissolve
    
    "……なんか、アグレッシブだな、今日のみそぎは。"
    
    "何か意図あってのことなのか、果たして天然なのか。"
    
    "ふと気づくと、教室にいたクラスメイトの半数以上の目がこっちを向いている。"
    
    "明らかに、明良のオーバーアクションの所為だな。いい迷惑だ。"
    
    "……ってか、こいつのテンションもバラつきが激しいよな。"
    
    "こいつらのおかげで、何か俺が損してる気がする。"
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    "その後、クラスメイトとも少し話をしたりしたが、それでも時間は余った。"
    
    "……あまり早くに学校来ても暇だな。"
    
    "しかし、眠気はあまり無いので、とりあえず廊下に出、学校の中をうろついてみることにした。"
    
    scene bg school passage
    with Fade(1, 0, 1)
    
    "とはいっても、特に目的も無い。"
    
    "さぁ、どうしようか。"
    
    #*plo6_s2
    
    menu:
        "生徒玄関へ行く":
            $ loveSi += 1
            jump sitone4_B # si_6.ks - si_6b
            
        "やっぱり教室に戻る":
            $ loveMi += 1
            jump misogi4_A # mi_6.ks - mi_6a
            
        "振り向く":
            $ loveKi += 1
            jump kiriko4_A # ki_6.ks - ki_6a
        
        "グラウンドへ行く":
            $ loveAy += 1
            jump ayame4_A # aya_6.ks - aya_6a
            
#;-------------------------------------------------
label main6_C:

    #*plo6_4|６月２５日（ＭＯＮ）：日常の賛歌（３）
    
    play music "sound/bgm/bgm_001.ogg" fadeout 2.0
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    "朝早く起きたためか、午前中の活動時間がいつもより多くなり、午前の授業が長く感じた。"
    
    so "「ん～っ！！」"
    
    "座ったまま反り返って伸びをする。"
    
    "授業が終わるたびに伸びをしなければ体の疲れがとれた気がしない。"
    
    "クラスメイトは次々に弁当を広げたり、食堂や購買に行ったりする。"
    
    "さて、俺はどうしようかな。"
    
    #*plo6_s3|
    
    $ f_snt = 1
    $ f_ki_t = 0
    $ f_si_t = 0
    $ f_aya_t = 0
    
    if loveKi >= 2:
        $ f_snt += 1
        $ f_ki_t = 1
        
    if loveSi >= 2 and f_sitone_6 == 1:
        $ f_snt += 1
        $ f_si_t = 1
        
    if loveAy >= 2:
        $ f_snt += 1
        $ f_aya_t = 1
    
    if f_snt == 1:
        menu:
            "教室で食べる":
                jump misogi4_B # mi_6.ks - mi_6b
    
    if f_snt == 2:
        jump f_snt2

    if f_snt == 3:
        jump f_snt3

    #f_snt == 4
    menu:
        "教室で食べる":
            jump misogi4_B # mi_6.ks - mi_6b

        "あ、職員室行かなきゃ":
            jump kiriko4_B # ki_6.ks - ki_6b

        "屋上で食べる":
            jump sitone4_C # si_6.ks - si_6c

        "ジュースを買いに行く":
            jump ayame4_B # aya_6.ks - aya_6b
            
#----------------------------------------------------

label f_snt2:
    
    if f_ki_t == 1:
        menu:
            "教室で食べる":
                jump misogi4_B # mi_6.ks - mi_6b

            "あ、職員室行かなきゃ":
                jump kiriko4_B # ki_6.ks - ki_6b

    if f_si_t == 1:
        menu:
            "教室で食べる":
                jump misogi4_B # mi_6.ks - mi_6b

            "屋上で食べる":
                jump sitone4_C # si_6.ks - si_6c

    if f_aya_t == 1:
        menu:
            "教室で食べる":
                jump misogi4_B # mi_6.ks - mi_6b

            "ジュースを買いに行く":
                jump ayame4_B # aya_6.ks - aya_6b

label f_snt3:
    
    if f_ki_t == 1 and f_aya_t == 1:
        menu:
            "教室で食べる":
                jump misogi4_B # mi_6.ks - mi_6b

            "あ、職員室行かなきゃ":
                jump kiriko4_B # ki_6.ks - ki_6b

            "ジュースを買いに行く":
                jump ayame4_B # aya_6.ks - aya_6b
    
    if f_ki_t == 1 and f_si_t == 1:
        menu:
            "教室で食べる":
                jump misogi4_B # mi_6.ks - mi_6b

            "あ、職員室行かなきゃ":
                jump kiriko4_B # ki_6.ks - ki_6b

            "屋上で食べる":
                jump sitone4_C # si_6.ks - si_6c

    if f_aya_t == 1 and f_si_t == 1:
        menu:
            "教室で食べる":
                jump misogi4_B # mi_6.ks - mi_6b

            "ジュースを買いに行く":
                jump ayame4_B # aya_6.ks - aya_6b

            "屋上で食べる":
                jump sitone4_C # si_6.ks - si_6c
