# -*- coding: utf-8 -*-

def get_section_lab7():
    return r'''
<section id="lab7">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 7 · การสูญเสียพลังงานหลัก การสูญเสียรอง และโครงข่ายท่อ</p>
    <h1>บทที่ 7: การสูญเสียพลังงานในท่อ (Loss in Pipe Network)</h1>
    <p class="sub">Darcy-Weisbach · สัมประสิทธิ์ความเสียดทาน f · การต่อท่อแบบขนานและแบบอนุกรม · ค่าแก้ระดับ Datum</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 7</span>การสูญเสียพลังงานในโครงข่ายท่อ</h2>
  <div class="stmt">
    <p>เมื่อของเหลวไหลในระบบท่อ ย่อมเกิดการสูญเสียพลังงานกลกลายสภาพเป็นพลังงานความร้อน แบ่งออกเป็น 2 ประเภทหลัก คือ <b>การสูญเสียหลัก (Major Losses)</b> อันเนื่องจากแรงเสียดทานตามความยาวท่อ และ <b>การสูญเสียรอง (Minor Losses)</b> อันเกิดจากข้อต่อ ข้องอ วาล์ว หรือการเปลี่ยนแปลงขนาดหน้าตัด การทดลองนี้ศึกษาพฤติกรรมการสูญเสียพลังงานในท่อเดี่ยว ท่อต่อขนาน และท่อต่ออนุกรม</p>
  </div>

  <div class="jump">
    <a href="#lab7-theory">ก. วัตถุประสงค์และสมการพลังงาน</a>
    <a href="#lab7-diagram">ข. ผังโครงข่ายท่อ A, B, C, D</a>
    <a href="#lab7-parallel-series">ค. การต่อท่อแบบขนาน vs แบบอนุกรม</a>
    <a href="#lab7-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab7-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab7-theory">ก. วัตถุประสงค์และสมการพลังงาน (Governing Energy Equations)</h3>
  <p>สมการพลังงานระหว่างจุดที่ 1 และจุดที่ 2 ของระบบท่อที่มีการเปลี่ยนแปลงระดับความสูง:</p>
  
  $$\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + Z_1 = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + Z_2 + h_L\tag{7.4}$$

  <p>สำหรับท่อที่มีขนาดเส้นผ่านศูนย์กลางคงที่ตลอดเส้นทาง (\(D_1 = D_2 \Rightarrow V_1 = V_2\)) เฮดความเร็วจะตัดกันหมด ทำให้การสูญเสียพลังงานรวม (\(h_L\)) มีค่าเท่ากับ:</p>
  
  $$h_L = \frac{P_1 - P_2}{\gamma} + (Z_1 - Z_2)\tag{7.5}$$

  <div class="ty">
    <div class="tyh">1. การสูญเสียพลังงานหลัก (Major Losses: แรงเสียดทาน)</div>
    <div class="tyb">
      <p>คำนวณจากสมการดาร์ซี-ไวส์บาค (Darcy-Weisbach Equation):</p>
      $$h_f = f \frac{L}{D} \frac{V^2}{2g} = \frac{8 f L Q^2}{\pi^2 g D^5}\tag{7.6}$$
      <p class="gq">• การไหลราบเรียบ (Laminar, \(Re < 2000\)): \(f = \frac{64}{Re}\)<br>
      • การไหลปั่นป่วน (Turbulent, \(Re > 4000\)): อ่านค่า \(f\) จาก Moody Chart หรือแก้สมการ Colebrook-White</p>
    </div>
  </div>

  <div class="ty">
    <div class="tyh">2. การสูญเสียพลังงานรอง (Minor Losses: ข้อต่อและอุปกรณ์)</div>
    <div class="tyb">
      $$h_m = K_L \frac{V^2}{2g}\tag{7.3}$$
      <p class="gq">โดยที่ \(K_L\) คือสัมประสิทธิ์การสูญเสียรอง (Loss Coefficient) ของข้อต่อ ข้องอ หรือวาล์วชนิดนั้นๆ</p>
    </div>
  </div>

  <h3 class="grp" id="lab7-diagram">ข. แผนผังโครงข่ายท่อทดสอบ (Pipes A, B, C, D)</h3>
  <figure>
    <svg viewBox="0 0 680 260" role="img" aria-label="แผนผังแผงทดสอบท่อ A, B, C, D พร้อมวาล์วควบคุม">
      <!-- Inflow header -->
      <line x1="80" y1="210" x2="600" y2="210" stroke="var(--ink)" stroke-width="3"/>
      <line x1="80" y1="210" x2="80" y2="245" stroke="var(--blue)" stroke-width="3" marker-start="url(#ar)"/>
      <text x="80" y="255" font-size="13" font-weight="700" text-anchor="middle" fill="var(--blue)">ทางน้ำเข้า (Qin, จุด H1)</text>

      <!-- Pipes A, B, C, D vertical branches -->
      <!-- Pipe A -->
      <line x1="160" y1="210" x2="160" y2="60" stroke="var(--navy)" stroke-width="4"/>
      <circle cx="160" cy="180" r="7" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>
      <circle cx="160" cy="90" r="7" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>
      <text x="160" y="140" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">ท่อ A</text>

      <!-- Pipe B -->
      <line x1="280" y1="210" x2="280" y2="60" stroke="var(--navy)" stroke-width="4"/>
      <circle cx="280" cy="180" r="7" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>
      <circle cx="280" cy="90" r="7" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>
      <text x="280" y="140" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">ท่อ B</text>

      <!-- Pipe C -->
      <line x1="400" y1="210" x2="400" y2="60" stroke="var(--navy)" stroke-width="4"/>
      <circle cx="400" cy="180" r="7" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>
      <circle cx="400" cy="90" r="7" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>
      <text x="400" y="140" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">ท่อ C</text>

      <!-- Pipe D -->
      <line x1="520" y1="210" x2="520" y2="60" stroke="var(--navy)" stroke-width="4"/>
      <circle cx="520" cy="180" r="7" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>
      <circle cx="520" cy="90" r="7" fill="var(--bg)" stroke="var(--ink)" stroke-width="2"/>
      <text x="520" y="140" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">ท่อ D</text>

      <!-- Outflow header -->
      <line x1="80" y1="60" x2="600" y2="60" stroke="var(--ink)" stroke-width="3"/>
      <line x1="600" y1="60" x2="600" y2="25" stroke="var(--red)" stroke-width="3" marker-end="url(#ar)"/>
      <text x="600" y="15" font-size="13" font-weight="700" text-anchor="middle" fill="var(--red)">ทางน้ำออก (Qout, จุด H2)</text>
    </svg>
    <figcaption>รูปที่ 7.1 ผังการต่อแผงท่อทดสอบ A, B, C, D พร้อมวาล์วสลับโหมดขนานและอนุกรม</figcaption>
  </figure>

  <h3 class="grp" id="lab7-parallel-series">ค. การต่อท่อแบบขนาน vs แบบอนุกรม (Parallel vs Series)</h3>
  <div class="tw">
    <table>
      <caption>กฎสมดุลของโครงข่ายท่อ 2 ลักษณะ (Network Laws)</caption>
      <thead>
        <tr><th>คุณลักษณะ</th><th>การต่อท่อแบบขนาน (Parallel Pipes)</th><th>การต่อท่อแบบอนุกรม (Series Pipes)</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><b>เฮดสูญเสีย (\(h_L\))</b></td>
          <td><b>เท่ากันทุกเส้นท่อ:</b><br>\(h_{L1} = h_{L2} = h_{L3} = h_{L,\text{total}}\)</td>
          <td><b>บวกสะสมรวมกัน:</b><br>\(h_{L,\text{total}} = h_{L1} + h_{L2} + h_{L3}\)</td>
        </tr>
        <tr>
          <td><b>อัตราการไหล (\(Q\))</b></td>
          <td><b>แยกไหลแล้วรวมกัน:</b><br>\(Q_{\text{total}} = Q_1 + Q_2 + Q_3\)</td>
          <td><b>เท่ากันทุกท่อ:</b><br>\(Q_1 = Q_2 = Q_3 = Q_{\text{total}}\)</td>
        </tr>
        <tr>
          <td><b>กรณีทดสอบในแล็บ</b></td>
          <td>(1) A+B (2) A+B+C (3) A+B+C+D</td>
          <td>(1) B+C (2) A+C (3) D+C+B</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="lab7-traps">ง. จุดดักคะแนนข้อสอบ</h3>
  <div class="bx trap">
    <b>กับดักค่าแก้ระดับความสูงท่อ \((Z_1 - Z_2)\):</b>
    <div>
      ในชุดทดลองของ Armfield หรือชุดท่อแนวตั้ง จุดวัดความดัน \(H_1\) และ \(H_2\) อยู่คนละระดับความสูง<br>
      • การคำนวณ \(h_L\) จากผลต่างความดันมาโนมิเตอร์ <b>ต้องบวกเทอมความต่างระดับ \((Z_1 - Z_2)\) เสมอ</b><br>
      • หากจุด 1 อยู่ต่ำกว่าจุด 2 ค่า \(Z_1 - Z_2\) จะติดลบ อย่าลืมดูเครื่องหมายให้ถูกต้อง
    </div>
  </div>

  <div class="bx chk">
    <b>ขั้นตอนการวิเคราะห์ผลการต่อท่อ:</b>
    <div>
      ในการทดลอง ให้นักศึกษาพล็อตกราฟมาตรฐาน \(Q\) vs \(h_L\) ของท่อเดี่ยวแต่ละท่อก่อน จากนั้นเมื่อทดสอบการต่อแบบขนานหรืออนุกรม ให้อ่านค่า \(Q\) หรือ \(h_L\) จากกราฟท่อเดี่ยวมาเปรียบเทียบกับค่ารวมที่วัดได้จริงจากถังตวง Volumetric Tank
    </div>
  </div>

  <h3 class="grp" id="lab7-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> ท่อ A และ ท่อ B ต่อขนานกัน ความยาวท่อเท่ากัน \(L = 20\text{ m}\) ท่อ A มี \(D_A = 50\text{ mm}, f_A = 0.020\) ท่อ B มี \(D_B = 25\text{ mm}, f_B = 0.024\) น้ำไหลผ่านระบบด้วยอัตราการไหลรวม \(Q_{\text{total}} = 0.0080\text{ m}^3/\text{s}\) (ไม่คิด minor loss) จงหาอัตราการไหลแยกในแต่ละท่อ \(Q_A\) และ \(Q_B\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & L = 20\ \text{m},\quad Q_{\text{total}} = 0.0080\ \text{m}^3/\text{s} \\ & D_A = 0.050\ \text{m},\ f_A = 0.020 \\ & D_B = 0.025\ \text{m},\ f_B = 0.024 \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">เงื่อนไขท่อขนาน</div>
      <div>$$h_{f,A} = h_{f,B} \Rightarrow \frac{8 f_A L Q_A^2}{\pi^2 g D_A^5} = \frac{8 f_B L Q_B^2}{\pi^2 g D_B^5}$$</div>
    </div>
    <div class="row">
      <div class="lab">อัตราส่วน QA / QB</div>
      <div>$$\begin{aligned} \frac{Q_A^2}{Q_B^2} &= \frac{f_B}{f_A} \left(\frac{D_A}{D_B}\right)^5 = \left(\frac{0.024}{0.020}\right)\left(\frac{50}{25}\right)^5 \\ &= (1.20)(2^5) = (1.20)(32) = 38.4 \\ \frac{Q_A}{Q_B} &= \sqrt{38.4} = 6.1968 \Rightarrow Q_A = 6.1968 Q_B \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">แก้สมการหา QA, QB</div>
      <div>$$\begin{aligned} Q_{\text{total}} &= Q_A + Q_B = 6.1968 Q_B + Q_B = 7.1968 Q_B \\ 0.0080 &= 7.1968 Q_B \\ Q_B &= \frac{0.0080}{7.1968} = 0.001112\ \text{m}^3/\text{s} = 1.11\ \text{L/s} \\ Q_A &= 0.0080 - 0.001112 = 0.006888\ \text{m}^3/\text{s} = 6.89\ \text{L/s}\quad \htmlClass{ok}{(\text{OK})} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(Q_A = 6.89\ \text{L/s}\ (86.1\%),\quad Q_B = 1.11\ \text{L/s}\ (13.9\%)\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab6">← บทที่ 6 การวัดด้วยฝาย</a>
    <a href="#lab8">บทที่ 8 การไหลผ่านรูลอด →</a>
  </div>
</section>
'''
