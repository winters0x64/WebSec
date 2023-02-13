# Containers

Containers are actually stored as layers like there would be a layer for linux to run(mainly alpine), There would be other specific configuration layer for the specific application that we're trying to install

why this layer structure?

Lets say that we've downloaded an image with version number 1 and then we downloaded another image with version number 2 now this since some of the core layers are the same we don't have to download it again and this saves time.