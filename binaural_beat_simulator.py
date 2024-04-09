import numpy as np
import sounddevice as sd

def generate_binaural_beat(frequency, binaural_frequency, duration, sample_rate=44100):
    """ Generate a binaural beat tone with specified frequencies """
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    
    # Create left and right channel tones
    left_tone = np.sin(2 * np.pi * frequency * t)
    right_tone = np.sin(2 * np.pi * (frequency + binaural_frequency) * t)
    
    # Combine tones for stereo playback
    stereo_tone = np.stack((left_tone, right_tone), axis=1)
    return stereo_tone

def play_binaural_beat(frequency, binaural_frequency, duration=10.0, sample_rate=44100):
    """ Play a binaural beat with specified frequencies """
    tone = generate_binaural_beat(frequency, binaural_frequency, duration, sample_rate)
    sd.play(tone, sample_rate)
    sd.wait()

def main():
    print("Welcome to the Binaural Beat Simulator!")

    while True:
        try:
            frequency = float(input("Enter base frequency (in Hz): "))
            binaural_frequency = float(input("Enter binaural frequency (in Hz): "))
            duration = float(input("Enter duration (in seconds): "))

            if frequency <= 0 or binaural_frequency <= 0 or duration <= 0:
                print("Please enter positive values for frequency, binaural frequency, and duration.")
                continue

            print(f"Playing binaural beat with base frequency {frequency} Hz and binaural frequency {binaural_frequency} Hz for {duration} seconds...")
            play_binaural_beat(frequency, binaural_frequency, duration)

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

        choice = input("Do you want to play another binaural beat? (yes/no): ").lower()
        if choice != 'yes':
            break

    print("toksa")

if __name__ == "__main__":
    main()
