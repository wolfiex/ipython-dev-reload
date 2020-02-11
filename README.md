# ipyReload

Reload files when modified using the ipython magic function %run.


## Install 
https://anaconda.org/wolfiex/ipyreload

		conda install -c wolfiex ipyreload		
		pip install --upgrade git+git://github.com/wolfiex/ipython-dev-reload/


## Example use:

```python
			import ipyReload as ipr

			#lets follow changes in test.py
			ipr.watch( 'test.py' )

			''' We can do whatever we like here, use ipython normally'''
			
			#if we want to stop it auto updating we can kill the thread
			ipr.kill()
```

## Or to use alternative callback functions:



```python
			import ipyReload as ipr
		
			def callbackfn():
				print 'hi, do this instead'
				# to run another file use :
				# ipython.magic("run " + filename)

			ipr.watch( 'test.py' , callbackfn)


```



## History - resubmit command
```python
			# glob history for all lines containing run  etc...
			ipr.hist('run *') 
			
			Select command to run from history

			(0, 'run other.py')
			(1, 'run test.py')
			(2, 'run tst.py')
			(3, "glob='run *'")
			
			Enter Selection:
			2
			
			# command is auto resubmitted
```


## No need for brackets when calling any functions
```python
			from ipyReload import *
			
			#previous method
			watch('filename.py')
			
			start()
			
			#new method - works for all functions you have
			watch filename.py
			
			

```			

## Uses: 

Saves on load times for modules/ipython. Provides a fast interactive dev environment.

## Future ideas:

Diff between current and previous file and only run new lines from the start of previous indent?
