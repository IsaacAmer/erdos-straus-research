المرحلة السابعة — حزمة مرشّح خارج القسمة الأرضية

محتويات الحزمة:
- src/phase7_floor_quotient.py
- tests/test_phase7_floor_quotient.py
- notes/ES-PHASE7-FLOOR-QUOTIENT-PREFILTER.md

طريقة الدمج:
1) استخرج ZIP إلى جذر المشروع الذي يحتوي على .git وsrc وtests وnotes.
2) من PowerShell داخل جذر المشروع نفّذ:

python -m unittest discover -s tests -p "test_phase7_floor_quotient.py" -v

python -m unittest discover -s tests -v

3) إذا نجحت الاختبارات، افحص الملفات الجديدة:

git status

4) ثم أضفها واحفظها وارفعها:

git add src/phase7_floor_quotient.py tests/test_phase7_floor_quotient.py notes/ES-PHASE7-FLOOR-QUOTIENT-PREFILTER.md README-PHASE7-AR.txt

git diff --cached --stat

git commit -m "Add floor-quotient prefilter for Type-II witnesses"

git push

git status

ملاحظات:
- لا تحذف أو تستبدل أي ملف قديم.
- لا تستخدم git init أو git push --force.
- الاختبار الجديد يحتوي على 9 اختبارات.
- المرشح يستبعد قيم k غير الممكنة قبل تحليل العوامل؛ اجتياز المرشح وحده لا يثبت وجود شاهد.
