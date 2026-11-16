# -*- coding: utf-8 -*-

def get_section_exam():
    return r'''
<section id="exam">
  <header class="top">
    <p class="kick">คลังข้อสอบเสมือนจริง 12 ข้อ ครอบคลุมครบทั้ง 11 บท</p>
    <h1>คลังข้อสอบและโหมดฝึกทำโจทย์ (Mock Exam Center)</h1>
    <p class="sub">โจทย์ปรนัยและอัตนัยตามแนวข้อสอบจริงอาจารย์ · มีเฉลยละเอียดทุกขั้นตอน · ซ้อมก่อนสอบ</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">โหมดฝึก</span>คำแนะนำในการเตรียมสอบปฏิบัติการ</h2>
  <div class="stmt">
    <p>อาจารย์ระบุว่า <i>"ข้อสอบมีสูตรมาให้หมด แต่จะวัดความเข้าใจขั้นตอน การแปลงหน่วย การอ่านรูปผังท่อ และการเลือกใช้สูตรให้ถูกต้องตามสภาวะ"</i> ขอแนะนำให้กดปุ่ม <b>"ฝึก"</b> ที่มุมบนขวา เพื่อซ่อนเฉลยวิธีทำ ลองคิดเลขในกระดาษทดก่อน แล้วแตะแต่ละบรรทัดเพื่อตรวจเช็คความถูกต้องทีละขั้นตอน</p>
  </div>

  <!-- Q1: Lab 1 Unit Conversion -->
  <h3 class="grp" id="eq1">ข้อ 1: การวัดอัตราการไหลและกับดักหน่วยยกกำลังสิบ (บทที่ 1)</h3>
  <div class="stmt">
    <p>ในการจับเวลาวัดอัตราการไหลด้วยโต๊ะชลศาสตร์ เก็บน้ำในถังตวงได้ปริมาตร \(24\text{ L}\) ภายในเวลา \(40.0\text{ วินาที}\) จงหาอัตราการไหลในหน่วยลูกบาศก์เมตรต่อวินาที (\(\text{m}^3/\text{s}\))</p>
    <p><b>ตัวเลือก:</b> ก. \(0.60\ \text{m}^3/\text{s}\) &nbsp;|&nbsp; ข. \(0.06\ \text{m}^3/\text{s}\) &nbsp;|&nbsp; ค. \(6.0 \times 10^{-4}\ \text{m}^3/\text{s}\) &nbsp;|&nbsp; ง. \(6.0 \times 10^{-5}\ \text{m}^3/\text{s}\)</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$\Delta V = 24\ \text{L},\quad \Delta t = 40.0\ \text{s}$$</div></div>
    <div class="row"><div class="lab">แปลงหน่วยลิตร</div><div>$$\Delta V = 24 \times 10^{-3}\ \text{m}^3$$</div></div>
    <div class="row"><div class="lab">คำนวณ Q</div><div>$$Q = \frac{\Delta V}{\Delta t} = \frac{24 \times 10^{-3}\ \text{m}^3}{40.0\ \text{s}} = 6.00 \times 10^{-4}\ \text{m}^3/\text{s}$$</div></div>
    <div class="row"><div class="lab">ข้อควรระวัง</div><div><p class="nt">• หากตอบ 0.60 จะผิดเพราะลืมแปลงลิตรเป็นลูกบาศก์เมตร (\(1\text{ L} = 10^{-3}\text{ m}^3\))</p></div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">ตอบข้อ ค. \(6.0 \times 10^{-4}\ \text{m}^3/\text{s}\)</span></div></div>
  </div>

  <!-- Q2: Lab 2 Partially Submerged -->
  <h3 class="grp" id="eq2">ข้อ 2: จุดศูนย์กลางแรงดันกรณีจมบางส่วน (บทที่ 2)</h3>
  <div class="stmt">
    <p>แผ่นพื้นรับแรงแนวดิ่งกว้าง \(B = 75\text{ mm}\) จมอยู่ในน้ำด้วยความลึก \(d = 60\text{ mm}\) (โดยความสูงแผ่น \(D = 100\text{ mm}\)) แรงดันน้ำตามทฤษฎี \(F\) และตำแหน่งจุดศูนย์กลางแรงดันจากผิวน้ำ \(y_{cp}\) มีค่าเท่าใด (\(\rho = 1000\text{ kg/m}^3, g = 9.81\text{ m/s}^2\))</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">ตรวจสอบสภาวะ</div><div class="given">$$d = 60\ \text{mm} < D = 100\ \text{mm}\quad \Rightarrow\ \text{จมบางส่วน (Partially Submerged)}$$</div></div>
    <div class="row"><div class="lab">คำนวณแรงดัน F</div><div>$$F = \frac{1}{2}\rho g B d^2 = \frac{1}{2}(1000)(9.81)(0.075)(0.060)^2 = 1.324\ \text{N}$$</div></div>
    <div class="row"><div class="lab">คำนวณ y_cp</div><div>$$y_{cp} = \frac{2}{3}d = \frac{2}{3}(60\ \text{mm}) = 40.0\ \text{mm} = 4.0\ \text{cm}\ \text{จากผิวน้ำ}$$</div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">\(F = 1.32\ \text{N},\quad y_{cp} = 40.0\ \text{mm}\)</span></div></div>
  </div>

  <!-- Q3: Lab 2 Fully Submerged -->
  <h3 class="grp" id="eq3">ข้อ 3: จุดศูนย์กลางแรงดันกรณีจมมิดทั้งหมด (บทที่ 2)</h3>
  <div class="stmt">
    <p>แผ่นพื้นกว้าง \(B = 75\text{ mm}\) สูง \(D = 100\text{ mm}\) จมอยู่ใต้น้ำที่ระดับความลึก \(d = 160\text{ mm}\) จงหาจุดศูนย์กลางแรงดันตามทฤษฎี \(y_{cp}\) วัดจากผิวน้ำ</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">ตรวจสอบสภาวะ</div><div class="given">$$d = 160\ \text{mm} \ge D = 100\ \text{mm}\quad \Rightarrow\ \text{จมมิดทั้งหมด (Fully Submerged)}$$</div></div>
    <div class="row"><div class="lab">จุดเซนทรอยด์ yc</div><div>$$y_c = d - \frac{D}{2} = 160 - 50 = 110\ \text{mm}$$</div></div>
    <div class="row"><div class="lab">คำนวณ y_cp</div><div>$$y_{cp} = y_c + \frac{D^2}{12 y_c} = 110 + \frac{(100)^2}{12(110)} = 110 + \frac{10000}{1320} = 110 + 7.58 = 117.58\ \text{mm}$$</div></div>
    <div class="row"><div class="lab">ตรวจสอบฟิสิกส์</div><div><p class="nt">• \(y_{cp} = 117.6\ \text{mm}\) อยู่ต่ำกว่า \(y_c = 110.0\ \text{mm}\) ถูกต้องตามหลักสถิตยศาสตร์</p></div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">\(y_{cp} = 117.6\ \text{mm}\ (11.76\ \text{cm}\ \text{จากผิวน้ำ})\)</span></div></div>
  </div>

  <!-- Q4: Lab 3 Impact of Jet -->
  <h3 class="grp" id="eq4">ข้อ 4: แรงกระแทกลำน้ำบนแผ่นเป้า (บทที่ 3)</h3>
  <div class="stmt">
    <p>ลำน้ำอัตราการไหล \(Q = 0.40\text{ L/s}\) พุ่งออกจากหัวฉีดด้วยความเร็ว \(v = 8.0\text{ m/s}\) เข้าชนฉากกั้น จงเปรียบเทียบแรงกระแทก \(F\) ระหว่างแผ่นเรียบแบน 90° กับ ถ้วยครึ่งวงกลม 180°</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$Q = 0.40 \times 10^{-3}\ \text{m}^3/\text{s},\quad v = 8.0\ \text{m/s},\quad \rho = 1000\ \text{kg/m}^3$$</div></div>
    <div class="row"><div class="lab">แผ่นแบน 90°</div><div>$$F_{\text{flat}} = \rho Q v = (1000)(0.40 \times 10^{-3})(8.0) = 3.20\ \text{N}$$</div></div>
    <div class="row"><div class="lab">ถ้วยครึ่งวงกลม</div><div>$$F_{\text{hemi}} = 2\rho Q v = 2 \times 3.20 = 6.40\ \text{N}\quad \htmlClass{ok}{(\text{เป็น 2 เท่าเสมอ})}$$</div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">แผ่นแบน: \(F = 3.20\ \text{N}\) · ถ้วยครึ่งวงกลม: \(F = 6.40\ \text{N}\)</span></div></div>
  </div>

  <!-- Q5: Lab 4 Venturi Cd -->
  <h3 class="grp" id="eq5">ข้อ 5: การคำนวณสัมประสิทธิ์การไหลท่อเวนจูรี่ (บทที่ 4)</h3>
  <div class="stmt">
    <p>ท่อเวนจูรี่มี \(A_1 / A_2 = 2.0\) เมื่อน้ำไหลผ่าน อ่านผลต่างระดับน้ำในมาโนมิเตอร์ได้ \(h_1 - h_2 = 15.0\text{ cm}\) ถ้าพื้นที่ทางเข้า \(A_1 = 5.0 \times 10^{-4}\text{ m}^2\) และวัดอัตราการไหลจริงได้ \(Q_{\text{act}} = 0.48\text{ L/s}\) จงหาค่าสัมประสิทธิ์การปรับแก้ \(C_d\)</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$A_1/A_2 = 2.0 \Rightarrow (A_1/A_2)^2 = 4.0,\quad \Delta h = 0.15\ \text{m},\quad Q_{\text{act}} = 4.8 \times 10^{-4}\ \text{m}^3/\text{s}$$</div></div>
    <div class="row"><div class="lab">คำนวณ v1 และ Q_th</div><div>$$\begin{aligned} v_1 &= \sqrt{\frac{2(9.81)(0.15)}{4.0 - 1}} = \sqrt{\frac{2.943}{3.0}} = \sqrt{0.981} = 0.9905\ \text{m/s} \\ Q_{\text{th}} &= A_1 v_1 = (5.0 \times 10^{-4})(0.9905) = 4.952 \times 10^{-4}\ \text{m}^3/\text{s} \end{aligned}$$</div></div>
    <div class="row"><div class="lab">หาค่า Cd</div><div>$$C_d = \frac{Q_{\text{act}}}{Q_{\text{th}}} = \frac{4.80 \times 10^{-4}}{4.952 \times 10^{-4}} = 0.9692$$</div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">\(C_d = 0.969\)</span></div></div>
  </div>

  <!-- Q6: Lab 5 Manning Bed -->
  <h3 class="grp" id="eq6">ข้อ 6: สมการแมนนิ่งและผลของหญ้าเทียม (บทที่ 5)</h3>
  <div class="stmt">
    <p>ในการทดลองรางน้ำเปิดปรับเอียง เมื่อปล่อยน้ำด้วยอัตราการไหลคงที่ \(Q\) เดิม แต่เปลี่ยนจาก <b>พื้นคลองเรียบ</b> เป็น <b>พื้นคลองมีหญ้าเทียม</b> จงวิเคราะห์ว่าระดับความลึกของน้ำ \(y\) และความเร็วเฉลี่ย \(V\) จะเปลี่ยนแปลงอย่างไร</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">วิเคราะห์ทางฟิสิกส์</div><div class="given">$$V = \frac{1}{n} R_h^{2/3} S_0^{1/2},\quad Q = V A = \text{คงที่}$$</div></div>
    <div class="row"><div class="lab">ผลของหญ้าเทียม</div><div><p>• หญ้าเทียมทำให้ค่าสัมประสิทธิ์ความขรุขระ \(n\) เพิ่มขึ้นอย่างมาก (แรงต้านทานการไหลสูงขึ้น)</p><p>• ส่งผลให้ความเร็วการไหล \(V\) ลดลง</p></div></div>
    <div class="row"><div class="lab">ผลต่อระดับน้ำ</div><div><p>• เมื่อ \(Q = VA\) มีค่าคงที่ แต่ \(V\) ลดลง พื้นที่หน้าตัด \(A = By\) จึง <b>ต้องเพิ่มขึ้น</b> ส่งผลให้ <b>ระดับน้ำ \(y\) ยกตัวสูงขึ้น</b></p></div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">ระดับน้ำ \(y\) สูงขึ้น และความเร็วเฉลี่ย \(V\) ลดลง</span></div></div>
  </div>

  <!-- Q7: Lab 6 Weirs -->
  <h3 class="grp" id="eq7">ข้อ 7: เปรียบเทียบฝายสี่เหลี่ยมกับฝายสามเหลี่ยม (บทที่ 6)</h3>
  <div class="stmt">
    <p>ถ้าอัตราการไหลของน้ำลดลงเหลือเพียง \(1/4\) ของเดิม (\(Q_2 = 0.25 Q_1\)) จงหาว่าระดับน้ำเหนือสันฝาย \(H\) ของ (ก) ฝายสี่เหลี่ยม (\(Q \propto H^{1.5}\)) และ (ข) ฝายสามเหลี่ยม V-Notch (\(Q \propto H^{2.5}\)) จะลดลงเหลือสัดส่วนเท่าใดของค่าเดิม</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">(ก) ฝายสี่เหลี่ยม</div><div>$$Q \propto H^{3/2} \Rightarrow \frac{H_2}{H_1} = \left(\frac{Q_2}{Q_1}\right)^{2/3} = (0.25)^{2/3} = 0.3969 \approx 39.7\%$$</div></div>
    <div class="row"><div class="lab">(ข) ฝายสามเหลี่ยม</div><div>$$Q \propto H^{5/2} \Rightarrow \frac{H_2}{H_1} = \left(\frac{Q_2}{Q_1}\right)^{2/5} = (0.25)^{0.4} = 0.5743 \approx 57.4\%$$</div></div>
    <div class="row"><div class="lab">วิเคราะห์ข้อสอบ</div><div><p class="nt">• จะเห็นว่าเมื่อ \(Q\) ลดลงฮวบฮาบ ฝายสามเหลี่ยมยังมีระดับน้ำ \(H\) เหลืออยู่ถึง 57.4% (สูงกว่าฝายสี่เหลี่ยมที่เหลือ 39.7%) จึงใช้ Hook Gauge วัดได้ง่ายและแม่นยำกว่ามากเมื่อน้ำไหลน้อย</p></div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">ฝายสี่เหลี่ยมเหลือ \(39.7\%\) · ฝายสามเหลี่ยมเหลือ \(57.4\%\)</span></div></div>
  </div>

  <!-- Q8: Lab 7 Parallel Pipes -->
  <h3 class="grp" id="eq8">ข้อ 8: โครงข่ายท่อต่อขนาน (บทที่ 7)</h3>
  <div class="stmt">
    <p>ท่อ 1 มี \(D_1 = 100\text{ mm}\) ต่อขนานกับ ท่อ 2 ที่มี \(D_2 = 50\text{ mm}\) ท่อยาวเท่ากันและมีค่า \(f\) เท่ากัน จงหาว่าท่อ 1 จะมีอัตราการไหลเป็นกี่เท่าของท่อ 2</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">สมดุลท่อขนาน</div><div class="given">$$h_{f1} = h_{f2} \Rightarrow \frac{8f L Q_1^2}{\pi^2 g D_1^5} = \frac{8f L Q_2^2}{\pi^2 g D_2^5}$$</div></div>
    <div class="row"><div class="lab">อัตราส่วน Q</div><div>$$\frac{Q_1^2}{Q_2^2} = \left(\frac{D_1}{D_2}\right)^5 = \left(\frac{100}{50}\right)^5 = 2^5 = 32$$$$\frac{Q_1}{Q_2} = \sqrt{32} = 5.657$$</div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">\(Q_1\) ไหลมากกว่า \(Q_2\) อยู่ถึง \(5.66\ \text{เท่า}\)</span></div></div>
  </div>

  <!-- Q9: Lab 7 Series Pipes & Datum -->
  <h3 class="grp" id="eq9">ข้อ 9: ท่อต่ออนุกรมและค่าแก้ระดับ Datum (บทที่ 7)</h3>
  <div class="stmt">
    <p>ท่อทดสอบขนาดคงที่ จุดวัดทางเข้า \(H_1\) อ่านความดันได้ \(P_1/\gamma = 4.20\text{ m}\) อยู่ที่ระดับความสูง \(Z_1 = 0.30\text{ m}\) จุดวัดทางออก \(H_2\) อ่านความดันได้ \(P_2/\gamma = 2.10\text{ m}\) อยู่ที่ระดับความสูง \(Z_2 = 1.50\text{ m}\) จงหาเฮดการสูญเสียพลังงานรวมในท่อ \(h_L\)</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">สมการพลังงาน</div><div class="given">$$h_L = \frac{P_1 - P_2}{\gamma} + (Z_1 - Z_2)$$</div></div>
    <div class="row"><div class="lab">แทนค่าตัวเลข</div><div>$$\begin{aligned} \frac{P_1 - P_2}{\gamma} &= 4.20 - 2.10 = 2.10\ \text{m} \\ Z_1 - Z_2 &= 0.30 - 1.50 = -1.20\ \text{m}\quad \htmlClass{no}{(\text{ติดลบเพราะจุด 2 สูงกว่า})} \\ h_L &= 2.10 + (-1.20) = 0.90\ \text{m} \end{aligned}$$</div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">\(h_L = 0.90\ \text{m}\)</span></div></div>
  </div>

  <!-- Q10: Lab 8 Orifice Trajectory -->
  <h3 class="grp" id="eq10">ข้อ 10: รูลอดและแนววิถีลำน้ำ (บทที่ 8)</h3>
  <div class="stmt">
    <p>น้ำพุ่งออกจากรูเจาะข้างถังที่มีระดับน้ำคงที่ \(H = 64.0\text{ cm}\) ลำน้ำวิ่งไปในแนวราบได้ระยะ \(x = 48.0\text{ cm}\) เมื่อตกลงมาในแนวดิ่ง \(y = 10.0\text{ cm}\) จงหาสัมประสิทธิ์ความเร็ว \(C_v\)</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">สูตรวิถีลำน้ำ</div><div class="given">$$x = 2 C_v \sqrt{yH} \Rightarrow C_v = \frac{x}{2\sqrt{yH}}$$</div></div>
    <div class="row"><div class="lab">แทนค่าพิกัด</div><div>$$\begin{aligned} yH &= (0.100\ \text{m}) \times (0.640\ \text{m}) = 0.0640\ \text{m}^2 \\ \sqrt{yH} &= \sqrt{0.0640} = 0.25298\ \text{m} \\ C_v &= \frac{0.480}{2(0.25298)} = \frac{0.480}{0.50596} = 0.9487 \end{aligned}$$</div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">\(C_v = 0.949\)</span></div></div>
  </div>

  <!-- Q11: Lab 9 Pump Series & Parallel -->
  <h3 class="grp" id="eq11">ข้อ 11: เครื่องสูบน้ำต่ออนุกรม-ขนาน และค่าแก้เกจ (บทที่ 9)</h3>
  <div class="stmt">
    <p>ข้อสอบถามว่า: ในการต่อปั๊มน้ำ 2 เครื่องแบบ <b>อนุกรม (Series)</b> และแบบ <b>ขนาน (Parallel)</b> ค่าแก้ระดับความสูงเกจความดัน (\(H_d\)) มีค่าเท่าใด และการต่อทั้งสองแบบมีผลต่อ Total Head (\(H\)) และอัตราการไหล (\(Q\)) อย่างไรเมื่อเทียบกับปั๊มเดี่ยว</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">การต่อแบบอนุกรม</div><div><p>• ค่าแก้ระดับ: \(H_d = 0.17 - 0.24 = \mathbf{-0.07\ \text{m}}\) (ติดลบ)</p><p>• ทางเข้าดูดจากถังพักเปิดสู่อากาศ: \(h_1 = 0 \Rightarrow H = h_0 - 0.07\)</p><p>• <b>ผลลัพธ์:</b> เฮดรวมเพิ่มขึ้นเป็น <b>2 เท่า (\(H_{\text{series}} \approx 2H_1\))</b> ที่ \(Q\) เท่าเดิม</p></div></div>
    <div class="row"><div class="lab">การต่อแบบขนาน</div><div><p>• ค่าแก้ระดับ: \(H_d = 0.96 - 0.02 = \mathbf{+0.94\ \text{m}}\) (ต่อเข้า Manifold ด้านบน)</p><p>• <b>ผลลัพธ์:</b> อัตราการไหลรวมเพิ่มขึ้นเป็น <b>2 เท่า (\(Q_{\text{parallel}} \approx 2Q_1\))</b> ที่ \(H\) เท่าเดิม</p></div></div>
    <div class="row"><div class="lab">สูตรกำลังไฮดรอลิก</div><div>$$W_i = \gamma Q H = 9,810 \times Q \times H\quad [\text{Watts}]$$</div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">อนุกรม: \(H_d = -0.07\ \text{m}\ (H \times 2)\) · ขนาน: \(H_d = +0.94\ \text{m}\ (Q \times 2)\)</span></div></div>
  </div>

  <!-- Q12: Lab 10 & 11 Sluice & Venturi Flume -->
  <h3 class="grp" id="eq12">ข้อ 12: การไหลวิกฤตในรางเวนจูรี่และบานประตูน้ำ (บทที่ 10 และ 11)</h3>
  <div class="stmt">
    <p>รางเวนจูรี่ในทางน้ำเปิดทำงานแบบ Free Flow วัดความลึกน้ำต้นน้ำได้ \(y_1 = 30.0\text{ cm}\) คอคอดกว้าง \(b = 20.0\text{ cm}\) จงหา (ก) ความลึกวิกฤตที่คอคอด \(y_c\) และ (ข) อัตราการไหลทางทฤษฎี \(Q_{\text{th}}\)</p>
  </div>
  <div class="exam">
    <div class="row"><div class="lab">ข้อมูลที่กำหนด</div><div class="given">$$y_1 = 0.300\ \text{m},\quad b = 0.200\ \text{m},\quad g = 9.81\ \text{m/s}^2$$</div></div>
    <div class="row"><div class="lab">(ก) ความลึกวิกฤต yc</div><div>$$y_c = \frac{2}{3}y_1 = \frac{2}{3}(0.300\ \text{m}) = 0.200\ \text{m} = 20.0\ \text{cm}$$</div></div>
    <div class="row"><div class="lab">(ข) อัตราการไหล Q_th</div><div>$$\begin{aligned} Q_{\text{th}} &= \left(\frac{2}{3}\right)^{1.5} \sqrt{g} b y_1^{1.5} \\ &= (0.54433) \times \sqrt{9.81} \times (0.200) \times (0.300)^{1.5} \\ &= (0.54433)(3.1321)(0.200)(0.16432) = 0.05603\ \text{m}^3/\text{s} = 56.03\ \text{L/s} \end{aligned}$$</div></div>
    <div class="row"><div class="lab">คำตอบที่ถูกต้อง</div><div><span class="fin">\(y_c = 20.0\ \text{cm},\quad Q_{\text{th}} = 0.0560\ \text{m}^3/\text{s}\ (56.0\ \text{L/s})\)</span></div></div>
  </div>

  <div class="pn">
    <a href="#lab11">← บทที่ 11 รางเวนจูรี่</a>
    <a href="#calc">เครื่องคิดเลขแล็บ →</a>
  </div>
</section>
'''
