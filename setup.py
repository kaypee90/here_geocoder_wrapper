from distutils.core import setup
setup(
  name = 'heregeocoder',
  packages = ['heregeocoder'],
  version = '0.10',
  license='MIT',
  description = 'Here Geocoder API wrapper',
  author = 'Kwabena Asante',
  author_email = 'asantekwabena2013@gmail.com',
  url = '',
  download_url = '',
  keywords = ['here', 'geocoder', 'api'],
  install_requires=[
          'requests',
      ],
  classifiers=[  # Optional
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)