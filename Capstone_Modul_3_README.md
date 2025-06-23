## Overview
Project Capstone Modul 3 merupakan model machine learning yang dikembangkan dengan tujuan memprediksi harga properti (apartemen) di Kota Daegu, Korea. Model machine learning yang digunakan adalah XGBoost dengan nilai persentase error (MAPE) 18.86% atau tingkat akurasi prediksi yang baik pada segmen harga middle-low. Model machine learning ini masih perlu dikembangkan sehingga dapat memiliki tingkat akurasi prediksi pada segmen harga high yang lebih baik.

## Problem
1. Faktor apa yang secara dominan memengaruhi harga apartemen
2. Bagaimana performa model machine learning dapat memprediksi harga apartemen

## Strategy
1. Data cleaning
2. Data preprocessing
3. Modeling
4. Model tuning & feature engineering
5. Model comparison & evaluation

## Goals
1. Menentukan model terbaik dari beberapa pilihan model dengan target performa model machine learning yang harus dicapai yakni memiliki `nilai persentase error (MAPE) < 20%`
2. Menentukan fitur atau kriteria spesifikasi yang paling berpengaruh terhadap harga apartemen
3. Memberikan rekomendasi terkait harga apartemen untuk user maupun pemilik properti

## Kesimpulan
1. Model terbaik yaitu XGBoost setelah melalui proses Tuning dan Feature Engineering.
2. Model paling mengandalkan fitur/kriteria Ukuran Apartemen dan Jumlah Fasilitas sebagai prediktor utama.
3. Model dapat dikategorikan layak dengan tingkat persentase error di bawah 20%, yakni sebesar 18.86%, dimana hasil prediksi yang dihasilkan cukup akurat dengan nilai error yang masih dapat ditoleransi.
4. Limitasi model: Model cenderung mendapatkan akurasi yang tinggi pada data dengan spesifikasi umum (mainstream), namun memiliki potensi kurang akurat pada apartemen dengan spesifikasi yang tidak umum (outlier), dalam hal ini model kurang akurat untuk memprediksi harga apartemen yang tinggi (> 300,000 WON).
4. Rekomendasi Bisnis:
    a. Gunakan Model Ini Sebagai Pricing Guidance Tool:
    - Model dapat membantu user untuk menilai kewajaran harga jual suatu apartemen, sehingga dapat digunakan untuk mendeteksi harga yang terlalu tinggi atau terlalu rendah dari harga pasar.
    - Bagi Developer/Agen/Pemilik properti, perlu mempertimbangkan perluasan fasilitas tempat parkir dan penambahan fasilitas di dalam apartemen untuk dapat meningkatkan harga jual untuk properti yang sudah dibangun. Namun, apabila properti baru akan dibangun, tentu faktor luas atau ukuran apartemen menjadi faktor utama yang perlu dipenuhi sehingga harga jual semakin tinggi.
    b. Future Development:
    - Model bisa terus diperbarui dengan data harga terbaru, terutama diperlukan penambahan untuk segmentasi harga yang mahal karena hasil prediksinya masih kurang akurat. Bisa juga dengan menambahkan fitur lain seperti Developer Apartemen (Popularitas), View Apartemen, dan Fasilitas Mewah untuk hasil yang lebih akurat pada segmen harga mahal.
