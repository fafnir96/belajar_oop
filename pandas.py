import pandas as pd

order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")
print(order_df.columns)
print(order_df.describe())

order_df["total_price"] = order_df["quantity"] * order_df["price"]

# 📌 Soal 1: Total Penjualan per Kategori Produk
category_total_price = (
    order_df["total_price"].groupby(order_df["product_category_name"]).sum()
)
print(category_total_price)

# 📌 Soal 2: Produk Terbanyak Terjual
top_quantity = (
    order_df["quantity"]
    .groupby(order_df["product_id"])
    .sum()
    .sort_values(ascending=False)
    .head(3)
)
print(top_quantity)

# 📌 Soal 3: Metode Pembayaran Populer
top_payment_type = order_df["payment_type"].value_counts()
print(top_payment_type)

# 📌 Soal 4: Transaksi Gagal
transaksi_gagal = order_df[order_df["order_status"] == "canceled"]
print(f"Jumlah Transaksi Gagal: {transaksi_gagal.shape[0]}")

# 📌 Soal 5: Persentase Transaksi Sukses
transaksi_sukses = order_df[order_df["order_status"] == "delivered"].shape[0]
presentase_sukses = (transaksi_sukses / order_df["order_status"].count()) * 100
print(f"Jumlah Presentase Sukses: {presentase_sukses}")

# 📌 Soal 6: Jumlah Pelanggan Unik
pelanggan_unik = order_df["customer_id"].nunique()
print(f"Pelanggan Unik: {pelanggan_unik}")

# 📌 Soal 7: Jumlah Produk Unik
product_unik = order_df["product_id"].nunique()
print(f"Produk Unik: {product_unik}")

# 📌 Soal 8: Kategori Produk Termahal
rata_rata_produk = order_df["price"].groupby(order_df["product_category_name"]).mean()
urutan_produk = rata_rata_produk.sort_values(ascending=False)
print(f"Produk Mahal: {urutan_produk}")

# 📌 Soal 9: Transaksi di Hari Sabtu
order_df["purchase_date"] = pd.to_datetime(order_df["purchase_date"])
sabtu_transaksi = order_df[order_df["purchase_date"].dt.day_name() == "Saturday"]

print(sabtu_transaksi[["product_category_name", "price", "purchase_date"]].head(5))

# 📌 Soal 10: Produk Favorit Setiap Metode Pembayaran
# grouped = order_df.groupby(["payment_type", "product_id"])["quantity"].sum()
grouped = (
    order_df["quantity"]
    .groupby([order_df["payment_type"], order_df["product_id"]])
    .sum()
)
grouped = grouped.reset_index()

favorit = grouped.sort_values(by="quantity", ascending=False).drop_duplicates(
    "payment_type"
)
print(favorit)
