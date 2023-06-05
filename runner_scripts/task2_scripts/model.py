from dataclasses import dataclass

@dataclass
class Folder:
    Key: str
    # Display name for the folder.
    DisplayName: str
    #Name of folder prepended by the names of its ancestors.
    FullyQualifiedName: str
    #Description of folder
    Description	: str
    # Folder type
    FolderType: str
    # True if Personal
    IsPersonal: bool
    # Robot provisioning type
    ProvisionType: str
    # Folder permissions model
    PermissionModel	: str
    #Id of parent folder in the folders hierarchy
    ParentId: int
    # Unique key for the parent folder
    ParentKey: str
    # Folder feed type
    FeedType: str
    # Folder ID
    Id: int