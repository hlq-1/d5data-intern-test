from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import asyncio

app = FastAPI(title="Streaming Demo")


async def stream_generator():
    """Simulate LLM-style character-by-character streaming output."""
    content = (
        "Hello! This is a FastAPI streaming demo for D5Data intern test. "
        "The stream response sends text chunk by chunk, just like an LLM typing."
    )
    for char in content:
        yield char
        await asyncio.sleep(0.05)


@app.get("/stream")
async def stream_endpoint():
    return StreamingResponse(
        stream_generator(),
        media_type="text/plain",
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
#（注：内容由AI生成）
