from pytube import YouTube // pytube kütüphanesi
import os

link=input("İndirmek istediğiniz videonun urlsini giriniz: ")
yt=YouTube(link)
video=yt.streams.get_highest_resolution()
print("Bu işlem internet bağlantınıza bağlı sürede değişiklik yaratabilir.")
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
video.download(desktop_path)
print("Videonuz İndirildi!.")
