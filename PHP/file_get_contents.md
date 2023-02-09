# file_get_contents

file_get_contents(
    string $filename,
    bool $use_include_path = false,
    ?resource $context = null,
    int $offset = 0,
    ?int $length = null
): string|false

file_get_contents — Reads entire file into a string

This function is similar to file(), except that file_get_contents() returns the file in a string, starting at the specified offset up to length bytes. On failure, file_get_contents() will return false.

A "resource context" in PHP is an optional parameter that allows you to modify the behavior of certain functions, such as file operations, by providing additional information about the context in which the operation should be performed. For example, a resource context can be used to specify the connection timeout when reading a remote file over HTTP, or the encoding to be used when reading a text file.

In this example, a resource context is created using the stream_context_create function, which takes an array of options that describe the context. The created resource context is then passed as the third parameter to file_get_contents to specify the behavior when reading the file.

The offset where the reading starts on the original stream. Negative offsets count from the end of the stream.

Maximum length of data read. The default is to read until end of file is reached. Note that this parameter is applied to the stream processed by the filters.

