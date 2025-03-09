from lightly.api import ApiWorkflowClient
from lightly.openapi_generated.swagger_client import DatasetType, DatasourcePurpose
import os
from config import LIGHTLY_KEY, DATASET_NAME, REPORTS_PATH

def create_or_reuse_dataset():
    client = ApiWorkflowClient(token=LIGHTLY_KEY)
    try:
        client.create_dataset(DATASET_NAME, DatasetType.IMAGES)
    except ValueError:
        client.set_dataset_id_by_name(DATASET_NAME)
    return client

def schedule_run(client, n_samples=20):
    client.set_local_config(
        purpose=DatasourcePurpose.INPUT,
        # relative_path="",  # Optional: relative path to the input_mount folder.
    )
    client.set_local_config(
        purpose=DatasourcePurpose.LIGHTLY,
        # relative_path="",  # Optional: relative path in the lighlty_mount folder.
    )
    scheduled_run_id = client.schedule_compute_worker_run(
        worker_config={
            "use_datapool": True,
            "datasource": {
                "process_all": True,
            },
        },
        selection_config={
            "n_samples": n_samples,
            "strategies": [{"input": {"type": "EMBEDDINGS"}, "strategy": {"type": "DIVERSITY"}}],
        },
    )
    return scheduled_run_id

def monitor_run(client, scheduled_run_id):
    for run_info in client.compute_worker_run_info_generator(scheduled_run_id):
        print(f"[{run_info.state}] {run_info.message}")
    return run_info.ended_successfully()

def export_selected_filenames(client):
    tags = client.get_all_tags()
    latest_tag = tags[0].name
    filenames = client.export_filenames_by_tag_name(latest_tag)
    os.makedirs(REPORTS_PATH, exist_ok=True)
    report_path = os.path.join(REPORTS_PATH, "selected_filenames.txt")
    with open(report_path, "w") as f:
        f.write(filenames)
    return filenames.splitlines()
