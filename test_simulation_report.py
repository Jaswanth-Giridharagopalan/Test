from simulation_report import classify_run


def test_at_limit_passes():
    assert classify_run(100) == "PASS"


def test_over_limit_fails():
    assert classify_run(101) == "FAIL"
