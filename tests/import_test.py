
def test_import_lazy():
    import d4rl
    import sys
    assert "mujoco_py" not in sys.modules
    assert "dm_control" not in sys.modules
