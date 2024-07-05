import pandas as pd

class Report:
    def __init__(self) -> None:
        pass

    def print_report(input_text, output_text, normal_score) -> None:
        res = [input_text, output_text, normal_score]
        df = pd.DataFrame(res, columns=['Input_Text', 'Output_Text', 'Normal_Similarity_Score'])
        df.to_excel('ml/report.xlsx', index=False)

        