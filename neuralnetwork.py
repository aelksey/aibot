from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("AlexKay/xlm-roberta-large-qa-multilingual-finedtuned-ru")
model = AutoModelForQuestionAnswering.from_pretrained("AlexKay/xlm-roberta-large-qa-multilingual-finedtuned-ru")


from transformers import pipeline
nlp = pipeline('question-answering',model=model,tokenizer=tokenizer)
def calculate_answer(question,context):
    tokenizer.encode(question,truncation=True,padding=True)
    answer = nlp({'question':question,'context':context})
    return answer.get('answer')




#Shell
#Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
#scripts\activate
# алгоритм хуйни: нейросеть сравнивает прикол с placeholder вопросом типа ебашит насколько они похожи а потом из двухмерного словаря выводит одну хуйню и другую 