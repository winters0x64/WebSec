# What's the difference between containers and vms?

So an Operating system is differentiated into 2 layers kernel layer and the application layer, so a vm actually virtualises both the kernel and the application layer whereas a container will only virtualize the application layer hence that's why docker can be fast to start but a windows docker image won't work on a linux host, because the kernel is not getting virtualized as opposed to a virtual machine.

Also a running docker image is called a container.