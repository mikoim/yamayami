label main5:
    jump main5_A

label main5_A:
    
    #*plo5|６月２０日（ＷＥＤ）：雨って憂鬱
    #@day nowday='６月２０日（ＷＥＤ）'
    
    play music "sound/bgm/bgm_002.ogg" fadeout 2.0
    
    scene bg bg_b02
    with Fade(1, 0, 1)
    
    so "「ふぁ、～あ、眠い……」"
    
    "昨晩も例によって宿題があったことを忘れ、夜になってから取り掛かった。"
    
    "とりあえず宿題は終わらせたものの、寝たのは昨晩深夜だ。"
    
    "毎日それなりに規則正しい生活をしている俺にとっては遅い時間の就寝だった。"
    
    "ああ、またもやこんな失態を犯してしまうとは、情けないことこの上ない。"
    
    "とは言っても、そんな生活が変わるわけでもなく。"
    
    show sitone si_2_07
    
    si "「何してたの、あんな時間まで？」"
    
    "しとねが、食卓に朝食を並べながら訊いてくる。"
    
    "お、今日も美味そうなご飯だな。"
    
    so "「え、ああ。昨日は日中遊んでたからさ、宿題あったの忘れててな、夜のうちにやっておこうと思って」"
    
    si "「もー。遊ぶ前にちゃんとしなきゃダメだよ？」"
    
    so "「……いただきます」"
    
    show sitone si_2_04
    
    si "「あー！　話はぐらかしちゃダメでしょー！？」"
    
    "俺は箸を手に取り、朝食を摂る。"
    
    "テレビ画面が天気予報に変わった。今は晴れているが、午後からまた降るらしい。"
    
    "７月に入っても、梅雨前線はまだ居座り続けるつもりだそうだ。"
    
    "雨は嫌いじゃないし、むしろ好きなくらいだが、こう毎日続くと気が滅入る。と言うよりは登下校時に濡れるのが嫌だ。"
    
    so "「あ～、もう鬱陶しいよなぁ。そろそろ夏になれば良いのになぁ」"
    
    show sitone si_2_01
    
    si "「だよねぇ。傘持って行くのも邪魔だし」"
    
    "本当に降るんだろうか。こんだけ晴れてんのに。"
    
    so "「お、今日の卵焼きは甘いやつだな」"
    
    show sitone si_2_10
    
    si "「うん！甘いほうが元気出るかと思って。美味しい？」"
    
    "しとねは、心なしか目を輝かせて尋ねてきた。"
    
    so "「ああ、流石しとねだな。おにいちゃんうれピー！」"
    
    "たまにはユーモアも織り交ぜておどけてみる。"
    
    show sitone si_2_02
    
    si "「ぷ、あははは！！おにいちゃん、その顔おかしいっ！あはははっ！」"
    
    so "「ちょ、笑いすぎだろそれはっ！！」"
    
    "そのような会話がしばらく続き、日常の朝が過ぎていく。ああ、平和だな。"
    
    scene bg bg_b02
    with Fade(1, 0, 1)
    
    show sitone si_2_01
    
    si "「それじゃ、先行くねっ！」"
    
    "支度を終えたしとねが玄関から声を上げる。"
    
    so "「おう、気をつけてな～」"
    
    "洗面所から顔を覗かせ、俺はしとねを見送る。"
    
    show sitone si_2_02
    
    si "「うん、行ってきます！」"
    
    "しとねは元気良く家を飛び出していった。"
    
    hide sitone
    
    so "「さぁ、俺もそろそろ行くかな」"
    
    scene bg bg_b07
    with Fade(1, 0, 1)
    
    "歯を磨き、寝癖を直して準備は万端だ。"
    
    "一度、うんっと伸びをする。"
    
    so "「う、やっぱり何か疲れてんな……ふぁ、あ～ぁ」"
    
    "玄関に置いてある傘を取り、ドアノブに手をかける。"
    
    scene bg bg_e00
    with Fade(1, 0, 1)
    
    "家を出て数分、先ほどまで晴れていた空が曇り始める。"
    
    so "「ああ、こりゃ本当に降るのか」"
    
    "曇天を見上げ、ため息を一つ吐く。"
    
    so "「まったく、昼からって言ってたのになぁ」"
    
    "ぼそぼそと独り言を呟きながら、曲がり角に差し掛かる。"
    
    "そこで、ふと思い出した。"
    
    so "「あ、もしかして、  昨日時間割合わせてないんじゃ……！？」"
    
    "時計を確認すると、確かにまだ時間はある。取りに帰れる時間だが、ちょっと厳しい。"
    
    "う～ん、どうするかなぁ……。"
    
    menu:
        "急いで取りに帰る":
            $ loveMi += 1
            jump misogi3_A # mi_5.ks - mi_5a
            
        "このまま学校へ向かう":
            jump main5_A_1
            
