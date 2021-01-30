# python-matlab

Simple API in Python 3, with flask, that runs Matlab scripts, in Docker environment.
This project depends of:
* `flask` and `oct2py` (python libraries)
* `octave` (Linux package that's come with octave_cli language)

**Octave is an open-source interpreter. The Octave syntax (mathematics-oriented) is largely compatible with Matlab. [source](https://www.gnu.org/software/octave/)**

## Run

Start container:

```sh
docker-compose up
```

## Examples

There are two examples:

* `fibonacci`: that calls [fibonacci.m](./python_matlab/scriptsMatlab/) file and calculates the Fibonacci series for a **number**. 
```sh
http://localhost:5000/fibonacci/{number} 
```

* `factorial`: that calls [factorial.m](./python_matlab/scriptsMatlab/) file and calculates the Factorial for a **number**. 
```sh
http://localhost:5000/factorial/{number} 
```
