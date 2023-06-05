from dataclasses import dataclass, asdict

@dataclass
class UseCase:

    task_Id : str
    task_name : str
    usecase_Id : str
    description : str
    comments : str
    LOB : str
    sub_LOB : str
    source_folder : str
    dest_folder : str
    task_status: str

