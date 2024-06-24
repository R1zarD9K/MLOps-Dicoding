import tensorflow as tf

LABEL_KEY = "Liked"
FEATURE_KEY = "Review"


def transformed_name(key):
    """Rename feature yang ditransform."""
    return key + "_xf"


def preprocessing_fn(inputs):
    """Preprocess input column into transformed columns."""
    outputs = {}
    outputs[transformed_name(LABEL_KEY)] = tf.cast(inputs[LABEL_KEY], tf.int64)
    outputs[transformed_name(FEATURE_KEY)] = tf.strings.lower(
        inputs[FEATURE_KEY])
    return outputs
