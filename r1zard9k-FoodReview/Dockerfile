FROM tensorflow/serving:latest

# Membuat direktori untuk model
RUN mkdir -p /models/food-review/1

# Menyalin model ke direktori yang sesuai
COPY ./serving_model_dir/food-review/1716985047 /models/food-review/1
COPY ./config /model_config

# Menetapkan variabel lingkungan
ENV MODEL_NAME=food-review
ENV MONITORING_CONFIG="/model_config/prometheus.config"
ENV PORT=8501

# Menambahkan entrypoint script
RUN echo '#!/bin/bash \n\n\
env \n\
tensorflow_model_server --port=8500 --rest_api_port=${PORT} \
--model_name=${MODEL_NAME} --model_base_path=/models/${MODEL_NAME} \
--monitoring_config_file=${MONITORING_CONFIG} \
"$@"' > /usr/bin/tf_serving_entrypoint.sh \
&& chmod +x /usr/bin/tf_serving_entrypoint.sh

# Mengubah entrypoint untuk menjalankan script yang baru ditambahkan
ENTRYPOINT ["/usr/bin/tf_serving_entrypoint.sh"]
