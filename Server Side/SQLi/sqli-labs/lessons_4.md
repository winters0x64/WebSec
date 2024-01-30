# Outfiles

Lets take this query

select * from users into outfile "/tmp/test.txt", This will write the contents of the query into /tmp/test.txt

select * from users into dumpfile "/tmp/test.txt", Same as outfile but this function only takes the first row of the query if there are more than one row it will give us an error.

Now

select load_file("/etc/passwd") into outfile "/tmp/test4", This will load the contents of /etc/passd using load_file and then write it to /tmp/test4 using outfile

This helps us to dump into an outfile which would be of real use during attacks.