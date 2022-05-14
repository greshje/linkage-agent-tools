# Initial Setup and Install for Windows

This document walks through the exact steps required to successfully install and run link-agent-tools in a Windows environment.  

## Install Docker
Download and install Docker from here:
<br/>
[https://docs.docker.com/desktop/windows/install/](https://docs.docker.com/desktop/windows/install/)
<br/><br/>
<b>! ! ! The install executable must be run as administrator ! ! !</b>
<br/>
If the install is not run as administrator, some components (including some WSL and Linux virtual machine components) will not be properly installed.  
<br/>
<b>Notes on re-installing Docker</b>
<br/>
During the development process, it is not uncommon for the Docker environment to get corrupted. The Windows un-install program can be used to un-install Docker. However, <b>the un-install program does not un-install all of the data files used by docker.</b> Before running the un-install program, run the clean-docker.bat file from a cmd prompt. This file is located in the /win/bat folder of this project.  

## Clone and Checkout the Source Code
Create a folder to work out of (for example, I create a folder called _PPRL in my Eclipse workspace to hold the PPRL projects).  Create a fork/branch for your work.  Clone and check out the annon-link project and the link-agent-tools project.  

![clone anonlink](./img/clone-anonlink.PNG?raw-true "clone-anonlink")



