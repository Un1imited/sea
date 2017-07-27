import pytest
from sea import utils


def test_import_string():
    from sea.app import Sea
    import datetime
    assert utils.import_string('datetime.date') is datetime.date
    assert utils.import_string('datetime.date') is datetime.date
    assert utils.import_string('XXXXXXXXXXXX', True) is None
    assert utils.import_string('datetime.XXXXXXXXXXXX', True) is None
    assert utils.import_string('sea.app:Sea') is Sea
    m = utils.import_string('app.servicers:WdServicer')
    from app.servicers import WdServicer
    assert m is WdServicer
    with pytest.raises(ImportError):
        utils.import_string('notexist')
