# Music-Generation
Music Generation using deep learning


In this project we will be using a DCGAN to generate music as a midi file. We are using pianoroll data from the LAKH midi classical piano dataset, and are only using the melodies (right hand) of each file to train the model and produce piano melodies. 

This project is conducted with Monash DeepNeuron and credit to Valerio Vadari for ideas and code with data processing. https://github.com/musikalkemist/generating-melodies-with-rnn-lstm/tree/master

**Pre-Processing:**

    1. Download the midi files and labels from the datapath
    2. Get rid of all notes that are of unaccetable durations (for example tuplets)
    3. Transpose each song into the key of C major / A minor so that the model can learn melodies easier
    4. Create a piano roll matrix representation of the input data.
    5. Create a tensor holding the 2D matrix for every song, and a tensor with the labels of each song.

**Model:**

   We are using a conditional DCGAN model architechture to generate music. 
   The label vector and either noise or matrix (depending on generator or discriminator) are concatenated together before 
   going through the convolutional layers on both models.
   Adam optimizer is used with learning rates of 0.0001 for the discriminator and 0.0002 for the generator.


**Future Improvements and results**

    The generator creates some decent samples that for the most part are melodically sound but are not always rthymic. 
    A better preprocessing and matrix to midi file conversion algorithms will improve the quality of the outputs, as well as 
    a more balanced and larger dataset for the model to train on.
    
