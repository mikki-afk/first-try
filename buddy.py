import random
FOOD={"苹果":(10,2,5),"鱼":(20,5,10),"蛋糕":(15,10,15),"牛奶":(8,3,3),"牛排":(30,8,25),"沙拉":(12,4,8)}
GAME={"捉迷藏":(15,-10),"接球":(10,-8),"跑步":(8,-15),"拼图":(12,-5),"唱歌":(20,-3)}
PETS={"猫":("🐱","独立"),"狗":("🐶","忠诚"),"兔子":("🐰","温柔"),"龙":("🐲","神秘"),"狐狸":("🦊","聪明"),"熊猫":("🐼","可爱")}
STAGES=[(0,"蛋"),(10,"幼年"),(50,"少年"),(150,"青年"),(300,"成年")]
CAT={"idle":"  /\\_/\\\n ( o.o )\n  > ^ <","happy":"  /\\_/\\\n ( ^.^ ) ♪\n  > ~ <","sleep":"  /\\_/\\\n ( -.- ) z Z\n  > ~ <","sad":"  /\\_/\\\n ( T.T )\n  > ~ <"}
DOG={"idle":"  / \\__\n (    @\\___\n /         O\n/_____/  U","happy":"  / \\__\n (    @\\___  ♪\n /         O\n/_____/  U ~","sleep":"  / \\__\n (    -\\___  z Z\n /         O\n/_____/  U","sad":"  / \\__\n (    T\\___\n /         O\n/_____/  U"}
BUN={"idle":" (\\ /)\n ( . .)\n c(\")(\")", "happy":" (\\ /)\n ( ^.^) ♪\n c(\")(\")", "sleep":" (\\ /)\n ( -.-) z Z\n c(\")(\")", "sad":" (\\ /)\n ( T.T)\n c(\")(\")"}
ARTS={"猫":CAT,"狗":DOG,"兔子":BUN,"龙":CAT,"狐狸":CAT,"熊猫":CAT}
TIPS=["加油！💪","bug只是还没变成feature~","休息一下吧！👀","记得喝水！🥤","每一行代码都是进步！📈","相信自己！🌟","代码能跑就是胜利！🏆","元气满满！🌈","困了就休息！😴","记得保存！📦"]
clamp=lambda v:max(0,min(100,v))
class VPet:
    def __init__(s,name,pt="猫"):
        s.name=name;<s.pt>=pt;s.emoji=PETS.get(pt,PETS["猫"])[0];s.hunger=50;s.happy=50;s.energy=80;s.hp=100;s.exp=0;<s.lv>=1;s.coins=50;s.sleeping=False;s.count=0
    def stage(s):
        r="蛋"
        for t,n in STAGES:
            if s.exp>=t:r=n
        return r
    def mood(s):
        if s.energy<20:return "困倦😴"
        if s.hunger<20:return "饥饿😫"
        if s.happy>80:return "兴奋🤩"
        if s.happy>50:return "开心😊"
        if s.happy<30:return "难过😢"
        return "普通😐"
    def bar(s,v):f=int(v/5);return "█"*f+"░"*(20-f)
    def status(s):
        print(f"\n{'='*40}\n  {s.emoji} {s.name} | {<s.pt>}\n  阶段:{s.stage()} 等级:{<s.lv>} 经验:{s.exp}\n  心情:{s.mood()} 金币:{s.coins}\n{'─'*40}")
        for n,v in [("饱腹",s.hunger),("快乐",s.happy),("体力",s.energy),("健康",s.hp)]:print(f"  {n}:[{s.bar(v)}]{v}%")
        print(f"  互动:{s.count}\n{'='*40}")
    def feed(s,food):
        if food not in FOOD:print(f"没有！可选:{','.join(FOOD.keys())}");return
        h,hp,p=FOOD[food]
        if s.coins<p:print(f"金币不够！要{p}有{s.coins}");return
        if s.sleeping:print("在睡觉！");return
        s.coins-=p;s.hunger=clamp(s.hunger+h);s.happy=clamp(s.happy+hp);s.exp+=5;<s.lv>=1+s.exp//30;s.count+=1
        print(f"{s.emoji}{s.name}吃了{food}！饱腹+{h} 快乐+{hp} -{p}币")
    def play(s,g):
        if g not in GAME:print(f"没有！可选:{','.join(GAME.keys())}");return
        if s.sleeping:print("在睡觉！");return
        if s.energy<10:print("太累了！");return
        hp,en=GAME[g];r=random.randint(3,12);s.happy=clamp(s.happy+hp);s.energy=clamp(s.energy+en);s.coins+=r;s.exp+=8;<s.lv>=1+s.exp//30;s.count+=1
        print(f"{s.emoji}{s.name}玩了{g}！快乐+{hp} 体力{en} +{r}币")
    def pet_it(s):
        s.happy=clamp(s.happy+8);s.exp+=3;<s.lv>=1+s.exp//30;s.count+=1
        print(f"{s.emoji}{s.name}{random.choice(['蹭了蹭你','转圈圈','眨眨眼','跳到怀里'])}！快乐+8")
    def toggle_sleep(s):
        if s.sleeping:s.sleeping=False;print(f"{s.emoji}{s.name}醒了！")
        else:s.sleeping=True;s.energy=clamp(s.energy+30);s.hp=clamp(s.hp+10);print(f"{s.emoji}{s.name}睡着了💤 体力+30")
    def art(s,st="idle"):print(f"\n{ARTS.get(<s.pt>,CAT).get(st,CAT['idle'])}\n")
