# -*- coding: utf-8 -*-

def get_section_lab10():
    return r'''
<section id="lab10">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 10 · การควบคุมทางน้ำเปิด พลังงานจำเพาะ และน้ำกระโดด</p>
    <h1>บทที่ 10: การไหลลอดประตูน้ำ (Flow under Sluice Gate)</h1>
    <p class="sub">Vertical Sluice Gate · สภาวะ Subcritical เทียบกับ Supercritical · Specific Energy · สัมประสิทธิ์การไหล</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 10</span>การไหลลอดบานประตูระบายน้ำ</h2>
  <div class="stmt">
    <p>ประตูระบายน้ำ (Sluice Gate) ทำหน้าที่ควบคุมระดับน้ำ ป้องกันน้ำท่วม และใช้วัดอัตราการไหลในคลองชลประทาน การไหลลอดประตูน้ำทำให้เกิดการเปลี่ยนแปลงสภาวะการไหลจาก <b>การไหลต่ำกว่าวิกฤต (Subcritical Flow)</b> ด้านเหนือน้ำ สู่ <b>การไหลเหนือวิกฤต (Supercritical Flow)</b> ลำน้ำพุ่งแรงด้านท้ายน้ำ ก่อนที่จะเปลี่ยนสภาวะกลับผ่านปรากฏการณ์ <b>น้ำกระโดด (Hydraulic Jump)</b></p>
  </div>

  <div class="jump">
    <a href="#lab10-theory">ก. วัตถุประสงค์และการพิสูจน์สมการ</a>
    <a href="#lab10-diagram">ข. แผนภาพประตูน้ำและ Hydraulic Jump</a>
    <a href="#lab10-coefficients">ค. สัมประสิทธิ์การไหลและ Specific Energy</a>
    <a href="#lab10-traps">ง. จุดดักคะแนนข้อสอบ</a>
    <a href="#lab10-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab10-theory">ก. วัตถุประสงค์และการพิสูจน์สมการ (Governing Equations)</h3>
  <p>สมมติว่าไม่มีการสูญเสียพลังงานระหว่างหน้าตัดที่ 0 (ต้นน้ำ) และหน้าตัดที่ 1 (ท้ายน้ำที่เกิดการหดตัวแคบที่สุด):</p>
  
  $$y_0 + \frac{V_0^2}{2g} = y_1 + \frac{V_1^2}{2g}\tag{10.2}$$

  <p>จากสมการความต่อเนื่องสำหรับทางน้ำเปิดสี่เหลี่ยมผืนผ้ากว้าง \(B\): \(V_0 = \frac{Q}{B y_0}\) และ \(V_1 = \frac{Q}{B y_1}\) แทนค่าลงในสมการพลังงานแล้วจัดรูป:</p>
  
  $$Q_{\text{theory}} = \frac{B y_1 \sqrt{2g y_0}}{\sqrt{\frac{y_1}{y_0} + 1}}\tag{10.6}$$
  $$V_{1,\text{theory}} = \frac{\sqrt{2g y_0}}{\sqrt{\frac{y_1}{y_0} + 1}}\tag{10.7}$$

  <h3 class="grp" id="lab10-diagram">ข. แผนภาพประตูน้ำ สภาวะการไหล และ Hydraulic Jump</h3>
  <figure>
    <svg viewBox="0 0 680 280" role="img" aria-label="ภาพด้านข้างของการไหลลอดประตูน้ำแสดงระดับน้ำต้นน้ำ ช่องเปิด และน้ำกระโดด">
      <!-- Bed line -->
      <line x1="50" y1="220" x2="630" y2="220" stroke="var(--ink)" stroke-width="4"/>
      <!-- Bed hatching -->
      <g stroke="var(--rule)" stroke-width="1.5">
        <line x1="60" y1="220" x2="50" y2="235"/>
        <line x1="120" y1="220" x2="110" y2="235"/>
        <line x1="180" y1="220" x2="170" y2="235"/>
        <line x1="240" y1="220" x2="230" y2="235"/>
        <line x1="300" y1="220" x2="290" y2="235"/>
        <line x1="360" y1="220" x2="350" y2="235"/>
        <line x1="420" y1="220" x2="410" y2="235"/>
        <line x1="480" y1="220" x2="470" y2="235"/>
        <line x1="540" y1="220" x2="530" y2="235"/>
        <line x1="600" y1="220" x2="590" y2="235"/>
      </g>

      <!-- Water Profile Upstream -->
      <path d="M 50 80 H 260 C 265 80 270 120 270 160 H 340 C 390 165 430 200 460 140 C 490 125 550 130 630 130 L 630 220 L 50 220 Z" fill="var(--water)" opacity="0.6"/>

      <!-- Sluice Gate Blade -->
      <rect x="260" y="30" width="16" height="135" fill="var(--ink)"/>
      <text x="268" y="22" font-size="13" font-weight="700" text-anchor="middle" fill="var(--ink)">บานประตูน้ำ</text>

      <!-- Gate opening yg -->
      <line x1="290" y1="165" x2="290" y2="220" stroke="var(--gold)" stroke-width="2" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="305" y="195" font-size="13" font-weight="700" fill="var(--gold)">yg</text>

      <!-- Upstream y0 -->
      <line x1="120" y1="80" x2="120" y2="220" stroke="var(--navy)" stroke-width="2" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="135" y="150" font-size="14" font-weight="700" fill="var(--navy)">y0 (ต้นน้ำ)</text>
      <text x="120" y="70" font-size="12" fill="var(--blue)">Subcritical (Fr &lt; 1)</text>

      <!-- Contracted depth y1 -->
      <line x1="350" y1="165" x2="350" y2="220" stroke="var(--red)" stroke-width="2" marker-start="url(#ar)" marker-end="url(#ar)"/>
      <text x="365" y="195" font-size="14" font-weight="700" fill="var(--red)">y1</text>
      <text x="350" y="155" font-size="12" fill="var(--red)">Supercritical (Fr &gt; 1)</text>

      <!-- Hydraulic Jump -->
      <text x="470" y="115" font-size="13" font-weight="700" fill="var(--gold)">Hydraulic Jump</text>
      <text x="470" y="132" font-size="11" fill="var(--gray)">(น้ำกระโดดสลายพลังงาน)</text>
    </svg>
    <figcaption>รูปที่ 10.1 สภาวะการไหลลอดบานประตูระบายน้ำ: จาก Subcritical สู่ Supercritical และ Hydraulic Jump</figcaption>
  </figure>

  <h3 class="grp" id="lab10-coefficients">ค. สัมประสิทธิ์การไหลและพลังงานจำเพาะ (Specific Energy)</h3>
  <ol class="st">
    <li><b>สัมประสิทธิ์การลดขนาดหน้าตัด (\(C_c\)):</b>
      $$C_c = \frac{y_1}{y_g}\tag{10.9}$$
      <p class="nt">โดย \(y_1\) คือความลึกของลำน้ำที่หน้าตัดหดตัวแคบที่สุด และ \(y_g\) คือระยะช่องเปิดของบานประตู</p>
    </li>
    <li><b>สัมประสิทธิ์การไหลจริง (\(C_d\)):</b>
      $$Q_{\text{actual}} = C_d y_g B \sqrt{2g y_0}\tag{10.12}$$
      $$C_d = \frac{C_v C_c}{\sqrt{\frac{y_1}{y_0} + 1}}\tag{10.11}$$
    </li>
    <li><b>พลังงานจำเพาะ (Specific Energy, \(E\)):</b>
      $$E = y + \frac{V^2}{2g}\tag{10.13}$$
    </li>
    <li><b>เลขฟรูด (Froude Number, \(Fr\)):</b>
      $$Fr = \frac{V}{\sqrt{g y}}$$
      <p class="gq">• \(Fr < 1\): การไหลต่ำกว่าวิกฤต (Subcritical Flow - น้ำลึก ไหลเอื่อย)<br>
      • \(Fr = 1\): การไหลวิกฤต (Critical Flow)<br>
      • \(Fr > 1\): การไหลเหนือวิกฤต (Supercritical Flow - น้ำตื้น พุ่งแรง)</p>
    </li>
  </ol>

  <h3 class="grp" id="lab10-traps">ง. จุดดักคะแนนข้อสอบ</h3>
  <div class="bx trap">
    <b>ความแตกต่างระหว่าง \(y_g\) กับ \(y_1\):</b>
    <div>
      • \(y_g\) คือ <b>ระยะยกของบานประตูน้ำ (Gate Opening)</b><br>
      • \(y_1\) คือ <b>ความลึกจริงของลำน้ำที่พุ่งออกมา (Vena Contracta Depth)</b><br>
      • \(y_1\) จะมีค่าน้อยกว่า \(y_g\) เสมอ (\(y_1 < y_g\)) เพราะสายน้ำเกิดการหดตัว (\(C_c = y_1/y_g \approx 0.60\)) อย่าแทนตัวเลขสลับกัน!
    </div>
  </div>

  <h3 class="grp" id="lab10-exam">จ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> ประตูน้ำบานตรงในทางน้ำเปิดกว้าง \(B = 0.50\text{ m}\) ยกบานสูง \(y_g = 5.0\text{ cm}\) วัดระดับน้ำต้นน้ำได้ \(y_0 = 45.0\text{ cm}\) และระดับน้ำที่หดตัวแคบที่สุดท้ายน้ำได้ \(y_1 = 3.1\text{ cm}\) จงหา (ก) อัตราการไหลทฤษฎี \(Q_{\text{th}}\) (ข) สัมประสิทธิ์การหดตัว \(C_c\) และ (ค) เลขฟรูด \(Fr_0\) เหนือน้ำ และ \(Fr_1\) ท้ายน้ำ</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & B = 0.50\ \text{m},\quad y_g = 0.050\ \text{m} \\ & y_0 = 0.450\ \text{m},\quad y_1 = 0.031\ \text{m} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) Q ทฤษฎี</div>
      <div>$$\begin{aligned} Q_{\text{th}} &= \frac{B y_1 \sqrt{2g y_0}}{\sqrt{\frac{y_1}{y_0} + 1}} \\ &= \frac{(0.50)(0.031)\sqrt{2(9.81)(0.450)}}{\sqrt{\frac{0.031}{0.450} + 1}} \\ &= \frac{(0.0155)(2.9714)}{\sqrt{1.06889}} = \frac{0.046057}{1.03387} = 0.04455\ \text{m}^3/\text{s} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) สัมประสิทธิ์ Cc</div>
      <div>$$C_c = \frac{y_1}{y_g} = \frac{3.1\ \text{cm}}{5.0\ \text{cm}} = 0.6200\quad (\text{ปกติ 0.60-0.64})$$</div>
    </div>
    <div class="row">
      <div class="lab">(ค) Froude Fr0 และ Fr1</div>
      <div>$$\begin{aligned} V_0 &= \frac{Q_{\text{th}}}{B y_0} = \frac{0.04455}{(0.50)(0.450)} = 0.1980\ \text{m/s} \\ Fr_0 &= \frac{V_0}{\sqrt{g y_0}} = \frac{0.1980}{\sqrt{(9.81)(0.450)}} = \frac{0.1980}{2.101} = 0.0942 < 1\ (\text{Subcritical}) \\ V_1 &= \frac{Q_{\text{th}}}{B y_1} = \frac{0.04455}{(0.50)(0.031)} = 2.8742\ \text{m/s} \\ Fr_1 &= \frac{V_1}{\sqrt{g y_1}} = \frac{2.8742}{\sqrt{(9.81)(0.031)}} = \frac{2.8742}{0.5515} = 5.212 > 1\ (\text{Supercritical}) \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(Q_{\text{th}} = 0.0446\ \text{m}^3/\text{s},\quad C_c = 0.620,\quad Fr_0 = 0.094\ (\text{Sub}),\quad Fr_1 = 5.21\ (\text{Super})\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab9">← บทที่ 9 การทดสอบเครื่องสูบน้ำ</a>
    <a href="#lab11">บทที่ 11 รางน้ำแบบเวนจูรี่ →</a>
  </div>
</section>
'''
