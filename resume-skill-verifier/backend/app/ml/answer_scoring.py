from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def score_answer(reference: str, candidate_answer: str):
    ref_emb = model.encode(reference, convert_to_tensor=True)
    cand_emb = model.encode(candidate_answer, convert_to_tensor=True)
    similarity = util.cos_sim(ref_emb, cand_emb)
    return float(similarity[0][0])