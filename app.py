import logging
import sys
from fastapi import FastAPI

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - [%(levelname)s] - %(message)s')

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler("app.log", encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

app = FastAPI()

@app.get("/health")
def health_check():
    logger.info("Проверка /health")
    logger.warning("Тестовый warning")
    return {"status": "ok"}