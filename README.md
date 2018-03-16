# ipyReload

Reload files when modified using the ipython magic function %run.


## Install 
https://anaconda.org/wolfiex/ipyreload

		conda install -c wolfiex ipyreload		
		pip install git+git://https://github.com/wolfiex/ipython-dev-reload/edit/master/README.md


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

			ipr.watch( 'test.py' , callbackfn)


```






## Uses: 

Saves on load times for modules/ipython. Provides a fast interactive dev environment.

## Future ideas:

Diff between current and previous file and only run new lines from the start of previous indent?
