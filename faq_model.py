import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class FAQChatbot:
    def __init__(self):
        # Load pre-trained BERT model
        self.model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

        # Load FAQ data
        self.faq_data = pd.read_csv("data.csv", header=0)
        self.questions = self.faq_data["question"].astype(str).tolist()
        self.answers = self.faq_data["answer"].astype(str).tolist()

        # Precompute embeddings
        self.question_embeddings = self.model.encode(self.questions)

    def get_answer(self, user_query):
        query_embedding = self.model.encode([user_query])
        similarities = cosine_similarity(query_embedding, self.question_embeddings)
        best_match_idx = similarities.argmax()
        return self.answers[best_match_idx]

# Test the chatbot
if __name__ == "__main__":
    bot = FAQChatbot()
    print(bot.get_answer("When do you open?"))  # Expected: "We are open from 9 AM to 6 PM."
