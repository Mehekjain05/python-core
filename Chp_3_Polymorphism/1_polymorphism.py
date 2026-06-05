# Polymorphism means "one interface, many forms."
#
# In simple terms, it allows you to use the same method name for different objects, and each object can behave differently.
#
# Real-life example
#
# Think of a remote control with a power button.
#
# On a TV, the power button turns on the TV.
# On an AC, the power button turns on the AC.
# On a speaker, the power button turns on the speaker.
#
# The button is the same, but the action depends on the device.


class Cat:
    def speak(self):
        return "meow!"

class Dog:
    def speak(self):
        return "woaf!"


# obj1 = Dog()
obj1 = Cat()
print(obj1.speak())

