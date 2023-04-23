# Objects

Object is like a container which is used to store data, below is the example of a javascript object.

```
const car = {};
car.name = "Toyota"
car.color = "Red"
```

or 

```
const car = {
    name : "Toyota",
    color: "Red"
}
```
We can use the traditional dot notation as well as the bracket notation for accessing the contents of the Object.

## Constructor

Now there is constructor which is a way to create a javascript objects, first we define a shape of the object like this 

```
function Person(name) {
  this.name = name;
  this.introduceSelf = function () {
    console.log(`Hi! I'm ${this.name}.`);
  };
}
```

Now we just use ```const ar = new Person("Arun");``` to create a new object names ar, Hence constructor is the name of the class that is used to crate an object generally after the new keyword.
