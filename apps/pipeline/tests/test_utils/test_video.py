from utils.video import video_snapshots


def test_video_processing():
    processed_frame_nrs = [frame_nr for _, frame_nr in video_snapshots("/tests/resources/sample.mp4", 2)]
    assert processed_frame_nrs == [60, 120], "Video not processed correctly"
