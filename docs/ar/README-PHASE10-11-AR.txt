حزمة المرحلتين العاشرة والحادية عشرة — تدقيق جاكوبي وتصنيف فئات المربعات

هذه الحزمة مبنية على المستودع الحالي، ولا تستبدل أي ملف من Phase 7 أو Phase 8 أو Phase 9.

المحتويات:

Phase 10 — تدقيق قانون جاكوبي المنشور:
- src/phase10_jacobi_audit.py
- src/phase10_demo.py
- tests/test_phase10_jacobi_audit.py
- notes/ES-PHASE10-JACOBI-AUDIT.md
- results/PHASE10-JACOBI-AUDIT.json

Phase 11 — بنية فئات المربعات عند u <= 4:
- src/phase11_small_u_character_profile.py
- src/phase11_demo.py
- src/phase11_span_demo.py
- tests/test_phase11_small_u_character_profile.py
- notes/ES-PHASE11-SMALL-U-CHARACTER-CLASSIFICATION.md
- results/PHASE11-CHARACTER-CLASSIFICATION-10000.json
- results/PHASE11-CHARACTER-CLASSIFICATION-10000.txt
- results/PHASE11-SQUARE-CLASS-SPAN-EXAMPLES.json

سجل التشغيل والبيئة:
- results/PHASE10-11-TEST-RUN.log
- results/PHASE10-11-TEST-ENVIRONMENT.txt
- results/PHASE10-DEMO-RUN.txt
- results/PHASE11-CLASSIFICATION-RUN.txt
- results/PHASE11-SPAN-DEMO-RUN.txt

الاعتماديات:
تحتاج هذه الحزمة إلى وجود الملفين السابقين كما هما في مشروعك:
- src/phase7_floor_quotient.py
- src/phase8_small_factor.py

لا يحتوي ZIP على نسخ من هذين الملفين، ولن يستبدلهما.
لا تحتاج هذه المرحلة إلى SymPy أو إلى أي مكتبة خارجية.

طريقة الدمج:
1) افتح PowerShell داخل جذر المشروع الذي يحتوي على .git وsrc وtests وnotes.
2) استخرج الحزمة إلى جذر المشروع:

Expand-Archive -LiteralPath "$HOME\Downloads\ES-PHASE10-11-CHARACTER-RIGIDITY-PACK.zip" -DestinationPath . -Force

3) شغّل اختبارات Phase 10:

python -m unittest discover -s tests -p "test_phase10_jacobi_audit.py" -v

4) شغّل اختبارات Phase 11:

python -m unittest discover -s tests -p "test_phase11_small_u_character_profile.py" -v

5) شغّل الاختبارات الكاملة:

python -m unittest discover -s tests -v

كان لديك 82 اختبارًا ناجحًا بعد Phase 9. تضيف هذه الحزمة 17 اختبارًا (7 للمرحلة العاشرة و10 للحادية عشرة)، ولذلك العدد المتوقع 99 اختبارًا إذا لم تتغير الاختبارات السابقة.

6) أعد إنتاج تدقيق جاكوبي لـ246 شاهدًا:

python src/phase10_demo.py

7) أعد إنتاج تصنيف صندوق المعاملات حتى a=10000، في ملف محلي مستقل حتى لا تستبدل النتيجة المرجعية:

python src/phase11_demo.py --limit 10000 --output results/PHASE11-CHARACTER-CLASSIFICATION-10000-LOCAL.json

8) أعد إنتاج شهادات فئات المربعات (ثمانية أمثلة، تشمل حالتي a=1):

python src/phase11_span_demo.py

9) افحص حالة Git:

git status

10) بعد نجاح الاختبارات، أضف الملفات الجديدة:

git add README-PHASE10-11-AR.txt src/phase10_jacobi_audit.py src/phase10_demo.py src/phase11_small_u_character_profile.py src/phase11_demo.py src/phase11_span_demo.py tests/test_phase10_jacobi_audit.py tests/test_phase11_small_u_character_profile.py notes/ES-PHASE10-JACOBI-AUDIT.md notes/ES-PHASE11-SMALL-U-CHARACTER-CLASSIFICATION.md results/PHASE10-JACOBI-AUDIT.json results/PHASE10-11-TEST-RUN.log results/PHASE10-11-TEST-ENVIRONMENT.txt results/PHASE10-DEMO-RUN.txt results/PHASE11-CHARACTER-CLASSIFICATION-10000.json results/PHASE11-CHARACTER-CLASSIFICATION-10000.txt results/PHASE11-SQUARE-CLASS-SPAN-EXAMPLES.json results/PHASE11-CLASSIFICATION-RUN.txt results/PHASE11-SPAN-DEMO-RUN.txt

git diff --cached --stat

git commit -m "Add Jacobi and small-u character rigidity audits"

git push

git status

التنبيه العلمي:
- قوانين جاكوبي، صلابة المرافقين، وعائق نوى المحارف نتائج داهان المنشورة على arXiv؛ لا ننسبها إلى المشروع.
- اللمّة ذات الحالات الأربع حول عدم كون -(a+u) مربعًا modulo 4ua، وتبسيط عدد المحارف الفردية، وشهادة امتداد فئة r أو -1 من فئات العوامل الأولية هي استنتاجات هذا العمل تحت الفرضيات المكتوبة في المذكرة.
- الشهادة الأخيرة تعني وجود حاصل ضرب لعدد محدود من العوامل الأولية، وعددها لا يتجاوز بُعد مجموعة فئات المربعات 2+omega((4ua)_odd). ولا تعني وجود شاهد Type II.
- عولجت حالتا a=1 المسموحتان على حدة: (u,a)=(2,1) بواسطة chi_4، و(u,a)=(4,1) بواسطة chi_-8؛ فلا ننسبهما خطأً إلى Dahan Theorem 2.8(b) الذي يشترط u,a>1.
- لم نثبت أن هذه القيود تكفي لإيجاد شاهد Type II لكل أولي، ولم نثبت أن اللمّة أو الاستنتاجات غير موجودة في كل الأدبيات السابقة.
- لا تحذف ملفات قديمة، ولا تستخدم git init أو git push --force.
