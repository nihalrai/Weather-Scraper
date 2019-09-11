from setuptools import setup

# Add requirements.txt as requirements
with open('./requirements.txt') as f:
    required = f.read().splitlines()

setup(name='weather-scraper',
      version='0.1',
      python_requires='>3.4.2',
      install_requires=required,
      author='Nihal Rai',
      author_email='niihalrai@gmail.com',
      packages=['weather'],
      zip_safe=False)