label main5_A_1:
    
    "このまま学校へ向かおう。教科書くらい誰か見せてくれるだろう。"
    
    "幸い、宿題だけは入っているようだ。"
    
    jump main5_B
    
label main5_B:
    
    #*plo5_2a|６月２０日（ＷＥＤ）：雨って憂鬱（２）
    
    play music "sound/bgm/bgm_001.ogg"
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    show akira aki_1_01
    
    ak "「おう、今日は早いじゃないか」"
    
    "自分の席へつくと、その隣に明良が近づいてきて、腰を下ろす。"
    
    so "「そうか？　そんなに変わらんと思うが」"
    
    ak "「そういえばそうだな。そんなに変わらねぇ」"
    
    "……いつもながら適当なやつだ。むしろ遅い位だと思うが。"
    
    show akira aki_1_02
    
    ak "「お、そういえばあれだな！もうちょっとで祭だな！！浴衣の幼女、美少女、美女！！！色気溢れる艶姿を拝める年に一度のお祭だぁッ！！」"
    
    "適当なことを言ったかと思うと、次には何か叫びだす。"
    
    "……疲れるヤツだな。"
    
    so "「お前、朝からテンション高いな。っていうか、幼女まで守備範囲なのかお前は……」"
    
    ak "「そりゃぁこの明良お兄さんにかかれば幼女から熟女までイチコロよ！！あ、熟女は勘弁かな」"
    
    so "「……節操ないな」"
    
    "俺が呆れてため息を吐くと、更に明良は突っかかってくる。"
    
    show akira aki_1_04
    
    ak "「お前なぁ、最近何かと女の子と一緒にいるのを見かけ　るが、いい気になってんじゃねぇぞ！！？　節操無い　のはお前の方だろうが！　羨ましいヤツめ！！」"
    
    so "「な！？　別にそんなことねぇだろ」"
    
    ak "「いいや！　傍から見るとそんな風に見えるんだよ！！　何で帰宅部で出会いの少なそうなお前がモテてこのハ　ンサムな俺様がモテないんだよぉぉぉ！！！」"
    
    "うぉぉぉぉ！！　と獣が泣き叫ぶような声で悔しがる明良。朝からうるさい。"
    
    "と言うか、それよりそんなに俺は傍からそう見えるんだろうか。"
    
    "……まぁ、みそぎ関係の出来事では散々言われたのは記憶に新しいが。"
    
    so "「うるさいからやめろ！　他に迷惑だろうが」"
    
    "明良は徐に立ち上がり、沈んだ表情で再び口を開く。"
    
    show akira aki_1_07
    
    ak "「……で、俺の何がいけないんだろうな」"
    
    so "「そういうところが、だろ」"
    
    "今に解ったことじゃないが、こういうところがダメなんだろう。"
    
    "黙っていれば二枚目の、ウケの良さそうな面持ちだが、口を開けばすぐに本性を表す。"
    
    "言動の内容が下品だったり、異様なテンションでまくし立てるみたいに喋ったり、その他諸々。"
    
    "敗因は、人前だろうが何だろうが、所構わずそういうことを言うからだな。"
    
    "そして、致命的なのは全く自覚症状が無いところだ。"
    
    ak "「もうちょっと解りやすく説明してくれよぉ」"
    
    "そこへ、本来その席に着くはずの女子が登校してきた。"
    
    "女子生徒Ａ" "「あの、進藤君、そこ私の席なんだけど」"
    
    show akira aki_1_02
    
    ak "「ああ、悪い悪い。さ、お嬢様、お座りになってくださいまし」"
    
    "と、本人はエスコートしたつもりなのだろうが、案の定──"
    
    "女子生徒Ａ" "「……ちょっと、そういうの気持ち悪いからやめてくれない！？」"
    
    show akira aki_1_09
    
    play sound "sound/se/se_110.ogg"
    
    ak "「……Σガーン！！」"
    
    "嫌悪の情を露骨に示されて撃沈。"
    
    hide akira
    
    "そして明良は、そのまま自分の席に戻っていった。"
    
    "背中が煤けて見えるぜ……。"
    
    play music "sound/bgm/bgm_001.ogg" fadeout 1.0
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    "午前の授業が終わり、昼飯を早々に終えたが、特にすることが無いことに気づく。"
    
    "時間は十分にある。"
    
    "天気予報で言っていたような雨の降る気配はまだ無い。"
    
    "さぁて、どうしたものか。"
    
    menu:
        "図書館へ行く":
            $ loveAy += 1
            jump ayame3_A # aya_5.ks - aya_5a
        
        "屋上へ行く":
            $ loveKi += 1
            jump kiriko3_A # ki_5.ks - ki_5a
        
        "みそぎに話しかける":
            $ loveMi += 1
            jump misogi3_B # mi_5.ks - mi_5b
        
        "教室で寝る":
            jump main5_B_1

