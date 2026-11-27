# pairwise-hrtf-spatial-audio

## 领域

游戏、图形与多媒体

## 主题

动态声源 HRTF 空间音频

## 说明

声源位置外推、HRTF 连续插值、距离增益平滑。

初始状态下 `av/hrtf_audio.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
