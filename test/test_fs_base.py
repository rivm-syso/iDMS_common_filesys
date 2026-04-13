import pytest
from src.idms.common.filesys.fs_base import fsFactory

@pytest.mark.unit
def test_fsfactory():
    fs_factory = fsFactory()
    fs_factory.register("test_fs", "test_person", "test_optionText")

    assert {"test_fs": "test_person"} == fs_factory._fscreators
    assert {"test_fs": "test_optionText"} == fs_factory._optiontext