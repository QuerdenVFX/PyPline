# 🎥 PyPline 🎥

### <ins><code style="color:red">PyPline is an educational project to help me learn Python and improve my skills.</code></ins>

PyPline is a pipeline tool designed to help VFX artists maintain consistency and organization for any project. This project is a command-line interface for VFX artists to improve their workflow.

## Changelog:

### <ins>23/10/2024</ins>

🎉 **First release of PyPline** 🎉

First version released with the following features:

- Add new project or shot
- Configure software list
- List all projects created with PyPline
- Run software with selected project and shot (**<ins><code style="color:darkorange">Houdini only</code></ins>** and set environment variables)

## Installation:

1. Download the latest version of PyPline from the [Releases](https://github.com/QuerdenVFX/PyPline/releases) page.
2. Extract the downloaded file to a folder of your choice.
3. Run the **PyPline.exe** file.
4. Configure your software list in the **config.csv** file using the <ins>**conf**</ins> command.

![Configuration window](https://gautier-rayeroux.fr/images/Git/Conf.jpg)
| | |
|-|-|
|Software| Write the name of the software you want to configure|
|Path| Write/Paste the path of the software executable|
|Directories| Write the folder you want to use for your project. For example: cache, flipbook, render, obj, etc.|
|Extension| Write the extension of your software file </br> <code style="color:darkred">WARNING:</code> </br> <code style="color:darkred">1. Make sure to use the same extension for all your project files </code> </br> <code style="color:darkred">2. One software can have multiple extensions, like Houdini (.hip, .hiplc, .hipnc) or Maya (.mb, .ma)</code>|

Press the [ **+** ] button to add software to your configuration file.

Press the [ **-** ] button to remove software from your configuration file.

Click on a line to edit the software configuration and press the [ **Update** ] button to save the changes.

<code style="color:gold">For each software added to your configuration file, a new command will be added to the command list. You can use this command to run the software with the selected project and shot.</code>

## Commands:

Here are the different commands available in PyPline so far:
| Commands | Description |
|--|--|
| help | Shows the available commands |
| add | Create a new project or shot |
| conf | Configure software list |
| list | Shows all projects created with PyPline |
| go | Run software with selected project and shot |
| clear | Clear the command-line app |
| reset | Reset the work environment |
| close | Close the PyPline app |
