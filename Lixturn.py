import discord
import time
import random
import datetime

nowdate = datetime.datetime.now()
client = discord.Client()
file = open("LOG.txt" , "a")




@client.event
async def on_ready():

    print(client.user.id)
    print("봇 구동이 준비됨.")
    game = discord.Game('/L 을 이용해 봇을 호출할 수 있어요!')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("/L") or ("/l"):
        msg = "g"
        try:
            msg = message.content.split(" ")[1]
        except IndexError:
            await message.channel.send()
        
        #기본 기능

        if msg == ("정보") or msg == ("팁"):
            await message.channel.send("**안녕하세요! 릭스틴이에요.**\n\n**나에 관해**\n 저에 대해 듣고싶나요? 😏\n 저는 6 월 초 한 개발자에 의해 탄생했어요.\n그 당시 저는 아무것도 못하는 돌덩이와 같았지만 지금은 이렇게 멋진 봇이 되었죠.\n참고로 이 봇은 개발단계에 있답니다 :)\n\n **서포트 서버**\n도움이 필요하신가요? 아래 링크를 통해 봇 서포트 서버에 가입하세요!\nhttps://discord.gg/nQfDdsgkQd")
            
        elif msg == ("개발자들") or msg == ("개발자") or msg == ("개발팀"):
            embed = discord.Embed(title="봇에 대하여",description="**개발팀**\nSmotion Studio\n**개발자**\n지프/!다ㅇ")
            await message.channel.send(embed=embed)
            
        elif msg == ("서포트") or msg == ("서포트 서버") or msg == ("지원") or msg == ("지원서버"):
            await message.channel.send("여기 당신을 위한 서포트 서버가 있어요!\nhttps://discord.gg/nQfDdsgkQd")

        elif msg == ("오늘날짜"):
            if datetime.datetime.now().hour < 12:
                await message.channel.send("{}년 {}월 {}일 오전 {}시 {}분".format(nowdate.year , nowdate.month , nowdate.day , nowdate.hour , nowdate.minute))
            else:
                over12 = 24 - nowdate.hour
                await message.channel.send("{}년 {}월 {}일 오후 {}시 {}분".format(nowdate.year , nowdate.month , nowdate.day , over12 , nowdate.minute))\
        
        #관리기능
        elif ("관리") in msg or msg in (" 관리") or msg == ("서버 관리"):
            embed = discord.Embed(title="서버 관리 기능",description="**역할 설정**\n\n**권한 설정**\n\n**뮤트, 킥, 벤 등 처벌**\n\n 봇은 위와 같은 관리기능을 탑재할 계획을 세우고 있지만 아직은 개발중이랍니다 :(")
            await message.channel.send(embed=embed)


        # 베이직 게임

        elif msg == ("게임 정보") or msg == ("게임") or msg == ("오락 정보") or msg == ("오락"):
            embed = discord.Embed(title="게임 종류",description="심심하신가 보네요! 제가 조금이라도 도와드릴게요! 😉 \n\n뽑기 : 희귀한 것들을 뽑아서 친구들과 경쟁해보세요!\n가위 바위 보 : 여러분이 알고계신 가위 바위 보랍니다! 하지만 아직 개발중이에요 :(")
            await message.channel.send(embed=embed)
        
        elif msg == ("뽑기"):
            await message.channel.send("**뽑기에 도전하셨군요**\n\n 뽑기 희귀도는 **꽝>일반>고급>최고급>에픽>신화>전설** 순입니다!\n 무엇이 나오게 될까요?😏")
            time.sleep(5)
            await message.channel.send("**\n펑!!**")
            time.sleep(1)
            draw = ["(꽝) ㅇr메ㅂr..." , "(꽝) 핵 폐기물" , "(일반) 샌즈를 닮은 종이인형" , "(꽝) 생선 찌꺼기" , "(꽝) 코딱지" , "(최고급) 샌즈!" , "(에픽) 쎄에엔즈으으으!!!" , "(일반) 숟가락" , "(전설) DJ언더테일PPAP레온BJ샌즈마크TV" , "(일반) 머그컵" , "(에픽) 개발자의 동상" , "(고급) 진득한 에스프레소" , "(일반) 동화책-아기돼지 3형제" , "(일반) 소설책-어린왕자" , "(신화) 벽돌 아닌 벽돌" , "(이스터에그!) 샌즈가 먹던 민트초코" , "(고급) 플라스틱 요술봉" , "(일반) A4 이면지" , "(일반) 아메리카노" , "(일반) 얼음물" , "(일반) 사물함 키" , "(일반) 100 원"]
            embed = discord.Embed(title=random.choice(draw))
            await message.channel.send(embed=embed)
            

        # 이스터에그
        elif (".py") in msg:
            py = ["와 파이썬 아시는구나! 참고로 겁.나.쉽.습.니.다." , "와 파이썬! 파이썬은 1991 년 네덜란드의 개발자가 개발한 고급 언어로서 현재 많은 대중들이 선호하는 프로그래밍 언어입니다!"]
            await message.channel.send(random.choice.py)





