# -*- coding: utf-8 -*-

def get_section_exam():
    return r'''
<section id="exam">
  <header class="top">
    <p class="kick">คลังข้อสอบเสมือนจริง 15 ข้อปรนัย + 12 ข้ออัตนัย ครอบคลุมครบทั้ง 11 บท</p>
    <h1>คลังข้อสอบและศูนย์ฝึกทำโจทย์ (Mock Exam Center)</h1>
    <p class="sub">ข้อสอบปรนัยตรวจคะแนนสดทันที · เจาะลึกแนวข้อสอบตามลายมืออาจารย์ · ข้อสอบอัตนัยแสดงวิธีทำละเอียด</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <!-- Exam Mode Switcher & Score Bar -->
  <div class="quiz-controls">
    <div class="quiz-tabs">
      <button type="button" id="btn-tab-quiz" class="quiz-tab-btn active" onclick="switchExamTab('quiz')">
        🎯 1. ข้อสอบปรนัยเสมือนจริง (Interactive Quiz 15 ข้อ)
      </button>
      <button type="button" id="btn-tab-step" class="quiz-tab-btn" onclick="switchExamTab('step')">
        📝 2. ข้อสอบอัตนัยแสดงวิธีทำ (Step-by-Step 12 ข้อ)
      </button>
    </div>
    <div class="quiz-status">
      <span class="quiz-score-badge">คะแนน: <strong id="quiz-score-val">0</strong> / 15 ข้อ</span>
      <button type="button" class="quiz-btn-reset" onclick="resetQuiz()">↺ เริ่มทำใหม่</button>
    </div>
  </div>

  <!-- TAB 1: INTERACTIVE MULTIPLE CHOICE QUIZ -->
  <div id="exam-tab-quiz">
    <h2 class="prob"><span class="tag">ปรนัย</span>ข้อสอบปรนัยเสมือนจริงตามลายมืออาจารย์ (15 ข้อ)</h2>
    <div class="stmt">
      <p>แนวข้อสอบแบบปรนัย 4 ตัวเลือก (ก, ข, ค, ง) ออกแบบตามลายมืออาจารย์หน้า 52–53 และข้อสอบจริงภาควิชา: <i>"ข้อสอบ 1 ข้อ มีสูตรมาให้หมด แทนค่าแล้วตอบ ตอบแบบปรนัย มีช้อยส์หลอกเรื่องการแปลงหน่วย มล. เป็น ลบ.ม., ค่าปรับหน้า Z ติดลบ, และภาพผังวาล์วน้ำ"</i> <b>คลิกเลือกตัวเลือกเพื่อตรวจคำตอบได้ทันที พร้อมอ่านเฉลยละเอียดและวิเคราะห์จุดหลอก</b></p>
    </div>

    <!-- Quiz Cards injected by assets/quiz.js -->
    <div id="quiz-list" class="quiz-container">
      <p style="text-align:center;padding:24px;color:var(--gray);">กำลังโหลดข้อสอบปรนัย 15 ข้อ...</p>
    </div>
  </div>

  <!-- TAB 2: STEP-BY-STEP CALCULATION PRACTICE -->
  <div id="exam-tab-step" style="display:none;">
    <h2 class="prob"><span class="tag">อัตนัย</span>ข้อสอบอัตนัยแสดงวิธีทำฉบับเต็ม (12 ข้อ)</h2>
    <div class="stmt">
      <p>รวบรวมโจทย์คำนวณอัตนัยครอบคลุมครบทั้ง 11 บท เหมาะสำหรับฝึกเขียนขั้นตอนการคำนวณส่งอาจารย์ตามลำดับเกณฑ์ตรวจ แนะนำให้กดปุ่ม <b>"ฝึก"</b> ที่แถบเมนูบนขวา เพื่อซ่อนวิธีทำ แล้วลองคำนวณในกระดาษทดก่อนแตะตรวจดูทีละขั้นตอน</p>
    </div>

    <!-- Q1: Lab 1 Unit Conversion -->
    <h3 class="grp" id="eq1">ข้อ 1: การวัดอัตราการไหลและกับดักหน่วยยกกำลังสิบ (บทที่ 1)</h3>
    <div class="stmt">
      <p>ในการจับเวลาวัดอัตราการไหลด้วยโต๊ะชลศาสตร์ เก็บน้ำในถังตวงได้ปริมาตร \(24\text{ L}\) ภายในเวลา \(40.0\text{ วินาที}\) จงหาอัตราการไหลในหน่วยลูกบาศก์เมตรต่อวินาที (\(\text{m}^3/\text{s}\))</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$\Delta V = 24\ \text{L},\quad \Delta t = 40.0\ \text{s}$$</div></div>
      <div class="row"><div class="lab">แปลงหน่วยลิตร</div><div>$$\Delta V = 24 \times 10^{-3}\ \text{m}^3$$</div></div>
      <div class="row"><div class="lab">คำนวณ Q</div><div>$$Q = \frac{\Delta V}{\Delta t} = \frac{24 \times 10^{-3}\ \text{m}^3}{40.0\ \text{s}} = 6.00 \times 10^{-4}\ \text{m}^3/\text{s} = 0.600\ \text{L/s}$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(Q = 6.00 \times 10^{-4}\ \text{m}^3/\text{s}\)</span></div></div>
    </div>

    <!-- Q2: Lab 2 Partially Submerged -->
    <h3 class="grp" id="eq2">ข้อ 2: จุดศูนย์กลางแรงดันกรณีจมบางส่วน (บทที่ 2)</h3>
    <div class="stmt">
      <p>ทุ่นเสี้ยววงกลม Essom (\(B = 75\text{ mm}, D = 100\text{ mm}, H = 200\text{ mm}, L = 280\text{ mm}\)) มีระดับน้ำท่วมแผ่นแนวดิ่ง \(d = 70\text{ mm}\) แขวนตุ้มน้ำหนักสมดุล \(m = 115.8\text{ g}\) จงหาแรงดันน้ำ \(F\), \(y_{cp,\text{theory}}\) และ \(y_{cp,\text{exp}}\)</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$d = 0.070\ \text{m} < D = 0.100\ \text{m}\quad (\text{จมบางส่วน}),\quad B = 0.075\ \text{m},\quad m = 0.1158\ \text{kg}$$</div></div>
      <div class="row"><div class="lab">แรงดันน้ำ F</div><div>$$F = \frac{1}{2}\rho g B d^2 = \frac{1}{2}(1000)(9.81)(0.075)(0.070)^2 = 1.8026\ \text{N}$$</div></div>
      <div class="row"><div class="lab">y_cp ทฤษฎี</div><div>$$y_{cp,\text{th}} = \frac{2}{3}d = \frac{2}{3}(70\ \text{mm}) = 46.67\ \text{mm}$$</div></div>
      <div class="row"><div class="lab">y_cp ทดลอง</div><div>$$\begin{aligned} h'' &= \frac{mgL}{F} = \frac{(0.1158)(9.81)(0.280)}{1.8026} = 0.1765\ \text{m} = 176.5\ \text{mm} \\ y_{cp,\text{exp}} &= h'' - (H - d) = 176.5 - (200 - 70) = 46.5\ \text{mm} \end{aligned}$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(F = 1.80\ \text{N},\quad y_{cp,\text{th}} = 46.7\ \text{mm},\quad y_{cp,\text{exp}} = 46.5\ \text{mm}\)</span></div></div>
    </div>

    <!-- Q3: Lab 2 Fully Submerged -->
    <h3 class="grp" id="eq3">ข้อ 3: จุดศูนย์กลางแรงดันกรณีจมมิดทั้งหมด (บทที่ 2)</h3>
    <div class="stmt">
      <p>ทุ่นเสี้ยววงกลมตัวเดิม มีระดับน้ำท่วมสูง \(d = 140\text{ mm}\) (\(d > D = 100\text{ mm}\)) จงหาตำแหน่งจุดศูนย์กลางแรงดันตามทฤษฎีจากผิวน้ำ (\(y_{cp,\text{th}}\))</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$d = 0.140\ \text{m},\quad D = 0.100\ \text{m},\quad B = 0.075\ \text{m}$$</div></div>
      <div class="row"><div class="lab">จุดเซนทรอยด์ yc</div><div>$$y_c = d - \frac{D}{2} = 0.140 - 0.050 = 0.090\ \text{m} = 90\ \text{mm}$$</div></div>
      <div class="row"><div class="lab">y_cp ทฤษฎี</div><div>$$y_{cp,\text{th}} = y_c + \frac{D^2}{12 y_c} = 90 + \frac{100^2}{12(90)} = 90 + 9.26 = 99.26\ \text{mm}$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(y_{cp,\text{th}} = 99.3\ \text{mm}\quad (\text{ต่ำกว่าจุดเซนทรอยด์}\ 9.26\ \text{mm})\)</span></div></div>
    </div>

    <!-- Q4: Lab 3 Impact of Jet -->
    <h3 class="grp" id="eq4">ข้อ 4: แรงกระแทกลำน้ำบนแผ่นเป้า (บทที่ 3)</h3>
    <div class="stmt">
      <p>หัวฉีดเส้นผ่านศูนย์กลาง \(d_0 = 8\text{ mm}\) ฉีดน้ำอัตราการไหล \(Q = 0.50\text{ L/s}\) พุ่งชนแผ่นเรียบแบน 90° ในแนวดิ่ง จงหาแรงกระแทกตามทฤษฎีบนแผ่นแบน และเปรียบเทียบกับกรณีเปลี่ยนเป็นถ้วยครึ่งวงกลม 180°</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$Q = 0.50 \times 10^{-3}\ \text{m}^3/\text{s},\quad A_0 = \frac{\pi(0.008)^2}{4} = 5.0265 \times 10^{-5}\ \text{m}^2,\quad \rho = 1000\ \text{kg/m}^3$$</div></div>
      <div class="row"><div class="lab">ความเร็วพุ่งออก</div><div>$$v = \frac{Q}{A_0} = \frac{0.50 \times 10^{-3}}{5.0265 \times 10^{-5}} = 9.947\ \text{m/s}$$</div></div>
      <div class="row"><div class="lab">แรงบนแผ่นแบน</div><div>$$F_{\text{flat}} = \rho Q v = (1000)(0.50 \times 10^{-3})(9.947) = 4.97\ \text{N}$$</div></div>
      <div class="row"><div class="lab">แรงบนถ้วยครึ่งวงกลม</div><div>$$F_{\text{hemi}} = 2 \rho Q v = 2 \times 4.97 = 9.95\ \text{N}\quad (\text{เป็น 2 เท่าเสมอ})$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(F_{\text{flat}} = 4.97\ \text{N},\quad F_{\text{hemi}} = 9.95\ \text{N}\)</span></div></div>
    </div>

    <!-- Q5: Lab 4 Venturi Cd -->
    <h3 class="grp" id="eq5">ข้อ 5: สัมประสิทธิ์การไหลท่อเวนจูรี่ (บทที่ 4)</h3>
    <div class="stmt">
      <p>ท่อเวนจูรี่ขนาด \(D_1 = 26\text{ mm}\), \(D_2 = 16\text{ mm}\) อ่านผลต่างมาโนมิเตอร์ได้ \(h_1 - h_2 = 18.5\text{ cm}\) ตวงน้ำจริงได้ \(Q_{\text{act}} = 3.40 \times 10^{-4}\text{ m}^3/\text{s}\) จงหาอัตราการไหลทฤษฎีและสัมประสิทธิ์ \(C_d\)</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$A_1 = 5.3093 \times 10^{-4}\ \text{m}^2,\quad (A_1/A_2)^2 = (26/16)^4 = 6.973,\quad \Delta h = 0.185\ \text{m}$$</div></div>
      <div class="row"><div class="lab">Q ทางทฤษฎี</div><div>$$Q_{\text{th}} = A_1 \sqrt{\frac{2g \Delta h}{(A_1/A_2)^2 - 1}} = (5.3093 \times 10^{-4})\sqrt{\frac{2(9.81)(0.185)}{5.973}} = 4.139 \times 10^{-4}\ \text{m}^3/\text{s}$$</div></div>
      <div class="row"><div class="lab">สัมประสิทธิ์ Cd</div><div>$$C_d = \frac{Q_{\text{act}}}{Q_{\text{th}}} = \frac{3.40 \times 10^{-4}}{4.139 \times 10^{-4}} = 0.821$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(Q_{\text{th}} = 4.14 \times 10^{-4}\ \text{m}^3/\text{s},\quad C_d = 0.821\)</span></div></div>
    </div>

    <!-- Q6: Lab 5 Manning's Equation -->
    <h3 class="grp" id="eq6">ข้อ 6: สมการแมนนิ่งและผลของหญ้าเทียม (บทที่ 5)</h3>
    <div class="stmt">
      <p>รางน้ำเปิดกว้าง \(b = 0.30\text{ m}\) ความลาดชัน \(S_0 = 0.002\) มีน้ำไหลลึก \(y = 0.12\text{ m}\) ถ้าท้องรางมีค่า \(n = 0.012\) จงหาอัตราการไหล \(Q\) และถ้าปูหญ้าเทียมทำให้ \(n = 0.024\) ความเร็วจะลดลงเหลือเท่าใดที่ความลึกเดิม</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">เรขาคณิตหน้าตัด</div><div class="given">$$A = b y = (0.30)(0.12) = 0.036\ \text{m}^2,\quad P = b + 2y = 0.30 + 0.24 = 0.54\ \text{m},\quad R_h = \frac{0.036}{0.54} = 0.0667\ \text{m}$$</div></div>
      <div class="row"><div class="lab">ความเร็วเดิม (n=0.012)</div><div>$$V_1 = \frac{1}{0.012}(0.0667)^{2/3}(0.002)^{1/2} = \frac{1}{0.012}(0.1644)(0.04472) = 0.6128\ \text{m/s}$$</div></div>
      <div class="row"><div class="lab">อัตราการไหล Q1</div><div>$$Q_1 = A V_1 = (0.036)(0.6128) = 0.0221\ \text{m}^3/\text{s} = 22.1\ \text{L/s}$$</div></div>
      <div class="row"><div class="lab">เมื่อปูหญ้าเทียม (n=0.024)</div><div>$$V_2 = V_1 \times \left(\frac{n_1}{n_2}\right) = 0.6128 \times \left(\frac{0.012}{0.024}\right) = 0.3064\ \text{m/s}\quad (\text{ลดลงเหลือครึ่งหนึ่ง})$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(Q_1 = 0.0221\ \text{m}^3/\text{s},\quad V_2 = 0.306\ \text{m/s}\)</span></div></div>
    </div>

    <!-- Q7: Lab 6 Weirs -->
    <h3 class="grp" id="eq7">ข้อ 7: เปรียบเทียบฝายสี่เหลี่ยมกับฝายสามเหลี่ยม (บทที่ 6)</h3>
    <div class="stmt">
      <p>ฝายสี่เหลี่ยมกว้าง \(b = 0.20\text{ m}\) และฝายสามเหลี่ยม 90° ทั้งสองมีเฮดเหนือน้ำ \(H = 0.08\text{ m}\) กำหนด \(C_{d,\text{rect}} = 0.62\), \(C_{d,\text{tri}} = 0.58\) จงหาอัตราการไหลของฝายทั้งสอง</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">ฝายสี่เหลี่ยม (H^1.5)</div><div>$$\begin{aligned} Q_{\text{rect}} &= \frac{2}{3} C_d b \sqrt{2g} H^{3/2} \\ &= \frac{2}{3}(0.62)(0.20)\sqrt{2(9.81)}(0.08)^{1.5} \\ &= (0.08267)(4.429)(0.02263) = 8.28 \times 10^{-3}\ \text{m}^3/\text{s} = 8.28\ \text{L/s} \end{aligned}$$</div></div>
      <div class="row"><div class="lab">ฝายสามเหลี่ยม (H^2.5)</div><div>$$\begin{aligned} Q_{\text{tri}} &= \frac{8}{15} C_d \sqrt{2g} \tan(45^\circ) H^{5/2} \\ &= \frac{8}{15}(0.58)(4.429)(1)(0.08)^{2.5} \\ &= (1.370)(0.00181) = 2.48 \times 10^{-3}\ \text{m}^3/\text{s} = 2.48\ \text{L/s} \end{aligned}$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(Q_{\text{rect}} = 8.28\ \text{L/s},\quad Q_{\text{tri}} = 2.48\ \text{L/s}\)</span></div></div>
    </div>

    <!-- Q8: Lab 7 Parallel Pipes -->
    <h3 class="grp" id="eq8">ข้อ 8: โครงข่ายท่อต่อขนาน (บทที่ 7)</h3>
    <div class="stmt">
      <p>ท่อ A (\(D_A = 20\text{ mm}, L = 1.0\text{ m}\)) และท่อ B (\(D_B = 10\text{ mm}, L = 1.0\text{ m}\)) ต่อขนานกัน ถ้าสัมประสิทธิ์แรงเสียดทาน \(f\) เท่ากัน จงหาอัตราส่วนของอัตราการไหล \(Q_A / Q_B\)</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">เงื่อนไขท่อขนาน</div><div class="given">$$h_{f,A} = h_{f,B} \Rightarrow \frac{8 f L Q_A^2}{\pi^2 g D_A^5} = \frac{8 f L Q_B^2}{\pi^2 g D_B^5}$$</div></div>
      <div class="row"><div class="lab">จัดรูปอัตราส่วน Q</div><div>$$\frac{Q_A^2}{Q_B^2} = \frac{D_A^5}{D_B^5} = \left(\frac{20}{10}\right)^5 = 32 \Rightarrow \frac{Q_A}{Q_B} = \sqrt{32} \approx 5.657$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(Q_A / Q_B = \sqrt{32} \approx 5.66\quad (\text{ท่อโตกว่า 2 เท่า ส่งน้ำได้มากกว่าถึง 5.66 เท่า})\)</span></div></div>
    </div>

    <!-- Q9: Lab 7 Series Pipes & Datum -->
    <h3 class="grp" id="eq9">ข้อ 9: ท่อต่ออนุกรมและค่าแก้ระดับ Datum (บทที่ 7)</h3>
    <div class="stmt">
      <p>ท่อส่งน้ำยาว \(100\text{ m}\) เชื่อมระหว่างจุด 1 (\(Z_1 = 15.0\text{ m}, P_1/\gamma = 40.0\text{ m}\)) และจุด 2 (\(Z_2 = 28.0\text{ m}, P_2/\gamma = 22.0\text{ m}\)) ถ้าขนาดท่อคงที่ จงหาการสูญเสียพลังงานรวม \(h_L\)</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">สมการพลังงาน</div><div class="given">$$\frac{P_1}{\gamma} + Z_1 = \frac{P_2}{\gamma} + Z_2 + h_L\quad (V_1 = V_2)$$</div></div>
      <div class="row"><div class="lab">คำนวณ hL</div><div>$$h_L = \left(\frac{P_1}{\gamma} - \frac{P_2}{\gamma}\right) + (Z_1 - Z_2) = (40.0 - 22.0) + (15.0 - 28.0) = 18.0 - 13.0 = 5.0\ \text{m}$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(h_L = 5.0\ \text{m}\)</span></div></div>
    </div>

    <!-- Q10: Lab 8 Orifice Trajectory -->
    <h3 class="grp" id="eq10">ข้อ 10: รูลอดและแนววิถีลำน้ำ (บทที่ 8)</h3>
    <div class="stmt">
      <p>ถังน้ำรักษาระดับคงที่ \(H = 0.40\text{ m}\) รูเจาะขอบคมมี \(C_v = 0.97\) ลำน้ำพุ่งตกลงมาในแนวดิ่งระยะ \(y = 0.15\text{ m}\) จงหาพิกัดระยะในแนวนอน \(x\) ของลำน้ำ</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$H = 0.40\ \text{m},\quad y = 0.15\ \text{m},\quad C_v = 0.97$$</div></div>
      <div class="row"><div class="lab">สมการวิถีลำน้ำ</div><div>$$x = 2 C_v \sqrt{y H} = 2(0.97)\sqrt{(0.15)(0.40)} = 1.94 \sqrt{0.060} = 1.94(0.2449) = 0.4752\ \text{m}$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(x = 0.475\ \text{m} = 47.5\ \text{cm}\)</span></div></div>
    </div>

    <!-- Q11: Lab 9 Pump Test -->
    <h3 class="grp" id="eq11">ข้อ 11: เครื่องสูบน้ำต่ออนุกรม-ขนาน และค่าแก้เกจ (บทที่ 9)</h3>
    <div class="stmt">
      <p>ในการทดสอบปั๊มน้ำต่อแบบอนุกรม อ่านเกจทางออกได้ \(h_0 = 16.5\text{ m}\) น้ำดูดจากถังเปิด (\(h_1 = 0\)) ระยะเกจ \(h_d(\text{outlet}) = 0.17\text{ m}, h_d(\text{bench}) = 0.24\text{ m}\) ตวงน้ำได้ \(18\text{ L}\) ในเวลา \(25.0\text{ s}\) จงหา Total Head \(H\) และกำลังไฮดรอลิก \(W_i\)</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">ค่าแก้ระดับ Hd</div><div class="given">$$H_d = 0.17 - 0.24 = \mathbf{-0.07\ \text{m}}\quad (\text{ค่าติดลบ!})$$</div></div>
      <div class="row"><div class="lab">Total Head H</div><div>$$H = (h_0 - h_1) + H_d = (16.5 - 0) + (-0.07) = 16.43\ \text{m}$$</div></div>
      <div class="row"><div class="lab">อัตราการไหล Q</div><div>$$Q = \frac{18 \times 10^{-3}\ \text{m}^3}{25.0\ \text{s}} = 7.20 \times 10^{-4}\ \text{m}^3/\text{s}$$</div></div>
      <div class="row"><div class="lab">กำลังไฮดรอลิก Wi</div><div>$$W_i = \gamma Q H = 9,810 \times (7.20 \times 10^{-4}) \times (16.43) = 116.05\ \text{Watts}$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(H = 16.43\ \text{m},\quad W_i = 116.1\ \text{Watts}\)</span></div></div>
    </div>

    <!-- Q12: Lab 10 & 11 Sluice Gate & Critical Depth -->
    <h3 class="grp" id="eq12">ข้อ 12: การไหลวิกฤตในรางเวนจูรี่และบานประตูน้ำ (บทที่ 10 และ 11)</h3>
    <div class="stmt">
      <p>คลองสี่เหลี่ยมกว้าง \(b = 0.50\text{ m}\) อัตราไหล \(Q = 0.080\text{ m}^3/\text{s}\) จงหาความลึกวิกฤต \(y_c\) และพลังงานจำเพาะต่ำสุด \(E_{\min}\)</p>
    </div>
    <div class="exam">
      <div class="row"><div class="lab">อัตราไหลต่อหน่วยกว้าง</div><div class="given">$$q = \frac{Q}{b} = \frac{0.080}{0.50} = 0.160\ \text{m}^2/\text{s}$$</div></div>
      <div class="row"><div class="lab">ความลึกวิกฤต yc</div><div>$$y_c = \left(\frac{q^2}{g}\right)^{1/3} = \left(\frac{0.160^2}{9.81}\right)^{1/3} = (0.002610)^{1/3} = 0.1377\ \text{m} \approx 13.8\ \text{cm}$$</div></div>
      <div class="row"><div class="lab">พลังงานจำเพาะ Emin</div><div>$$E_{\min} = \frac{3}{2} y_c = 1.5 \times 0.1377 = 0.2065\ \text{m} \approx 20.7\ \text{cm}$$</div></div>
      <div class="row"><div class="lab">คำตอบสุดท้าย</div><div><span class="fin">\(y_c = 0.138\ \text{m},\quad E_{\min} = 0.207\ \text{m}\)</span></div></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab11">← บทที่ 11 รางน้ำเวนจูรี่</a>
    <a href="#calc">เครื่องคิดเลขแล็บ →</a>
  </div>
</section>
'''
