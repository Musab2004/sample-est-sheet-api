## Sample Estimate sheet API

## Cogent-Wiki-RAG setup

- setup your .env first. Refer to .env.example to see .env file configrations

### install requirements and run app

```bash
cd sample_estsheet
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### dockerise app

```bash
docker compose build
docker compose up
```

### Test API in python coding language

```bash
import requests
import pandas as pd

url = 'http://localhost:8000/api/est-sheet-gen/'
file_path = '/home/kamran/RAG_models/data/medical-policy.pdf'   # Update with the path to your file

with open(file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

print(response)
data=response.json()
df = pd.DataFrame([dict(row) for row in data['table']])
df
```