def virtual_pet():
    print("\n🎮 虚拟宠物")
    for k,(e,t) in PETS.items():print(f"  {e}{k}-{t}")
    pt=input("选类型:").strip();pt=pt if pt in PETS else "猫";name=input("起名字:").strip() or "小宝"
    p=VPet(name,pt);print(f"\n🎉{p.emoji}{name}诞生了！")
    while True:
        p.status();p.art();print("[1]喂食[2]玩[3]摸[4]睡[5]鼓励[0]返回")
        c=input("> ").strip()
        if c=="0":break
        elif c=="1":print(f"食物:{','.join(f'{k}¥{v[2]}' for k,v in FOOD.items())}");p.feed(input("选:").strip())
        elif c=="2":print(f"游戏:{','.join(GAME.keys())}");p.play(input("选:").strip())
        elif c=="3":p.pet_it()
        elif c=="4":p.toggle_sleep()
        elif c=="5":p.art("happy");print(f"💬{name}:{random.choice(TIPS)}")
def cli_companion():
    print("\n🖥️ CLI伙伴");pt=input("选(猫/狗/兔子):").strip();pt=pt if pt in ARTS else "猫";name=input("起名字:").strip() or "伙伴";art=ARTS.get(pt,CAT)
    while True:
        print(f"\n伙伴:{name}\n[1]看[2]鼓励[3]聊[0]返回");c=input("> ").strip()
        if c=="0":break
        elif c=="1":print(f"\n{art['idle']}")
        elif c=="2":print(f"\n{art['happy']}\n💬{name}:{random.choice(TIPS)}")
        elif c=="3":
            w=input("说:").strip()
            if any(x in w for x in ["error","bug","错","难"]):print(f"\n{art['sad']}\n💬{name}:别灰心！")
            elif any(x in w for x in ["done","完成","棒","好"]):print(f"\n{art['happy']}\n💬{name}:太棒了！🎉")
            elif any(x in w for x in ["累","困"]):print(f"\n{art['sleep']}\n💬{name}:休息吧💤")
            else:print(f"\n{art['idle']}\n💬{name}:我陪着你！")
pets_db={}
def pet_manager():
    emo={"猫":"🐱","狗":"🐶","兔子":"🐰","鸟":"🐦","鱼":"🐟","仓鼠":"🐹","乌龟":"🐢"}
    while True:
        print("\n📋宠物管理\n[1]列表[2]添加[3]详情[4]疫苗[5]备注[0]返回");c=input("> ").strip()
        if c=="0":break
        elif c=="1":
            if not pets_db:print("还没有宠物！");continue
            for n,p in pets_db.items():print(f"  {emo.get(p['s'],'🐾')}{n}|{p['s']}|{p['a']}岁{p['w']}kg")
        elif c=="2":
            n=input("名字:").strip();s=input("种类:").strip();b=input("品种:").strip()
            try:a=float(input("年龄:").strip() or "0")
            except:a=0
            try:w=float(input("体重kg:").strip() or "0")
            except:w=0
            pets_db[n]={"s":s,"b":b,"a":a,"w":w,"v":[],"n":[]};print(f"🐾已添加{n}!")
        elif c=="3":
            n=input("名字:").strip()
            if n not in pets_db:print("找不到");continue
            p=pets_db[n];print(f"\n{emo.get(p['s'],'🐾')}{n}\n种类:{p['s']} 品种:{p['b']}\n年龄:{p['a']}岁 体重:{p['w']}kg")
            if p["v"]:print("💉疫苗:");[print(f"  -{v}") for v in p["v"]]
            if p["n"]:print("📝备注:");[print(f"  -{x}") for x in p["n"][-5:]]
        elif c=="4":
            n=input("名字:").strip()
            if n not in pets_db:print("找不到");continue
            v=input("疫苗:").strip();d=input("日期:").strip();pets_db[n]["v"].append(f"{v}({d})");print(f"💉已记录{v}")
        elif c=="5":
            n=input("名字:").strip()
            if n not in pets_db:print("找不到");continue
            x=input("备注:").strip();pets_db[n]["n"].append(x);print("📝已添加")
def main():
    while True:
        print("\n╔════════════════════════╗\n║  🐾 Buddy 宠物系统 🐾 ║\n║ 1.🎮虚拟宠物          ║\n║ 2.🖥️ CLI伙伴           ║\n║ 3.📋宠物管理          ║\n║ 0.🚪退出              ║\n╚════════════════════════╝")
        c=input("选(1/2/3/0):").strip()
        if c=="0":print("👋再见！");break
        elif c=="1":virtual_pet()
        elif c=="2":cli_companion()
        elif c=="3":pet_manager()
if __name__=="__main__":main()
