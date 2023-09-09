from typing import Union


def filter_wave(wave: Union[list, tuple], times: int) -> list:
    """Smooth the wave based on the formula,
        new_wave[i] = old_wave[i - 1] * 0.2 + old_wave[i] * 0.6 + old_wave[i + 1] * 0.2
        Loop the formula for {times} times

    Args:
        wave (list | tuple): input collection of values
        times (int): number of times the smoothing technique is applied

    Returns:
        list: smoothed wave
    """
    old_wave = wave.copy()

    for i in range(times):
        new_wave = [0] * len(old_wave)
        for i in range(len(wave)):
            if i == 0:
                new_wave[i] = int(old_wave[i] * 0.6 + old_wave[i + 1] * 0.2)
            elif i == len(wave) - 1:
                new_wave[i] = int(old_wave[i - 1] * 0.2 + old_wave[i] * 0.6)
            else:
                new_wave[i] = int(
                    old_wave[i - 1] * 0.2 + old_wave[i] * 0.6 + old_wave[i + 1] * 0.2
                )
        old_wave = new_wave
    return old_wave


# test case 1
if __name__ == "__main__":
    original_wave = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(filter_wave(original_wave, 1))
