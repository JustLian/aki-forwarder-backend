from fastapi import UploadFile, File, Form, HTTPException, APIRouter
from fastapi.responses import JSONResponse, Response

from aiogram.types import BufferedInputFile

from main.data import session_to_uid
from main.bot.client import bot


router = APIRouter()


@router.post("/upload")
async def upload_file(
    sessionId: str = Form(...),
    file: UploadFile = File(...),
) -> Response:
    
    user_id: int | None = session_to_uid.get(sessionId)

    if not user_id:
        raise HTTPException(status_code=400, detail="No telegram user is linked to this session")
    
    
    data = await file.read()

    if len(data) > 8 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="File too large")

    input_file = BufferedInputFile(
        file=data,
        filename=file.filename or "file",
    )

    try:
        await bot.send_document(
            chat_id=user_id,
            document=input_file,
            caption=file.filename or None,
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=502,
            detail=f"Failed to send file: {e}"
        )

    return JSONResponse({"message": "File sent successfully"})