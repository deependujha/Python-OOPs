# Instance & Class variables

## Instance variables

- are associated with instance, and can be different for all instances.
- to check all the instance variables associated with an instance, use `__dict__`.

```python
print(f"{emp1.__dict__ }")
```

---

## Class variable

- are associated with the whole class, and are shared by all the instances.
- can be used to track some unique property, like, employee count, or yearly_increment.
- To update the class instance, update it using `CLASS_NAME.class_variable`.
- The updated value will be reflected in all the instances.

> But, if we update a class variable using any instance,
> it will simply create an instance variable for that instance
> and for the rest of the class & instances,
> the class variable will remain unchanged.

---

## Order of searching

When we use `instance.some_variable`, it first looks for the `instance variable`, and if unable to find, it will look for `class variable`.