client.run("import discord
import time
import random
import datetime

nowdate = datetime.datetime.now()
client = discord.Client()
file = open("LOG.txt" , "a")




@client.event
async def on_ready():

    print(client.user.id)
    print("봇 구동이 준비됨.")
    game = discord.Game('/L 을 이용해 봇을 호출할 수 있어요!')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("/L") or ("/l"):
        msg = "g"
        try:
            msg = message.content.split(" ")[1]
        except IndexError:
            await message.channel.send()
        
        #기본 기능

        if msg == ("정보") or msg == ("팁"):
            await message.channel.send("**안녕하세요! 릭스틴이에요.**\n\n**나에 관해**\n 저에 대해 듣고싶나요? 😏\n 저는 6 월 초 한 개발자에 의해 탄생했어요.\n그 당시 저는 아무것도 못하는 돌덩이와 같았지만 지금은 이렇게 멋진 봇이 되었죠.\n참고로 이 봇은 개발단계에 있답니다 :)\n\n **서포트 서버**\n도움이 필요하신가요? 아래 링크를 통해 봇 서포트 서버에 가입하세요!\nhttps://discord.gg/nQfDdsgkQd")
            
        elif msg == ("개발자들") or msg == ("개발자") or msg == ("개발팀"):
            embed = discord.Embed(title="봇에 대하여",description="**개발팀**\nSmotion Studio\n**개발자**\n지프/!다ㅇ")
            await message.channel.send(embed=embed)
            
        elif msg == ("서포트") or msg == ("서포트 서버") or msg == ("지원") or msg == ("지원서버"):
            await message.channel.send("여기 당신을 위한 서포트 서버가 있어요!\nhttps://discord.gg/nQfDdsgkQd")

        elif msg == ("오늘날짜"):
            if datetime.datetime.now().hour < 12:
                await message.channel.send("{}년 {}월 {}일 오전 {}시 {}분".format(nowdate.year , nowdate.month , nowdate.day , nowdate.hour , nowdate.minute))
            else:
                over12 = 24 - nowdate.hour
                await message.channel.send("{}년 {}월 {}일 오후 {}시 {}분".format(nowdate.year , nowdate.month , nowdate.day , over12 , nowdate.minute))\
        
        #관리기능
        elif ("관리") in msg or msg in (" 관리") or msg == ("서버 관리"):
            embed = discord.Embed(title="서버 관리 기능",description="**역할 설정**\n\n**권한 설정**\n\n**뮤트, 킥, 벤 등 처벌**\n\n 봇은 위와 같은 관리기능을 탑재할 계획을 세우고 있지만 아직은 개발중이랍니다 :(")
            await message.channel.send(embed=embed)


        # 베이직 게임

        elif msg == ("게임 정보") or msg == ("게임") or msg == ("오락 정보") or msg == ("오락"):
            embed = discord.Embed(title="게임 종류",description="심심하신가 보네요! 제가 조금이라도 도와드릴게요! 😉 \n\n뽑기 : 희귀한 것들을 뽑아서 친구들과 경쟁해보세요!\n가위 바위 보 : 여러분이 알고계신 가위 바위 보랍니다! 하지만 아직 개발중이에요 :(")
            await message.channel.send(embed=embed)
        
        elif msg == ("뽑기"):
            await message.channel.send("**뽑기에 도전하셨군요**\n\n 뽑기 희귀도는 **꽝>일반>고급>최고급>에픽>신화>전설** 순입니다!\n 무엇이 나오게 될까요?😏")
            time.sleep(5)
            await message.channel.send("**\n펑!!**")
            time.sleep(1)
            draw = ["(꽝) ㅇr메ㅂr..." , "(꽝) 핵 폐기물" , "(일반) 샌즈를 닮은 종이인형" , "(꽝) 생선 찌꺼기" , "(꽝) 코딱지" , "(최고급) 샌즈!" , "(에픽) 쎄에엔즈으으으!!!" , "(일반) 숟가락" , "(전설) DJ언더테일PPAP레온BJ샌즈마크TV" , "(일반) 머그컵" , "(에픽) 개발자의 동상" , "(고급) 진득한 에스프레소" , "(일반) 동화책-아기돼지 3형제" , "(일반) 소설책-어린왕자" , "(신화) 벽돌 아닌 벽돌" , "(이스터에그!) 샌즈가 먹던 민트초코" , "(고급) 플라스틱 요술봉" , "(일반) A4 이면지" , "(일반) 아메리카노" , "(일반) 얼음물" , "(일반) 사물함 키" , "(일반) 100 원"]
            embed = discord.Embed(title=random.choice(draw))
            await message.channel.send(embed=embed)
            

        # 이스터에그
        elif (".py") in msg:
            py = ["와 파이썬 아시는구나! 참고로 겁.나.쉽.습.니.다." , "와 파이썬! 파이썬은 1991 년 네덜란드의 개발자가 개발한 고급 언어로서 현재 많은 대중들이 선호하는 프로그래밍 언어입니다!"]
            await message.channel.send(random.choice.py)





client.run("ODIyMDAyNzczMzA5Nzg0MDY2.YFL7vQ.qCyrpnDXzEFLhZuhoC9TCz77uTQ")





#[[ 저장고
# https://tenor.com/view/sans-undertale-dance-gif-12730380 
# 
# 
# 
")





#[[ 저장고
# https://tenor.com/view/sans-undertale-dance-gif-12730380 
# 
# 
# 
