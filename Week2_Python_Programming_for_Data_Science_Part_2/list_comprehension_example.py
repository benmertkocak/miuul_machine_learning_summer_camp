# Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe  çeviriniz ve başına NUM ekleyiniz. Numeric olmayan değişkenlerin de isimleri büyümeli.Tek bir list comprehension  yapısı kullanılmalı.

import seaborn as sns

df = sns.load_dataset("car_crashes")
var = df.columns

df.columns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]

# Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde"no" barındırmayan değişkenlerin isimlerinin sonuna"FLAG" yazınız.

import seaborn as sns

df = sns.load_dataset("car_crashes")
print([col.upper() + "_FLAG" if "NO" not in col.upper() else col.upper() for col in df.columns])

# Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerinisimlerini seçiniz ve yeni bir data frame oluşturunuz
import seaborn as sns

df = sns.load_dataset("car_crashes")
og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
print(new_df.head())