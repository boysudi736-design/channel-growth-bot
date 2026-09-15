import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME", "")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "👋 እንኳን ወደ Channel Growth Bot በደህና መጡ!\n\n"
        "🚀 Channel ለመቀላቀል /join ይጠቀሙ።\n"
        "📤 ለጓደኞች ለማጋራት /share ይጠቀሙ።\n"
        "📊 መረጃ ለማየት /stats ይጠቀሙ።"
    )
    await update.message.reply_text(text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Commands:\n\n"
        "/start - መጀመሪያ\n"
        "/help - እርዳታ\n"
        "/join - Channel መቀላቀያ\n"
        "/share - Link ማጋራት\n"
        "/stats - Statistics\n"
        "/referral - Referral\n"
        "/leaderboard - Leaderboard\n"
        "/about - ስለ Channel\n"
        "/contact - Admin\n"
        "/support - Support"
    )

async def join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if CHANNEL_USERNAME:
        link = f"https://t.me/{CHANNEL_USERNAME.lstrip('@')}"
        await update.message.reply_text(f"📢 Channel ለመቀላቀል:\n{link}")
    else:
        await update.message.reply_text("⚠️ Channel link ገና አልተዘጋጀም።")

async def share(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_username = context.bot.username
    link = f"https://t.me/{bot_username}?start=ref_{update.effective_user.id}"
    await update.message.reply_text(
        f"📤 ይህን link ለጓደኞችህ አጋራ:\n\n{link}"
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 Statistics\n\n"
        "👤 User ID: " + str(update.effective_user.id)
    )

async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    bot_username = context.bot.username
    link = f"https://t.me/{bot_username}?start=ref_{update.effective_user.id}"
    await update.message.reply_text(
        f"🎁 Your referral link:\n\n{link}"
    )

async def leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 Leaderboard\n\n"
        "ገና ስታቲስቲክስ እየተሰበሰበ ነው..."
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ ስለ Channel\n\n"
        "ይህ Bot ተጠቃሚዎች በፈቃዳቸው Channel እንዲቀላቀሉ ይረዳል።"
    )

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📩 Admin ለማግኘት የChannel Admin ጋር ይገናኙ።"
    )

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 Support\n\n"
        "ችግር ካለ የChannel Admin ያግኙ።"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("share", share))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("referral", referral))
    app.add_handler(CommandHandler("leaderboard", leaderboard))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(CommandHandler("support", support))

    print("🚀 CHANNEL GROWTH BOT IS ONLINE")
    app.run_polling()

if __name__ == "__main__":
    main()
