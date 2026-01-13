from sqlmodel import SQLModel

# Create a single MetaData instance for the entire application
metadata = SQLModel.metadata
