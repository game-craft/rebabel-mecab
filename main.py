import MeCab
from fastapi import FastAPI
from typing import List

APP = FastAPI()
WAKATI = MeCab.Tagger("-Owakati")

@APP.post("/analysis")
async def analysis(word_item: List[dict]):
    response_data = []

    for i in range(len(word_item)):
        wakati = WAKATI.parse(word_item[i]["word"]).split()
        data = {
            "worlds_id": word_item[i]["worlds_id"],
            "word_list": wakati
        }
        response_data.append(data)

    return response_data