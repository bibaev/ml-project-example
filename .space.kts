job("Train model") {
    container("tensorflow/tensorflow:2.2.0") {
        entrypoint("python")
        args("/mnt/space/work/src/train.py", "/mnt/space/share/model")
    }

    container("tensorflow/tensorflow:2.2.0") {
        entrypoint("python")
        args("/mnt/space/work/src/evaluate.py", "/mnt/space/share/model")
    }
}
