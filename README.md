# ipyReload

Reload files when modified using the ipython magic function %run.


## Install 
https://anaconda.org/wolfiex/ipyreload

		conda install -c wolfiex ipyreload		


## Example use:

```python
			import ipyReload as ipr

			#lets follow changes in test.py
			ipr.watch( 'test.py' )

			''' We can do whatever we like here, use ipython normally'''
			
			#if we want to stop it auto updating we can kill the thread
			ipr.kill()
```

## Uses: 

Saves on load times for modules/ipython. Provides a fast interactive dev environment.
