#!/bin/bash
#トークンを記述
token="rMK2tpGpCcN7j93I4xVurPwXINyjkGZIW4Zr61dPNgX"
#メッセージを送信
curl -X POST -H "Authorization: Bearer ${token}" -F "message = ラズパイだよ！ぽよぽよ〜" https://notify-api.line.me/api/notify