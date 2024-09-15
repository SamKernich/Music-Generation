# Music-Generation
Music Generation using deep learning


In this project we will be using a DCGAN to generate music as a midi file. We are using pianoroll data from the LAKH midi dataset, and initially are only using the melodies (right hand) of each file to train the model and produce piano melodies. 

This project is conducted with Monash DeepNeuron and credit to Valerio Vadari for ideas and code with data processing. https://github.com/musikalkemist/generating-melodies-with-rnn-lstm/tree/master

**Pre-Processing:**

    1. Download the midi files and labels from the datapath
    2. Get rid of all notes that are of unaccetable durations (for example tuplets)
    3. Create a piano roll matrix representation of the midi files.
    4. Create a tensor holding the 2D matrix for every song, and a tensor with the labels of each song.

**Model:**

   We are using a DCGAN model architechture to generate music. The generator model 
