المرحلة العاشرة — تدقيق جاكوبي لشواهد Type II

محتويات الحزمة:
- src/phase10_jacobi_audit.py
- src/phase10_demo.py
- tests/test_phase10_jacobi_audit.py
- notes/ES-PHASE10-JACOBI-AUDIT.md

الاعتماديات:
- يجب أن تبقى ملفات Phase 7 وPhase 8 في src كما هي:
  src/phase7_floor_quotient.py
  src/phase8_small_factor.py
- لا تحتاج المرحلة العاشرة إلى SymPy أو أي مكتبة خارجية.

طريقة الدمج:
1) استخرج ZIP إلى جذر المشروع، دون حذف أو استبدال ملفات سابقة.
2) اختبر المرحلة العاشرة:

python -m unittest discover -s tests -p "test_phase10_jacobi_audit.py" -v

3) اختبر المشروع كله:

python -m unittest discover -s tests -v

4) شغّل التدقيق وأنتج ملف الشهادات:

python src/phase10_demo.py

5) افحص Git:

git status

6) بعد نجاح الاختبارات، أضف الملفات الجديدة:

git add README-PHASE10-AR.txt src/phase10_jacobi_audit.py src/phase10_demo.py tests/test_phase10_jacobi_audit.py notes/ES-PHASE10-JACOBI-AUDIT.md results/PHASE10-JACOBI-AUDIT.json

git diff --cached --stat

git commit -m "Add Jacobi reciprocity audit for Type-II witnesses"
git push
git status

تنبيهات:
- قانون جاكوبي نفسه مأخوذ من Dahan, arXiv:2611.08717, Theorem 2.4؛ لا ندعي اكتشافه.
- المرحلة تدقق الشواهد التي يعيدها Phase 8 ولا تثبت وجود شاهد لكل أولي.
- لا تحذف أو تستبدل ملفات Phase 7 أو Phase 8 أو Phase 9.
- لا تستخدم git init أو git push --force.
