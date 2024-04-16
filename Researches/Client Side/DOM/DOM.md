# Hacking DOM

The Window object is the parent object in which a lot of global properties are defined.

```html
document.defaultView //Returns a reference to the window object
```

lets say for some reason ```document``` is blacklisted or something we can use something like 

```js
let node = document.createElement('div');
node.ownerDocument.defaultView.alert(1337)
```

## DOM Clobbering

**Window Level & Document Level**

When we create an html element with an id it creates an entry under the window object, so if id=x, then window.x or x would return the html element.

```html
<form id='x'></form>
```

```js
window.x // returns the form element
document.x // Does not return the form element
```

Now when we create an element with the name attribute set that will also create an object under the window object but this will also create an object under the document object as well that means

```html
<form name='y'></form>
```

```js
window.y // returns the form element
document.y // Also returns the form element
```

Only certain elements can be used to clobber the DOM using the name attr those are embed,form,iframe,image,img and object.

**Anchor Tags**

Now when we call toString() on an anchor tag it'll return the href attr, 
```html
<a id='x' href='http://example.com'></a>
```
```js
alert(x) //Calls toString internally since x is of type object, and href would be alerted
```

**2 Layer deep clobbering**

When two elements have the same id they'll form an HTML collection, which is an array we can then access individual elements as ``id.name`` or ``id[index]``
ie, we can access elements in same collection with giving ``name`` as well as ``index``

So we can do something like

```html
<a id='x'></a>
<a id='x' name='y' href='http://example.com'></a>
```

```js
x.y // Returns the second a tag
x[1] // Returns the second a tag
alert(x.y) // Alerts the href of second a tag
```

This doesn't work for three layers tho.

**3 Layer deep clobbering**

We can use form tags for this

```html
<form id='x' name='y'><input id='z' value=1337></form>
<form id='x'></form>
<script>
    alert(x.y.z.value) // Returns 1337
</script>
```

**Multi level clobbering**

We can use iframes for this

```html
<iframe name=foo srcdoc="<a id=bar href=clobbered:1337></a>"></iframe>
<style>
    @import 'https://garethheyes.co.uk';
</style>
<script>
    alert(foo) // Returns the iframe window object
    alert(foo.bar) // Returns the href of the a tag
</script>
```
As to why use the import statement is that the iframes srcdoc requires sometime to render in the DOM, so inorder to give enough time to pollute the value we're doing the import to delay the alert

**NOTE**
``We can use html encoding inside the srcdoc attr of iframe, so we can use any number qoutes as we want inside the srcdoc``

We can further nest as much iframes as we want inside the srcdoc and get a multilevel clobber chain going.

```html
    <iframe srcdoc="<iframe srcdoc='<iframe name=c srcdoc=<a/id=d&amp;amp;#x20;name=e&amp;amp;#x20;href=\clobbered:1337&amp;amp;gt;<a&amp;amp;#x20;id=d&amp;amp;gt;> >' name=b>" name=a>
```

Here whilst we can use html encoding to surpass the single qoute and double qoute limitation we need to HTML encode as much times as we're nesting the iframe.

With DOM clobbering we can evade filters, by clobbering attributes of elements native DOM tags etc etc

**Clobbering getElementId()**

```html
<div id="x"></div>
<body id="x">
<script>alert(document.getElementById('x'))</script>
```

Normally getElementById returns the first element but since we're using body/html (which will placed above in the HTML collection) it will return the body tag. Same technique can be applied for querySelector() as well.


References : Javascript for hackers - gareth hayes