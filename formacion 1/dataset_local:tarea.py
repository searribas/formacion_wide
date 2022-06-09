from clearml import Task, Dataset

task = Task.init(project_name="myproject", task_name="mytask")

dataset = Dataset.create(
    dataset_name="boro1_csv",
    dataset_project=task.get_project_name(),
    use_current_task=False,
)
dataset.add_files(
    path="//home/usuario/formacion 1",
)
dataset.upload(output_url="/home/user/server_local_storage/clearml_training_dataset")
dataset.finalize()
