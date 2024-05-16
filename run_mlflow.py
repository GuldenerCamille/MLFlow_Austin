import os
import mlflow

# Set the default artifact root
os.makedirs("mlruns", exist_ok=True)
artifact_root = os.path.abspath("mlruns")

if __name__ == "__main__":
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_registry_uri("sqlite:///mlflow.db")
    mlflow.server(host='0.0.0.0', port=5000, backend_store_uri='sqlite:///mlflow.db', default_artifact_root=artifact_root)