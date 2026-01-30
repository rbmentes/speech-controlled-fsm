import numpy as np

def compute_energy(audio_signal):
    """
    Compute short-time energy of the audio signal.
    """
    return np.mean(audio_signal ** 2)


def is_speech(audio_signal, threshold=0.001):
    """
    Determine whether the input contains speech
    based on energy thresholding.
    """
    energy = compute_energy(audio_signal)

    if energy > threshold:
        return True, energy
    else:
        return False, energy


if __name__ == "__main__":
    # Simple test example
    test_signal = np.random.randn(16000) * 0.01
    speech, energy = is_speech(test_signal)

    print("Speech detected:", speech)
    print("Energy:", energy)
