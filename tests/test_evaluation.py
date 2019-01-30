import nose.tools
import evaluation
import numpy as np

def test_overall_chroma_accuracy():
    ref_cent = np.array([0, 0, 1195, 1800, 2405])
    est_cent = np.array([0, 0, 1200, 1200, 1200])
    ref_voicing = ref_cent>0
    est_voicing = est_cent>0
    score = evaluation.melody.overall_chroma_accuracy(ref_voicing, ref_cent, est_voicing, est_cent)
    assert np.allclose(0.8, score)

    # ref_cent = np.array([0, 0, 1395, 1800, 2605])
    ref_cent = np.array([0, 0, 1195, 1800, 2605])
    est_cent = np.array([0, 0, 0, 0, 0])
    ref_voicing = ref_cent > 0
    est_voicing = est_cent > 0
    score = evaluation.melody.overall_chroma_accuracy(ref_voicing, ref_cent, est_voicing, est_cent)
    assert np.allclose(0.4, score)

def test_voicing_accuracy():
    ref = np.array([])
    est = np.array([])
    score = evaluation.melody.voicing_accuracy(ref, est)
    assert np.allclose(0.0, score)

    ref = np.array([0,0])
    est = np.array([1])
    nose.tools.assert_raises(ValueError, evaluation.melody.voicing_accuracy, ref, est)

    ref = np.array([1, 1, 0, 0], dtype=np.bool)
    est = np.array([0, 1, 0, 1], dtype=np.bool)
    score = evaluation.melody.voicing_accuracy(ref, est)

    assert np.allclose(0.5, score)

    ref = np.array([1, 1, 0, 0], dtype=np.bool)
    est = np.array([1, 1, 0, 0], dtype=np.bool)
    score = evaluation.melody.voicing_accuracy(ref, est)

    assert np.allclose(1.0, score)

    ref = np.array([0, 0, 1, 1], dtype=np.bool)
    est = np.array([1, 1, 0, 0], dtype=np.bool)
    score = evaluation.melody.voicing_accuracy(ref, est)

    assert np.allclose(0.0, score)
