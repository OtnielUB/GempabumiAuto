# GempabumiAuto
Mengirimkan informasi gempa bumi terbaru melalui Discord dan Telegram.

## Fitur
1. **Discord**: Diimplementasikan menggunakan WebHook pada channel spesifik (grup bersifat private, tetapi Anda dapat mengaturnya sendiri).
2. **Telegram**: Diimplementasikan pada public channel [t.me/bot_by_otniel](https://t.me/bot_by_otniel).

## Cara Setup untuk Personal
1. Fork atau clone repository ini.
2. Dapatkan Webhook URL dari Discord dan/atau Bot Token & Chat ID dari Telegram.
3. Buka repository Anda di GitHub, pergi ke **Settings** > **Secrets and variables** > **Actions**.
4. Tambahkan *Repository secrets* berikut:
   - `DISCORD_WEBHOOK`: URL Webhook Discord Anda.
   - `TELEGRAM_TOKEN`: Token bot Telegram Anda (dari BotFather).
   - `TELEGRAM_CHAT_ID`: ID Chat atau Username Channel Telegram Anda (contoh: `@bot_by_otniel`).
5. Pergi ke tab **Actions** di repository GitHub Anda dan izinkan workflow untuk berjalan.
6. Workflow akan berjalan otomatis setiap 5 menit, atau Anda bisa menjalankannya secara manual dengan tombol **Run workflow**.