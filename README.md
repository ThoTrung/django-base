# Recipe App API (v2) Source Code

This is the code for the second edition of the course that was released in 2022.

Course code for: [Build a Backend REST API with Python &amp; Django - Advanced](https://londonapp.dev/c2)


# Setting github action job
https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment


# Add SimpleJWT token
```
  curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"email": "tho.nt@gmail.com", "password": "123456"}' \
  http://localhost:8880/api/token/
```


# Log changed DB
https://django-auditlog.readthedocs.io/en/latest/usage.html


# Clear docker none
docker rmi $(docker images -a|grep "<none>"|awk '$1=="<none>" {print $3}')

# Theme
https://upmin-react.blueupcode.com/




import pathlib
import re
pattern = re.compile(r"^02 - *$")
directory_path = pathlib.Path('/LocalDrive/')
for subfolder_path in directory_path.glob(f"*"):
    print(subfolder_path.resolve())
    # if subfolder_path.is_dir():


from pathlib import Path
import os

for path in Path('/LocalDrive/sub*/Input').rglob('*'):
for path in Path('/LocalDrive/sub*').rglob('*'):

for path in Path('/LocalDrive/').glob('sub*/Input'):
for path in Path('/LocalDrive/').glob('sub*/Input/*/'):
    print(path.resolve())
    print(datetime.fromtimestamp(path.lstat().st_mtime).strftime('%Y-%m-%d %H:%M'))
    if path.is_dir():



import os
from pathlib import Path

for path in Path('/LocalDrive/').glob('sub*/Input/*'):
    if path.is_dir():
        print(os.listdir(path))


# Transistion
https://hashedin.com/blog/a-guide-to-managing-finite-state-machine-using-django-fsm/

# Logger
https://cheat.readthedocs.io/en/latest/django/logging.html
https://xxx-cook-book.gitbooks.io/django-cook-book/content/Logs/Handlers/FileHandler/timed-rotating-file-handler.html
