# Imports
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import qrcode
from io import BytesIO

app = FastAPI()

class Url(BaseModel):
    url: str = Field(..., example="https://xminds.com")

@app.post("/generate")
async def generate_qr_code(url: Url):
    try:
        # Create QR code image in memory
        img = qrcode.make(url.url)
        
        # Save QR code image to BytesIO buffer
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        
        # Get the BytesIO buffer content as bytes
        image_bytes = buffer.getvalue()
        
        # Return the bytes of the QR code image
        return {"message": "QR code generated successfully!", "qrcode": image_bytes}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

