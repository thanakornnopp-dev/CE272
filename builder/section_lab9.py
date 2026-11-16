# -*- coding: utf-8 -*-

def get_section_lab9():
    return r'''
<section id="lab9">
  <header class="top">
    <p class="kick">ปฏิบัติการที่ 9 · การทดสอบสมรรถนะเครื่องสูบน้ำและระบบต่ออนุกรม-ขนาน</p>
    <h1>บทที่ 9: การทดสอบเครื่องสูบน้ำ (Centrifugal Pump Test)</h1>
    <p class="sub">ปั๊มเดี่ยว · ปั๊มต่ออนุกรม (เฮด x2) · ปั๊มต่อขนาน (Q x2) · ค่าแก้ระดับเกจ Hd · กำลังไฮดรอลิก Wi</p>
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
    <a href="#lab9-power">ง. กำลังไฮดรอลิกและประสิทธิภาพ</a>
    <a href="#lab9-traps">จ. จุดดักคะแนนข้อสอบของอาจารย์</a>
    <a href="#lab9-exam">ฉ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ</a>
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
      <caption>ระยะจากระดับอ้างอิงถึงจุดวัดความดัน (Head Correction Factors)</caption>
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
          $$H_d = h_d(\text{outlet}) - h_d(\text{bench}) = 0.17 - 0.24 = \mathbf{-0.07\ \text{m}}\quad \htmlClass{no}{(\text{ค่าติดลบ!})}$$
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
    <svg viewBox="0 0 680 300" role="img" aria-label="แผนภาพเปรียบเทียบการไหลของปั๊มเดี่ยว อนุกรม และขนาน">
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

  <h3 class="grp" id="lab9-power">ง. กำลังไฮดรอลิกและประสิทธิภาพของเครื่องสูบน้ำ</h3>
  <ol class="st">
    <li><b>กำลังที่น้ำได้รับ (Water Horsepower / Hydraulic Power, \(W_i\)):</b>
      $$W_i = \gamma Q H = 9,810 \times Q \times H\quad [\text{Watts}]\tag{9.7}$$
      <p class="nt">• \(\gamma = \rho g = 9,810\text{ N/m}^3\)<br>
      • \(Q\) ต้องเป็นหน่วย \(\text{m}^3/\text{s}\) เท่านั้น (ห้ามใส่หน่วย L/s เด็ดขาด!)<br>
      • \(H\) คือ Total Head ในหน่วยเมตร [m]</p>
    </li>
    <li><b>ประสิทธิภาพรวมของเครื่องสูบน้ำ (\(\eta_o\)):</b>
      $$\eta_o = \frac{W_i}{W_m} \times 100\%$$
      <p class="nt">โดยที่ \(W_m\) คือกำลังไฟฟ้าที่ป้อนเข้ามอเตอร์ปั๊ม [Watts]</p>
    </li>
  </ol>

  <h3 class="grp" id="lab9-traps">จ. จุดดักคะแนนข้อสอบของอาจารย์ (Handwritten Exam Notes)</h3>
  <div class="bx trap">
    <b>ข้อสอบถามเรื่องวาล์วและทิศทางการไหล:</b>
    <div>
      อาจารย์บันทึกไว้ในข้อสอบว่า: <i>"จะเขียนรูปผังท่อให้ 1-3 รูป แล้วถามว่า น้ำเข้าทางไหน ออกทางไหน วาล์วไหนเปิดหรือปิด"</i><br>
      • <b>ปั๊มเดี่ยว:</b> น้ำเข้าตรงจากถัง Sump เข้าปั๊มตัวนอก ออกผ่านวาล์วปรับอัตราการไหล (Discharge Control Valve)<br>
      • <b>ปั๊มอนุกรม:</b> น้ำออกจากปั๊มในโต๊ะ (Pump 1) ส่งต่อเข้าทางดูดของปั๊มตัวนอก (Pump 2) วาล์วเชื่อมระหว่างปั๊มต้องเปิด<br>
      • <b>ปั๊มขนาน:</b> ปั๊มทั้ง 2 ตัวดูดน้ำจาก Sump แยกกัน แล้วส่งท่อออกไปรวมกันที่ Manifold ด้านบน
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

  <h3 class="grp" id="lab9-exam">ฉ. ตัวอย่างโจทย์ข้อสอบและการแสดงวิธีทำ (Exam Practice)</h3>
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
      <div>$$\begin{aligned} H &= (h_0 - h_1) + H_d \\ &= (14.8 - 0) + (-0.07) = 14.73\ \text{m}\quad \htmlClass{ok}{(\text{อย่าลืมเครื่องหมายลบ})} \end{aligned}$$</div>
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
