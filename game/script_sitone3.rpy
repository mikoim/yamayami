label sitone3_A:
    #*si_5|６月２０日（ＷＥＤ）：食欲をそそらない料理漫画
    
    so "「パー」"
    
    ak "「チョキ」"
    
    "負けた。まあ実際どちらでもよかったしな。"
    
    show akira aki_1_02
    with dissolve
    
    ak "「へっへっへ、俺の勝ちだな。じゃあトリアーエズ本屋に行って、後のことはその後に考えようぜ」"
    
    scene bg bg_d00
    with Fade(1, 0, 1)
    
    "というわけで俺たちは繁華街の中にある本屋に入った。この本屋は結構大きくてさまざまなジャンルの本が取り揃えてあるので客層も幅広いものになっている。"
    
    so "「それで？本屋に来たはいいが何をどうするんだ」"
    
    show akira aki_1_01
    with dissolve
    
    ak "「おいおい心の友、本屋に来てやることといったらただ一つ、女体の美しさについて更なる造詣を深めるに決まっているだろう」"
    
    "いや、俺は今週出た漫画を買うとかいろいろ目的はあるから同列の変態に向けて語るような言い草は止めてもらいたい。"
    
    so "「そうか、頑張れ」"
    
    "そう言い残してコミックの書架に向かおうとした。"
    
    show akira aki_1_02
    
    ak "「かまととぶっちゃあいけねえなあ、いけねえよ。お前だって興味津々の癖に」"
    
    so "「……」"
    
    "まあ、勿論興味がないわけではないが明良みたいにオープンにしすぎるのはどうかとおもう。"
    
    ak "「沈黙は承諾だ。さーあちゃっちゃと行くぞ！」"
    
    "意見を差し挟む間もなく写真集コーナーに引きずられていく途中で、見覚えのある顔が横目に入った。"
    
    "しとねだ。"
    
    "とりあえず明良を引っぺがして、しとねがいるコーナーに向かう。"
    
    scene bg bg_d00
    with Fade(1, 0, 1)
    
    show sitone si_2_01
    with dissolve
    
    "近くまで来てみたが、まだしとねはこちらに気付いていないように思われた。"
    
    "せっかくなので後ろから声をかけてみる。"
    
    so "「お客さん、立ち読みはご遠慮願えますか」"
    
    si "「あと１０分ぐらいで読み終わるので、それまで待ってて下さい」"
    
    "何と。あのしとねがこんな横柄ことを言うなんてお兄様考えたこともありませんでした。"
    
    "……と思ったらこっちを見て笑みを浮かべた。既にばれてたのは遺憾だが、まあ少し安心した。"
    
    show sitone si_2_02
    
    si "「入り口であんな風に話してたら、そりゃあわかっちゃうよ」"
    
    "ですよねー。"
    
    show sitone si_2_01
    
    si "「それでおにいちゃんはこんな雨の日にどうしたの？」"
    
    so "「その言葉をそっくりそのまま返したい気もするが、そこで会話に入り込めずいじけてる明良に連れられて来たんだよ」"
    
    show akira aki_1_02 at left
    show sitone si_2_01 at right
    with dissolve
    
    ak "「実はそうなんだよしとねちゃん！相変わらず今日も可愛いＮＥ！」"
    
    "いきなり復活されるのもイラッとくるな。"
    
    si "「こんにちは、明良さん」"
    
    ak "「かーっ！これだよ、これ！この何でもない動作ににじみ出るしとねちゃんの清楚さがたまらないね！」"
    
    "明良の頭からは脳汁と知性がにじみ出ているようだな。"
    
    #[tl sto=aki_1_07 le=-30]
    
    ak "「それより聞いてくれよしとねちゃん！この馬鹿兄がせっかく本屋に来たっていうのにグラんぐっ」"
    
    play sound "sound/se/se_001.ogg"
    
    hide akira aki_1_02
    hide sitone si_2_01
    with dissolve
    
    show sitone si_2_09
    with dissolve
    
    "済んでのところで明良の口を押さえる。こういう余計な事を言い過ぎるのがもてない最大の原因であるのは間違いないだろう。"
    
    so "「明良が頭の悪くなる病気にかかっているようなので、とりあえずここを出るわ」"
    
    show sitone si_2_01
    
    si "「うんわかった。わたしはもうこれを読み終わるから、帰ってご飯の準備しておくね」"
    
    ak "「ふごー！ふごー！！」"
    
    "物分りのいいしとねと別れ、何か言いたがってる明良を引きずりながら本屋から出て行った。"
    
    scene bg bg_c05
    with Fade(1, 0, 1)
    
    "まあ中学生であるしとねに、余計な知識を植えつけずに済んだのでよかったことにしよう。"
    
    "後に最近の少女漫画は下手なグラビア雑誌なんかよりもよっぽど性的興奮を惹起させていることを知ったが、それはまた別の話。"
    
    jump main5_E #plo5.ks - *plo5_b

