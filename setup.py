"""Setup."""


from setuptools import setup

with open('README.md') as f:
    long_description = f.read()  # pylint: disable=invalid-name

TEST_DEPS = [
    'mock',
    'pytest',
]

EXTRAS = {
    'test': TEST_DEPS,
}

VERSION = '0.0.1'

setup(
    author='NIWC Pacific',
    name='statick-web',
    description='Statick analysis plugins for Web (css, html, js) files.',
    version=VERSION,
    packages=['statick_tool',
              'statick_tool.plugins.discovery',
              'statick_tool.plugins.tool'],
    package_dir={'statick_tool': '.',
                 'statick_tool.plugins.discovery': 'src/statick_web/plugins/web_discovery_plugins',
                 'statick_tool.plugins.tool': 'src/statick_web/plugins/web_tool_plugins'},
    package_data={'statick_tool': ['rsc/*'],
                  'statick_tool.plugins.discovery': ['*.yapsy-plugin'],
                  'statick_tool.plugins.tool': ['*.yapsy-plugin']},
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['statick'],
    tests_require=TEST_DEPS,
    extras_require=EXTRAS,
    url='https://github.com/sscpac/statick',
    classifiers=[
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
    ],
)
