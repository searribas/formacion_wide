from clearml import Dataset

dataset = Dataset.create(
    dataset_name="boro1_csv",
    dataset_project="acciona_repo"
)
dataset.add_files(
    path="/home/usuario/formacion 1",
)
dataset.upload(output_url="/home/user/server_local_storage/clearml_training_dataset")
dataset.finalize()
