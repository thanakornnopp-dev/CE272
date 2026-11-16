# -*- coding: utf-8 -*-

def get_section_lab9():
    return r'''
<section id="lab9">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 9 · การทดสอบสมรรถนะเครื่องสูบน้ำและระบบต่ออนุกรม-ขนาน</p>
    <h1>บทที่ 9: การทดสอบเครื่องสูบน้ำ (Centrifugal Pump Test)</h1>
    <p class="sub">ปั๊มเดี่ยว · ปั๊มต่ออนุกรม (เฮด x2) · ปั๊มต่อขนาน (Q x2) · ค่าแก้ระดับเกจ Hd · กราฟ H-Q ตามจอ iPad · กำลังน้ำ Wi</p>
    <p class="by">CE 272 ปฏิบัติการกลศาสตร์ของไหล · ภาควิชาวิศวกรรมโยธา มหาวิทยาลัยธรรมศาสตร์</p>
    <p class="pracnote">โหมดฝึกเปิดอยู่: ซ่อนวิธีทำไว้ แตะแต่ละขั้นเพื่อดู (ลองเขียนเองก่อน) กดปุ่ม "ฝึก" อีกครั้งเพื่อปิด</p>
  </header>

  <h2 class="prob"><span class="tag">บทที่ 9</span>สมรรถนะปั๊มน้ำหอยโข่งและค่าแก้ระดับเกจ</h2>
  <div class="stmt">
    <p>เครื่องสูบน้ำหอยโข่ง (Centrifugal Pump) เป็นหัวใจสำคัญในการขนถ่ายของเหลวในงานวิศวกรรมโยธา การทดลองนี้ศึกษาความสัมพันธ์ระหว่างอัตราการไหล (\(Q\)) เฮดรวม (\(H\)) กำลังงานที่ถ่ายทอดให้น้ำ (\(W_i\)) และประสิทธิภาพของปั๊ม พร้อมเปรียบเทียบข้อแตกต่างระหว่างการต่อแบบอนุกรม (Series: เพื่อเพิ่มแรงดัน) และการต่อแบบขนาน (Parallel: เพื่อเพิ่มปริมาณน้ำ) <b>บทนี้เป็นบทที่อาจารย์เน้นย้ำและออกข้อสอบเข้มข้นที่สุด</b></p>
  </div>

  <div class="jump">
    <a href="#lab9-theory">ก. วัตถุประสงค์และสมการพลังงานปั๊ม</a>
    <a href="#lab9-datum">ข. ค่าแก้ระดับเกจวัดความดัน (Hd 3 โหมด)</a>
    <a href="#lab9-diagram">ค. แผนภาพวาล์วและการไหล 3 รูปแบบ</a>
    <a href="#lab9-valves">ง. ตารางเปิด-ปิดวาล์วตามข้อสอบ</a>
    <a href="#lab9-hq">จ. กราฟความสัมพันธ์ H-Q (ตามจอ iPad)</a>
    <a href="#lab9-power">ฉ. กำลังไฮดรอลิกและประสิทธิภาพ</a>
    <a href="#lab9-traps">ช. จุดดักคะแนนข้อสอบของอาจารย์</a>
    <a href="#lab9-exam">ซ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
  </div>

  <h3 class="grp" id="lab9-theory">ก. วัตถุประสงค์และสมการพลังงานข้ามเครื่องสูบน้ำ</h3>
  <p>เมื่อน้ำไหลผ่านเครื่องสูบน้ำ ปั๊มจะเพิ่มพลังงานกลให้แก่ของเหลว เขียนสมการพลังงานระหว่างท่อดูด (จุด 1) และท่อส่ง (จุด 2):</p>
  
  $$\frac{P_1}{\gamma} + \frac{V_1^2}{2g} + Z_1 + H = \frac{P_2}{\gamma} + \frac{V_2^2}{2g} + Z_2 + h_L\tag{9.1}$$

  <p>เมื่อท่อดูดและท่อส่งมีขนาดเส้นผ่านศูนย์กลางเท่ากัน (\(V_1 = V_2\)) และรวมการสูญเสียภายในเป็นสมรรถนะสุทธิของปั๊ม จะได้เฮดรวมของเครื่องสูบน้ำ (Total Head, \(H\)):</p>
  
  $$H = (h_2 - h_1) + (Z_2 - Z_1) = (h_2 - h_1) + H_d\tag{9.6}$$

  <h3 class="grp" id="lab9-datum">ข. ค่าแก้ระดับความสูงของเกจวัดความดัน (Datum Head Correction, Hd)</h3>
  <p>เนื่องจากเกจวัดความดันด้านขาเข้าและขาออกไม่ได้ติดตั้งอยู่ที่ระนาบความสูงเดียวกัน ค่าระดับความสูงอ้างอิงจากคู่มือหน้า 69 มีดังนี้:</p>
  
  <div class="tw">
    <table>
      <caption>ระยะจากระดับอ้างอิงถึงจุดวัดความดัน (Head Correction Factors จากคู่มือหน้า 49)</caption>
      <thead>
        <tr><th>ตำแหน่งเกจวัด</th><th>สัญลักษณ์</th><th>ระยะความสูงจากจุดอ้างอิง (m)</th></tr>
      </thead>
      <tbody>
        <tr><td>เกจท่อร่วมด้านบน (Manifold Gauge)</td><td>\(h_d(\text{manifold})\)</td><td>0.96 m</td></tr>
        <tr><td>เกจท่อส่งออก (Outlet Gauge)</td><td>\(h_d(\text{outlet})\)</td><td>0.17 m</td></tr>
        <tr><td>เกจท่อดูดเข้า (Inlet Gauge)</td><td>\(h_d(\text{inlet})\)</td><td>0.02 m</td></tr>
        <tr><td>ทางเข้าปั๊มในโต๊ะ (Bench Pump Inlet)</td><td>\(h_d(\text{bench})\)</td><td>0.24 m</td></tr>
      </tbody>
    </table>
  </div>

  <div class="ty">
    <div class="tyh">การคำนวณ \(H_d\) สำหรับการต่อปั๊มทั้ง 3 รูปแบบ (จำแม่นๆ ออกข้อสอบ 100%)</div>
    <div class="tyb">
      <ol class="st">
        <li><b>1. เครื่องสูบน้ำตัวเดียว (Single Pump):</b>
          $$H_d = h_d(\text{outlet}) - h_d(\text{inlet}) = 0.17 - 0.02 = \mathbf{+0.15\ \text{m}}$$
          $$H = (h_0 - h_1) + 0.15$$
        </li>
        <li><b>2. เครื่องสูบน้ำต่อแบบอนุกรม (Series Pumps):</b>
          <p>ปั๊มตัวแรกดูดน้ำจากถังพัก Sump Tank ซึ่งเปิดสู่บรรยากาศ ความดันเกจทางเข้าจึงถือเป็นศูนย์ (\(h_1 = 0\)) และใช้ระยะท่อดูดของโต๊ะ:</p>
          $$H_d = h_d(\text{outlet}) - h_d(\text{bench}) = 0.17 - 0.24 = \mathbf{-0.07\ \text{m}}\quad (\text{ค่าติดลบ!})$$
          $$H = (h_0 - 0) - 0.07 = h_0 - 0.07$$
          <p class="gq">• ผลลัพธ์: Total Head รวมเพิ่มขึ้นเป็น <b>2 เท่า (\(H_{\text{series}} \approx 2 H_1\))</b> ที่อัตราการไหล \(Q\) เท่าเดิม</p>
        </li>
        <li><b>3. เครื่องสูบน้ำต่อแบบขนาน (Parallel Pumps):</b>
          <p>น้ำจากปั๊มทั้งสองตัวจะถูกส่งไปรวมกันที่ท่อร่วมด้านบน (Manifold):</p>
          $$H_d = h_d(\text{manifold}) - h_d(\text{inlet}) = 0.96 - 0.02 = \mathbf{+0.94\ \text{m}}$$
          $$H = (h_m - h_1) + 0.94$$
          <p class="gq">• ผลลัพธ์: อัตราการไหลรวมเพิ่มขึ้นเป็น <b>2 เท่า (\(Q_{\text{parallel}} \approx 2 Q_1\))</b> ที่เฮด \(H\) เท่าเดิม</p>
        </li>
      </ol>
    </div>
  </div>

  <h3 class="grp" id="lab9-diagram">ค. แผนภาพวาล์วและการไหลในระบบปั๊มทั้ง 3 โหมด</h3>
  <figure>
    <svg viewBox="0 0 680 290" role="img" aria-label="แผนภาพเปรียบเทียบการไหลของปั๊มเดี่ยว อนุกรม และขนาน">
      <!-- 1. Single Pump -->
      <g transform="translate(30, 20)">
        <text x="90" y="20" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">1. ปั๊มเดี่ยว (Single)</text>
        <rect x="20" y="40" width="140" height="90" fill="var(--hover)" stroke="var(--ink)" stroke-width="1.5"/>
        <circle cx="70" cy="85" r="20" fill="var(--bg)" stroke="var(--navy)" stroke-width="2"/>
        <text x="70" y="90" font-size="11" font-weight="700" text-anchor="middle" fill="var(--navy)">P1</text>
        <path d="M 20 85 H 50" stroke="var(--blue)" stroke-width="3" marker-end="url(#ar)"/>
        <path d="M 70 65 V 40 H 130 V 160" stroke="var(--red)" stroke-width="2.5" marker-end="url(#ar)"/>
        <text x="90" y="190" font-size="13" font-weight="600" text-anchor="middle" fill="var(--navy)">\(H_d = +0.15\text{ m}\)</text>
        <text x="90" y="215" font-size="12" fill="var(--gray)" text-anchor="middle">\(H_1, Q_1\)</text>
      </g>

      <!-- 2. Series Pump -->
      <g transform="translate(250, 20)">
        <text x="90" y="20" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">2. ปั๊มอนุกรม (Series)</text>
        <rect x="10" y="40" width="160" height="90" fill="var(--hover)" stroke="var(--ink)" stroke-width="1.5"/>
        <circle cx="50" cy="85" r="18" fill="var(--bg)" stroke="var(--navy)" stroke-width="2"/>
        <circle cx="120" cy="85" r="18" fill="var(--bg)" stroke="var(--navy)" stroke-width="2"/>
        <text x="50" y="90" font-size="10" font-weight="700" text-anchor="middle" fill="var(--navy)">P1</text>
        <text x="120" y="90" font-size="10" font-weight="700" text-anchor="middle" fill="var(--navy)">P2</text>
        <!-- Connection from P1 out to P2 in -->
        <path d="M 50 67 V 55 H 100 V 85 H 102" stroke="var(--blue)" stroke-width="2.5" marker-end="url(#ar)"/>
        <!-- Out from P2 -->
        <path d="M 120 67 V 40 H 155 V 160" stroke="var(--red)" stroke-width="2.5" marker-end="url(#ar)"/>
        <text x="90" y="190" font-size="13" font-weight="700" text-anchor="middle" fill="var(--red)">\(H_d = -0.07\text{ m}\)</text>
        <text x="90" y="215" font-size="12" font-weight="600" fill="var(--navy)" text-anchor="middle">เฮดรวม \(H \approx 2H_1\)</text>
      </g>

      <!-- 3. Parallel Pump -->
      <g transform="translate(470, 20)">
        <text x="90" y="20" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">3. ปั๊มขนาน (Parallel)</text>
        <rect x="10" y="40" width="160" height="90" fill="var(--hover)" stroke="var(--ink)" stroke-width="1.5"/>
        <circle cx="50" cy="95" r="18" fill="var(--bg)" stroke="var(--navy)" stroke-width="2"/>
        <circle cx="120" cy="95" r="18" fill="var(--bg)" stroke="var(--navy)" stroke-width="2"/>
        <text x="50" y="100" font-size="10" font-weight="700" text-anchor="middle" fill="var(--navy)">P1</text>
        <text x="120" y="100" font-size="10" font-weight="700" text-anchor="middle" fill="var(--navy)">P2</text>
        <!-- Both outputs to Manifold top -->
        <line x1="20" y1="50" x2="160" y2="50" stroke="var(--gold)" stroke-width="4"/>
        <text x="90" y="45" font-size="11" font-weight="700" text-anchor="middle" fill="var(--gold)">Manifold</text>
        <path d="M 50 77 V 52" stroke="var(--blue)" stroke-width="2"/>
        <path d="M 120 77 V 52" stroke="var(--blue)" stroke-width="2"/>
        <path d="M 160 50 H 170 V 160" stroke="var(--red)" stroke-width="2.5" marker-end="url(#ar)"/>
        <text x="90" y="190" font-size="13" font-weight="700" text-anchor="middle" fill="var(--navy)">\(H_d = +0.94\text{ m}\)</text>
        <text x="90" y="215" font-size="12" font-weight="600" fill="var(--navy)" text-anchor="middle">อัตราไหลรวม \(Q \approx 2Q_1\)</text>
      </g>
    </svg>
    <figcaption>รูปที่ 9.1 แผนภาพเปรียบเทียบการไหลและค่าแก้ระดับเกจความดันของปั๊มทั้ง 3 รูปแบบ</figcaption>
  </figure>

  <h3 class="grp" id="lab9-valves">ง. ตารางสรุปสถานะการเปิด-ปิดวาล์วตามข้อสอบของอาจารย์</h3>
  <div class="stmt">
    <p>จากลายมืออาจารย์ระบุว่า <i>"ข้อสอบจะเขียนให้รูป 1-3 รูป ถามว่าเข้าทางไหนออกทางไหน วาล์วไหนเปิดหรือปิด"</i> สรุปตามขั้นตอนปฏิบัติการจริงดังนี้:</p>
  </div>
  <div class="tw">
    <table>
      <caption>ตารางสถานะวาล์วและการวัดค่าสำหรับการต่อปั๊ม 3 รูปแบบ</caption>
      <thead>
        <tr>
          <th>รูปแบบการต่อ</th>
          <th>Sump Drain Valve</th>
          <th>Bench Control Valve</th>
          <th>Discharge Control Valve</th>
          <th>เกจวัดความดันขาเข้า (\(h_{\text{in}}\))</th>
          <th>เกจวัดความดันขาออก (\(h_{\text{out}}\))</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><b>1. ปั๊มตัวเดียว (Single)</b></td>
          <td><span class="ok">เปิด (Open)</span></td>
          <td><span class="no">ปิด (Closed)</span></td>
          <td>ปรับหรี่ 10 ค่า</td>
          <td>\(h_1\) (Inlet Gauge)</td>
          <td>\(h_0\) (Outlet Gauge)</td>
        </tr>
        <tr>
          <td><b>2. ปั๊มต่ออนุกรม (Series: 2H)</b></td>
          <td><span class="no">ปิด (Closed)</span></td>
          <td><span class="ok">เปิดสุด (Fully Open)</span></td>
          <td>ปรับหรี่ 10 ค่า</td>
          <td><b>\(h_1 = 0\)</b> (บรรยากาศ)</td>
          <td>\(h_0\) (Outlet Gauge)</td>
        </tr>
        <tr>
          <td><b>3. ปั๊มต่อขนาน (Parallel: 2Q)</b></td>
          <td><span class="ok">เปิด (Open)</span></td>
          <td><span class="ok">เปิดสุด (Fully Open)</span></td>
          <td>ปรับหรี่ 10 ค่า</td>
          <td>\(h_1\) (Inlet Gauge)</td>
          <td>\(h_m\) (Manifold Gauge)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <h3 class="grp" id="lab9-hq">จ. กราฟสมรรถนะ H-Q และเส้นความต้านทานระบบ (System Curve)</h3>
  <p>แผนภาพเส้นโค้งลักษณะสมรรถนะของปั๊ม (Pump Performance Curves) ตามที่อาจารย์เขียนบนกระดานและหน้าจอ iPad หน้า 53:</p>

  <figure>
    <svg viewBox="0 0 680 340" role="img" aria-label="กราฟความสัมพันธ์ H-Q ของปั๊มเดี่ยว อนุกรม และขนาน พร้อม System Curve">
      <!-- Grid Lines -->
      <line x1="80" y1="280" x2="620" y2="280" stroke="var(--ink)" stroke-width="2"/>
      <line x1="80" y1="40" x2="80" y2="280" stroke="var(--ink)" stroke-width="2"/>
      <!-- Arrows -->
      <path d="M 620 280 L 610 275 L 610 285 Z" fill="var(--ink)"/>
      <path d="M 80 40 L 75 50 L 85 50 Z" fill="var(--ink)"/>
      <!-- Axis Labels -->
      <text x="630" y="285" font-size="14" font-weight="700" fill="var(--navy)">Q (m³/s หรือ L/s)</text>
      <text x="75" y="30" font-size="14" font-weight="700" text-anchor="middle" fill="var(--navy)">H (m)</text>

      <!-- Tick Marks on H-axis -->
      <line x1="75" y1="180" x2="85" y2="180" stroke="var(--ink)" stroke-width="1.5"/>
      <text x="65" y="185" font-size="13" font-weight="700" text-anchor="end" fill="var(--navy)">H</text>

      <line x1="75" y1="80" x2="85" y2="80" stroke="var(--ink)" stroke-width="1.5"/>
      <text x="65" y="85" font-size="13" font-weight="700" text-anchor="end" fill="var(--red)">2H</text>

      <!-- Tick Marks on Q-axis -->
      <line x1="330" y1="275" x2="330" y2="285" stroke="var(--ink)" stroke-width="1.5"/>
      <text x="330" y="305" font-size="13" font-weight="700" text-anchor="middle" fill="var(--navy)">Q</text>

      <line x1="560" y1="275" x2="560" y2="285" stroke="var(--ink)" stroke-width="1.5"/>
      <text x="560" y="305" font-size="13" font-weight="700" text-anchor="middle" fill="var(--green)">2Q</text>

      <!-- 1. Single Pump Curve: from (80, 180) to (330, 280) -->
      <path d="M 80 180 Q 200 190 330 280" fill="none" stroke="var(--navy)" stroke-width="3"/>
      <text x="210" y="215" font-size="12" font-weight="700" fill="var(--navy)">ปั๊มเดี่ยว (Single)</text>

      <!-- 2. Series Pump Curve (2H): from (80, 80) to (340, 280) -->
      <path d="M 80 80 Q 230 110 340 280" fill="none" stroke="var(--red)" stroke-width="3" stroke-dasharray="6 3"/>
      <text x="180" y="105" font-size="12" font-weight="700" fill="var(--red)">ปั๊มอนุกรม (Series: 2H)</text>

      <!-- 3. Parallel Pump Curve (2Q): from (80, 180) to (560, 280) -->
      <path d="M 80 180 Q 360 190 560 280" fill="none" stroke="var(--green)" stroke-width="3"/>
      <text x="410" y="215" font-size="12" font-weight="700" fill="var(--green)">ปั๊มขนาน (Parallel: 2Q)</text>

      <!-- System Head Curve (Purple Line as in iPad) -->
      <path d="M 80 230 Q 300 210 520 60" fill="none" stroke="#7c3aed" stroke-width="2.5"/>
      <text x="460" y="70" font-size="12" font-weight="700" fill="#7c3aed">เส้นความต้านทานระบบ (System Curve)</text>

      <!-- Operating Points -->
      <circle cx="240" cy="200" r="5" fill="var(--navy)"/>
      <circle cx="280" cy="150" r="5" fill="var(--red)"/>
      <circle cx="380" cy="192" r="5" fill="var(--green)"/>
      <text x="245" y="195" font-size="11" fill="var(--navy)">จุดทำงานเดี่ยว</text>
      <text x="285" y="145" font-size="11" fill="var(--red)">จุดทำงานอนุกรม</text>
      <text x="385" y="185" font-size="11" fill="var(--green)">จุดทำงานขนาน</text>
    </svg>
    <figcaption>รูปที่ 9.2 กราฟความสัมพันธ์ H-Q ของปั๊มทั้ง 3 รูปแบบ และจุดตัดกับ System Head Curve (ถอดแบบจากหน้าจอ iPad หน้า 53)</figcaption>
  </figure>

  <h3 class="grp" id="lab9-power">ฉ. กำลังไฮดรอลิกและประสิทธิภาพของเครื่องสูบน้ำ</h3>
  <ol class="st">
    <li><b>กำลังที่น้ำได้รับ (Water Horsepower / Hydraulic Power, \(W_i\)):</b>
      $$W_i = \gamma Q H = 9,810 \times Q \times H\quad [\text{Watts}]\tag{9.7}$$
      <p class="nt">• \(\gamma = \rho g = 9,810\text{ N/m}^3\)<br>
      • \(Q\) ต้องเป็นหน่วย \(\text{m}^3/\text{s}\) เท่านั้น (ห้ามใส่หน่วย L/s หรือ mL/s เด็ดขาด!)<br>
      • \(H\) คือ Total Head ในหน่วยเมตร [m]</p>
    </li>
    <li><b>ประสิทธิภาพรวมของเครื่องสูบน้ำ (\(\eta_o\)):</b>
      $$\eta_o = \frac{W_i}{W_m} \times 100\%$$
      <p class="nt">โดยที่ \(W_m\) คือกำลังไฟฟ้าที่ป้อนเข้ามอเตอร์ปั๊ม [Watts]</p>
    </li>
  </ol>

  <h3 class="grp" id="lab9-traps">ช. จุดดักคะแนนข้อสอบของอาจารย์ (Handwritten Exam Notes)</h3>
  <div class="bx trap">
    <b>ข้อสอบถามเรื่องวาล์วและทิศทางการไหล:</b>
    <div>
      อาจารย์บันทึกไว้ในข้อสอบว่า: <i>"จะเขียนรูปผังท่อให้ 1-3 รูป แล้วถามว่า น้ำเข้าทางไหน ออกทางไหน วาล์วไหนเปิดหรือปิด"</i><br>
      • <b>ปั๊มเดี่ยว:</b> Sump Drain Valve เปิด, Bench Control Valve ปิด, น้ำเข้าผ่านเกจ \(h_1\) เข้าปั๊มตัวนอก ออกผ่าน Discharge Control Valve<br>
      • <b>ปั๊มอนุกรม:</b> Sump Drain Valve ปิด, Bench Control Valve เปิดสุด, น้ำดูดจากถังเปิดสู่ปั๊มในโต๊ะ (\(h_1 = 0\)) ส่งอัดเข้าทางดูดปั๊มตัวนอก (\(H_d = -0.07\text{ m}\))<br>
      • <b>ปั๊มขนาน:</b> Sump Drain Valve เปิด, Bench Control Valve เปิดสุด, ปั๊มทั้ง 2 ตัวดูดน้ำแยกกัน แล้วส่งท่อออกไปรวมกันที่ Manifold ด้านบน (\(H_d = +0.94\text{ m}\))
    </div>
  </div>

  <div class="bx trap">
    <b>จุดดักเครื่องหมายค่าแก้ระดับเกจ \(H_d\):</b>
    <div>
      • ปั๊มเดี่ยว: \(H_d = +0.15\text{ m}\)<br>
      • ปั๊มอนุกรม: \(H_d = \mathbf{-0.07\text{ m}}\) (ถ้าเขียน \(+0.07\) จะคิดเลขผิดทันที)<br>
      • ปั๊มขนาน: \(H_d = +0.94\text{ m}\)
    </div>
  </div>

  <div class="bx trap">
    <b>จุดดักการแปลงหน่วยยกกำลังสิบ (มล. เป็น ลบ.ม.):</b>
    <div>
      • \(1\text{ L} = 10^{-3}\text{ m}^3 = 0.001\text{ m}^3\)<br>
      • \(1\text{ mL} = 10^{-6}\text{ m}^3 = 0.000001\text{ m}^3\)<br>
      • ต้องแปลงปริมาตรเป็น \(\text{m}^3\) และเวลาเป็นวินาที ก่อนแทนค่าในสูตร \(W_i = \gamma Q H\) เสมอ
    </div>
  </div>

  <h3 class="grp" id="lab9-exam">ซ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
  <div class="stmt">
    <p><b>โจทย์ตัวอย่าง:</b> ในการทดสอบปั๊มน้ำ 2 เครื่องต่อแบบอนุกรม (Series Pumps) อ่านเกจความดันด้านทางออกได้ \(h_0 = 14.8\text{ m}\) ของน้ำ ตวงน้ำได้ปริมาตร \(25\text{ L}\) ในเวลา \(32.0\text{ s}\) ถ้ามอเตอร์ปั๊มกินกำลังไฟฟ้า \(W_m = 250\text{ W}\) จงหา (ก) เฮดรวม \(H\) (ข) อัตราการไหล \(Q\) (ค) กำลังไฮดรอลิกที่น้ำได้รับ \(W_i\) และ (ง) ประสิทธิภาพรวม \(\eta_o\)</p>
  </div>

  <h4 class="cardt">เฉลยวิธีทำ (เขียนส่งอาจารย์ตามลำดับ)</h4>
  <div class="exam">
    <div class="row">
      <div class="lab">ข้อมูลที่กำหนด</div>
      <div class="given">$$\begin{aligned} & \text{โหมดอนุกรม (Series)}:\ h_1 = 0,\ H_d = -0.07\ \text{m} \\ & h_0 = 14.8\ \text{m} \\ & V = 25\ \text{L} = 0.025\ \text{m}^3,\quad t = 32.0\ \text{s} \\ & W_m = 250\ \text{W},\quad \gamma = 9,810\ \text{N/m}^3 \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ก) เฮดรวม H</div>
      <div>$$\begin{aligned} H &= (h_0 - h_1) + H_d \\ &= (14.8 - 0) + (-0.07) = 14.73\ \text{m}\quad (\text{อย่าลืมเครื่องหมายลบ}) \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ข) อัตราการไหล Q</div>
      <div>$$Q = \frac{\Delta V}{\Delta t} = \frac{0.025\ \text{m}^3}{32.0\ \text{s}} = 7.8125 \times 10^{-4}\ \text{m}^3/\text{s} = 0.781\ \text{L/s}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ค) กำลังน้ำ Wi</div>
      <div>$$\begin{aligned} W_i &= \gamma Q H \\ &= 9,810 \times (7.8125 \times 10^{-4}) \times (14.73) \\ &= 112.89\ \text{Watts} \end{aligned}$$</div>
    </div>
    <div class="row">
      <div class="lab">(ง) ประสิทธิภาพ η_o</div>
      <div>$$\eta_o = \frac{W_i}{W_m} \times 100\% = \frac{112.89}{250} \times 100\% = 45.16\%$$</div>
    </div>
    <div class="row">
      <div class="lab">คำตอบสุดท้าย</div>
      <div><span class="fin">\(H = 14.73\ \text{m},\quad Q = 7.81 \times 10^{-4}\ \text{m}^3/\text{s},\quad W_i = 112.9\ \text{W},\quad \eta_o = 45.2\%\)</span></div>
    </div>
  </div>

  <div class="pn">
    <a href="#lab8">← บทที่ 8 การไหลผ่านรูลอด</a>
    <a href="#lab10">บทที่ 10 การไหลลอดประตูน้ำ →</a>
  </div>
</section>
'''
