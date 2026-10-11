import flet as ft
import asyncio
import threading
from pyrogram import Client

# Pyrogram istemcisi (Termux / Flet için temel ayarlar)
# Session adı ve bot/userbot bilgileri
app_client = Client(
    "dreclipse_session",
    api_id=1234567,  # Kendi API ID'ni buraya yazabilirsin
    api_hash="your_api_hash"  # Kendi API Hash'ini buraya yazabilirsin
)

def main(page: ft.Page):
    page.title = "Dreclipse Core v4.8"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    # Arayüz Bileşenleri
    status_text = ft.Text("Durum: Bağlantı Bekleniyor...", color=ft.colors.RED_400, size=16)
    
    def start_bot_click(e):
        status_text.value = "Durum: Bot Başlatılıyor..."
        status_text.color = ft.colors.YELLOW_400
        page.update()
        
        # Arka planda Pyrogram çalıştırma thread'i
        def run_pyrogram():
            try:
                app_client.start()
                status_text.value = "Durum: Bot Aktif ve Çalışıyor! 🚀"
                status_text.color = ft.colors.GREEN_400
                page.update()
            except Exception as ex:
                status_text.value = f"Hata: {str(ex)}"
                status_text.color = ft.colors.RED_400
                page.update()

        threading.Thread(target=run_pyrogram, daemon=True).start()

    start_button = ft.ElevatedButton(
        text="Botu Başlat",
        on_click=start_bot_click,
        color=ft.colors.WHITE,
        bgcolor=ft.colors.BLUE_700
    )

    page.add(
        ft.Text("Dreclipse Core v4.8", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN_ACCENT),
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        status_text,
        ft.Divider(height=20, color=ft.colors.TRANSPARENT),
        start_button
    )

ft.app(target=main)
