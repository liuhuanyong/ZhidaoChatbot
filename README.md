# ZhidaoChatbot
ZhidaoChatbot, a chatbot that can be an expert on the common questions like why,how,when,who,what based on the online question-answer website，基于线上公开问答数据的知道类问答机器人demo，与检索方式不同，可以进行常规问题的问答，如为什么，怎么样，是什么等，基于该方式，可以作为问答机器人常识接口，也可以作为常识知识库构建 
# 项目介绍
&emsp;目前，基于百科知识的问答机器人有很多，但这大多实现的是实体属性的知识问答，在逻辑的问答上还显得较为欠缺，然而，目前可以支持逻辑问答的方式主要有两种方式：  
&emsp;一是基于结构化逻辑尝试知识库的问答，这种方法下需要提前构建起一个尽可能大的结构化尝试知识库，类似于我的基于因果图谱（https://github.com/liuhuanyong/EventPredictBasedOnEG)  的预测性问答项目，根据原因或者条件找未来影响.  
&emsp;第一种方式前期成本较大，且准确性不好把控．第二种方式需要有预先准备好的问答对，在没有自动生产的条件下，数量上难以快速提升  
&emsp;然而，目前诸如百度知道，搜狗问问等线上问答社区，在这种逻辑性和常识性问答上积累了大量的数据，它集成了广大网友的智慧，涵盖的主题包括天文地理，既可以接近生活，在文化内涵上也不含糊，因此，通过使用这些数据，为问答机器人提供一个查询检索，也是个不错的想法，  
&emsp;zhidaochatbot，一个基于线上问答社区的常识性知识问答接口，该接口基于搜狗问问线上资源，通过问句检索，答案抽取与排序，最终以尽可能简短的方式给出问答答案以及用户进一步可能需要问的问题  

# 项目运行
python chatbot.py 
# 项目结果
１，　常识因果逻辑之求因

    ******************************************
    你的问题:为什么要读书
    回答: ['赚钱！', '读书改变命运', '读书可以改变你的容貌', '为了融入社会，必须读书，', '知识改变命运，教育成就未来']
    你可能还想问: ['为什么要读书的理由', '读书和不读书的区别', '孩子 我为什么要你读书', '为什么要上学', '为什么要读书幽默回答', '为什么要读书作文800字', '为什么要努力读书', '人为什么要读书呢', '为什么要读书300字', '农村人为什么要读书', '我们为什么而读书', '人为啥要上学读书', '我们为什么要上学读书', '为什么想读书', '为什么要读书视频', '为什么要读书段子', '为什么要读书议论文', '为什么要读书举个例子来说', '为什么有的人会读书', '我们为何而读书', '为什么要读书龙应台', '没有读书的原因', '我们为什么要读书作文', '自己为什么而读书作文', '人读书是为了什么', '为什么要读书的演讲', '为什么读书作文', '面对为什么读书', '读书的意义最好的回答']
    ******************************************
    你的问题:为什么要自信
    回答: ['因为我们不能自卑，天下唯自卑的人无药可救。所以我们必须自信。', '自信是精神动力，有好多事，精神动力起着不可忽视的作用。人自信，精神面貌也好。', '自信能给人智慧，自信能让人更可爱，自信是一种好品质，是对自身优缺点的充分认识与发掘，女人自信更女人，男人自信更男人。', '没自信的人有没有向往生活的勇气，没有勇气自然就没有动力，没动力就自然没有先进的把握，没把握就没有了一切，都是自信惹的祸！', '人只有树立起自信心，才会有奋斗的目标，才会去努力，去争取，去拼搏，因此自信心非常关键。如果没有自信心，你会对人很事物不感兴趣，会过的没有滋味。']
    你可能还想问: ['为什么说自信很重要?', '自信对一个人的重要性', '人为什么会不自信', '关于自信的名言', '为什么最重要是自信', '中国人为什么要自信', '怎样让自己变得自信', '没自信之人的四大特征', '怎样做到自信', '为什么要拥有自信', '怎么样才能做到自信', '如何增加一个人的自信', '我们为什么自信', '自信应该怎么做', '怎样才能自信起来', '为什么需要自信', '我们为什么需要自信', '论自信的重要性', '怎样才能让自己更自信', '对自己不自信的表现', '女人到啥时候都要自信', '人为什么应该自信', '不自信的表现有哪些', '不自信的原因心理', '自信使人成功的例子', '为什么说自信很重要', '为什么会没有自信', '我凭什么自信', '因自信而成功的名人事例', '自卑没有朋友']
    ******************************************
    你的问题:为什么要有女朋友
    回答: ['来回答一下', '为下一代啊。呵呵', '因为你需要女朋友', '男女搭配.干活不累啊.', '因为爱，不是寂寞，更不是跟风!']
    你可能还想问: ['找女朋友的意义是什么', '男人为什么要找女朋友', '有女朋友是什么感觉', '五种男生找不到女朋友', '有女朋友的真正的好处', '男生为什么要交女朋友', '男生为什么要找女朋友', '为什么女朋友需要哄', '有女朋友的十大好处', '男生为什么需要女朋友?', '为什么找不到女朋友', '女生为什么要找男朋友', '女生为什么要男朋友', '为什么需要一个女朋友', '男生为什么想要女朋友', '有女朋友晚上的好处', '男生交女朋友为了什么', '为什么我找不到女朋友呢', '为什么要有男朋友', '为什么要交女朋友', '我为什么要找男朋友', '为什么找不到女朋友歌曲', '为什么那么的爱女朋友', '男人不找女朋友可以吗', '有女朋友和没女朋友的区别', '为什么我没有女朋友呢', '为什么和女朋友做没感觉', '学校什么时候发女朋友', '男人为什么找女朋友', '女孩不找帅哥当男朋友']
    ******************************************
