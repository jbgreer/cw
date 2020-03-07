#!/usr/bin/python3 -d

import numpy as np
import simpleaudio as sa


class Didah:

    FS = 44100  # samples per second
    NUM_CHANNELS = 1
    BYTES_PER_SAMPLE = 2
    dit_sound = None
    dah_sound = None
    space_sound = None
    letter_space_sound = None
    word_space_sound = None

    def generate_tone(self, dur, freq):
        # Generate array with seconds*sample_rate steps between 0 and seconds
        t = np.linspace(0, dur, int(dur * Didah.FS), False)

        # Generate sine wave for frequency
        note = np.sin(freq * t * 2 * np.pi)

        # Ensure that highest value is in 16-bit range
        audio = note * (2**15 - 1) / np.max(np.abs(note))

        # Convert to 16-bit data
        audio = audio.astype(np.int16)
        return audio

    def generate_silence(self, dur):
        silence = np.zeros((int(Didah.FS*dur), 2))
        silence = silence.astype(np.int16)
        return silence

    def play_tone(self, audio):
        # Start playback
        play_obj = sa.play_buffer(audio, Didah.NUM_CHANNELS, 
                Didah.BYTES_PER_SAMPLE, Didah.FS)

        # Wait for playback to finish before exiting
        play_obj.wait_done()

    def dit(self):
        self.play_tone(Didah.dit_sound)

    def dah(self):
        self.play_tone(Didah.dah_sound)

    def space(self):
        self.play_tone(Didah.space_sound)

    def letter_space(self):
        self.play_tone(Didah.letter_space_sound)

    def word_space(self):
        self.play_tone(Didah.word_space_sound)


    def __init__(self, freq=440, wpm=25):
        self.freq = freq
        dit_dur = 6.0 / (5.0 * wpm)
        dah_dur = dit_dur * 3
        space_dur = dit_dur
        letter_space_dur = dit_dur * 3
        word_space_dur = dit_dur * 7
        #print("wpm:" + str(wpm) 
                #+ ", dit:" + str(dit_dur)
                #+ ", dah:" + str(dah_dur) 
                #+ ", space:" + str(space_dur)
                #+ ", letter:" + str(letter_space_dur) 
                #+ ", word:" + str(word_space_dur))
        Didah.dit_sound = self.generate_tone(dit_dur, freq)
        Didah.dah_sound = self.generate_tone(dah_dur, freq)
        Didah.space_sound = self.generate_silence(space_dur)
        Didah.letter_space_sound = self.generate_silence(letter_space_dur)
        Didah.word_space_sound = self.generate_silence(word_space_dur)


if __name__ == "__main__":
    cw = Didah()
    cw.dit()
    cw.space()
    cw.dit()
    cw.space()
    cw.dit()
    cw.letter_space()
    cw.dah()
    cw.space()
    cw.dah()
    cw.space()
    cw.dah()
    cw.letter_space()
    cw.dit()
    cw.space()
    cw.dit()
    cw.space()
    cw.dit()
    cw.word_space()
