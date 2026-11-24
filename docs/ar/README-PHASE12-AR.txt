حزمة المرحلة 12 — تحسين تطبيق مبرهنة الكثافة على u=1,2,3,4

ما الذي تحسّن؟
بدل استخدام حد خشن لمتوسط phi(4ua)، اشتققنا صيغة مجموع دقيقة لكل شريحة ثابتة u=1,2,3,4. ثم اخترنا أربع حدود مختلفة A_u بحيث نحصل على عائلة تضم نحو 0.253164 loglog(N) زوجًا، مع المحافظة على شرط متوسط دالة أويلر في Theorem 4.6.

النتيجة التابعة:
|E_4(N)| <= N exp(-(kappa+o(1))(loglog N)^2)
حيث kappa = 504317*pi^2/377487360 ~= 0.01318563165.

هذه نتيجة مشتقة من مبرهنة Dahan 4.6 في مسودته arXiv:2611.08717v1؛ وليست برهانًا لتخمين إردوش–شتراوس أو مبرهنة مستقلة جديدة.

المجلدات:
- notes/ES-PHASE12-OPTIMIZED-U4-DENSITY.md: البرهان والتحقق من شروط المبرهنة وتحسين القطوع.
- src/phase12_density_optimization.py: تدقيق حسابي للأعداد الصحيحة والحدود.
- tests/test_phase12_density_optimization.py: 9 اختبارات.
- results/PHASE12-OPTIMIZED-U4-DENSITY.json و.txt: النتائج.
- results/PHASE12-TEST-RUN.log: سجل الاختبارات.
- results/PHASE12-ENVIRONMENT-AND-COMMANDS.txt: بيئة وأوامر إعادة الإنتاج.

لا توجد مكتبات خارجية مطلوبة. لا يستبدل أي ملف قديم، ولا يحتاج إلى تعديل كود سابق.

من جذر المستودع نفّذ:
1) python -m unittest discover -s tests -p "test_phase12_density_optimization.py" -v
2) python -m unittest discover -s tests -v
3) python src/phase12_density_optimization.py --output results/PHASE12-OPTIMIZED-U4-DENSITY-LOCAL.json
4) git status

بعد نجاح الاختبارات، أضف الملفات الجديدة فقط، راجع git diff --cached --stat، ثم commit وpush. لا تستخدم git init أو git push --force.

المساهمة الدقيقة:
- متوسط totient: مبرهن تحليليًا في المذكرة.
- اختيار العائلة: يحقق 99% من الحد الأمثل لعدد الأزواج ضمن عائلات القطوع المستطيلة ذات الشرائح الأربع، تحت قيد المتوسط asymptotic.
- الثابت العددي: ناتج عن تطبيق Dahan Theorem 4.6.
- ما زال وجود شاهد لكل أولي غير مثبت؛ حد الكثافة لا يلغي الاستثناءات.
