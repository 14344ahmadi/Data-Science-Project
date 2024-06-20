# Data-Science-Project

# Installation Instructions

## Installing Python 3.12.1

We are using [Python-3.12.1](https://www.python.org/downloads/release/python-3121/) for the analysis. Look at using [pyenv](https://github.com/pyenv-win/pyenv-win) for version management (not required).

You will probably need `Windows installer (64-bit)`. Make sure to restart VSCode after installing Python.

You can check your Python version by typing `Python` in any terminal (like cmd). You should see something like this.:
```
Microsoft Windows [Version 10.0.19045.3803]
(c) Microsoft Corporation. All rights reserved.

C:\Users\Marijn Korthouwer>python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
For this project make sure you are using `Python 3.12.1`. If you see another version To exit python type: `exit()`.

## Installing Visual Studio Code (VSCode)
1. Download [VScode](https://code.visualstudio.com/download)
2. Install
3. Profit

## Cloning the repository

### Why Git? How do I use Git?
* [Git in 100 seconds](https://www.youtube.com/watch?v=hwP7WQkmECE)
* [Git in Visual Studio Code Tutorial](https://www.youtube.com/watch?v=i_23KUAEtUM)

### Install Git
1. Download Git:
Go to the official Git website: [Download Git](https://www.git-scm.com/downloads).

2. Install Git:
Follow the wizard's instructions

### Install GitHub Desktop:
1. Download and install [GitHub Desktop](https://desktop.github.com/).
2. Open GitHub Desktop
3. Sign in to your GitHub Account:

### Clone the Repository:

1. Click on the "File" menu at the top left corner of the GitHub Desktop window. Select "Clone repository..." from the dropdown menu.

2. Choose the Repository:
In the "Clone a repository" window that appears, you'll see a "URL" tab.
Paste the repository URL "https://github.com/14344ahmadi/Data-Science-Project" into the "URL" field.

3. Choose Local Path: Choose the local path where you want to clone the repository on your Windows machine. You can do this by clicking "Choose..." and selecting the desired folder or directory.
Clone the Repository:

4. Once the URL and the local path are set, click on the "Clone" button at the bottom right corner of the window.
Wait for Cloning:

GitHub Desktop will now start the cloning process. It will download the repository files to the specified local directory.
Access the Cloned Repository:

After the cloning process is complete, you'll be able to access the cloned repository from within GitHub Desktop.
Open in File Explorer or IDE:

You can choose to "Open in Visual Studio Code" to view and edit the code.

## Using virtual environment
I reccomend using a [virtual environment](https://linuxhostsupport.com/blog/why-using-a-python-virtual-environment-is-a-good-choice/), you can create a virtual environment as such:

1. Open the VSCode terminal
Click on Terminal > New Terminal

2. Install the `virtualenv` package

```powershell
pip install virtualenv
```

3. Creating the virtual environment
```powershell
virtualenv venv
```
This creates a virtual environment called `venv`. 

### (!) You might get an error (invalid execution policy, running scripts is disabled on this system)
This error can be fixed as follows. [source: StackOverflow](https://stackoverflow.com/questions/56199111/visual-studio-code-cmd-error-cannot-be-loaded-because-running-scripts-is-disabl):
1. Open Visual Studio Code
2. Press `ctrl+shift+p`
3. Type:
```vscode
Preferences: Open User Settings (JSON)
```


At the **top** of the JSON file add this (below the "\{"):
```json
    "terminal.integrated.defaultProfile.windows": "PowerShell",
    "terminal.integrated.profiles.windows": {
        "PowerShell": {
            "source": "PowerShell",
            "args": [
                "-ExecutionPolicy",
                "Bypass"
            ]
        }
    },
```

4. Activate the virtual environment
```powershell
./venv/Scripts/Activate
```
You will now see a `(venv)` in front of the command line cursor.

5. Now you can follow the instructions for installing packages from `requirements.txt`.

## Using the requirements file

### Installing packages
Packages can be installed using the command.
```powershell
pip install -r requirements.txt
```
### Adding packages
If you decide to add new packages to the project you can create/update the `requirements.txt` file using:
```powershell
pip freeze > requirements.txt
```
Make sure to tell others the requirements have changed.

## Creating a new (Jupyter) Notebook:
1. Open Visual Studio Code
2. Press `ctrl+shift+p`
3. Type: 
```vscode
create: New Jupyter Notebook
```

## Using Notebooks with the virtual environment

> (!) Make sure to select `venv` python interpreter at the top right of any notebook (.ipynb) files. It should say: `venv (Python 3.12.1)`
![Select venv](https://code.visualstudio.com/assets/docs/datascience/jupyter/native-kernel-picker.png)

This will make sure your notebook uses the packages installed in your virtual environment.
