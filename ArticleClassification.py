#https://huggingface.co/joeddav/xlm-roberta-large-xnli?text=Can+you+please+amend+the+invoice+to+reflect+true+capital+expenditure+and+anticipated+revenue%3F&candidate_labels=Medical%2Cbusiness%2Cfinance&multi_class=true

# CUDA 11.1
# Site to visit for later version: https://pytorch.org/get-started/previous-versions/
!pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
!pip install transformers
!pip install sentencepiece

classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")

def get_Sector_of_Deployment(text):
  sectorDeployment = ['Information and communication', 'Arts, entertainment and recreation', 'Transportation and storage', 'Public administration and defence', 'Administrative and support service activities', 'Human health and social work activities', 'Education', 'Professional, scientific and technical activities', 'Financial and insurance activities', 'Wholesale and retail trade', 'Activities of households as employers', 'Accommodation and food service activities']
  vector = classifier(text, sectorDeployment)
  index = vector['labels'][0]
  return sectorDeployment[index]

def get_infrastructure_sector(text):
  infrastructureSector = ['Transportation', 'Healthcare and public health', 'Government facilities', 'Communications', 'Food and agriculture', 'Critical manufacturing', 'Nuclear', 'Financial services', 'Information technology']
  vector = classifier(text, infrastructureSector)
  index = vector['labels'][0]
  return infrastructureSector[index]

