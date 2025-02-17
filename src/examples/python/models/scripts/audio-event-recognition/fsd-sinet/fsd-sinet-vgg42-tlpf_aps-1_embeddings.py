from essentia.standard import MonoLoader, TensorflowPredictFSDSINet

audio = MonoLoader(filename="audio.wav", sampleRate=22050)()
model = TensorflowPredictFSDSINet(graphFilename="fsd-sinet-vgg42-tlpf_aps-1.pb", output="model/global_max_pooling1d/Max")
embeddings = model(audio)
