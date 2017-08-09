port os, sys, glob
from distutils.core import setup

libdir = 'share/tubedown'
sys.path += [os.path.join(os.curdir, libdir)]

setup(name='tubedown',
      version='0.1',
      description='youtube-dl gui',
      license='GPL3',
      url='',
      author='Diego Sarzi',
      author_email='diegosarzi@gmail.com',
      scripts=['tubedown'],
      data_files=[(libdir, ['img/youtube.png'])]
      )
