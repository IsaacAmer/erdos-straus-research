# ملحق المرحلة الحادية عشرة — تقدير كثافة استثناءات Type II عند تثبيت u ≤ 4

**Erdős–Straus Research Lab**
**تاريخ المذكرة:** 23 نوفمبر 2026
**Claim ID:** `ES4-DENSITY-01`
**الحالة:** نتيجة تابعة مستخرجة من مبرهنة في مسودة Dahan (2026)، وليست برهانًا للتخمين الأصلي ولا مبرهنة مستقلة جديدة.

---

## 1. المسألة المحددة

نثبت الترميز التالي. للأولي \(p\equiv1\pmod{24}\)، يكون زوج \((u,a)\) شاهد Type II إذا

\[
\gcd(u,a)=1,\qquad s\mid ap+u,
\qquad s\equiv-1\pmod{4ua},
\]

لعدد صحيح موجب \(s\).

نريد دراسة الحالة المقيدة

\[
1\le u\le4,
\]

مع السماح لـ\(a\) بأن يكبر مع \(p\). عرّف مجموعة الاستثناءات

\[
\mathcal E_4(N)=\left\{p\le N:\begin{array}{l}
 p\text{ أولي},\ p\equiv1\pmod{24},\\
 \text{ولا يوجد شاهد }(u,a,s)\text{ مع }1\le u\le4
 \end{array}\right\}.
\]

المطلوب ليس افتراض أن \(\mathcal E_4(N)\) فارغة؛ بل إعطاء حد لحجمها.

## 2. المبرهنة المنشورة التي سنطبقها

في مسودة Benjamin Dahan، *Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture*، يعرّف المؤلف لكل عائلة منتهية \(\mathcal P\) من الأزواج المتباينة نسبيًا مجموعة \(E_{\mathcal P}(N)\) للأوليات التي لا تملك شاهد Type II لأي زوج في العائلة.

وتنص Theorem 4.6 في المسودة على حد من الشكل

\[
|E_{\mathcal P}(N)|\ll N\exp\!\left(
-\frac{5}{96}P\,
\frac{\left(\log\frac{\log z}{\log J^5}\right)^2}{\log\log N}
+O(P\log\log J)\right),
\]

تحت الشروط المحددة في المبرهنة، حيث \(P=|\mathcal P|\)، و\(\mathcal P\subseteq\mathcal P_2(J)\)، و

\[
\overline\varphi(\mathcal P)
=\frac1P\sum_{(u,a)\in\mathcal P}(\varphi(4ua)-2),
\qquad
\log z=\frac{\log N}{4P\log\log N}.
\]

أهم نقطة هنا أن المبرهنة تسمح بعائلة مختارة \(\mathcal P\subseteq\mathcal P_2(J)\)، ولا تشترط استعمال كل الأزواج في المربع.

## 3. اختيار العائلة التي تناسب مشروعنا

ضع

\[
L=\log\log N,
\qquad
Y=\left\lfloor\beta L\right\rfloor,
\qquad \beta=\frac1{100},
\]

واختر العائلة

\[
\mathcal P_4(Y)=\left\{(u,a):1\le u\le4,\ ua\le Y,\ \gcd(u,a)=1\right\}.
\]

هذه العائلة تحقق \(\mathcal P_4(Y)\subseteq\mathcal P_2(J)\) عند أخذ \(J=\lceil Y\rceil\) ولـ\(N\) كبير بما يكفي.

### 3.1 حساب عدد الأزواج

باستخدام أن عدد الأعداد \(a\le X\) المتباينة نسبيًا مع \(u\) هو

\[
\frac{\varphi(u)}uX+O(1),
\]

نحصل على

\[
\begin{aligned}
P(Y)&=\sum_{u=1}^4\#\{a\le Y/u:\gcd(a,u)=1\}\\
&=Y+\frac Y4+\frac{2Y}{9}+\frac Y8+O(1)\\
&=\boxed{\frac{115}{72}Y+O(1)}.
\end{aligned}
\]

ومن ثم

