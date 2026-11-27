import pytest
import av.hrtf_audio as mod

CASES = [
    ("source_pose_extrapolate", (1,)),
    ("hrtf_continuous_interp", (1,)),
    ("distance_gain_smooth", (1,)),
    ("occlusion_reverb_sync", (1,)),
    ("samplerate_recalc", (1,)),
    ("panning_latency_calib", (1,)),
    ("load_hrtf", (1,)),
    ("place_source", (1,)),
    ("render_hrtf", (1,)),
    ("present_hrtf", (1,)),
    ("validate_hrtf", (1,)),
    ("metrics_hrtf", (1,)),
    ("audit_hrtf", (1,)),
    ("fallback_hrtf", (1,)),
    ("determinism_hrtf", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
