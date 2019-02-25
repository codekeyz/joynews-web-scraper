from setuptools import setup

setup(name='joyscraper',
      version='1.0.0',
      description='Module for getting news from the Joy News Ghana Website',
      author='Precious Keyz',
      author_email='ositachima.co@gmail.com',
      url='https://github.com/codekeyz/joynews-web-scraper',
      packages=['joyscraper'],
      install_requires=['beautifulsoup4', 'requests'],
      license='MIT',
      zip_safe=False
      )
