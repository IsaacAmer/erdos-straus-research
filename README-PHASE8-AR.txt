المرحلة الثامنة — بحث العامل الأصغر دون تحليل عوامل العدد

محتويات الحزمة:
- src/phase8_small_factor.py
- tests/test_phase8_small_factor.py
- notes/ES-PHASE8-SMALL-FACTOR-SEARCH.md

المتطلبات:
- يجب أن تكون المرحلة السابعة موجودة في src/phase7_floor_quotient.py.
- لا تحتاج المرحلة الثامنة إلى مكتبات خارجية؛ تستخدم مكتبة Python القياسية فقط.

طريقة الدمج:
1) استخرج ZIP إلى جذر المشروع الذي يحتوي على .git وsrc وtests وnotes.
2) لا تحذف ولا تستبدل أي ملف سابق.
3) من PowerShell داخل جذر المشروع نفّذ:

python -m unittest discover -s tests -p "test_phase8_small_factor.py" -v

python -m unittest discover -s tests -v

4) إذا نجحت الاختبارات، افحص الملفات:

git status

5) ثم احفظ التعديلات وارفعها:

git add README-PHASE8-AR.txt src/phase8_small_factor.py tests/test_phase8_small_factor.py notes/ES-PHASE8-SMALL-FACTOR-SEARCH.md

git diff --cached --stat

git commit -m "Add factorization-free Type-II small-factor search"

git push

git status

ملاحظات علمية:
- المرحلة الثامنة تستخدم مرشح k من المرحلة السابعة.
- لا تحلل M = p + 4*k*u^2 إلى عوامله الأولية؛ تبحث عن العامل الأصغر في فئتين معياريتين.
- الخوارزمية استنفادية عند تثبيت p وu، ولا تفرض سقفًا خارجيًا على a.
- اجتياز الاختبارات لا يثبت التخمين لجميع الأعداد الأولية.
- لا تستخدم git init ولا git push --force.
