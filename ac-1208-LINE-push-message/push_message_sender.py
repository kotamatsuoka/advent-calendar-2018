from linebot import LineBotApi
from linebot.models import TextSendMessage

LINE_CHANNEL_ACCESS_TOKEN = "ご自身のチャネルのアクセストークン"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)


def main():
    user_id = "プッシュ通知を送りたLINEユーザーのuser_id"

    messages = TextSendMessage(text=f"こんにちは😁\n\n"
                                    f"最近はいかがお過ごしでしょうか?")
    line_bot_api.push_message(user_id, messages=messages)


if __name__ == "__main__":
    main()
