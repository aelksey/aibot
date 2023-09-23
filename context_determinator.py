from transformers import AutoTokenizer, AutoModel
from transformers import pipeline
#import db

tokenizer = AutoTokenizer.from_pretrained("d0rj/e5-base-en-ru")
model = AutoModel.from_pretrained("d0rj/e5-base-en-ru")

pipe = pipeline("sentence-similarity", model="d0rj/e5-base-en-ru")


# tokenize words and compare initial question and answer things then select chunks of context to pass to telegram bot

question = "Какие существуют основания для блокировки на Портале Поставщиков?"

answer = "Основаниями для блокировки на Портале поставщиков являются: - невыполнение обязательств по итогам котировочной сессии; - прекращение деятельности поставщика (юридического лица, ИП); - размещения поставщиков недостоверной информации на Портале поставщиков; - подача поставщиком заявления о прекращении использования Портала поставщиков."

print(pipeline({'query':question,'passage':answer}))