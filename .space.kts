job("Train model") {
    container("tensorflow:2.2.0") {
        entrypoint("/bin/bash")
        args("train.sh")
    }

    container("tensorflow:2.2.0") {
        entrypoint("/bin/bash")
        args("evaluate.sh")
    }
}
