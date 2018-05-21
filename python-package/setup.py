from setuptools import setup

setup(name='ml_2048',
      version='0.1',
      description='A bot playing 2048',
      author='Emmanuel-Lin Toulemonde',
      author_email='el.toulemonde@protonmail.com',
      license='MIT',
      test_suite="tests",
      packages=['game'],
      zip_safe=False)