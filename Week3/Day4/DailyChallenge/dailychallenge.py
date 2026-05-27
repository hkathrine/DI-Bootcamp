import math

class Circle():
    def __init__(self, radius: float):
        self._radius = float(radius)

    #Properties
    
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = float(value)

    @property
    def diameter(self) -> float:
        return self._radius * 2

    @diameter.setter
    def diameter(self, value: float):
        if value < 0:
            raise ValueError("Diameter cannot be negative")
        self._radius = float(value) / 2

    
    @classmethod
    def from_diameter(cls, diameter: float):
        return cls(diameter / 2)

    # S
    
    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    # Dunder methods

    def __repr__(self) -> str:
        return f"Circle(radius={self._radius})"

    def __str__(self) -> str:
    
        return f"A circle with radius = {self._radius:.2f} and diameter = {self.diameter:.2f}"

    def __add__(self, other: 'Circle') -> 'Circle':
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(self.radius + other.radius)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius == other.radius

    def __lt__(self, other: 'Circle') -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius < other.radius

    def __gt__(self, other: 'Circle') -> bool:
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius
    



# --- Decorator & Constructor Validation ---
c1 = Circle(3)                 # Created via radius
c2 = Circle.from_diameter(8)   # Created via diameter (radius becomes 4)

print(f"Query c1 radius: {c1.radius} (Expected: 3.0)")
print(f"Query c1 diameter: {c1.diameter} (Expected: 6.0)")
print(f"Query c2 radius (built from d=8): {c2.radius} (Expected: 4.0)\n")

# Updating via diameter setter
c1.diameter = 10
print(f"Diameter setter: changed d to 10. New c1 radius: {c1.radius} (Expected: 5.0)")
print("-" * 50)


# Requirement 1: Compute the circle's area
print("1. Compute Area:")
print(f"Area of c1 (r=5): {c1.area:.4f}")
print(f"Area of c2 (r=4): {c2.area:.4f}")
print("-" * 50)


# Requirement 2: Print attributes (__str__ and __repr__)
print("2. Print Attributes (Dunder Methods):")
# Triggers __str__
print("Using print(c1) [__str__]:")
print(c1) 

# Triggers __repr__ (when object is inside a collection)
print("\nInside a list [__repr__]:")
print([c1, c2])
print("-" * 50)


# Requirement 3: Add two circles together (__add__)
print("3. Add Two Circles (+):")
c3 = c1 + c2  # r=5 + r=4 should yield a new circle with r=9
print(f"c1 (r={c1.radius}) + c2 (r={c2.radius}) = c3 (r={c3.radius})")
print(f"Returned object type: {type(c3)} (Expected: <class '__main__.Circle'>)")
print("-" * 50)


# Requirement 4: Compare which is bigger (__gt__)
print("4. Compare Greater Than (>):")
print(f"Is c1 (r={c1.radius}) > c2 (r={c2.radius})? {c1 > c2} (Expected: True)")
print(f"Is c2 (r={c2.radius}) > c1 (r={c1.radius})? {c2 > c1} (Expected: False)")
print("-" * 50)


# Requirement 5: Check if equal (__eq__)
print("5. Check Equality (==):")
c4 = Circle(5)  # Create another circle with radius 5 (matches c1)
print(f"Is c1 (r={c1.radius}) == c4 (r={c4.radius})? {c1 == c4} (Expected: True)")
print(f"Is c1 (r={c1.radius}) == c2 (r={c2.radius})? {c1 == c2} (Expected: False)")
print("-" * 50)


# Requirement 6: Store in a list and sort (__lt__)
print("6. Store Multiple Circles and Sort:")
# Unsorted list of circles
circles_list = [Circle(10), Circle(2), Circle(5), Circle(1)]
print("List before sorting:")
print(circles_list)

# sorted() automatically invokes the __lt__ (<) method to sort the items
sorted_list = sorted(circles_list)
print("\nList after sorting (ascending order of radius):")
print(sorted_list)
print("-" * 50)

