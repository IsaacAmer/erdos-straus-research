حزمة المرحلة 14 — عائلة الشواهد المحددة بحد دالة أويلر

النتيجة:
بدل تقسيم a حسب أنماط العوامل الأولية الصغيرة، نختار مباشرة جميع الأزواج (u,a) التي تحقق u<=4 و gcd(u,a)=1 و phi(4ua)<=T، حيث T=2*gamma*(1/8-delta0)*loglog(N).

باستخدام سلسلة ديريشليه ومبرهنة Wiener–Ikehara نحصل على:
|E_4(N)| <= N exp(-(kappa+o(1))(loglog N)^2)
حيث، باختيار gamma=999/1000 وdelta0=1/65536:
kappa ~= 0.013993650132.

هذا يساوي 99.8878% من الحد الأقصى لهذا التطبيق من Dahan Theorem 4.6 تحت قيد متوسط phi(4ua)-2 عندما u<=4:
kappa_inf ~= 0.014009367918.

الأهم: أثبتنا أن اختيار الأزواج وفق حد totient هو أمثل asymptotically في مسألة تعظيم عدد الأزواج تحت قيد متوسط الكلفة؛ أي إننا لا نكتفي باقتراح عائلة جيدة.

الملفات:
- notes/ES-PHASE14-TOTIENT-SUBLEVEL-DENSITY.md: البرهان التحليلي الكامل، سلسلة ديريشليه، ثابت الكثافة، والتحقق من شروط Dahan.
- src/phase14_totient_sublevel.py: بناء العائلة وتدقيق الحسابات الصحيحة.
- tests/test_phase14_totient_sublevel.py: 11 اختبارًا.
- results/PHASE14-TOTIENT-SUBLEVEL-DENSITY.json و.txt: النتائج.
- results/PHASE14-TEST-RUN.log: سجل الاختبارات.
- results/PHASE14-ENVIRONMENT-AND-COMMANDS.txt: إصدار Python وأوامر إعادة الإنتاج.

لا توجد مكتبات خارجية مطلوبة. لا يستبدل أي ملف سابق.

من جذر المستودع نفّذ:
1) python -m unittest discover -s tests -p "test_phase14_totient_sublevel.py" -v
2) python -m unittest discover -s tests -v
3) python src/phase14_totient_sublevel.py --output results/PHASE14-TOTIENT-SUBLEVEL-DENSITY-LOCAL.json
4) git status
5) بعد نجاح الاختبارات أضف الملفات الجديدة فقط، وراجع git diff --cached --check وgit diff --cached --stat، ثم commit وpush.

التحفظ العلمي:
- Theorem 4.6 من Dahan؛ لا ننسبها للمشروع.
- Wiener–Ikehara أداة تحليلية قياسية نطبقها على سلسلة ديريشليه مستخرجة من phi(4ua).
- النتيجة تضبط حجم مجموعة الاستثناءات ولا تثبت خلوها. لا يوجد برهان عام للتخمين.