label main5_B_1:
    
    "と、いろいろ思考をめぐらせてみたものの、特に思いつかず、午前の疲れが出てきた。"
    
    "よし、こんなときは寝るに限る。"
    
    "そして俺は机の上に腕を組み、それを枕として首を横たえ、眠りに落ちた。"
    
    jump main5_C
    
label main5_C:
    
    #*plo5_4|６月２０日（ＷＥＤ）：雨って憂鬱（３）
    
    play music "sound/bgm/bgm_003.ogg"
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    "さて、午後の授業だ。えーっと、次は……？"
    
    "「おいおまいら。席に着いてください。授業をはじめますよ」"
    
    "……そうだ、英語だった。このやたら流暢ながら、何かが致命的に偏っている日本語。間違いなく、英語のトミー先生だ。"
    
    "トミー" "「ではまず宿題age」"
    
    "男子生徒" "「ageんなsageろ」"
    
    "トミー" "「宿題sage」"
    
    "男子生徒" "「sageればもらえると思っている香具師はDQN」"
    
    "……いやお前等、遊びすぎだから。気持ちはわかるけど。"
    
    "十島佳織" "「イタい教師と生徒がいるクラスはここですか？」"
    
    #[wait time=1000]
    
    "……いま、なにか、見てはいけないものを見てしまったような気が……。"
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    "トミー" "「では、ここで問題でつ」"
    
    "トミー" "「次のうち英語では『cat』が含まれることわざを答えなさい。間違えたら何かがボッシュート」"
    
    "トミー" "「では……目が猫っぽいミスタ雨宮」"
    
    "……俺かよ。てか前にも似たような理由で当たったな。えっと……"
    
    menu:
        "「言うは易く行うは難し」":
            jump main5_C_1
            
        "「転がる石にコケはつかない」":
            jump main5_C_2
            
        "「時は金なり」":
            jump main5_C_2
    
label main5_C_1:
    
    "トミー" "「グッジョブ！『who shall tie the bell around the cat's neck～』……イソップ童話ですね」"
    
    "ふぅ、正解したか……。"
    
    "トミー" "「では次はリスニングの授業ですね。視聴覚室でミクミクにしてやんよ！！」"
    
    "……あ、買ったんだ……。どこぞの休載漫画家のごとく……。"
    
    jump main5_D
    
label main5_C_2:
    
    "トミー" "「残念、ユーの家だけネコ娘が第三期～」"
    
    so "「うわあああああああああ」"
    
    ak "「アニオタ必死だな」"
    
    so "「って俺は別に観てねぇ！！」"
    
    "トミー" "「はいはい、では静かに。正座して再放送を待ちましょ  う」"
    
    so "「ちーーーがーーーうーーーーー！！！」"
    
    jump main5_D
    
label main5_D:
    
    play music "sound/bgm/bgm_001.ogg"
    
    scene bg school classroom
    with Fade(1, 0, 1)
    
    "午後の授業も終え、部活もしていない俺はもはやここに用はない。"
    
    "さて、帰るかな。"
    
    "と思ったところへ、明良が話しかけてきた。"
    
    show akira aki_1_01
    
    ak "「なぁ、これからどっか行かねぇか？」"
    
    so "「え、いや、どうしようか」"
    
    "午後から急に降り出した雨は、未だ止む気配も無い。"
    
    "……何が悲しくてこんな日にこいつと二人で遊ばねばならんのか、とも考えたが、断る理由が無いと言えば無い。"
    
    "どうしようか。"
    
    menu:
        "明良に付き合う":
            jump main5_D_1
            
        "やめておく":
            jump main5_D_2

