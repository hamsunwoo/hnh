from hnh.utils import get_max_score

def test_max_p_label():
    p = [
        {'label': 'hot dog', 'score': 0.54},
        {'label': 'not hot dog', 'score': 0.46}
    ]

    r = get_max_score(p)
    assert r == "hot dog"