\[
P(Y)=\left(\frac{115\beta}{72}+o(1)\right)L.
\]

### 3.2 تقدير متوسط المقياس

لكل \((u,a)\in\mathcal P_4(Y)\) لدينا \(ua\le Y\)، ولذلك

\[
\varphi(4ua)-2\le\varphi(4ua)\le4ua\le4Y.
\]

إذن

\[
\boxed{\overline\varphi(\mathcal P_4(Y))\le4Y
=\frac{4}{100}L+O(1).}
\]

### 3.3 التحقق من بقية شروط Theorem 4.6

خذ \(\delta_0=1/16\)، فيكون الطرف الأيمن لشرط المتوسط في Theorem 4.6 مساويًا

\[
\left(\frac18-\delta_0\right)
\log\left(\frac{\log z}{\log J^5}\right)
=\frac1{16}\log\left(\frac{\log z}{\log J^5}\right).
\]

وبما أن \(P\asymp L\)، فإن

\[
\log z=\frac{\log N}{4PL}
\asymp\frac{e^L}{L^2}.
\]

كما أن \(J\asymp L\)، ولذلك

\[
B_N:=\log\left(\frac{\log z}{\log J^5}\right)
=L-O(\log L)\sim L.
\]

ومن ثم، عندما يكون \(N\) كبيرًا بما يكفي،

\[
\overline\varphi(\mathcal P_4(Y))
\le0.04L
<\frac1{16}B_N.
\]

كذلك \(\log P=O(\log L)=o(L)\)، و\(\log z>\log J^5\) في النهاية؛ فتتحقق الشروط الأخرى للمبرهنة.

## 3.4 نتيجة أقوى: تكفي عائلة ذات u=1 لإثبات كثافة الاستثناءات

هناك تطبيق أكثر مباشرة للسؤال الذي بدأ منه هذا المسار. لا نحتاج إلى جمع القيم الأربع لـ\(u\) كي نثبت أن استثناءات حالة \(u=1\) نادرة.

عرّف

\[
\mathcal P_1(Y):=\{(1,a):1\le a\le Y\}.
\]

كل أزواج هذه العائلة متباينة نسبيًا، وهي محتواة في \(\mathcal P_2(J)\) عند \(J=\lceil Y\rceil\). وعددها

\[
P_1(Y)=Y+O(1).
\]

كما أن

\[
\overline\varphi(\mathcal P_1(Y))
=\frac1{P_1(Y)}\sum_{a\le Y}(\varphi(4a)-2)
\le 4Y
=0.04\log\log N+O(1).
\]

خذ \(Y=\lfloor\frac1{100}\log\log N\rfloor\) كما سبق، و\(J=\lceil Y\rceil\). عندئذ \(P_1\asymp\log\log N\)، ومن ثم

\[
\log P_1=O(\log\log\log N)=o(\log\log N).
\]

وكذلك، مع \(L=\log\log N\)، فإن

\[
B_N:=\log\left(\frac{\log z}{\log J^5}\right)=L-O(\log L)\sim L.
\]

لذلك تتحقق فرضية المتوسط في Theorem 4.6 عند \(\delta_0=1/16\)، لأن

\[
0.04L < \frac1{16}B_N
\]

لكل \(N\) كبير بما يكفي. بتطبيق المبرهنة نفسها نحصل على ثابت \(c_1>0\) بحيث

\[
|E_{\mathcal P_1(Y)}(N)|\ll N\exp(-c_1(\log\log N)^2).
\]

عرّف \(\mathcal E_1(N)\) بأنها مجموعة الأوليات \(p\le N\)، \(p\equiv1\pmod{24}\)، التي لا تملك شاهد Type II لأي قيمة موجبة لـ\(a\) عند \(u=1\). من التعريف

\[
\mathcal E_1(N)\subseteq E_{\mathcal P_1(Y)}(N),
\]

وبالتالي

\[
\boxed{|\mathcal E_1(N)|\ll N\exp(-c_1(\log\log N)^2).}
\]

