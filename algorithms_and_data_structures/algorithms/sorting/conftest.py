import pytest


@pytest.fixture()
def test_cases():
    return {
        "empty": {
            "in": [],
            "out": []
        },

        "singleton": {
            "in": [4],
            "out": [4]
        },

        "reverse": {
            "in": [2, 1, 0, -1, -2],
            "out": [-2, -1, 0, 1, 2]
        },

        "complex": {
            "in": [2.3, 0.9, -1.3, 1.4],
            "out": [-1.3, 0.9, 1.4, 2.3]
        }
    }


@pytest.fixture()
def test_all_subjects(test_cases):
    def run_tests(test_subjects):
        for subject in test_subjects:
            for _, io in test_cases.items():
                assert subject.algorithm(io["in"]) == io["out"]

    return run_tests
