SCRIPT = '''
def test_foo():
    pass
'''


def test_repeater_plugin(testdir):
    """ Testing if repeater plugin is working. """
    script = testdir.makepyfile(SCRIPT)
    result = testdir.runpytest('--repeat', '10', script)
    result.stdout.fnmatch_lines(['*10 passed*'])
    assert result.ret == 0