**التفسير الأقوى:** باستثناء مجموعة بهذا الحجم، يملك كل أولي \(p\equiv1\pmod{24}\) شاهدًا بالفعل عند \(u=1\)، بل يمكن اختيار \(a\le\frac1{100}\log\log N\).

وهذا لا يثبت نجاح \(u=1\) لكل أولي؛ إذ لا يزال الحد يسمح بوجود استثناءات. لكنه يعني أن فشل \(u=1\) نفسه نادر جدًا وفق هذا التقدير.

وبما أن الفشل في جميع الحالات \(u\le4\) يستلزم الفشل عند \(u=1\)، فلدينا أيضًا

\[
\mathcal E_4(N)\subseteq\mathcal E_1(N).
\]

إذن نتيجة \(u=1\) وحدها تكفي لإثبات ندرة استثناءات \(u\le4\) من حيث الرتبة، بينما تطبيق العائلة \(\mathcal P_4(Y)\) في القسم التالي يعطي تقديرًا مباشرًا قد يكون ذا ثابت أُسّي أفضل لمجموعة \(\mathcal E_4(N)\).

هذه النتيجة أيضًا **تابعة من Theorem 4.6 نفسها**، وليست مبرهنة مستقلة جديدة.

---

## 4. النتيجة التابعة للمشروع

بتطبيق Theorem 4.6 على \(\mathcal P_4(Y)\)، ومع استعمال

\[
P=\left(\frac{115\beta}{72}+o(1)\right)L,
\qquad B_N\sim L,
\]

نجد

\[
|E_{\mathcal P_4(Y)}(N)|
\ll N\exp\left(-c(\log\log N)^2\right)
\]

لبعض الثابت \(c>0\).

لكن كل أولي في \(\mathcal E_4(N)\) يفشل لكل \(a\)، ومن ثم يفشل بالتأكيد لكل الأزواج المحدودة في \(\mathcal P_4(Y)\). لذلك

\[
\mathcal E_4(N)\subseteq E_{\mathcal P_4(Y)}(N),
\]

وبالتالي نحصل على النتيجة:

\[
\boxed{
|\mathcal E_4(N)|\ll
N\exp\left(-c(\log\log N)^2\right)
}
\]

لبعض ثابت موجب \(c\).

**التفسير:** باستثناء مجموعة صغيرة جدًا وفق هذا الحد، كل أولي \(p\equiv1\pmod{24}\) حتى \(N\) يملك شاهدًا Type II مع

\[
1\le u\le4,
\qquad ua\le\frac1{100}\log\log N.
\]

وهذا أقوى من مجرد القول إن معظم الأوليات تملك شاهدًا عند عمق ثابت؛ فالحد المسموح لـ\(ua\) ينمو مع \(N\)، وإن كان ببطء.

## 5. ما الذي لا تثبته النتيجة؟

هذه النتيجة **لا تثبت** أن \(\mathcal E_4(N)\) فارغة أو منتهية. بالفعل، الحد

\[
N\exp\left(-c(\log\log N)^2\right)
\]

لا يزال يتجه إلى ما لا نهاية مع \(N\)، لأن \(\log N\) ينمو أسرع من أي قوة ثابتة لـ\(\log\log N\).

إذن لا يجوز تحويل تقدير الكثافة إلى برهان لكل أولي. كما أن النتيجة تظل استنتاجًا من مسودة بحثية؛ وينبغي توثيق اعتمادنا عليها ومراجعة تفاصيل برهانها قبل تقديمها كجزء من ورقة بحثية مستقلة.

## 6. ربط المرحلة العاشرة: اختزال تدقيق جاكوبي

استخدم متغيرات المرحلة الرابعة:

\[
s=4uak-1,\qquad Q=\frac{ap+u}{s},
\qquad t=\frac{u+Q}{a}.
\]

عند وجود الشاهد، تكون \(Q,t\) أعدادًا صحيحة موجبة، ولدينا

\[
Q=at-u,
\qquad p+t=4uQk.
\]

وهذا يطابق متغيرات الصيغة Type II القياسية بوضع

\[
\alpha=k,\qquad v=Q,\qquad c=t.
\]

