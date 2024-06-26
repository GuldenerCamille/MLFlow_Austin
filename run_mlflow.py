import os
import mlflow

# Set the default artifact root
os.makedirs("mlruns", exist_ok=True)
artifact_root = os.path.abspath("mlruns")

# Get the port from the environment variable
port = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    mlflow.set_tracking_uri("sqlite:///mlflow.db")
    mlflow.set_registry_uri("sqlite:///mlflow.db")
    mlflow.server(host='0.0.0.0', port=port, backend_store_uri='sqlite:///mlflow.db', default_artifact_root=artifact_root)