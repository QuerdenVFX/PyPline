# :movie_camera: PyPline :movie_camera:

### <ins><code style="color:red">PyPline is an educational project to help me to learn python and to improve my skills firstly. </code></ins>

PyPline is a pipeline tool to help VFX artist to have consistency and organization for any projects.
This project is a command line interface for VFX artists to help them to have a better workflow.

## Changelog:

### <ins>23/10/2024</ins>

:tada: **First release of PyPline** :tada:

First verion released with the following features:

- Add new project or shot
- Configure software list
- List all project created with PyPline
- Run software with selected project and shot (**<ins><code style="color:darkorange">Houdini only:</code></ins>** and set environment variables)

## Installation:

1. Download the latest version of PyPline from the [Releases](https://github.com/PyPline/PyPline/releases) page.
2. Extract the downloaded file to a folder of your choice.
3. Run the **PyPline.exe** file.
4. Configure your software list in the **config.csv** file using the <ins>**conf**</ins> command.

![Configuration window](https://gautier-rayeroux.fr/images/Git/Conf.jpg)
| | |
|-|-|
|Software| Write the name of the software you want to configure|
|Path| Write / Paste the path of the software executable|
|Matrices| Write the folder you want to use for your project. For exemple: cache flipbook render obj ...|
| Extension| Write the extension of your software file </br> <code style="color:darkred">WARNING:</code> </br> <code style="color:darkred">1. Make sure to use the same extension for all your project files </code> </br> <code style="color:darkred">2. One software can have multiple extensions file like Houdini (.hip, .hiplc and .hipnc) or Maya (.mb and .ma)</code>|

Press [ **+** ] button to add software to your configuration file.

Press [ **-** ] button to remove software to your configuration file.

Click on a line to edit the software configuration and press [ **Update** ] button to save the changes.

<code style="color:gold">For each software added to your configuration file will add a new command in the command list. You can use this command to run the software with the selected project and shot.</code>

## Commands:

There is the differents commands available on PyPine yet:
| Commands | Description |
|--|--|
| help | Obviously, this command show you the differents commands available |
|add|Create new project or shot|
|conf|Configure software list|
|list| Show you all project created with PyPline|
|go| Run software with selected project and shot|
|clear| Clear the command line app|
|reset| Reset work environment|
|close| Close PyPline app
