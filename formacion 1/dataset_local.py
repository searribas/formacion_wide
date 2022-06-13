from clearml import Dataset

dataset = Dataset.create(
    dataset_name="boro.csv",
    dataset_project="acciona_repo"
)
dataset.add_files(
    path="boro.csv",
)
dataset.upload()
dataset.finalize()
