from pythonforandroid.recipe import CompiledComponentsPythonRecipe


class CythonRecipe(CompiledComponentsPythonRecipe):

    version = '3.0.11-1'
    url = 'https://github.com/cython/cython/releases/download/{version}-1/cython-{version}.tar.gz'
    site_packages_name = 'cython'
    depends = ['setuptools']
    call_hostpython_via_targetpython = False
    install_in_hostpython = True


recipe = CythonRecipe()
