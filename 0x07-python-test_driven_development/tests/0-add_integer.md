>>> add_integer = __import__('0-add_integer').add_integer

Test
	>>> add_integer(1, 5)
	6

	>>> add_integer(-1, 8)
	7

	>>> add_integer(9, -26)
	-17

	>>> add_integer(3.7, 8)
	11

	>>> add_integer(12, 2.5)
	14

	>>> add_integer(-5, 2.6)
	-3

	>>> add_integer(-7.2, 12)
	5

	>>> add_integer(-4, -2)
	-6

	>>> add_integer(-6.2, -9.2)
	-15

	>>> add_integer(3.8, 2.2)
	5

	>>> add_integer(6, [6, 8, 9])
	Traceback (most recent call last):
		...
	TypeError: b must be an integer
	>>> add_integer()
	Traceback (most recent call last):
		...
	TypeError: add_integer() missing 1 required positional argument: 'a'
	>>> add_integer(10)
	108

	>>> add_integer(-1)
	97

	>>> add_integer(238e18383)
	Traceback (most recent call last):
		...
	OverflowError: cannot convert float infinity to integer
	>>> add_integer(float('nan'))
	Traceback (most recent call last):
     	       ...
	ValueError: cannot convert float NaN to integer
