from distutils.core import setup
setup(
  name = 'Topsis-Shikhar-102083055',         # How you named your package folder (MyLib)
  packages = ['Topsis-Shikhar-102083055'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Topsis Calculation',   # Give a short description about your library
  author = 'Shikhar Saini',                   # Type in your name
  author_email = 'shikharsaini25@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/shikharsaini',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Topsis', 'TopsisPackage'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',     
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)