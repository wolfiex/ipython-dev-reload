from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

## test with python setup.py develop

setup(
      name='ipyreload',
      packages=['ipyreload'],
      version= 1.3,
      description='ipython productivity tools',
      long_description=readme(),
      url="https://github.com/wolfiex/ipython-dev-reload",
      keywords= 'ipython reload'.split(' '),
      author='Dan Ellis',
      author_email='ipyreload (at) danielellisresearch.com',
      license='MIT',
      zip_safe=False)
