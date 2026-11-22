إضافة للمرحلة الرابعة: نتائج أدق للحالة u=1.

الملف الرئيسي:
  notes/ES4-U1-SHARP-BOUNDS.md

برنامج البحث الدقيق:
  src/u1_factor_criterion.py

اختبارات:
  tests/test_u1_factor_criterion.py

التشغيل من جذر المشروع:
  .\.venv\Scripts\python.exe -m unittest discover -s tests -v
  .\.venv\Scripts\python.exe .\src\u1_factor_criterion.py

النتيجة الأساسية المضافة:
  a <= floor((p+11)/28)
  k <= floor((p+3)/20)

هذه حدود مثبتة لكل شاهد u=1 عند p أولي وp ≡ 1 (mod 24).
ولا تعني أنها تحل تخمين إردوش–شتراوس أو التخمين الفرعي u<=4.
