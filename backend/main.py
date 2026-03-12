from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import shutil, os, traceback

from ai_engine import reply
from file_reader import read_file
from image_reader import read_image


app = FastAPI()

# ⭐ SUPER CORS (testing mode)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("uploads", exist_ok=True)


@app.post("/chat")
async def chat(message: str = Form(...), file: UploadFile = File(None)):
    try:
        print("\n===== NEW REQUEST =====")
        print("USER MESSAGE:", message)

        context = ""

        if file:
            path = f"uploads/{file.filename}"

            with open(path, "wb") as f:
                shutil.copyfileobj(file.file, f)

            print("FILE:", file.filename)

            if file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
                context = read_image(path)
            else:
                context = read_file(path)

        # ⭐ Direct AI call (NO TRANSLATION)
        ai_reply = reply(message, context)

        print("AI REPLY:", ai_reply)

        return {"reply": ai_reply}

    except Exception as e:
        print("\n🔥 BACKEND CRASHED 🔥")
        traceback.print_exc()
        return {"reply": "Backend error — check terminal"}



