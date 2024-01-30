# Prototypes

## Prerequisite for learning prototype pollution

Here is an object literal in javascript

```js
const user = {
  username : "Arun",
  password : "N00B",
  //This below definition is called a method
  do_some: () => {
    console.log("Logged")
  }
}
```

Almost everything in javascript is objects under the hood.

```js
let myString = "";
Object.getPrototypeOf(myString);
```

This returns ```String.prototype```, Every object in javascript is related to some other object in javascript as in this case our string inherits all the properties of its prototype in this case the string prototype so when we create a string it already has the properties of its prototype such as toLowerCase().

So

```js
let myObject = {};
```
Even though this object has no properties it inherits the default properties of it's prototype that is the ```Object.prototype```.


### The prototype chain

So every object inherits properties from it's prototype which is also an
object so it inherits from it's own prototype so the prototype chain goes
up in heirarchy until we reach the ```Object.prototype``` which has it's prototype set to null,objects inherit properties not just from their immediate prototype, but from all objects above them in the prototype chain.

We can access an objects prototype using the ```__proto__``` keyword

eg: ```username.__proto__`

Prototypes can be used to modify already existing builtins of js as follows

```js
String.prototype.toUpperCase() = function(){
    console.log("Holy...Cow...")
}
```







