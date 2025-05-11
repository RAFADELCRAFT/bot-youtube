from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# === CAMBIA ESTA URL POR LA DE TU VIDEO DE YOUTUBE ===
video_url = "https://www.youtube.com/watch?v=Lrq8V3w-t5A"  # <-- Reemplaza esto
loop_times = 15  # Repetir 15 veces

# Configuración del navegador (modo headless)
chrome_options = Options()
chrome_options.add_argument('--headless')  # Ejecutar sin ventana visible
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Iniciar navegador
driver = webdriver.Chrome(options=chrome_options)

print(f"✅ Bot iniciado. Reproduciendo video: {video_url}")
print(f"🔁 Se repetirá {loop_times} veces.")

for i in range(loop_times):
    try:
        driver.get(video_url)
        print(f"\n🎬 Reproducción #{i + 1} iniciada.")
        
        # Espera de 11 horas por reproducción
        for remaining in range(11 * 60 * 60, 0, -1):
            mins, secs = divmod(remaining, 60)
            hours, mins = divmod(mins, 60)
            print(f"⏳ Tiempo restante: {hours:02d}:{mins:02d}:{secs:02d}", end='\r')
            time.sleep(1)
        
        print(f"\n✅ Reproducción #{i + 1} terminada.")
    
    except Exception as e:
        print(f"❌ Error en la reproducción #{i + 1}: {e}")
        break

driver.quit()
print("🏁 Finalizado. El bot ha terminado todas las reproducciones.")