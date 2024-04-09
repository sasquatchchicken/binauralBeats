import random
import datetime
import numpy as np
import sounddevice as sd

class FluxCapacitor:
    def __init__(self):
        self.flux_state = False

    def generate_flux(self):
        # Simulate Flux Capacitor activation based on random chance (adjust as needed)
        self.flux_state = random.random() < 0.5  # Adjust probability as desired

    def is_fluxing(self):
        return self.flux_state

def generate_tone(frequency, duration, sample_rate=44100):
    """ Generate a pure tone at a specified frequency and duration """
    t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
    tone = np.sin(2 * np.pi * frequency * t)
    return tone

def play_stereo_tones(left_frequency, right_frequency, duration=1.0, sample_rate=44100):
    """ Play tones on left and right channels based on specified frequencies """
    left_tone = generate_tone(left_frequency, duration, sample_rate)
    right_tone = generate_tone(right_frequency, duration, sample_rate)
    
    stereo_tone = np.stack((left_tone, right_tone), axis=1)
    sd.play(stereo_tone, sample_rate)
    sd.wait()

def main():
    flux_capacitor = FluxCapacitor()
    print("Flux Capacitor: Online")
    print("Required power: 1.21 gigawatts")

    while True:
        input_date = input("Enter the date in YYYY-MM-DD format or 'exit' to quit: ")
        
        if input_date.lower() == 'exit':
            break
        
        try:
            year, month, day = map(int, input_date.split('-'))
            chosen_date = datetime.datetime(year, month, day)
            print(f"You've chosen {chosen_date.strftime('%B %d, %Y')}.")

            left_frequency = float(input("Enter frequency for left audio channel (in Hz): "))
            right_frequency = float(input("Enter frequency for right audio channel (in Hz): "))
            
            duration = float(input("Enter duration (in seconds): "))
            if duration <= 0:
                print("Please enter a positive duration.")
                continue
            
            # Play specified frequencies in stereo
            play_stereo_tones(left_frequency, right_frequency, duration)

            # Activate Flux Capacitor after playing tones
            flux_capacitor.generate_flux()
            
            if flux_capacitor.is_fluxing():
                print("Flux Capacitor is fluxing. Power level: 1.21 gigawatts. Prepare for temporal displacement!")
            else:
                print("Flux Capacitor did not flux. No temporal displacement occurred.")
        
        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

if __name__ == "__main__":
    main()
