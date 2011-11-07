import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = ['pyramid', 'apache-libcloud', 'pyramid_debugtoolbar']

setup(name='mist.io',
      version='0.1',
      description='cloud management web app',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='unweb.me',
      author_email='we@unweb.me',
      url='http://mist.io',
      keywords='web pyramid pylons',
      packages=find_packages('src'),
      package_dir = {'':'src'},
      namespace_packages=['mist'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="mistio",
      entry_points = """\
      [paste.app_factory]
      main = mistio:main
      """,
      paster_plugins=['pyramid'],
      )

