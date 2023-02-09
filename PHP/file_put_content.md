# file_put_content

file_put_contents —> Write data to a file

This function is identical to calling fopen(), fwrite() and fclose() successively to write data to a file.

If filename does not exist, the file is created. Otherwise, the existing file is overwritten, unless the FILE_APPEND flag is set.

