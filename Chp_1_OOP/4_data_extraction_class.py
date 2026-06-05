import pandas as pd
class DataExtraction:
    def __init__(self, file_path:str):
        self.file_path = file_path

    def read_text(self, separator):
        text_df = pd.read_csv(self.file_path, sep=separator)
        print(text_df.head())

    def read_json(self):
        json_df = pd.read_json(self.file_path)
        print(json_df.head())

    def read_parquet(self):
        parquet_df = pd.read_parquet(self.file_path)
        print(parquet_df.head())


# obj = DataExtraction("./files/orders.tsv")
# obj.read_text("\t")
#
# obj = DataExtraction("./files/orders.csv")
# obj.read_text(",")

# obj = DataExtraction("./files/orders.json")
# obj.read_json()

obj = DataExtraction("./files/orders.parquet")
obj.read_parquet()