# CROSS ORIGIN READ BLOCKING(CORB)

In the context of web, "CORB" stands for Cross-Origin Read Blocking. It is a security feature implemented by web browsers to prevent cross-site scripting attacks.

To prevent these attacks, web browsers implement security measures such as the Same-Origin Policy, which restricts the ability of a website to access resources from a different origin. However, certain types of data, such as images, can be loaded and read across different origins, making them potential vectors for XSS attacks.

To address this issue, web browsers have implemented CORB, which blocks or restricts the ability of a website to read certain types of cross-origin resources, such as images and other media, if they are determined to be potentially dangerous. This helps to prevent XSS attacks by limiting the ability of malicious scripts to access sensitive information.

There are two types of data that can be requested from a server:

data resources such as HTML, XML, or JSON documents and

media resources such as images, JavaScript, CSS, or fonts.

Hence CORBS...