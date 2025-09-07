from aiogram import Router, types
from aiogram.filters import CommandStart

from main.data import session_to_uid, active_sessions


router = Router()


@router.message(CommandStart())
async def start_command(msg: types.Message) -> None:

    if msg.from_user is None:
        return
    if msg.text is None:
        return

    data = msg.text.split()

    if len(data) == 1:
        await msg.reply("💗 Aki Forwarder\n  Start a session at https://aki.rian.moe")
        return

    if len(data) != 2:
        return

    session_id = data[1]
    session_to_uid[session_id] = msg.from_user.id

    await active_sessions[session_id].send_json({"status": "linked"})

    await msg.reply("🍾 Session linked!")
