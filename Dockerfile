FROM python:3.12.5
WORKDIR /503FinalProject/FastAPI
COPY  ./FastAPI /503FinalProject/FastAPI
COPY ./requirements.txt /503FinalProject/FastAPI/requirements.txt
RUN pip install -r /503FinalProject/FastAPI/requirements.txt
COPY ./Model/final_model_experiment_7.pkl /503FinalProject/Model/
COPY ./Model/xgb_pipeline_expt7.pkl /503FinalProject/Model/




CMD ["fastapi", "run", "main.py", "--port", "80"]