import os
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
FRONTEND_DIR = PROJECT_DIR.joinpath("frontend")


def init_project():
    os.system("pip install -r requirements.txt")
    os.system(f"cd {FRONTEND_DIR.absolute()} && npm ci && npm run build")
    os.system("python manage.py migrate")
    os.system("python manage.py runserver")

is_pve_activated_answers = {"yes": "yes it is", "no": "no"}

while True:

    is_pve_activated = input(
        f"Is the python virtual environment currently activated ? ['{is_pve_activated_answers['yes']}/{is_pve_activated_answers['no']}'] : "
    )

    if is_pve_activated == is_pve_activated_answers["yes"]:
        init_project()
        break
    elif is_pve_activated == is_pve_activated_answers["no"]:
        print("A python virtual environment must be activated.")
        break
    else:
        print(f"Your answer is must be either '{is_pve_activated_answers['yes']}' or '{is_pve_activated_answers['no']}'.")

