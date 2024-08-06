# Proyek Akhir: Menyelesaikan Permasalahan Human Resource pada Perusahaan

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### Permasalahan Bisnis

1. Perusahaan kesulitan dalam mengelola jumlah karyawan yang tergolong besar sehingga berimbas terhadap tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

2. Departemen Human Resource belum memiliki business dashboard untuk membantunya memonitori berbagai faktor yang dapat memantau dalam pengelolaan jumlah karyawan seperti tingginya attrition rate.

### Cakupan Proyek

1. Menganalisis kebutuhan (requirements) perusahaan yang terdiri atas tahapan
- Business Understanding
- Data Understanding
2. Mengembangkan model, yang terdiri atas tahapan
- Data preparation
- Modeling
- Model Evaluation
- Dashboard
3. Menggunakan model yang dihasilkan dengan menggunakan prediksi terhadap data inputan baru menggunakan model dengan evalusi terbaik.



### Persiapan

Sumber data: [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:

1. Pengguna telah menginstal Anaconda di komputer yang digunakan
2. Membuka terminal atau command prompt (cmd)
3. Buat Virtual Environment Baru:
```
conda create --name myenv python=3.8
conda activate myenv
```
5. Melakukan Install library yang digunakan:
Pastikan Anda menggunakan versi scikit-learn yang sama (misalnya 1.2.2):
```
pip install scikit-learn==1.2.2
pip install joblib pandas numpy
```
6. Menjalankan jupyter notebook
7. Membuka prediction.py :
```
python prediction.py
```
9. Menginput daya yang ingin diprediksi sesuai dengan label yang tertera pada terminal/cmd/command prompt
10. Mengisi semua data yang diperlukan dan tunggu hingga hasil prediksi keluar. 

- Metabase 
```
from sqlalchemy import create_engine

URL = "postgresql://postgres.zdnzmigbpzluxwvcebdp:JayaJayaMaju123@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

engine = create_engine(URL)
reshape_df.to_sql('employee_data', engine)
```
```
Host : aws-0-ap-southeast-1.pooler.supabase.com
Database name : postgres
port: 6543
user : postgres.gprvjwvcrejjcuyyvxaj
```

- Keterangan Dataset
```
The data contains demographic details, work-related metrics and attrition flag.

    EmployeeId - Employee Identifier
    Attrition - Did the employee attrition? (0=no, 1=yes)
    Age - Age of the employee
    BusinessTravel - Travel commitments for the job
    DailyRate - Daily salary
    Department - Employee Department
    DistanceFromHome - Distance from work to home (in km)
    Education - 1-Below College, 2-College, 3-Bachelor, 4-Master,5-Doctor
    EducationField - Field of Education
    EnvironmentSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
    Gender - Employee's gender
    HourlyRate - Hourly salary
    JobInvolvement - 1-Low, 2-Medium, 3-High, 4-Very High
    JobLevel - Level of job (1 to 5)
    JobRole - Job Roles
    JobSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
    MaritalStatus - Marital Status
    MonthlyIncome - Monthly salary
    MonthlyRate - Mounthly rate
    NumCompaniesWorked - Number of companies worked at
    Over18 - Over 18 years of age?
    OverTime - Overtime?
    PercentSalaryHike - The percentage increase in salary last year
    PerformanceRating - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
    RelationshipSatisfaction - 1-Low, 2-Medium, 3-High, 4-Very High
    StandardHours - Standard Hours
    StockOptionLevel - Stock Option Level
    TotalWorkingYears - Total years worked
    TrainingTimesLastYear - Number of training attended last year
    WorkLifeBalance - 1-Low, 2-Good, 3-Excellent, 4-Outstanding
    YearsAtCompany - Years at Company
    YearsInCurrentRole - Years in the current role
    YearsSinceLastPromotion - Years since the last promotion
    YearsWithCurrManager - Years with the current manager
```

## Business Dashboard
Akses dashboard melalui tautan yang disediakan docker melalui [link](http://localhost:3000/public/dashboard/cd5c7be7-8018-4176-9154-9c2073743a4c)

![san-limbong dashboard](https://github.com/user-attachments/assets/b13e4ced-0eb9-4de0-9b5d-24851dc740c2)


Analisis Dashboard 
Data yang digunakan berfokus terhadap pengurangan karayawan yang dilakukan (Attrition bernilai 1 or Yes) untuk mengindentifikasi perilaku yang menyebabkan keluarnya karyawan dari perusahaan tersebut.

1. Persentase berdasarkan performa karyawan (PerformanceRating)
Berdasarkan analisis yang dilakukan, urutan mayoritas yang keluar terdapat tingkatan Excellent (Sangat Baik) diikuti pada tingkat Outstanding (Luar Biasa)

2. Persentase berdasarkan Departement (Department)
Berdasarkan analisis yang dilakukan mayoritas karyawan yang keluar dari perusahaan berasal dari departemen Research & Development

3. Persentase berdasarkan Jenis Kelamin (Gender)
Berdasarkan analisis yang dilakukan mayoritas karyawan yang keluar berjenis kelamin Laki - laki

4. Persentase berdasarkan Kepuasan Terhadap Lingkungan Kerja (EnvironmentSatisfaction)
Berdasarkan analisis yang dilakukan mayoritas karyawan yang keluar memiliki tingkatan yang rendah (Low) terhadap kepuasan lingkungan kerja 

5. Persentase berdasarkan Work Life Balance
Berdasarkan analisis yang dilakukan mayoritas karyawan yang keluar berada pada tingkatan Sangat Baik (Excellent) pada Kondisi Work Life Balancenya.

6. Persentase berdasarkan Seberapa sering melakukan perjalan bisnis (BusinessTravel)
Berdasarkan analisis yang dilakukan mayoritas karyawan yang keluar berada pada tingkatan karyawan yang jarang melakukan perjalan bisnis (Travel_rarely)

7. Persentase berdasarkan Umur (Age)
Berdasarkan analisis yang dilakukan mayoritas karyawan yang keluar berada pada usia 31-32 sebanyak 14 orang diikuti usia 29-30 sebanyak 12 orang.

8. Persentase berdasarkan tingkatan pendidikan (Education)
Berdasarkan analisis yang dilakukan mayoritas karyawan yang keluar memilki riwayat pendidikan sebagai Sarjana (Bachelor)

9. Persentase berdasarkan jarak dari rumah terhadap kantor/perusahaan (Distance From Home)
Berdasarkan analisis yang dilakukan mayoritas karyawan yang keluar berjarak 2-3 KM dari rumah sebanyak 22 orang, diikuti jarak 1-2 KM sebanyak 20 orang


## Conclusion

Berdasarkan analisis yang dilakukan terhadap data attrition karyawan, beberapa pola dan faktor yang signifikan telah diidentifikasi. Berikut adalah kesimpulan utama dari analisis tersebut:

1. Persentase berdasarkan performa karyawan (PerformanceRating)
    - Mayoritas karyawan yang keluar memiliki tingkat performa Excellent (Sangat Baik), diikuti oleh tingkat Outstanding (Luar Biasa).
    - Hal ini menunjukkan bahwa karyawan dengan performa tinggi cenderung meninggalkan perusahaan, yang mungkin mengindikasikan ketidakpuasan meskipun kinerja mereka sangat baik.

2. Persentase berdasarkan Departement (Department)
    - Departemen Research & Development merupakan sumber terbesar karyawan yang keluar dari perusahaan.
    - Hal ini bisa mengindikasikan masalah spesifik dalam departemen tersebut, seperti budaya kerja, beban kerja, atau manajemen.

3. Persentase berdasarkan Jenis Kelamin (Gender)
    - Mayoritas karyawan yang keluar adalah laki-laki.
    - Hal ini menunjukkan adanya kemungkinan masalah yang lebih mempengaruhi karyawan laki-laki dibandingkan perempuan, atau bisa juga menunjukkan bahwa proporsi karyawan laki-laki yang lebih tinggi di perusahaan.

4. Persentase berdasarkan Kepuasan Terhadap Lingkungan Kerja (EnvironmentSatisfaction)
    - Mayoritas karyawan yang keluar memiliki tingkat kepuasan yang rendah (Low) terhadap lingkungan kerja.
    - Hal ini menunjukkan bahwa peningkatan kepuasan terhadap lingkungan kerja bisa menjadi langkah penting dalam mengurangi attrition.

5. Persentase berdasarkan Work Life Balance
    - Mayoritas karyawan yang keluar memiliki Work Life Balance pada tingkat Excellent (Sangat Baik).
    - Hal ini mungkin mengindikasikan bahwa meskipun Work Life Balance dianggap baik, faktor lain seperti kepuasan kerja, pengembangan karir, atau kompensasi mungkin tidak terpenuhi.

6. Persentase berdasarkan Seberapa sering melakukan perjalan bisnis (BusinessTravel)
    - Mayoritas karyawan yang keluar jarang melakukan perjalanan bisnis (Travel_Rarely).
    - Hal ini bisa menunjukkan bahwa perjalanan bisnis yang jarang mungkin berhubungan dengan kurangnya kesempatan pengembangan atau keterlibatan dalam proyek penting.

7. Persentase berdasarkan Umur (Age)
    - Karyawan yang keluar kebanyakan berusia 31-32 tahun, diikuti oleh usia 29-30 tahun.
    - Hal ini dapat menunjukkan bahwa rentang usia ini seringkali merupakan periode dalam karir ketika karyawan mencari peluang pengembangan lebih lanjut atau peningkatan karir yang mungkin tidak mereka temukan di perusahaan saat ini.

8. Persentase berdasarkan tingkatan pendidikan (Education)
    - Mayoritas karyawan yang keluar memiliki tingkat pendidikan Sarjana (Bachelor). 
    - Hal ini dapat menunjukkan bahwa karyawan dengan pendidikan Sarjana mungkin merasa kurangnya kesempatan untuk menggunakan atau mengembangkan keterampilan mereka di perusahaan.

9. Persentase berdasarkan jarak dari rumah terhadap kantor/perusahaan (Distance From Home)
    - Karyawan yang keluar kebanyakan tinggal pada jarak 2-3 KM dari kantor, diikuti oleh 1-2 KM. 
    - Hal ini dapat mengindikasikan bahwa jarak yang dekat tidak cukup untuk mempertahankan karyawan jika faktor-faktor lain seperti kepuasan kerja dan pengembangan karir tidak terpenuhi.

10. Hasil Evaluasi model terbaik ditemukan pada Gradient Boosting

### Rekomendasi Action Items (Optional)
1. Fokus pada Retensi Karyawan Berperforma Tinggi dengan mengidentifikasi serta menangani penyebab ketidakpuasan diantara karyawan tersebut.
2. Evaluasi dan Perbaiki Kondisi di Departemen Research & Development
3. Tingkatkan Kepuasan Lingkungan Kerja dengan melakukan survey ataupun kegiatan liburan bersama untuk menjalin kekerabatan.
4. Menunjau Kebijakan dan Manfaat Work Life Balance.
    Meskipun Work Life Balance dianggap baik, penting untuk memastikan bahwa manfaat ini benar-benar seimbang dengan kebutuhan pengembangan karir dan kepuasan kerja.

