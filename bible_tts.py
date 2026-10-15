Python
import asyncio
import edge_tts

text = "여호와는 나의 목자시니 내게 부족함이 없으리로다."
voice = "ko-KR-SunHiNeural"

async def generate_bible_audio():
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("bible_output.mp3")
    print("생성 완료")

if __name__ == "__main__":
    asyncio.run(generate_bible_audio())
