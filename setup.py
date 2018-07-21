import setuptools


if __name__ == "__main__":
    setuptools.setup(
        name='ashape',
        version='0.1.0',
        install_requires=[],
        packages=setuptools.find_packages(),
        include_package_data=True,
        py_modules=['ashape'],
        data_files=[],
        entry_points={
            'console_scripts': [
                'ashape=ashape:main',
            ],
        },
    )
