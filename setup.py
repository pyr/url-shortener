from setuptools import setup, find_packages

with open('requirements.txt') as reqs:
    install_requires = [line for line in reqs.read().split('\n') if (
        line and not line.startswith('--'))
    ]

print("found install_requires: " + str(install_requires))

setup(name='url_shortener',
      version='0.5.6',
      description='Simple URL Shortener',
      url='https://github.com/pyr/url-shortener',
      author='Pierre-Yves Ritschard',
      author_email='pyr@spootnik.org',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      install_requires=install_requires,
      scripts=['bin/url-shortener'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3'
      ],
      zip_safe=False)
