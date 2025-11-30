from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

def extract_skills(text: str):
    entities = nlp(text)
    skills = [e['word'] for e in entities if e['entity_group'] == 'MISC']
    return list(set(skills))