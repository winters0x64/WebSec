# Docker

Docker is a software platform that allows you to build,test,deploy applications quickly, Docker packages software into standardized units called containers that has everything the software needs to run including libraries,system tools,code and runtime.

# Containers

-> A way to package application with all the necessary dependancies and configuration.
-> It's portable, can easily be shared and moved around.
-> Makes development and deployment more efficient.

# Where do we store the containers 

-> We store the containers in a repository, On such collection of docker containers is the docker hub.

# But why Containers?

So before the concept of containers were introduced, lets say that you have to make a webapp so you'd have to install some database management system like postgresql,mysql etc , you'd have to install some frontend libraries like react js etc also you'd have to configure all these software then only you could build something this in itself is a tedious process Now imagine that your team consist of 10 people now all the 10 people have to install all these dependencies individually on their computers which is really a hassle so we use containers, containers are basically an isolated virtual machine all the dependencies and packages are already installed for the project and we just have to run the container, so container acts as different environment on top of our existing operating system , this environment is bundled with all the dependencies and software we need to make the project, so no need to install anything hence the time is saved.

