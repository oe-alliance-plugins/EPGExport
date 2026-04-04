from setuptools import setup
import setup_translate

pkg = 'Extensions.EPGExport'
setup(name='enigma2-plugin-extensions-epgexport',
       version='3.0',
       description='EPGExport Plugin',
       package_dir={pkg: 'EPGExport'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'epgexport.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
