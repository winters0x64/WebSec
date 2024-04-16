# Prototype pollution

## Client Side PP

In javascript everything is an object, and when we do 


```js
let a = "sdc";
a.__proto__.admin = true;
a.admin // returns true
```

This happens because of prototype pollution, as in js when we create a string or any other instance of a datatype it inherits the properties of its parent object.

The prototype chaining is as follows

```
Object Object -> String Object -> a Object
```

We can access the keys of the prototype(parent object) of an object using ```__proto__```
and we can assign and values to the parent object, when the js engine looks for a value as in the above example like 'admin' it finds that it doesn't exist in the child object(here 'a') so it checks its parent object and finds that 'admin' key does exist in the parent object so ```a.admin``` returns true.

Once we have control over an objects prototype, the object is polluted.

So as of now we have a polluted object now we need to elevate it.

Now what if __proto__ is blocked, we can use another notation of accessing objects in js the box notation, ie 
```js
let a  = 'as';
a['constructor']['prototype']['admin']=1;
// OR
a.constructor.prototype.cool = 'damn';
```

Here ``constructor`` returns the object which created the the object so in case of ``a`` that would be the String object and then we assign the key to the prototype of ``a`` that would be the string object.

``Object.getPrototypeOf(a)`` returns the prototype of the object ``a``.


## Prototype pollution to RCE in kibana (CVE-2019-7609)

Michael found some cool gadgets in kibana, which leads to RCE from prototype pollution

[Kibana_RCE](https://research.securitum.com/prototype-pollution-rce-kibana-cve-2019-7609/)


Once prototype pollution is achieved we'll need to elevate it using gadgets
lets say there is a piece of code as follows, we need to find a property that is undefined
```js
let a = "as";
a.__proto__.cmd = "ls"; // pp 
eval(a.cmd) // PP gadget
```

We can overwrite Native Javascript APIs like fetch,defineProperty are all vulnerable If we have PP.


## Server Side PP

Server side PP sinks are often hard to detect due to their blind nature, But one thing is that we can use the --inspect with the node process to further debug the process and the test for sinks.