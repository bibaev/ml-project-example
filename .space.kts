job("Train model") {
    container("tensorflow:2.2.0") {
        entrypoint("/bin/sh")
        args("train.sh")
    }

    container("tensorflow:2.2.0") {
        entrypoint("/bin/sh")
        args("evaluate.sh")
    }
}
