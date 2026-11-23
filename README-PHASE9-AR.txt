المرحلة التاسعة — دراسة أداء Phase 7 مقابل Phase 8

محتويات الحزمة:
- src/phase9_scaling.py
- tests/test_phase9_scaling.py
- notes/ES-PHASE9-SCALING-STUDY.md
- results/PHASE9-SCALING-RESULTS.csv
- results/PHASE9-SCALING-RESULTS.json
- results/PHASE9-SCALING-RESULTS.txt
- results/PHASE9-1E9-EXTENDED.json
- results/PHASE9-1E9-EXTENDED.txt

الاعتماديات:
- يجب أن تكون ملفات المشروع السابقة موجودة كما هي:
  src/phase7_floor_quotient.py
  src/phase8_small_factor.py
- لا تحتاج هذه المرحلة إلى أي مكتبة خارجية.

طريقة الاستخدام من جذر المشروع:
1) استخرج ZIP إلى مجلد المشروع الرئيسي دون حذف الملفات السابقة.
2) اختبر المرحلة التاسعة:

python -m unittest discover -s tests -p "test_phase9_scaling.py" -v

3) اختبر المشروع كله:

python -m unittest discover -s tests -v

4) أعد تنفيذ القياس الأساسي بخمس إعادات:

python src/phase9_scaling.py --repeats 5 --output-dir results/phase9-local

5) أعد تجربة المليار بشكل منفصل، بثلاث إعادات:

python src/phase9_scaling.py --primes 1000000009 --repeats 3 --output-dir results/phase9-local-1e9

6) تحفظ نتائج جهازك داخل مجلدين مستقلين، فلا تستبدل نتائج Linux المرفقة. افحص النتائج والملفات:

git status

7) بعد مراجعة النتائج، احفظ وارفع:

git add README-PHASE9-AR.txt src/phase9_scaling.py tests/test_phase9_scaling.py notes/ES-PHASE9-SCALING-STUDY.md results/PHASE9-SCALING-RESULTS.csv results/PHASE9-SCALING-RESULTS.json results/PHASE9-SCALING-RESULTS.txt results/PHASE9-1E9-EXTENDED.json results/PHASE9-1E9-EXTENDED.txt

# أضف نتائج جهازك بعد تشغيل القياس الأساسي:
git add results/phase9-local/

# أضف هذا المجلد فقط إذا نفذت اختبار المليار الاختياري:
git add results/phase9-local-1e9/

git diff --cached --stat

git commit -m "Add reproducible Type-II search scaling study"
git push
git status

تنبيهات:
- لا تنفذ git init أو git push --force.
- لا تحذف ملفات Phase 7 أو Phase 8.
- نتائج التوقيت تعتمد على الجهاز ونسخة Python.
- مرحلة 9 تقيس الأداء فقط، ولا تثبت التخمين الرياضي العام.
- ملفات النتائج المرفقة هي قياسات أُجريت في بيئة CPython 3.13.5/Linux، وليست نتائج جهازك.
