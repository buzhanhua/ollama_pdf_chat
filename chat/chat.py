import os
from pdf_helper import PDFHelper, load_embedding_model
from config import Config, question

load_embedding_model(model_name=Config.EMBEDDING_MODEL_NAME)

for root, dirs, files in os.walk("./pdfs", topdown=False):
    for name in files:
        if name != '.DS_Store':
            file_path = os.path.join(root, name)
            print(root, name, file_path, files)
            pdf_helper = PDFHelper(
                ollama_api_base_url=Config.OLLAMA_API_BASE_URL,
                model_name=Config.MODEL
            )
            response = pdf_helper.ask(
                pdf_file_path=file_path,
                question=question
            )
            resFile = open(os.path.join('./results', name.split('.')[0]), "a")
            resFile.write(response)
            resFile.close()


