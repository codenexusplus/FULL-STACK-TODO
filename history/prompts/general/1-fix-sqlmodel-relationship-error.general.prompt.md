---
id: 1
title: Fix SQLModel Relationship Error
stage: general
date_iso: 2026-01-12
surface: agent
model: Qwen
feature: none
branch: main
user: batool1
command: python -m uvicorn src.main:app --host 0.0.0.0 --port 8002 --reload
labels:
  - sqlmodel
  - relationships
  - KeyError
  - backend
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - C:\Users\batool1\Desktop\full-stack - Copy\backend\src\models\user.py
  - C:\Users\batool1\Desktop\full-stack - Copy\backend\src\models\session.py
  - C:\Users\batool1\Desktop\full-stack - Copy\backend\src\models\todo.py
tests_yaml: []
prompt_text: |
  This is the Qwen Code. We are setting up the context for our chat.
  Today's date is Monday, 12 January 2026 (formatted according to the user's locale).
  My operating system is: win32
  I'm currently working in the directory: C:\Users\batool1\Desktop\full-stack - Copy
  Here is the folder structure of the current working directories:

  Showing up to 20 items (files + folders). Folders or files indicated with ... contain more items not shown, were ignored, or the display limit (20 items) was reached.

  C:\Users\batool1\Desktop\full-stack - Copy\
  ├───.env
  ├───.gitignore
  ├───.gitignore_temp
  ├───backend_server_with_init.py
  ├───backend_server.py
  ├───check_env.py
  ├───check_paths.py
  ├───CLAUDE.md
  ├───create_sample_user.py
  ├───debug_backend.py
  ├───debug_imports.py
  ├───debug_models.py
  ├───load_env.py
  ├───minimal_backend.py
  ├───parse_env.py
  ├───QWEN.md
  ├───README.md
  ├───reproduce_error.py
  ├───run_backend.py
  ├───run_debug_server.py
  ├───...
  └───...

  PS C:\Users\batool1\Desktop\full-stack - Copy> cd backend
  PS C:\Users\batool1\Desktop\full-stack - Copy\backend> python -m uvicorn src.main:app --host 0.0.0.0 --port 8002 --reload
  >> 
  INFO:     Will watch for changes in these directories: ['C:\\Users\\batool1\\Desktop\\full-stack - Copy\\backend']
  INFO:     Uvicorn running on http://0.0.0.0:8002 (Press CTRL+C to quit)
  INFO:     Started reloader process [2368] using WatchFiles
  Process SpawnProcess-1:
  Traceback (most recent call last):
    File "C:\Python314\Lib\multiprocessing\process.py", line 320, in _bootstrap
      self.run()
      ~~~~~~~~^^
    File "C:\Python314\Lib\multiprocessing\process.py", line 108, in run
      self._target(*self._args, **self._kwargs)
      ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Users\batool1\AppData\Roaming\Python\Python314\site-packages\uvicorn\_subprocess.py", line 76, in subprocess_started
      target(sockets=sockets)
      ~~~~~~^^^^^^^^^^^^^^^^^
    File "C:\Users\batool1\AppData\Roaming\Python\Python314\site-packages\uvicorn\server.py", line 61, in run
      return asyncio.run(self.serve(sockets=sockets))
             ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "C:\Python314\Lib\asyncio\runners.py", line 204, in run
      return runner.run(main)
             ~~~~~~~~~~^^^^^^
    File "C:\Python314\Lib\asyncio\runners.py", line 127, in run
      return self._loop.run_until_complete(task)
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^
    File "C:\Python314\Lib\asyncio\base_events.py", line 719, in run_until_complete
      return future.result()
             ~~~~~~~~~~~~~^^
    File "C:\Users\batool1\AppData\Roaming\Python\Python314\site-packages\uvicorn\server.py", line 68, in serve
      config.load()
      ~~~~~~~~~~~^^
    File "C:\Users\batool1\AppData\Roaming\Python\Python314\site-packages\uvicorn\config.py", line 467, in load
      self.loaded_app = import_from_string(self.app)
                        ~~~~~~~~~~~~~~~~~~^^^^^^^^^^
    File "C:\Users\batool1\AppData\Roaming\Python\Python314\site-packages\uvicorn\importer.py", line 21, in import_from_string
      module = importlib.import_module(module_str)
    File "C:\Python314\Lib\importlib\__init__.py", line 88, in import_module
      return _bootstrap._gcd_import(name[level:], package, level)
             ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "<frozen importlib._bootstrap>", line 1398, in _gcd_import
    File "<frozen importlib._bootstrap>", line 1371, in _find_and_load
    File "<frozen importlib._bootstrap>", line 1342, in _find_and_load_unlocked
    File "<frozen importlib._bootstrap>", line 938, in _load_unlocked
    File "<frozen importlib._bootstrap_external>", line 762, in exec_module
    File "<frozen importlib._bootstrap>", line 491, in _call_with_frames_removed
    File "C:\Users\batool1\Desktop\full-stack - Copy\backend\src\main.py", line 8, in <module>   
      from src.api import auth, todos
    File "C:\Users\batool1\Desktop\full-stack - Copy\backend\src\api\auth.py", line 9, in <module>
      from ..models.user import User, UserCreate, UserRead
    File "C:\Users\batool1\Desktop\full-stack - Copy\backend\src\models\user.py", line 13, in <module>
      class User(SQLModel, table=True):
      ...<12 lines>...
          sessions = Relationship(back_populates="user")
    File "C:\Users\batool1\AppData\Roaming\Python\Python314\site-packages\sqlmodel\main.py", line 593, in __init__
      raw_ann = cls.__annotations__[rel_name]
                ~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  KeyError: 'todos'
response_text: |
  I've identified and fixed the issue causing the KeyError: 'todos' in your SQLModel relationships. The problem was in the User model where the relationships were defined without proper type annotations that SQLModel could understand.

  I've updated the following files:

  1. `backend/src/models/user.py` - Added proper type annotations for the relationships:
     - Changed `todos = Relationship(back_populates="user")` to `todos: list["Todo"] = Relationship(back_populates="user")`
     - Changed `sessions = Relationship(back_populates="user")` to `sessions: list["SessionModel"] = Relationship(back_populates="user")`

  2. `backend/src/models/session.py` - Ensured proper type annotation:
     - Changed `user = Relationship(back_populates="sessions")` to `user: "User" = Relationship(back_populates="sessions")`

  3. `backend/src/models/todo.py` - Ensured proper type annotation:
     - Changed `user = Relationship(back_populates="todos")` to `user: "User" = Relationship(back_populates="todos")`

  The issue was that SQLModel needs explicit type annotations for relationships to properly understand the model structure during initialization. The KeyError occurred because the runtime couldn't find the 'todos' annotation in the class annotations dictionary.

  The server is now running successfully on http://0.0.0.0:8002.
outcome: |
  The KeyError: 'todos' issue in the SQLModel relationships has been successfully resolved by adding proper type annotations to all relationship fields in the models. The backend server is now running without errors.
evaluation: |
  The fix was successful - the server starts without the KeyError and database tables are synced properly. The solution follows SQLModel best practices for defining relationships with proper type annotations.
---
