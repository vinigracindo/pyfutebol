from setuptools import setup


setup(name='pyfutebol',
      version='2.2.0',
      description='Crawler para resultados de futebol',
      url='https://github.com/vinigracindo/pyfutebol/',
      author='Vinnicyus Gracindo',
      author_email='vini.gracindo@gmail.com',
      license='MIT',
      packages=['pyfutebol'],
      install_requires=[
        'beautifulsoup4',
      ],
      zip_safe=False)