from distutils.core import setup
import sys

sys.path.append('lakitu')
import lakitu


setup(name='lakitu',
      version='0.0.1',
      author='Karl Grzeszczak',
      author_email='karl@karlgrz.com',
      url='http://github.com/karlgrz/lakitu/',
      download_url='https://github.com/karlgrz/lakitu/files/',
      description='ec2 connection tool',
      long_description='ec2 connection tool'
      package_dir={'': 'lakiutu'},
      py_modules=['lakitu'],
      provides=['lakitu'],
      keywords='lakitu ec2 aws connect ssh',
      license='Lesser Affero General Public License v3',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Internet',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Scientific/Engineering :: GIS',
                  ],
     )