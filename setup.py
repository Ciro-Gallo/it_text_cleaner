from distutils.core import setup
setup(
  name = 'it_text_cleaner',         # How you named your package folder (MyLib)
  packages = ['it_text_cleaner'],   # Chose the same as "name"
  package_data={'it_text_cleaner': ['resources/*.csv']}, # Necessary to include additional resources files (.csv in this case)
  version = '0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Cleans text in italian language. Designed for machine learning.',   # Give a short description about your library
  author = 'Ciro Gallo',                   # Type in your name
  author_email = 'ciro.gallo.sw@gmail.com',      # Type in your E-Mail
  url = 'https://www.cirogallo.com/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Ciro-Gallo/it_text_cleaner/archive/v0.2-beta.tar.gz',    # I explain this later on
  keywords = ['textclean', 'text', 'machinelearningpreprocess',"machinelearningtext"],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'unidecode',
          'pandas',
          'nltk'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
  include_package_data=True # Needed to include the .csv files in the dist
)
