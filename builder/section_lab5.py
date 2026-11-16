# -*- coding: utf-8 -*-

def get_section_lab5():
    return r'''
<section id="lab5">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 5 · การไหลในทางน้ำเปิดและความต้านทานท้องคลอง</p>
    <h1>บทที่ 5: สมการแมนนิ่ง (Manning's Equation)</h1>
    <p class="sub">Open Channel Flow · สัมประสิทธิ์ความขรุขระ n · รัศมีชลศาสตร์ Rh · คลองเรียบเทียบกับคลองมีหญ้า</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 5</span>การไหลในทางน้ำเปิดและสมการแมนนิ่ง</h2>
  <div class="stmt">
    <p>การไหลในทางน้ำเปิด (Open Channel Flow) แตกต่างจากการไหลในท่อปิดตรงที่มี <b>ผิวน้ำอิสระสัมผัสกับบรรยากาศ (Free Surface)</b> และการไหลขับเคลื่อนด้วย <b>แรงโน้มถ่วง (Gravity Force)</b> ตามความลาดชันของท้องคลอง สมดุลกับ <b>แรงต้านทานความเสียดทาน (Boundary Shear Resistance)</b> จากพื้นผิวคลอง สมการแมนนิ่งเป็นสมการเอมพิริคัลที่ใช้กันแพร่หลายที่สุดในวิศวกรรมชลศาสตร์และแหล่งน้ำ</p>
  </div>

  <div class="jump">
    <a href="#lab5-principle">ก. วัตถุประสงค์และสมการควบคุม</a>
    <a href="#lab5-diagram">ข. รูปตัดทางน้ำเปิดและเส้นขอบเปียก</a>
    <a href="#lab5-smooth-rough">ค. การเปรียบเทียบพื้นเรียบ vs พื้นมีหญ้า</a>
    <a href="#lab5-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab5-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab5-principle">ก. วัตถุประสงค์และสมการควบคุม (Manning's Equation)</h3>
  <p>ในปี ค.ศ. 1889 วิศวกรชาวไอริช โรเบิร์ต แมนนิ่ง (Robert Manning) ได้นำเสนอสมการความเร็วเฉลี่ยในทางน้ำเปิด ซึ่งในระบบหน่วย SI เขียนได้ดังนี้:</p>
  
  $$V = \frac{1}{n} R_h^{2/3} S_0^{1/2}\tag{5.2}$$
  $$Q = V A = \frac{1}{n} A R_h^{2/3} S_0^{1/2}$$

  <ol class="st">
    <li><b>\(V\):</b> ความเร็วเฉลี่ยของการไหลในทางน้ำเปิด [m/s]</li>
    <li><b>\(n\):</b> สัมประสิทธิ์ความขรุขระของแมนนิ่ง (Manning's Roughness Coefficient) แสดงถึงความต้านทานของผนังคลอง</li>
    <li><b>\(R_h\):</b> รัศมีชลศาสตร์ (Hydraulic Radius) [m] หาจากอัตราส่วนพื้นที่หน้าตัดการไหลต่อเส้นขอบเปียก:
      $$R_h = \frac{A}{P_w}$$
    </li>
    <li><b>\(S_0\):</b> ความลาดชันของท้องคลอง (Bed Slope) หาจาก \(\tan\theta\) (เช่น มุมเอียง \(\theta = 0.125^\circ \Rightarrow S_0 = \tan 0.125^\circ\))</li>
  </ol>

  <h3 class="grp" id="lab5-diagram">ข. เรขาคณิตหน้าตัดทางน้ำเปิดสี่เหลี่ยมผืนผ้า</h3>
  <figure>
    <svg viewBox="0 0 680 240" role="img" aria-label="ภาพตัดขวางทางน้ำเปิดสี่เหลี่ยมผืนผ้าแสดงเส้นขอบเปียก">
      <!-- Channel Bed & Walls -->
      <polyline points="180,50 180,180 500,180 500,50" fill="none" stroke="var(--ink)" stroke-width="4"/>
      <!-- Water body -->
      <rect x="182" y="100" width="316" height="78" fill="var(--water)" opacity="0.6"/>
      <!-- Water surface line -->
      <line x1="182" y1="100" x2="498" y2="100" stroke="var(--blue)" stroke-width="2" stroke-dasharray="6 3"/>
      <polygon points="340,100 335,90 345,90" fill="var(--blue)"/>
      <text x="355" y="95" font-size="13" fill="var(--blue)">ผิวน้ำอิสระ (ไม่คิดใน P_w!)</text>

      <!-- Wetted Perimeter highlighted in Red -->
      <line x1="175" y1="100" x2="175" y2="185" stroke="var(--red)" stroke-width="3"/>
      <line x1="175" y1="185" x2="505" y2="185" stroke="var(--red)" stroke-width="3"/>
      <line x1="505" y1="185" x2="505" y2="100" stroke="var(--red)" stroke-width="3"/>
      <text x="340" y="215" font-size="14" font-weight="700" text-anchor="middle" fill="var(--red)">เส้นขอบเปียก P_w = B + 2y (เส้นสีแดง 3 ด้าน)</text>

      <!-- Dimensions B and y -->
      <line x1="180" y1="40" x2="500" y2="40" stroke="var(--navy)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="340" y="32" font-size="14" font-weight="600" text-anchor="middle" fill="var(--navy)">ความกว้างคลอง B</text>

      <line x1="520" y1="100" x2="520" y2="180" stroke="var(--navy)" stroke-width="1.5" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="535" y="145" font-size="14" font-weight="600" fill="var(--navy)">ความลึก y</text>
    </svg>
    <figcaption>รูปที่ 5.1 หน้าตัดคลองสี่เหลี่ยมผืนผ้า: พื้นที่ \(A = By\) และเส้นขอบเปียก \(P_w = B + 2y\)</figcaption>
  </figure>

  <h3 class="grp" id="lab5-smooth-rough">ค. การเปรียบเทียบพื้นคลองเรียบ vs พื้นคลองมีหญ้า</h3>
  <div class="tw">
    <table>
      <caption>เปรียบเทียบพฤติกรรมการไหลในห้องแล็บที่อัตราการไหล Q เท่ากัน</caption>
      <thead>
        <tr><th>ลักษณะพื้นคลอง</th><th>ค่าสัมประสิทธิ์ความขรุขระ n</th><th>ความเร็วการไหล V</th><th>ระดับความลึกของน้ำ y</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><b>1. พื้นคลองเรียบ (Smooth Bed)</b></td>
          <td>ต่ำ (\(n \approx 0.010 - 0.012\))</td>
          <td><b>ไหลเร็ว</b> แรงต้านน้อย</td>
          <td><b>ตื้นกว่า</b> (\(y\) ต่ำ)</td>
        </tr>
        <tr>
          <td><b>2. พื้นคลองมีหญ้า (Rough Grass Bed)</b></td>
          <td>สูง (\(n \approx 0.025 - 0.035\))</td>
          <td><b>ไหลช้า</b> แรงเสียดทานสูง</td>
          <td><b>ลึกกว่า</b> (\(y_1\) ยกตัวสูงขึ้น)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="lab5-traps">ง. จุดดักคะแนนข้อสอบ</h3>
  <div class="bx trap">
    <b>กับดักเส้นขอบเปียก (Wetted Perimeter Trap):</b>
    <div>
      เส้นขอบเปียก \(P_w\) หมายถึง <b>เฉพาะขอบเขตที่สัมผัสกับของแข็งเท่านั้น</b><br>
      • สำหรับคลองสี่เหลี่ยมผืนผ้า \(P_w = B + 2y\) (พื้นคลอง + ผนัง 2 ข้าง)<br>
      • <b>ห้ามบวกผิวน้ำด้านบนเด็ดขาด!</b> ผิวน้ำด้านบนเป็นของไหลสัมผัสอากาศ ไม่ใช่ของแข็ง
    </div>
  </div>

  <div class="bx chk">
    <b>ความลาดชันท้องคลอง \(S_0\):</b>
    <div>
      ในคู่มือระบุมุมเอียงเป็นองศา เช่น \(0.125^\circ\) ต้องแทนค่าในสูตรด้วย \(S_0 = \tan(0.125^\circ)\) เสมอ
    </div>
  </div>

  <h3 class="grp" id="lab5-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> ทางน้ำเปิดรูปสี่เหลี่ยมผืนผ้ากว้าง \(B = 30\text{ cm}\) ปรับความลาดชันท้องคลอง \(\theta = 0.25^\circ\) ปล่อยน้ำด้วยอัตราการไหล \(Q = 18\text{ m}^3/\text{hr}\) วัดความลึกน้ำที่พื้นเรียบได้ \(y = 4.2\text{ cm}\) จงหา (ก) รัศมีชลศาสตร์ \(R_h\) (ข) ความเร็วเฉลี่ย \(V\) และ (ค) ค่าสัมประสิทธิ์ความขรุขระ Manning's \(n\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & B = 0.30\ \text{m},\quad y = 0.042\ \text{m} \\ & Q = 18\ \text{m}^3/\text{hr} = \frac{18}{3600} = 0.0050\ \text{m}^3/\text{s} \\ & S_0 = \tan(0.25^\circ) = 4.3633 \times 10^{-3} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) หา A, P_w, R_h</div>
      <div>$$\begin{aligned} A &= B \cdot y = (0.30)(0.042) = 0.0126\ \text{m}^2 \\ P_w &= B + 2y = 0.30 + 2(0.042) = 0.384\ \text{m} \\ R_h &= \frac{A}{P_w} = \frac{0.0126}{0.384} = 0.03281\ \text{m} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) ความเร็วเฉลี่ย V</div>
      <div>$$V = \frac{Q}{A} = \frac{0.0050\ \text{m}^3/\text{s}}{0.0126\ \text{m}^2} = 0.3968\ \text{m/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ค) สัมประสิทธิ์ Manning n</div>
      <div>$$\begin{aligned} V &= \frac{1}{n} R_h^{2/3} S_0^{1/2} \\ n &= \frac{R_h^{2/3} S_0^{1/2}}{V} \\ &= \frac{(0.03281)^{2/3} \sqrt{4.3633 \times 10^{-3}}}{0.3968} \\ &= \frac{(0.1025)(0.06605)}{0.3968} = 0.01706\quad \htmlClass{ok}{(\text{ค่าสมเหตุสมผลสำหรับพื้นผิวแล็บ})} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(R_h = 0.0328\ \text{m},\quad V = 0.397\ \text{m/s},\quad n = 0.0171\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab4">← บทที่ 4 สมการเบอร์นูลี่</a>
    <a href="#lab6">บทที่ 6 การวัดอัตราการไหลด้วยฝาย →</a>
  </div>
</section>
'''