label main5_D_1:
    
    so "「そうだな、別に予定もないし、たまにはいいな」"
    
    "俺は明良の提案を受け入れ、こいつについて行くことにした。"
    
    show akira aki_1_02
    
    ak "「そうかそうか！　いやー、お前と友達でよかったわ」"
    
    "俺の肩に腕を回し、ぽんぽん、と叩く。"
    
    so "「やめろ。こんなじめじめした季節に暑苦しいことするんじゃねぇ」"
    
    show akira aki_1_07
    
    ak "「……ああ。俺もやって後悔した。男なんかと密着するんじゃなかったぜ」"
    
    "そういって、即座に俺から離れる。"
    
    "……もうちょっと先に気づいてくれ、気持ち悪い。"
    
    show akira aki_1_01
    
    ak "「じゃぁ、とりあえず街の方へ行こうぜ」"
    
    "帰り支度を済ませ、俺たちは街を目指して歩いた。"
    
    play music "sound/bgm/bgm_101.ogg" fadeout 1.0
    
    scene bg bg_c05
    with Fade(1, 0, 1)
    
    show akira aki_1_01
    
    ak "「……さぁ、これからどうするか」"
    
    so "「はぁ！？お前目的もなしに来たのかよ！！」"
    
    "街に来たは良いものの、そこで明良が目的がないことを暴露する。"
    
    "正直、呆れたやつだ。"
    
    show akira aki_1_05
    
    ak "「な！？心外だな。俺はさっき『どっか行かねぇか？』って言ったんだぜ？そりゃ目的なんか決まってねぇよ。暇潰しだ暇潰し！」"
    
    "こ、こいつ……。こんなことなら帰ったほうがよかったかもしれないな。"
    
    ak "「で、どうする？」"
    
    so "「どうする？って言われてもなぁ……」"
    
    "そりゃ俺はこいつについてきただけだし、目的は特にない。"
    
    show akira aki_1_01
    
    ak "「じゃぁこうしようぜ！じゃんけんで、俺が勝ったら  本屋、お前が勝ったらゲーセンだな」"
    
    "なんと言う二択か。選択肢がそれしかないこいつの頭は終わってるな。"
    
    so "「ああ、まぁそれで良いや。じゃぁ行くぞ、最初はグー、ジャンケン……」"
    
    menu:
        "グー":
            $ loveAy += 1
            jump ayame3_B # aya_5.ks - aya_5b
        
        "パー":
            $ loveSi += 1
            jump sitone3_A # si_5.ks - si_5

label main5_D_2:
    
    so "「いや、今日はやめておく。雨もまぁまぁ降ってるしな」"
    
    show akira aki_1_07
    
    ak "「人付き合い悪いなー。友達減るぞ？」"
    
    so "「余計な世話だ。こんな日にお前と二人で外出歩いて何　が楽しいんだよ」"
    
    "遠まわしに理由をつけて断ろうとも思ったが、明良の言動がちょっと癪だったので、本音を言うことにした。"
    
    show akira aki_1_05
    
    ak "「うをっ！？すっぱり言ったな……」"
    
    so "「まぁ、また今度な。今日はそんな気分じゃない」"
    
    "明良とつるむことなんて多々あることだ。今日ぐらい断っても今後幾度となくあることだろうし、罰は当たるまい。"
    
    show akira aki_1_07
    
    ak "「そうかいそうかい。じゃ、俺は部の方に顔出してくるわ」"
    
    so "「何だ。部活あるのかよ」"
    
    ak "「いやぁ、ね。外は雨で、部室にこもって黙々と碁を打つなんてジジ臭いことから、たまには逃れたい気もするだろ？」"
    
    so "「お前、自分で選んだ部活に良くそんなこと言えるよな」"
    
    show akira aki_1_04
    
    ak "「くそっ！俺に彼女でもいればこんな生活とおさらば出来るのに！！」"
    
    "涙を拭くようなしぐさをして、明良は比較的大声で嘆く。"
    
    "うるさい。"
    
    so "「じゃぁな、そろそろ俺帰るわ。付き合いきれん」"
    
    show akira aki_1_09
    
    ak "「ひ、酷いっ！私を置いて帰るなんて！」"
    
    so "「酷くない。お前みたいなうるさいのは置いて帰るのが妥当だと判断したまでだ」"
    
    show akira aki_1_05
    
    ak "「何ィ！？こ、今度からノートとか見せてやらんからな！！」"
    
    "……それは困るな。"
    
    "調子に乗りやすい明良の事だ。ちょっといいこと言ってやればそんな気も失せるだろう。"
    
    so "「いや、俺はお前のこと信じてるぞ。口ではそんなこと言っても、困ってる人を見れば助けずにはいられないってことを、俺は知ってる」"
    
    "言っておいてなんだが、恥ずかしくなるような台詞だな。"
    
    "明良は心もち照れるような表情を浮かべながら返事をする。"
    
    show akira aki_1_01
    
    ak "「お、おう。わかったよ。困ったときはお互いさまだもんな！」"
    
    so "「じゃぁな。お疲れ」"
    
    ak "「おう、お疲れ～」"
    
    hide akira
    
    "俺は鞄を持って教室を出、そのまま昇降口に向かった。"
    
    "さて、これからどうしようか。"
    
    menu:
        "そのまま玄関へ":
            $ loveMi += 1
            jump misogi3_C # mi_5.ks - mi_5c
        
        "トイレに寄る":
            $ loveKi += 1
            jump kiriko3_B # ki_5.ks - ki_5b

