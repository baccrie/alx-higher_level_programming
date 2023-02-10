#!/usr/bin/node


function factorial(arg) {
	if (arg == 0) {
		return (1)
	}
	return arg * factorial(arg - 1)
}

console.log(factorial(4))
