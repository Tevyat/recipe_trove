# Recipe Trove

Made using the Flask module of Python. A website wherein users can upload their own recipes. Afterwards, they can delete or update their recipes.

This is an updated version of a [previous project](https://github.com/Tevyat/RecipeTrove).

## Preview

Search Page

![image](https://github.com/user-attachments/assets/c713a1c5-884c-41a0-a5b1-8d6e12234796)

Add Page

![image](https://github.com/user-attachments/assets/0d60b088-4143-41a6-9e5c-ac5f4f2a988c)

View Page

![image](https://github.com/user-attachments/assets/3bc609f8-c887-49c9-836f-3c3ec90f76e3)

## Run Locally

Create a virtual environment

```bash
  python -m venv <name_of_venv>
```

Clone the project

```bash
  git clone https://github.com/Tevyat/recipe_trove
```

Activate virtual environment

```bash
  # In cmd.exe
  venv\Scripts\activate.bat

  # In PowerShell
  venv\Scripts\Activate.ps1

  # In Linux/MacOS
  $ source myvenv/bin/activate
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  flask run
```

## Live Demo

[RecipeTrove](https://patrickpangilinan.pythonanywhere.com)

## License

[MIT](https://choosealicense.com/licenses/mit/)