2, 专业因果逻辑之求因

    ******************************************
    你的问题:股票为什么会跌
    回答: ['供求关系，就像物价一样。', '多人看好，少人不看好——多人买，少人卖——为了达到平衡，所以股价要升——平衡了——新的不平衡——股价移动——平衡——新的不平衡。。。。。。（一直循环下去）', '股票是有价证券。价值决定价格。价格会围绕价值中枢上下波动。前期向上波动的周期过长，幅度过大，所以后面紧跟着要做反方向的波动，长周期，大幅度。这都是符合事物的客观规律的。', '大家都看好的东西就会争相购买，形成供小于求的局面后，就有价高者先得到的结果；比如，一只股票你我都要买的话，你出一块我就出一块五，反复交替，就把价格拉起来了，反之，就会跌下去的。', '股票价格无论什么时候都是由股票的供给和需求决定的，短期和长期都是这样。。股票的价值和人们的预期是影响需求和供给的重要因素，比如股票内在价值的上升导致更多的人看好该股票，也就有更多的人想要买该股票，所以其需求上升，最终价格上升。。但同时也存在着其他一些影响供给和需求的因素，比如市场操纵，政策等等。这些因素都可以在短期内对供求造成相当大的影响，最终表现给股价的大幅度波动。短期来看,股票价格的涨跌与市场行为有关,买的人比卖的人多,它就涨,如果卖的人比买的人多,它就跌,是一种市场心理的表现;长期来看与公司创造价值的能力相关,能持续稳定为股东创造价值的股票,它就涨,经营不当,盈利倒退或亏损的公司,股价就跌,甚至破产清算,从而摘牌退市.']
    你可能还想问: ['股市行情', '股票市场', '股票为什么会跌涨', '小米股票为什么会跌', '股票跌', '股票一直跌', '股票止跌信号', '梦见股票跌了', '最近股票跌了', '京东股票为什么跌', '腾讯股票为什么跌', '周五股票为什么跌', '网易股票为什么跌', '今年股票为什么跌', '股票分红为什么会跌', '股票跌了为什么要补仓', '股票最近为什么一直跌', '华谊兄弟股票为什么跌', '蓝思科技股票为什么跌', '股票为什么会涨和跌', '股票为什么会涨会跌', '股票为什么一买就跌', '股票为什么有涨有跌', '股票为什么一直跌', '最近股票为什么跌', '股票跌涨跟什么有关', '股票不涨不跌什么意思', '股票补跌是什么意思', '股票一直跌是什么原因', '股票跌是什么颜色']
    ******************************************
    你的问题:为什么会发生贸易战
    回答: ['中美爆发贸易战是美国主导、挑起的。因为美国不愿意看到中国崛起、威胁了美国的利益；因为美国说中国制造政府补贴，属于不公平竞争；因为美国利益优先，美国需要就是标准。。。。', '首先，贸易争端的出现与特朗普一贯坚持的政治理念和经济思想密切相关，这是基于这种理念及思想的影响所做出的一项决定。从大格局来看，这更是特朗普的一种战略行为。自2016年美国总统大选以来，他奉行的思想主张无不体现了美国至上、美国贸易保护主义和单边主义的理念，其目的是为了让美国再次强大起来。在全球经济一体化的大趋势下，这种贸易保护主义政策势必会给国与国之间的贸易往来，经济交流与合作带来巨大的影响。其次，此次贸易争端由美国发起，是出于美国国内政治的需要。特朗普就任总统一年多来，执政过程中遭遇了各种不顺的局面，面临了多种指责。其中由于国内政治压力巨大，特朗普急于摆脱这种信任危机，需要一些国际热点事件转移民众在国内政治方面的注意力。而中美贸易争端正好在这个时候成为了一个不错的战略选择。再次，贸易争端的发起也与国际政治和经济的需要紧密相连。二战结束以来，全球处于70多年相对的和平时期，全球经济和贸易的发展迎来了前所未有的繁荣时期，随着区域和全球经济一体化进程加快，金砖五国和一大批的新兴国家都迎来了各自的黄金发展期。其中日本在上个世纪六十和七十年代崛起，后来成长为世界第二大经济体。中国坚持改革开放的基本国策，通过几十年的持续发展，终于在2010年正式取代日本一跃成为世界第二大经济体。而美国进入21世纪以后，经济发展势头平缓，2008年经济危机则重创了经济的发展，十年以后才得到缓解。因为这种此消彼长的关系，美国的国际影响力正在下降，而中国的国际地位正在上升。在世界各地，美国都遭到了前所未有的挑战，在中东地区受到强有力阻击，对拉丁美洲的控制也遭到抵制，欧盟的发展和金砖五国的崛起都在经济发展上构成了不小的威胁。一些有国际影响力的国际合作组织已经把美国排除在外，都对美国的全球领导力构成了挑战。此外，美国自身国力相比上个世纪后半期在全球的影响力已经有所下降。美国要想继续维持全球霸主地位，就必须有一套新的战略主张和经济发展策略。']
    你可能还想问: ['为什么会产生贸易战', '2018年中美贸易战简介', '为什么会有贸易战', '美国打贸易战的原因', '解析中美贸易战原因', '为什么会爆发贸易战', '中国和美国贸易战最新', '中美贸易战的起因过程', '中美贸易战的根本原因', '中美贸易战的有关情况', '中美发为何会爆发贸易战', '美国为什么要打贸易战', '中美贸易战中国将很惨', '中美为什么打贸易战', '美国发动贸易战原因', '美国对中国贸易战结果', '贸易战对房价影响', '中美贸易战为什么开始', '中美贸易战 什么会涨', '为什么会有中美贸易战', '美国为什么挑起贸易战', '引发中美贸易战的根源', '中美贸易战后果预测', '中美贸易战的影响', '中国怎么应对贸易战', '中美爆发贸易战的影响', '如果中美爆发贸易战', '中美贸易战对我国的影响', '为什么中美要打贸易战']
    ******************************************