label main5_E:
    
    #*plo5_b|６月２０日（ＷＥＤ）：雨って憂鬱（４）
    
    play music "sound/bgm/bgm_001.ogg"
    
    scene bg bg_b02
    with Fade(1, 0, 1)
    
    so "「いやぁ、憂鬱だ」"
    
    "晩御飯の時間になり、しとねが食卓にいろいろと物を運んでくる。"
    
    show sitone si_2_01
    
    si "「どうしたの？　何が憂鬱？」"
    
    so "「雨だ。なんかな、嫌いじゃないが、こうも頻繁に降る　とな」"
    
    "窓の外では、依然として雨が降っている。"
    
    si "「でも、明日からは数日間晴れるみたいよ？」"
    
    so "「そうか。でもな、今の状態じゃ俄には信じがたいよな」"
    
    si "「そうだね。でも、お祭は晴れるかなぁ……」"
    
    "しとねはご飯を食卓に並べ終え、席に着く。"
    
    so "「ああ、祭か。そういえば、今日明良も言ってたな」"
    
    show sitone si_2_06
    
    si "「おにいちゃんは、どうするの？」"
    
    so "「ん？　いや、まだ何も決めてないけどな」"
    
    "この祭は、ちょっと特殊な行事があり、それがメインイベントでもあったりする。"
    
    "……それはそれで、厄介な行事ではあるのだが。"
    
    si "「そ、そう？」"
    
    "しとねは、ちょっと伏目がちに返事をする。"
    
    so "「そういうお前は、何かあるのか？」"
    
    si "「い、いや、無いんだけど……」"
    
    so "「けど？」"
    
    si "「べ、別に、何も無いよ……」"
    
    "しとねの顔が妙に紅潮しているような気もするが、敢えてそこには触れないことにした。"
    
    "……何かあるんだろうな。"
    
    so "「そうか。まぁ、また今年もいつも通りなんだろうけど　な。いただきます」"
    
    "並べられたご飯に箸をつける。"
    
    show sitone si_2_01
    
    si "「あ、うん。いただきます」"
    
    scene bg bg_b00
    with Fade(1, 0, 1)
    
    so "「あ～あ、疲れた」"
    
    "宿題を終え、椅子の後ろにあるベッドに倒れこむ。"
    
    so "「いやぁ、もう学校とか行きたくねぇな」"
    
    "独り言が口から出るが、気にしない。"
    
    "耳を澄ますと、窓の外からはまだ雨の音が聞こえてくる。"
    
    "こういう時に聞く雨の音は静かで、心が洗われるようだ。"
    
    "せめて、じめじめしてなければいいんだが。"
    
    so "「ふぁ～ぁ」"
    
    "安堵感が押し寄せ、急に睡魔が襲ってくる。"
    
    so "「……あ」"
    
    "しかし、ふと、勉強の合間にお菓子を食べたことを思い出す。"
    
    so "「……歯磨かなきゃな」"
    
    "正直、このまま寝てしまいたいが、どうしたものか。"
    
    so "「いや、いいか。もう寝よう」"
    
    "動くのがめんどくさいので俺はそのまま目を閉じた。"
    
    "明日の朝は歯垢とか凄いんだろうな、などと思いながら、俺は眠りに落ちた。"
    
    if f_kiriko_5==1:
        jump kiriko3_C # ki_5.ks - *ki_5z
    
    jump main6 # plo6.ks - Top
