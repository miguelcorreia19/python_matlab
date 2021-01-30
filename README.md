# python-octave

Simple API in Python 3, with flask, that runs scripts Matlab/Octave, in Docker environment.
This project depends of:
* `flask` and `oct2py` (python libraries)
* `octave` (Linux package that's come with octave_cli language)

## Run

Start container:

```sh
docker-compose up
```

## Examples

There are two examples:

* `fibonacci`: that calls [fibonacci.m](./python_octave/scriptsMatlab/) file and calculates the Fibonacci series for a **number**. 
```sh
http://localhost:5000/fibonacci/{number} 
```

* `factorial`: that calls [factorial.m](./python_octave/scriptsMatlab/) file and calculates the Factorial for a **number**. 
```sh
http://localhost:5000/factorial/{number} 
```
