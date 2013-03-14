from setuptools import setup, find_packages

print(find_packages())
setup(name='url_shortener',
      version='0.5.0',
      description='Simple URL Shortener',
      url='https://github.com/pyr/url-shortener',
      author='Pierre-Yves Ritschard',
      author_email='pyr@spootnik.org',
      license='Private',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['redis', 'flask'],
      scripts=['bin/url-shortener'],
      zip_safe=False)
