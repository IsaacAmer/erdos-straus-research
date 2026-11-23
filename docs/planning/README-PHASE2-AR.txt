حزمة المرحلة الثانية — قاموس المعايير: Rosati / Dahan / Pomerance–Weingartner

الغرض
-----
هذه الحزمة تنظّم تحويلات جبرية بين معايير معروفة لوجود تمثيل Erdős–Straus لعدد أولي p ≡ 1 (mod 4). وهي ليست برهانًا للتخمين الأصلي، ولا تدّعي اكتشاف معيار جديد.

تصحيح توثيقي مهم
----------------
- Dahan Theorem 3.9 + Lemma 3.10: معيار Type II ذو المعاملين u,a.
- Dahan Theorem 3.14: صحة/تعقيد Algorithm 2، وليس معيار Type I.
- Pomerance–Weingartner Corollary 2.2: معيار Type I.
- Pomerance–Weingartner Corollary 2.4: معيار Type II.
- Salez 2014, Proposition 1: الصيغ المعيارية لمعياري Rosati.

التركيب
------
src/rosati_dahan_bridge.py
    تحويلات Rosati مع شاهد Dahan Type II، وتحويل Type I المعياري الذي يطابق P&W Corollary 2.2. أسماء بعض الدوال القديمة محفوظة للتوافق، لكن أوصافها داخل الملف توضّح أن Type I ليس من Dahan Theorem 3.14.

src/parameter_dictionary.py
    التحويلات الصريحة بين Rosati وDahan Type II وP&W Type I/II.

tests/
    اختبارات حتمية، وتحويل ذهاب وإياب، وأمثلة مع gcd تطبيعي أكبر من 1، ومسوح محدودة لشهود مولّدة.

التشغيل على Windows PowerShell
------------------------------
انتقل إلى مجلد المشروع الداخلي، ثم شغّل:

.\.venv\Scripts\python.exe -m unittest discover -s tests -v

.\.venv\Scripts\python.exe .\src\rosati_dahan_bridge.py

لا تحتاج الحزمة إلى SymPy أو NumPy أو أي مكتبة خارجية؛ تستخدم مكتبات Python القياسية فقط.

تفسير الاختبارات
----------------
نجاح الاختبارات يثبت أن التنفيذ البرمجي يحقق العلاقات التي اختبرناها على الحالات المولّدة. ولا يثبت أن جميع الشهود موجودة لكل عدد أولي، ولا يثبت تخمين Erdős–Straus.
