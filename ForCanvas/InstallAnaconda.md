#  Anaconda Python Distribution

Anaconda Python Distribution is a free (for personal use) Python distribution developed by [Anaconda, Inc.](https://www.anaconda.com) that provides several nice features and ease of installation. This is the generally recommended Python distribution for data science.

## Download

Go to [the Anaconda download site](https://www.anaconda.com/products/individual). Make sure you get the graphical installer for your operating system, and the 64-bit version. Direct links to the installers are below

|                                                              |                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Windows](https://repo.anaconda.com/archive/Anaconda3-2020.11-Windows-x86_64.exe) | [Mac](https://repo.anaconda.com/archive/Anaconda3-2020.11-MacOSX-x86_64.pkg) | [Linux](https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh) |

## Installation
Click the downloaded installer to run it and follow the directions. Installing Anaconda Python Distribution does not require administrator priviledges, since it installs for your account and not globally.

### On a Mac

|               Select windows from installation               |                                                              |
| :----------------------------------------------------------: | ------------------------------------------------------------ |
| <img src="image-20210318003827272.png" alt="image-20210318003827272" style="zoom:50%;" /> | <img src="image-20210318004029196.png" alt="image-20210318004029196" style="zoom:50%;" /> |
| <img src="image-20210318004117199.png" alt="image-20210318004117199" style="zoom:50%;" /> | <img src="image-20210318004143242.png" alt="image-20210318004143242" style="zoom:50%;" /> |

### On Windows



## Creating the computational environment for this class

Best practice when starting a Python project is to create and work in a computational environment specific to the project that has the appropriate packages. Traditionally these were called `virtualenv`. Anaconda created a similar environment called a _conda environment_, which we will use. 

In Canvas, you will find a file called *biof440_environment.yml*. This contains the specifications for the environment we will be using in this class. Download this file to your computer.

The Anaconda installation installed an app called Anaconda Navigator on your computer. You can access it from `Start Menu > Anaconda3 (64-bit) > Anaconda Navigator`  (Windows) or the Applications folder (Mac). On Linux you can start it from a terminal by typing `anaconda-navigator`. 

![image-20210318005406109](image-20210318005406109.png)

We're going to go to the **Environments** tab on the left.

![image-20210318005952180](image-20210318005952180.png)

This screen shows the Python packages installed with the installer. We will install a new computational environment using this screen. At the bottom, click on the **Import** button.

![image-20210318010138861](image-20210318010138861.png)

Click on the folder icon to load a specification file. Don't write in a name, since the file we'll load will take care of that. 

Find the *biof440_environment.yml* file that you downloaded from Canvas and select it.

![image-20210318010323193](image-20210318010323193.png)

Click **Import**. 

<img src="nav1.png" style="zoom:50%;" />

The following bit takes a few minutes to install. At the end of the process, you'll see the following screen.

![image-20210318012822604](image-20210318012822604.png)



## An alternative method using the terminal

You can also install the conda environment using a terminal and the command line. 

On Windows, you need to start **Anaconda Prompt** from `Start Menu > Anaconda3 (64-bit) > Anaconda Prompt (Anaconda3)`. On a Mac, you'd open the **Terminal** app from Applications.

In the terminal, you would type in the following command:

```shell
conda env create -f biof440_environment.yml
```

This will create the conda environment we will use on your computer.

![image-20210318012756518](image-20210318012756518.png)



