    async def show_stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """عرض إحصائيات القناة"""
        query = update.callback_query

        try:
            chat = await context.bot.get_chat(self.channel_id)
            members_count = await context.bot.get_chat_member_count(self.channel_id)
            members_text = f"👥 *عدد الأعضاء:* {members_count}"

            stats_text = f"""
📊 *إحصائيات القناة*

📌 *الاسم:* {chat.title}
🆔 *المعرف:* `{chat.id}`
{members_text}
📝 *الوصف:* {chat.description or 'لا يوجد'}

🖼️ *الصور في المكتبة:* {self.media_manager.list_contents()['images_count']}
📄 *المنشورات:* {self.media_manager.list_contents()['posts_count']}
"""

            keyboard = [[InlineKeyboardButton("🔙 رجوع", callback_data="back")]]
            reply_markup = InlineKeyboardMarkup(keyboard)

            await query.edit_message_text(
                stats_text,
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )

        except Exception as e:
            await query.edit_message_text(f"❌ خطأ: {e}")
