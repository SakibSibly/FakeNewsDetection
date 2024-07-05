import spacy
import pandas as pd


class SimilarityFinder:
    input_text = ""
    def __init__(self, input_text: str):
        self.input_text = input_text
        self.nlp = spacy.load("en_core_web_lg")

    def calculate_similarity(self, sentence1: str, sentence2: str) -> float:
        doc1 = self.nlp(sentence1)
        doc2 = self.nlp(sentence2)
        similarity_score = doc1.similarity(doc2)
        return similarity_score

    def findSimilarity(self):
        result_text = open('ml/result.txt', 'r', encoding='utf-8')
        final_output = open('ml/final_output.txt', 'a', encoding='utf-8')
        count = 0
        similarity_score_list = []
        temporary_sentence = ""
        df_list = []
        for line in result_text:
            if line.count('||'):# Title and snippet is concatenated for better comparison
                similarity_score = self.calculate_similarity(self.input_text, line)
                similarity_score_list.append(similarity_score)

                # Storing the similarity score
                final_output.write("-------------------------------------------------------------------\n")
                final_output.write(self.input_text)
                final_output.write(line)
                final_output.write(f"[Case {count}]: Similarity between the two sentences: {similarity_score}")
                final_output.write("-------------------------------------------------------------------\n\n")
                df_list.append([self.input_text, line, similarity_score])
                # pd.concat([df, pd.DataFrame(df, columns=['Input_Text', 'Output_Text', 'Similarity_Score'])], ignore_index=True)
                
        df = pd.DataFrame(df_list, columns=['Input_Text', 'Output_Text', 'Normal_Similarity_Score'])

        # Additional Data
        final_output.write(f"Average Similarity between the two sentences: {sum(similarity_score_list) / len(similarity_score_list)}")
        final_output.write(f"Max Similarity between the two sentences: {max(similarity_score_list)}")
        final_output.close()
        df.to_excel('ml/report.xlsx', index=False)