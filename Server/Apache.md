# Apache 

Apache is a http web server software that is very commonly used it used to host websites over the internet, It's default port number is 80 and it's default directory is /var/www/html, this is where a default index.html is located and will be displayed if we access localhost:80  or just localhost, 

Here we can add our own Website and we'll need to change the ownership of that folder coz it's in the root directory we have to change the ownership to our user for that use sudo chown -R $USER:$USER /var/www/html/your_website_name and then sudo chmod -R 755 /var/www/html/your_website_name, then we can start working on our website