#;----------------------------------------------------------------------
label sitone3_B:
   #*si_5b|６月２０日（ＷＥＤ）：お嬢ちゃん、パンツ何色？
   
   so "「しょうがない。磨いておこう」"
   
   "このままだと明日の朝後悔すること請け合いだ。"
   
   scene bg bg_b03
   with Fade(1, 0, 1)
   
   "しとねはもう寝ているだろうから静かに階段を下りる。"
   
   scene bg bg_b04
   with Fade(1, 0, 1)
   
   so "「しかし、何で毎夜毎夜こんな時間まで宿題に追われなきゃならんのか……」"
   
   "自業自得なのは分かっているが、愚痴りたくもなる。さすがに毎度明良に任せるのも気が引けるし。"
   
   so "「ＷＡＷＡＷＡ忘れ物～」"
   
   play sound "sound/se/se_034.ogg"
   
   "……"
   
   "…………"
   
   "俺が時を止めた……"
   
   "やれやれだぜ……"
   
   "……これはあれだ。"
   
   "体内や脳でアドレナリンやら何やらが分泌されて、一瞬が何秒にも感じられるというあれだ。"
   
   "なぜなら、俺の感覚では結構な時間が過ぎ去っているのに、しとねが驚いた顔をしたきり微動だにしていない。"
   
   "個人的にはマンダムの方が現状を改善するためには好ましかった気がするが、贅沢は言えない。"
   
   so "「あ――」"
   
   si "「き……」"
   
   si "「きゃああああああああああああああああーー！！！」"
   
   "車がドリフト気味に急ブレーキをかけたような悲鳴が響き渡った。はい、当然ですね。"
   
   so "「す、すみませんごめんなさい！」"
   
   si "「なな何でおにいちゃんがまだ起きてるの！？寝たんじゃなかったの！？」"
   
   so "「い、いやそれがですね……」"
   
   si "「いいから出てってーーーー！！」"
   
   "何という理不尽。"
   
   "そんなこんなで追放されました。"
   
   so "「いや、本当に申し訳ありません」"
   
   si "「何でノックとかそういうことをしないの！？」"
   
   so "「いや実際もう寝てるとばっかり思っていましたので。それにしとねさんもそう考えたからこそ油断していたわけで」"
   
   si "「む～～～～！！！だからって何でよりにもよって出た後で来るのよ！」"
   
   so "「ええ、本当に申し開きもございません」"
   
   "もはや余計な口は挟まずに謝罪を続けるしか明日の朝日を拝める方法はなさそうだ。"
   
   "しかし今の自分だけを抜き出すと、壁に向かってひたすら謝罪を続けている何とも近寄りたくない存在だな。"
   
   so "「本当にガチで故意であるところのものは一切なく、純然たる過失ですのでどうか許していただけませんか」"
   
   si "「ん～～～～……。まあわざとじゃないみたいだし……わたしもぼんやりしてたし……」"
   
   "度重なる謝罪で何とか機嫌を直すことに成功した。"
   
   "ここで余計な冗談を挟んで度胸試しをする必要はないので、早々に部屋に戻って時間が解決するのを待とう。"
   
   "いやはや疲れた疲れた。"
   
   so "「あ」"
   
   "歯磨きしなきゃ……"
   
   jump main6 # plo6.ks - Top