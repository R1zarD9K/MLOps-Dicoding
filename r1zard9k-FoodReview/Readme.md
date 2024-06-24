# Final Submission: Machine Learning Pipeline - Food Review Prediction
Nama: Rahmat Pratami

Username dicoding: r1zard9k

![Food Review](https://feedbacklabs.org/wp-content/uploads/2020/08/iStock-911978098-1254x627.jpg)


| | Deskripsi |
| ----------- | ----------- |
| Dataset | [Food Review Prediction](https://www.kaggle.com/datasets/d4rklucif3r/restaurant-reviews) |
| Masalah | Restoran sering kali menawarkan berbagai macam menu. Dengan menganalisis ulasan makanan dari pelanggan, restoran dapat memahami preferensi pelanggan dan menyesuaikan menu mereka untuk meningkatkan kepuasan pelanggan. Food Review Prediction dapat membantu dalam memahami tren dan preferensi pelanggan berdasarkan ulasan yang diterima. |
| Solusi machine learning | Dengan menganalisis ulasan makanan, model machine learning dapat memberikan rekomendasi untuk menu yang dapat ditingkatkan atau diubah. Misalnya, jika sebagian besar ulasan negatif terkait dengan suatu item menu tertentu, restoran dapat mempertimbangkan untuk menghapus atau memodifikasi item tersebut. |
| Metode pengolahan | Data ulasan awal pelanggan akan dibagi menjadi data pelatihan dan evaluasi dengan rasio 80:20. Selanjutnya, data akan divalidasi untuk mengidentifikasi anomali dan kemudian diproses untuk siap untuk pelatihan. Setelah pelatihan selesai, model akan dievaluasi dan dikirim ke endpoint yang siap untuk digunakan. |
| Arsitektur model | Arsitektur yang digunakan cukup sederhana, terdiri dari layer Embedding dan satu layer Dense sebagai lapisan yang tersembunyi. Karena ini adalah klasifikasi binar, fungsi aktivasi pada lapisan output menggunakan Sigmoid.|
| Metrik evaluasi | Metrik evaluasi yang digunakan yaitu ExampleCount, AUC, FalsePositives, TruePositives, FalseNegatives, TrueNegatives, dan BinaryAccuracy |
| Performa model | Model memiliki performa antara lain adalah AUC sebesar 75%, kemudian example_count 201, dengan BinaryAccuracy 70%, dan loss sebesar 2.772. Untuk False Negatives 34, False Positive 31, True Negative 64 dan True Positive 72. Model yang telah dibuat dapat dilakukan peningkatan performa, karena model belum cukup baik karena BinaryAccuracy masih dibawah 80% |
| Opsi deployment | Untuk deployment, sistem ini akan dideploy menggunakan platform dari cloudeka |
| Web app | [food-review-classifications](http://103.190.215.173:8501/v1/models/food-review/metadata)|
| Monitoring | Monitoring pada sistem ini dilakukan menggunakan prometheus dan grafana. Disini hanya dilakukan proses monitoring untuk menampilkan request yang masuk pada sistem yang akan menamplkan status pada tiap request yang dilakukan, pada sistem ini terdapat tiga status yang ditampilkan yaitu apabila proses request pada sistem klasifikasi not found, invalid argument dan proses klasifikasi berhasil ditandakan dengan ok |