job("Train model") {
    container("tensorflow/tensorflow:2.2.0") {
        entrypoint("/bin/bash")
        args("train.sh")
    }

    container("tensorflow/tensorflow:2.2.0") {
        entrypoint("/bin/bash")
        args("evaluate.sh")
    }
}
