from fastapi import FastAPI
from story.core.config import settings


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, 
            **kwargs, 
            version ="1.0.0",
            title = settings.PROJECT_NAME,
            root_path = settings.ROOT_PATH
            )
      
app =App()