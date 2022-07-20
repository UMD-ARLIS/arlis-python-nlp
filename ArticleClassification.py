#https://huggingface.co/joeddav/xlm-roberta-large-xnli?text=Can+you+please+amend+the+invoice+to+reflect+true+capital+expenditure+and+anticipated+revenue%3F&candidate_labels=Medical%2Cbusiness%2Cfinance&multi_class=true

# CUDA 11.1
# Site to visit for later version: https://pytorch.org/get-started/previous-versions/
!pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
!pip install transformers
!pip install sentencepiece

classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

def get_Sector_of_Deployment(text)
  candidate_labels_0 = ['Education', 'Arts, entertainment and recreation', 'Transportation and storage']
  # we can specify candidate labels in Russian or any other language above:
  vector = classifier(text, candidate_labels_0)
  return max(vector)
