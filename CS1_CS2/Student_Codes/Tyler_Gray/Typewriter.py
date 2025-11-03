import sys
import time
import random
import os
def typewriter_sound():
    """Play a simple typewriter sound using system beep"""
    # Different frequencies for variation
    if os.name == 'nt':  # Windows
        import winsound
        winsound.Beep(random.choice([800, 850, 900]), 50)
    else:  # Unix/Linux/Mac
        sys.stdout.write('\a')
        sys.stdout.flush()
def typewriter_print(text, sound=True):
    """
    Print text with a realistic typewriter effect.
    
    Args:
        text: String to print
        sound: Whether to play typing sounds (default True)
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        # Play sound occasionally (not every character, too annoying)
        if sound and random.random() < 0.3:
            try:
                typewriter_sound()
            except:
                pass  # Skip sound if it fails
        
        # Realistic typing delays
        if char == ' ':
            # Spaces are faster
            time.sleep(random.uniform(0.05, 0.1))
        elif char in '.,!?;:':
            # Pause after punctuation
            time.sleep(random.uniform(0.3, 0.6))
        elif char == '\n':
            # Longer pause for new lines
            time.sleep(random.uniform(0.4, 0.8))
        else:
            # Random typing speed for letters
            # Simulate bursts of fast typing and occasional slow downs
            if random.random() < 0.15:
                # Occasional slow character (thinking/looking at keyboard)
                time.sleep(random.uniform(0.25, 0.50))
            else:
                # Normal typing speed with variation
                time.sleep(random.uniform(0.01, 0.05))
    
    print()  # New line at end
# Example usage
if __name__ == "__main__":
    sample_text = """The quick brown fox jumps over the lazy dog. 
This is a test of the typewriter effect!
Notice how it pauses naturally at punctuation, and the speed varies randomly."""
    
    print("Starting typewriter effect...\n")
    time.sleep(1)
    
    typewriter_print(sample_text, sound=True)  # Set to True for sound
    
    print("\n--- Done! ---")