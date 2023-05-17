import MeCab
from fastapi import FastAPI
from pydantic import BaseModel

class WordItem(BaseModel):
    id: int
    word: str

APP = FastAPI()
WAKATI = MeCab.Tagger("-Owakati")

@APP.post("/analysis")
async def analysis(word_item: WordItem):
    wakati = WAKATI.parse(word_item.word).split()
    response = {
        "id": word_item.id,
        "word_list": wakati
    }

    return response