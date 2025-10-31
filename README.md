task
Bu loyiha **[*********] kompaniyasi uchun texnik topshiriq** bo‘lib, test API bilan ishlash ko‘nikmalarini namoyish etadi.  
Skript `POST` va `GET` so‘rovlar orqali server bilan muloqot qiladi, ma’lumotni qayta ishlaydi va yakuniy javobni konsolga chiqaradi.



Algoritm (ishlash jarayoni)
1. POST so‘rovi yuboriladi:  
   API manzili: `https://test.icorp.uz/interview.php`  
   JSON tarkibi:
     json
     {
       "msg": "Hello",
       "url": "https://webhook.site/...."
     }
     ```
   - Natijada birinchi qism kodi (`part1`) olinadi.

2. `part2` kodi webhook orqali avtomatik yuboriladi. Skript ushbu kodni **30 soniya** davomida kutadi.

3. Ikkala kod (`part1` va `part2`) Birlashtirilinadi va yakuniy kod hosil qilinadi.

4. Shu birlashtirilgan kod `GET` so‘rovi orqali yana `https://test.icorp.uz/interview.php` manziliga yuboriladi.

5. Server javobi (yakuniy xabar yoki xatolik) konsolga chiqariladi.


ishlatib ko'rish 
1. Loyihani klonlash yoki faylni yuklab olish:
   ```bash
   git clone https://github.com/alikkhan1680/icorp.git
   cd icorp
   va terminalda yokiy code editorda run qilish kifoya 
