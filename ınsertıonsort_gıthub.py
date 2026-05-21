import time
import random
import tracemalloc
import matplotlib.pyplot as plt

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def test_ve_olcum(veri_seti, senaryo_adi, boyut):
    tracemalloc.start() # Bellek (RAM) ölçümü
    baslangic_zamani = time.time() # Kronometre başlangıç
    
    insertionSort(veri_seti) # Algoritmayı çalıştırır
    
    bitis_zamani = time.time() # Kronometre durdur
    _, peak = tracemalloc.get_traced_memory() # Tüketilen maksimum bellek ölçümü
    tracemalloc.stop() # Bellek ölçümü durdur
    
    gecen_sure = bitis_zamani - baslangic_zamani
    peak_kb = peak / 1024 # Byte'ı Kilobyte'a çevir
    
    print(f"[{boyut} Eleman] {senaryo_adi} | Süre: {gecen_sure:.4f} sn | Bellek: {peak_kb:.2f} KB")
    return gecen_sure

if __name__ == "__main__":
    # Test edilecek farklı veri boyutları 
    boyutlar = [1000, 5000, 10000] 
    
    # Grafiği çizebilmek için süreleri tutacağımız listeler
    sureler_rastgele = []
    sureler_sirali = []
    sureler_ters = []

    print("Proje Testleri Başlıyor, lütfen bekleyin...\n")

    for boyut in boyutlar:
        # Veri setlerini otomatik üret
        rastgele_veri = [random.randint(1, 100000) for _ in range(boyut)]
        sirali_veri = list(range(1, boyut + 1))
        ters_sirali_veri = list(range(boyut, 0, -1))

        # Testleri çalıştır 
        sure_rastgele = test_ve_olcum(rastgele_veri.copy(), "Rastgele Veri", boyut)
        sureler_rastgele.append(sure_rastgele)

        sure_sirali = test_ve_olcum(sirali_veri.copy(), "Sıralı Veri (En İyi)", boyut)
        sureler_sirali.append(sure_sirali)

        sure_ters = test_ve_olcum(ters_sirali_veri.copy(), "Ters Sıralı (En Kötü)", boyut)
        sureler_ters.append(sure_ters)
        
        print("-" * 65) 

    print("Testler bitti! Grafik ekranda açılıyor...")

    plt.figure(figsize=(10, 6))
plt.plot(boyutlar, sureler_rastgele, label='Rastgele Veri', marker='o', color='blue')
plt.plot(boyutlar, sureler_sirali, label='Sıralı Veri (Best Case)', marker='s', color='green')
plt.plot(boyutlar, sureler_ters, label='Ters Sıralı (Worst Case)', marker='^', color='red')

plt.title('Insertion Sort Zaman Karmaşıklığı Analizi')
plt.xlabel('Veri Boyutu (Eleman Sayısı)')
plt.ylabel('Çalışma Süresi (Saniye)')
plt.legend()
plt.grid(True)
plt.show() 