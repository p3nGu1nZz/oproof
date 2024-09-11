from setuptools import setup, find_packages

setup(
    name='oproof',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tenacity',
        'rich',
        'loguru',
        'pydantic',
        'jinja2',
        'ollama',
        'flake8',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'oproof=oproof.main:Main.run'
        ],
    },
)
