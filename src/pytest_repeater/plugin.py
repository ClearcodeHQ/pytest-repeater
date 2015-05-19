def pytest_addoption(parser):
    """ Adding repeat argument for parser. """
    parser.addoption(
        '--repeat',
        action='store',
        help='Number of times to repeat each test'
    )


def pytest_generate_tests(metafunc):
    """ Repeating each test n times, based on --repeat argument. """
    if metafunc.config.option.repeat is not None:
        count = int(metafunc.config.option.repeat)
        metafunc.fixturenames.append('tmp_ct')
        metafunc.parametrize('tmp_ct', range(count))