ومن ثم

\[
sv=ap+u,
\qquad u+v=ac,
\qquad p+c=4ukv.
\]

تنتج قوانين جاكوبي في Theorem 2.4 من هذه العلاقات. ويمكن اختزال تدقيقها كما يلي:

1. من \(s=4uak-1\)، وباستخدام قانون التبادل التربيعي لرمز جاكوبي، ينتج
   \[
   \left(\frac{k}{s}\right)=1.
   \]
2. وبما أن \(4uak=s+1\)، ينتج
   \[
   \left(\frac{ua}{s}\right)=1.
   \]
3. من \(sv=ap+u\)، نضرب التطابق modulo \(s\) في \(a\):
   \[
   a^2p\equiv-ua\pmod s.
   \]
   وبما أن \(s\equiv3\pmod4\)، نحصل على
   \[
   \left(\frac ps\right)=-1.
   \]
   ولأن \(p\equiv1\pmod4\)، فإن
   \[
   \left(\frac sp\right)=-1.
   \]
4. ولأن \(p\equiv1\pmod{24}\)، فإن \((u/p)=1\) لكل \(u=1,2,3,4\). ومن \(sv\equiv u\pmod p\) ينتج
   \[
   \left(\frac vp\right)=-1,
   \qquad \left(\frac{uv}{p}\right)=-1.
   \]
5. وأخيرًا، من \(p+c=4ukv\) ينتج
   \[
   \left(\frac{kc}{p}\right)=-1.
   \]

إذن ففحوص جاكوبي الستة مفيدة كاختبارات اتساق مستقلة في البرنامج، لكنها ليست ستة قيود مستقلة: معظمها يتبع من صيغة \(s\)، ومن قسمة \(sv=ap+u\)، ومن الهوية \(p+c=4ukv\).

**تنبيه:** الرمز \((\cdot/s)\) هنا هو رمز جاكوبي، وليس ادعاءً بأن البسط مربع بترديد \(s\) عندما يكون \(s\) مركبًا.

## 7. مثال تحقق يدوي

خذ

\[
p=73,\quad u=1,\quad a=2,\quad k=1.
\]

إذن

\[
s=4(1)(2)(1)-1=7,
\qquad 2\cdot73+1=147=7\cdot21.
\]

وعليه

\[
v=21,\qquad c=\frac{u+v}{a}=11,
\qquad p+c=84=4ukv.
\]

والرموز تحقق

\[
\left(\frac{k}{s}\right)=1,
\quad\left(\frac{ua}{s}\right)=1,
\quad\left(\frac{s}{p}\right)=-1,
\quad\left(\frac{uv}{p}\right)=-1,
\quad\left(\frac{kc}{p}\right)=-1.
\]

## 8. قرار المرحلة التالية

1. تسجيل `ES4-DENSITY-01` والنتيجة الأقوى `ES1-DENSITY-01` بوصفهما **نتيجتين تابعتين لمسودة Dahan**، لا بوصفهما برهانًا أصليًا للمشروع.
2. الإبقاء على المسألة الكلية مفتوحة: هل \(\mathcal E_1(N)=\varnothing\) أو \(\mathcal E_4(N)=\varnothing\) لكل \(N\)؟ تقدير الكثافة لا يزيل الاستثناءات.
3. في الكود، الاحتفاظ بفحوص جاكوبي الستة لأغراض تدقيق المتغيرات، مع توثيق أن العلاقات بينها مترابطة.
4. لا تحتاج هذه المذكرة إلى تعديل كود أو إعادة تشغيل الاختبارات؛ فهي إضافة نظرية وتوثيقية فقط.

---

## المصادر

- Benjamin Dahan, *Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture*, arXiv:2611.08717 (2026), خاصة Theorem 4.6 وTheorem 2.4. https://arxiv.org/abs/2611.08717
- Benjamin Dahan, *Sieve dimension and search depth for the Erdős–Straus conjecture, \(n\equiv1\pmod{24}\)*, arXiv:2608.24035 (2026). https://arxiv.org/abs/2608.24035