3, 常识因果逻辑之求果

    ******************************************
    你的问题:人失恋了会怎么样
    回答: ['说不准', '会习惯沉默一段时间', '会很想另一半……并且很长一段时间忘不了他、还很痛苦', '后果轻了好说，严重则无法想象，那就要看你爱的有多深了', '如果愛的冭深,會狠難忘記,,如過愛的吥深,,吔就無所謂了..吥管祂值吥值得,袮覺得這樣值得那就遈值得..一個秂靜丅會比較恏吧..吥要想冭哆了..']
    你可能还想问: ['怎么样安慰失恋的人', '怎么安慰失恋的人', '怎么样安慰失恋的人', '怎么安慰失恋的人的话', '怎么安慰失恋的人搞笑', '该怎么安慰失恋的人', '安慰失恋人的歌', '安慰一个失恋的人', '安慰失恋的人句子', '安慰分手失恋的人', '安慰失恋人的诗句', '安慰人失恋的句子', '安慰失恋人的句子', '安慰失恋人的话语', '安慰失恋人的说说', '安慰人失恋的诗句', '怎么样劝失恋的人']
    ******************************************
    你的问题:中美如果发生战争了会怎么样
    回答: ['世界末日！', '后果很严重，两败俱伤', '也许会引发第3次世界大战……天知道……', '印度和巴基斯坦打起来，朝鲜和韩国打起来，大陆和台湾打起来，你受命空降日本，奋勇刺杀安培，英勇负伤，凯旋而归，你与输血美女护士好起来，你爸和隔壁老王打起来', '不大可能，美国人没有那么傻，和一个15亿人口的大国开战就等于断送了整个美国，中国是联合国安理会常任理事国，中国也是核武器大国，中国军队也不是吃素的。如果和中国开战就是同世界上五分之一的人口为敌，到时候美国就会得不偿失。']
    你可能还想问: ['如果中美发生战争', '如果明天发生中美战争', '中美如果发生战争', '如果中美发生战争', '如果明天发生中美战争', '如果明天发生中美战争', '中美发生战争会怎么样', '中美会发生战争吗', '中美会不会发生战争', '中美是否会发生战争', '中美发生战争谁会赢', '中美之间会发生战争吗', '中美未来会发生战争吗', '中美战争发生结果推演', '中美南海会发生战争吗', '2017中美会发生战争吗', '中美发生战争', '中美能发生战争吗', '梦见中美发生战争', '中美可能发生战争吗', '中美发生战争的可能性', '中美有可能发生战争吗']
   
 3, 专业因果逻辑之求果  
 
    你的问题:降准以后会怎样
    回答: ['降息的目的，是为了增加市场的成交量', '下周一主力又有逢高出货的机会了，大盘肯定会高开，之后将冲高回落。', '首先，是会影响股票的走势。其次，是刺激居民的消费。再次，就是提升国家的经济效益。', '降准降息：1.降准、（存款准备金）降低银行存款准备金（银行吸储后要放一部分保证金在央行。为的是争抢银行的抗风险能力）2降息。、就是降低你存在银行的利息。简单点就是银行利息降低。按照目前国家政策。已经降准了。很快就会有一次降息。然后看今年经济形势如何。经济形势还是没怎么起色的话（gdp在7%以下）。肯定还会有第二次降准降息的。政府通过降准。好让银行有跟多的钱放到市场。刺激经济', '降准就是降低银行准备金率。比如银行有100块钱，原来的准备金率是10%（意思就是必须强制留100*10%=10元钱在银行），现在要降低到9%的准备金率。那么，你可以看出，降准之后，市场上就由原来的90块钱的货币流通量变为91块钱的货币流通量。货币流通量的增大，会造成通货膨胀。降息就是降低银行的贷款利率。其主要是为了鼓励企业的投资行为，但不一定代表货币流通量就会因此增加。所以，降准是投放流通货币，降息是鼓励投资。']
    你可能还想问: ['降准以后a股的走势', '降准以后可能降息吗', '降准', '降准以后a股的走势', '降准以后可能降息吗', '降准有空间', '2019央行降息降准', '央行降准', '央行降准对楼市的影响', '降准降息', '降准加息', '降准的影响', '降准什么意思', '降准会降息吗', '降准2018', '降准对股市影响', '降准降息的影响', '降准对房价的影响', '降准加息什么意思', '降准和降息的区别', '降准和加息的区别', '降准释放7500亿', '降准降息是什么意思', '降准对银行股的影响', '降准对房地产的影响', '降准是加息还是降息', '降准降息后影响房价吗', '定向降准', '银行降准对股市的影响', '央行降准是指什么']
    ******************************************
    你的问题:投资人投资意愿下降以后会怎样
    回答: ['你好！一般是对投资人的股份进行回购。', '个人对股票的看法不同，下跌时候接盘，估计是短期下跌，看涨', '这要看个人意愿了有的需要钱。那就收钱有的不急需。还可以继续投资还有的可能只是继续持有股份不在继续不同人有不同需求不同环境有不同结果', '下跌有人接盘有多种情况，其中下跌也有几种情况；这里先说几种下跌的情况：1.利空信息2.庄家洗盘3.牛市到来接盘的几种情况：1.散户抄底2.庄家吸筹', '每个人对股市的判断不一样啊，有人判断跌，有人判断涨，所以才有的股市的涨涨跌跌。所以在下跌过程中，依旧有人看好后市，就在补仓，或是抢反弹，抢的人多了，又会推动股市涨。']

# 总结
1,本项目完成了一个基于线上问答社区的常识逻辑性问答机器人接口demo  
2,本项目的问答机器人接口可以满足原因逻辑，结果逻辑，可以回答为什么，有了会怎么样等问题，也可以推荐相似性的问题，可以作为基于逻辑事理知识的一种补充  
3,本项目的问答机器人接口可以作为开源实体性问答机器人的逻辑性问答补充，也可以为逻辑性知识库的构建提供帮助  
4,本项目基于sougou问问实现，后期如有需要，可以加入百度知道等其他百科社区或者垂直型问答网站   
5,除了能够回答什么是什么的问题，能够进一步回答一些逻辑性的问题是个很棒的事情，基于逻辑知识库和问答对检索的方式两种结合将是个很好的应用方式，目前正在这两个方面做一些工作   

If any question about the project or me ,see https://liuhuanyong.github.io/

如有自然语言处理、知识图谱、事理图谱、社会计算、语言资源建设等问题或合作，可联系我：  
1、我的github项目介绍：https://liuhuanyong.github.io  
2、我的csdn博客：https://blog.csdn.net/lhy2014  
3、about me:刘焕勇，中国科学院软件研究所，lhy_in_blcu@126.com  
