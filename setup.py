from setuptools import setup


setup(
    zip_safe=True,
    name='news-cast',
    version='0.1',
    author='adaml',
    author_email='adam.lavie@gmail.com',
    packages=[
        'rest_service'
    ],
    license='LICENSE',
    description='A news-cast API for adding, updating or deleting articles.',
    install_requires=[
        'flask==0.12',
        'flask-restful==0.2.5',
        'sqlalchemy==1.1.5',
    ]
)
