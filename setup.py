from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()


setup(
      name='ipyReload',
      packages=['ipyReload']
      version='0.01.00',
      description='rerun an ipython program upon modification',
      long_description=readme(),
      url="https://github.com/wolfiex/ipython-dev-reload",
      keywords= 'ipython reload'.split(' '),
      author='Dan Ellis',
      author_email='daniel.ellis.research@gmail.com',
      license='MIT',
      install_requires=['IPython'],
      zip_safe=False)
